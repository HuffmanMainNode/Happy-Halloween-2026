# Happy Halloween 2026 🎃

**Happy Halloween by MrCakes.**

Instead of passing out candy, we're passing out algorithms.

This repository is the front door to a small collection of open-source projects created around Halloween 2026. The goal is to make useful research and engineering tools easier for people and independent agents to discover, inspect, and improve together.

This is an index and community landing page, not a separate OSINT application. The working tools live in their own repositories so they can be developed, tested, reviewed, and released independently.

## Start here

| Project | What it provides | Human guide | Agent guide |
|---|---|---|---|
| [Halloween OSINT 2026](https://github.com/HuffmanMainNode/Halloween-OSINT-2026) | Local-first evidence manifests, passive DNS/TLS observations, offline transaction analysis, and local MCP tools | [Onboarding](https://github.com/HuffmanMainNode/Halloween-OSINT-2026/blob/main/docs/USER-ONBOARDING.md) | [Agent integration](https://github.com/HuffmanMainNode/Halloween-OSINT-2026/blob/main/docs/AGENT-INTEGRATION.md) |
| [Open Intelligence Exchange](https://github.com/HuffmanMainNode/Open-Intelligence-Exchange) | Experimental protocol for signed agent identities, verified messages, optional encryption, and approval-gated exchange | [Onboarding](https://github.com/HuffmanMainNode/Open-Intelligence-Exchange/blob/main/docs/USER-ONBOARDING.md) | [Agent onboarding](https://github.com/HuffmanMainNode/Open-Intelligence-Exchange/blob/main/docs/AGENT-ONBOARDING.md) |
| [Huffman Cyber Observatory](https://github.com/HuffmanMainNode/Huffman-Cyber-Observatory) | Local defensive security checks, evidence integrity, SBOM inventory, KEV correlation, and file cryptography | [Onboarding](https://github.com/HuffmanMainNode/Huffman-Cyber-Observatory/blob/main/docs/USER-ONBOARDING.md) | [Agent onboarding](https://github.com/HuffmanMainNode/Huffman-Cyber-Observatory/blob/main/docs/AGENT-ONBOARDING.md) |
| [Open-Swarm](https://github.com/HuffmanMainNode/-Open-Swarm) | Local-first task orchestration, bounded workers, approval gates, and durable event handling | [Onboarding](https://github.com/HuffmanMainNode/-Open-Swarm/blob/main/docs/USER-ONBOARDING.md) | [Agent onboarding](https://github.com/HuffmanMainNode/-Open-Swarm/blob/main/docs/AGENT-ONBOARDING.md) |
| [Huffman Defensive Intelligence](https://github.com/HuffmanMainNode/Huffman-Defensive-Intelligence) | Integration layer connecting the four projects through versioned events and evidence references | [Onboarding](https://github.com/HuffmanMainNode/Huffman-Defensive-Intelligence/blob/main/docs/USER-ONBOARDING.md) | [Agent onboarding](https://github.com/HuffmanMainNode/Huffman-Defensive-Intelligence/blob/main/docs/AGENT-ONBOARDING.md) |

## How to participate

1. Choose the smallest project that fits your task. You do not need to install the whole collection.
2. Read its human or agent onboarding guide before using it.
3. Inspect the code, tests, security model, license, and documented limitations.
4. Start with local examples and synthetic data where possible.
5. Propose improvements through issues or pull requests in the project that owns the relevant code.

## Shared principles

- Open protocols and inspectable implementations.
- Local-first operation where practical, without mandatory paid APIs for core workflows.
- Human approval for consequential actions.
- Evidence provenance and explicit uncertainty.
- Privacy, civil liberties, and authorized use.
- No claims of production readiness or security certification without evidence.

## Important limitations

These projects are independent and at different maturity levels. Their presence in this index is not an endorsement or security certification. Agent identity signatures do not prove real-world identity or truth; a hash does not prove source authenticity; a catalog entry does not prove a tool is safe. Review each project's current documentation and threat model.

The machine-readable [collection index](collection.json) provides the same project links for scripts and agents.

---

*Built in the open. Shared with the community. Happy Halloween 2026.*
