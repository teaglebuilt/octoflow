from octoflow.config import settings
from octoflow.core.project import loaders
from octoflow.core.interfaces.tenant import TenantInterface


def main():
    tenants = loaders[settings.core.loader](str(settings.core.tenants_home))
    for k, v in tenants.items():
        TenantInterface.register(k, v)

main()

