# Introduction to AI Agent Service security controls

> Study notes from the 2025 challenge. See the [documentation scope and compatibility notes](../README.md#scope-and-compatibility) before following portal instructions or SDK examples.

## Contents

- [Security responsibilities](#security-responsibilities)
- [Hub and project boundaries](#hub-and-project-boundaries)
- [Role-based access control](#role-based-access-control)
- [Network access](#network-access)
- [Operational checks](#operational-checks)
- [Summary](#summary)

## Security responsibilities

A managed agent service reduces infrastructure work, but the application owner still controls identities, permissions, data access, tools, and network exposure. Consider access to the agent and the agent's access to downstream systems separately.

The original course used hub-based Azure AI Foundry projects. Its resource hierarchy, role assignments, and network screens are historical examples; they are not universal defaults for other project types.

## Hub and project boundaries

In the learning setup, hubs centralized shared connections, compute, and network configuration. Projects isolated development work and used resources made available through the hub. Different security requirements could justify separate hubs.

Review the Azure resource hierarchy and effective permissions in the environment you actually deploy. Do not assume that creating a project grants every required downstream permission.

## Role-based access control

Azure RBAC assigns permissions to identities at a particular scope. The course discussed the following roles:

| Role | Learning context |
| --- | --- |
| Owner | Resource administration and access assignment. |
| Contributor | Resource administration without access assignment. |
| Azure AI Administrator | Administrative operations for the configured AI resource. |
| Azure AI Developer | Development operations in the assigned scope. |
| Azure AI Inference Deployment Operator | Model deployment operations. |
| Reader | Resource inspection. |

Verify role definitions and assignment behavior for the specific resource instead of relying on the old portal defaults.

| Persona | Access to evaluate |
| --- | --- |
| IT administrator | Resource governance and access assignments. |
| Team lead | Shared connections and project administration where required. |
| Developer | Only the project and service operations needed for development. |
| Application identity | Only the data and tools needed by the deployed workload. |

![Hub user role](https://learn.microsoft.com/pt-br/training/advocates/intro-ai-agent-service-security-controls/media/hub-user-role.png)

A signed-in developer and the service's managed identity can require different permissions. For example, access to a connected storage account requires the relevant data-plane role and a working network path; access to the project alone is insufficient.

## Network access

The original hub configuration covered public access, private endpoint connections, and managed outbound access. A private endpoint requires suitable DNS and routing as well as authorization. Restricting inbound access does not automatically restrict outbound access to external systems.

Historical outbound options included unrestricted access, internet access with managed private connections, and access limited to approved destinations. Check which option applies to the compute and services in your deployment.

![Networking configuration](https://learn.microsoft.com/pt-br/training/advocates/intro-ai-agent-service-security-controls/media/networking-configuration.png)

The learning material also illustrated a gateway approach for reaching resources outside the managed network. It is an architecture example, not a requirement for every agent application. Choose connectivity based on the target resource and supported network design.

![Ai foundry app gateway](https://learn.microsoft.com/pt-br/training/advocates/intro-ai-agent-service-security-controls/media/ai-foundry-app-gateway.png)

## Operational checks

Before using a connected tool, verify:

1. The user or application identity can access the agent.
2. The agent's execution identity can access the required data or action.
3. Network paths, DNS, and firewall rules permit that access.
4. Logs and artifacts do not expose secrets or unnecessary personal data.
5. Tool permissions match the workflow's intended authority.

## Summary

Treat identity, authorization, resource configuration, and networking as separate controls. A managed service still requires deliberate configuration and review of downstream access.
