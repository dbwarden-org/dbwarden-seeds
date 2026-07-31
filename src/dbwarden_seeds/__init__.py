from __future__ import annotations

from dbwarden_seeds.code_seeds import (
    apply_code_seed,
    discover_code_seeds,
    get_pending_code_seeds,
    rollback_code_seed,
)
from dbwarden_seeds.commands import (
    seed_apply_cmd,
    seed_create_cmd,
    seed_list_cmd,
    seed_rollback_cmd,
)
from dbwarden_seeds.engine import (
    PYTHON_SEED_TEMPLATE,
    SQL_SEED_TEMPLATE,
    apply_single_seed,
    generate_seed_filename,
    get_next_seed_number,
    get_pending_seeds,
    get_seeds_to_rollback,
    rollback_single_seed,
)
from dbwarden_seeds.export import export_seeds_cmd

__version__ = "0.1.0"

# The DBWarden plugin contract this package targets. Core refuses to load a
# plugin declaring a version it does not provide, so a mismatched pairing fails
# at load with one clear message instead of somewhere inside a migration.
DBWARDEN_PLUGIN_API = 1


def seed_create(
    description: str,
    *,
    seed_type: str = "sql",
    database: str | None = None,
    verbose: bool = False,
) -> None:
    seed_create_cmd(description, seed_type=seed_type, database=database, verbose=verbose)


def seed_apply(
    *,
    version: str | None = None,
    dry_run: bool = False,
    database: str | None = None,
    all_databases: bool = False,
    verbose: bool = False,
) -> None:
    seed_apply_cmd(
        version=version,
        dry_run=dry_run,
        database=database,
        all_databases=all_databases,
        verbose=verbose,
    )


def seed_list(
    *,
    database: str | None = None,
    all_databases: bool = False,
    verbose: bool = False,
    prune: bool = False,
) -> None:
    seed_list_cmd(
        database=database,
        all_databases=all_databases,
        verbose=verbose,
        prune=prune,
    )


def seed_rollback(
    *,
    count: int | None = None,
    to_version: str | None = None,
    database: str | None = None,
    all_databases: bool = False,
    verbose: bool = False,
) -> None:
    seed_rollback_cmd(
        count=count,
        to_version=to_version,
        database=database,
        all_databases=all_databases,
        verbose=verbose,
    )


def seed_export(
    *,
    database: str | None = None,
    all_databases: bool = False,
    output_dir: str = "seeds",
) -> None:
    export_seeds_cmd(database=database, all_databases=all_databases, output_dir=output_dir)


def setup(registrar) -> None:
    registrar.register("seed_create", seed_create)
    registrar.register("seed_apply", seed_apply)
    registrar.register("seed_list", seed_list)
    registrar.register("seed_rollback", seed_rollback)
    registrar.register("seed_export", seed_export)


__all__ = [
    "PYTHON_SEED_TEMPLATE",
    "SQL_SEED_TEMPLATE",
    "apply_code_seed",
    "apply_single_seed",
    "discover_code_seeds",
    "generate_seed_filename",
    "get_next_seed_number",
    "get_pending_code_seeds",
    "get_pending_seeds",
    "get_seeds_to_rollback",
    "rollback_code_seed",
    "rollback_single_seed",
    "seed_apply",
    "seed_create",
    "seed_export",
    "seed_list",
    "seed_rollback",
    "setup",
]
