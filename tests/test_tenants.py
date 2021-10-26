from octoflow.core.interfaces.tenant import load_tenants_namespace


def test_registered_tenant():
    tenants = load_tenants_namespace()
    breakpoint()