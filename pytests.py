# import pytest
# from azure.identity import DefaultAzureCredential
# from azure.mgmt.resource import ResourceManagementClient

# @pytest.fixture(scope="module")
# def azure_client():
#     credential = DefaultAzureCredential()
#     subscription_id = '13e1ebd2-b4ab-48f5-ba4e-73d8e2db4f85'
#     return ResourceManagementClient(credential, subscription_id)

# def test_resource_group_exists(azure_client):
#     rg_name = 'packer'
#     resource_group = azure_client.resource_groups.get(rg_name)
#     resource_group is not None, f"Resource group '{rg_name}' found successfully!"

# Get the Azure creds to test against azure without using azure devops
# Az module or graph api

import pytest
from subprocess import run


@pytest.fixture
def resource_group_name():
    return "packer"  # Replace with your actual resource group name


def test_resource_group_exists(resource_group_name):
    # Use az CLI command to check if resource group exists
    command = ["az", "resource", "group", "show", "-n", resource_group_name]
    result = run(command, capture_output=True, text=True)

    # Assert successful execution (exit code 0) and existence in output
    assert result.returncode == 0, f"Resource group '{resource_group_name}' not found."
    assert f'"{resource_group_name}"' in result.stdout, "Resource group name not found in output."
