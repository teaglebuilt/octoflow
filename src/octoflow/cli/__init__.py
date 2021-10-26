import sys
import logging
import importlib
import subprocess
from pathlib import Path
from typing import List
import click
from octoflow.core.project import Project
from octoflow.cli.utils import load_module_by_name

# tenants = {
#     name: importlib.import_module(name) 
#     for finder, name, ispkg in iter_tenants(tenants)
# }


def setup_logging(verbose: int):
    root = logging.getLogger()
    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter(
        "[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    root.addHandler(handler)

    if verbose == 0:
        root.setLevel(logging.WARNING)
    elif verbose == 1:
        root.setLevel(logging.INFO)
    else:
        root.setLevel(logging.DEBUG)

    return handler.stream


@click.group()
@click.option(
    "--tenant",
    "-t",
    help="Choose a target tenant for the subcommand (default is current directory).",
)
@click.option("-v", "--verbose", count=True)
@click.pass_context
def cli(ctx: click.Context, tenant: str, verbose: int):
    """
    Poop tastes like it smells, ... delicious.
    """
    ctx.ensure_object(dict)
    ctx.obj["PROJECT"] = Project() if tenant is None else Path(tenant).absolute()
    setup_logging(verbose)
    ctx.obj["PROJECT"].load()


@cli.command()
@click.pass_context
def list_tenants(ctx: click.Context):
    breakpoint()


@cli.command()
@click.pass_context
def server(ctx: click.Context):
    subprocess.run(
        ['uvicorn', 'octoflow.server.main:app'],
        capture_output=True,
        shell=True,
        check=True
    )