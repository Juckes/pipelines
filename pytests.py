import pytest
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

@pytest.fixture(scope="module")
def azure_client():
    credential = DefaultAzureCredential()
    subscription_id = '13e1ebd2-b4ab-48f5-ba4e-73d8e2db4f85'
    return ResourceManagementClient(credential, subscription_id)

def test_resource_group_exists(azure_client):
    rg_name = 'packer'
    resource_group = azure_client.resource_groups.get(rg_name)
    assert resource_group is not None, f"Resource group '{rg_name}' does not exist"
