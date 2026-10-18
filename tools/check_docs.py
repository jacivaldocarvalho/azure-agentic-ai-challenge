"""Check the repository's inline Markdown links, fences, and Python/JSON excerpts.

This intentionally supports the Markdown conventions used by this repository,
rather than implementing a complete Markdown renderer. It performs no network
requests and never executes code excerpts.
"""

import ast
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})(.*)$")
LINK = re.compile(r"\]\(([^)\n]+)\)")


def heading_slug(text):
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")


def scan_document(path):
    """Return anchors, inline link destinations, and syntax errors."""
    anchors = set()
    counts = Counter()
    links = []
    errors = []
    fence = None
    code = []
    language = ""
    start = 0
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = FENCE.match(line)
        if fence is not None:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                try:
                    source = "\n".join(code)
                    if language == "python":
                        # Parsing only: allow async fragments without running them.
                        compile(source, str(path), "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
                    elif language == "json":
                        json.loads(source)
                except (SyntaxError, ValueError) as exc:
                    errors.append(f"{path}:{start}: invalid {language} excerpt: {exc}")
                fence = None
            else:
                code.append(line)
            continue
        if match:
            fence = match[1]
            language = match[2].strip().split(maxsplit=1)[0] if match[2].strip() else ""
            code = []
            start = number
            continue
        heading = re.match(r"^#{1,6}\s+(.+?)(?:\s+#+)?$", line)
        if heading:
            slug = heading_slug(heading[1])
            anchor = slug
            while anchor in anchors:
                counts[slug] += 1
                anchor = f"{slug}-{counts[slug]}"
            anchors.add(anchor)
        links.extend((number, destination) for destination in LINK.findall(line))
    if fence is not None:
        errors.append(f"{path}:{start}: unclosed code fence")
    return anchors, links, errors


def check_documents(paths, root):
    """Validate local files and Markdown fragments using cached document scans."""
    documents = {path.resolve(): scan_document(path) for path in paths}
    errors = []
    link_count = 0
    for path in paths:
        _, links, syntax_errors = documents[path.resolve()]
        errors.extend(syntax_errors)
        for line, destination in links:
            url = urlsplit(destination)
            if url.scheme or url.netloc:
                continue
            link_count += 1
            target = unquote(url.path)
            if target.startswith("/"):
                target_path = root / target.lstrip("/")
            else:
                target_path = path.parent / target if target else path
            target_path = target_path.resolve()
            if not target_path.exists():
                errors.append(f"{path}:{line}: missing local target: {destination}")
                continue
            if url.fragment and target_path.suffix.lower() == ".md":
                if target_path not in documents:
                    documents[target_path] = scan_document(target_path)
                if unquote(url.fragment) not in documents[target_path][0]:
                    errors.append(f"{path}:{line}: missing heading anchor: {destination}")
    return errors, link_count


def main():
    paths = [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]
    errors, link_count = check_documents(paths, ROOT)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"Documentation checks passed: {len(paths)} Markdown files, {link_count} local references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
