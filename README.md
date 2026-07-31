# gemma4-coder-gguf-runner

[![CI](https://github.com/jabrahns-source/gemma4-coder-gguf-runner/actions/workflows/ci-build.yml/badge.svg)](https://github.com/jabrahns-source/gemma4-coder-gguf-runner/actions/workflows/ci-build.yml)

**Production-ready local GGUF runner for Gemma 4 12B Coder with llama.cpp, auto-quant, Docker & systemd support.**

Part of Even The Odds Foundry tooling surface — zero-gatekeeper local inference for coding agents.

## Quick start

```bash
# Docker Compose
cd docker
docker compose up -d

# Or build image directly
docker build -f docker/Dockerfile -t gemma4-coder-runner .
```

See `config/server.conf` for server parameters and `docker/gemma4-coder.service` for systemd unit.

## Layout

| Path | Role |
|------|------|
| `docker/Dockerfile` | Multi-stage build with llama.cpp + quant support |
| `docker/docker-compose.yml` | One-command local stack |
| `docker/gemma4-coder.service` | systemd unit for always-on hosts |
| `config/server.conf` | Runtime configuration |
| `.github/workflows/` | CI build + Docker publish |

## Design notes

- Deterministic, inspectable configuration
- No cloud credentials required for local run
- Compatible with Chromebook / low-resource hosts when quant is applied

## License

MIT (add formal LICENSE file on next polish pass if not present).

— Even The Odds Foundry
