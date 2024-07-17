import os
import pytest
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

@pytest.fixture(scope="module")
def azure_client():
    credential = DefaultAzureCredential()
    subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
    return ResourceManagementClient(credential, subscription_id)

def test_resource_group_exists(azure_client):
    rg_name = 'your-resource-group-name'
    resource_group = azure_client.resource_groups.get(rg_name)
    assert resource_group is not None, "Resource group does not exist"
