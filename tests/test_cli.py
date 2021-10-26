from click.testing import CliRunner
from octoflow.cli import list_tenants


def test_cli_entrypoint():
    result = CliRunner().invoke(list_tenants)
    breakpoint()