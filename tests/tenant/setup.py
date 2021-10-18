from setuptools import setup, find_packages


setup(
  name="tenant",
  packages=find_packages("src"),
  package_dir={"":"src"},
  entry_points={
    "octoflow.tenants": "tenant = octoflow.tenants.tenant.cli:main"
  }
)