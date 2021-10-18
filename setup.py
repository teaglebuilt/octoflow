from setuptools import setup, find_packages


setup(
  name="octoflow",
  packages=find_packages("src"),
  package_dir={"":"src"},
  entry_points={
    "console_scripts": "octoflow=octoflow.core.cli:main"
  }
)