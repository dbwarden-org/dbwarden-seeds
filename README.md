# dbwarden-seeds

[![Python](https://img.shields.io/badge/Python-3.12.7%2B-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/pypi/v/dbwarden-seeds?logo=pypi&logoColor=white&style=for-the-badge)](https://pypi.org/project/dbwarden-seeds/)
[![CI](https://img.shields.io/github/actions/workflow/status/dbwarden-org/dbwarden-seeds/test.yml?logo=github&logoColor=white&style=for-the-badge)](https://github.com/dbwarden-org/dbwarden-seeds/actions/workflows/test.yml)

Seed data management for [DBWarden](https://github.com/dbwarden-org/dbwarden).

Backs the `dbwarden seed` command group. Without this plugin those commands tell you to install it; with it installed they work unchanged.

## Hooks

| Hook | Command |
|---|---|
| `seed_create` | `dbwarden seed create`: scaffold a versioned SQL or Python seed |
| `seed_apply` | `dbwarden seed apply`: apply pending file and code seeds, tracked by checksum |
| `seed_list` | `dbwarden seed list`: show seed status, with `--prune` for orphaned records |
| `seed_rollback` | `dbwarden seed rollback`: roll back seed tracking records |
| `seed_export` | `dbwarden seed export`: render code seeds to replayable `ROC__*.sql` files |

`seed_apply` also runs after `dbwarden migrate --apply-seeds`, and covers both file seeds (`seeds/V0001__*.sql`) and code seeds (`Seed` subclasses discovered from your models).

## Installation

```bash
dbwarden plugin add dbwarden-seeds
```

## Trust tier

This is an **official** DBWarden plugin. Its distribution name is classified before any of its code is imported, and `dbwarden plugin add` verifies the PyPI Trusted-Publishing attestation (PEP 740) against `dbwarden-org/dbwarden-seeds` before installing. It loads automatically once installed, with no `dbwarden plugin trust` step.

## Development

```bash
uv venv && uv pip install -e . -e ../dbwarden pytest
pytest -q
```

The `tests/test_conformance.py` suite runs DBWarden's shared conformance harness (`dbwarden.plugin_conformance`): entry point resolution, no import-time side effects, hook signatures, public-API-only imports, and idempotent `setup()`.

## License

MIT
