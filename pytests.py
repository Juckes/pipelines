import pytest
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

@pytest.fixture(scope="module")
def azure_client():
    credential = DefaultAzureCredential()
    return ResourceManagementClient(credential)

def test_resource_group_exists(azure_client):
    rg_name = 'your-resource-group-name'
    resource_group = azure_client.resource_groups.get(rg_name)
    assert resource_group is not None, f"Resource group '{rg_name}' does not exist"
