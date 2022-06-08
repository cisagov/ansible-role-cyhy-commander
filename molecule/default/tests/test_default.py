"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["curl", "git", "unzip"])
def test_apt_packages(host, pkg):
    """Test that the apt packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["cyhy-commander"])
def test_pip_packages(host, pkg):
    """Test that the pip packages were installed."""
    assert pkg in host.pip_package.get_packages()


@pytest.mark.parametrize(
    "f",
    [
        "/var/log/cyhy",
        "/var/cyhy/commander",
        "/lib/systemd/system/cyhy-commander.service",
    ],
)
def test_files(host, f):
    """Test that the expected files and directories are present."""
    assert host.file(f).exists
