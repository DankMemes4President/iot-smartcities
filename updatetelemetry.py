from azure.digitaltwins.core import DigitalTwinsClient
from azure.identity import DefaultAzureCredential
# DefaultAzureCredential supports different authentication mechanisms and determines the appropriate credential type based of the environment it is executing in.
# It attempts to use multiple credential types in an order until it finds a working credential.

# - AZURE_URL: The URL to the ADT in Azure
url = "https://IoT-1.api.wcus.digitaltwins.azure.net"

# DefaultAzureCredential expects the following three environment variables:
# - AZURE_TENANT_ID: The tenant ID in Azure Active Directory
# - AZURE_CLIENT_ID: The application (client) ID registered in the AAD tenant
# - AZURE_CLIENT_SECRET: The client secret for the registered application
credential = DefaultAzureCredential()
service_client = DigitalTwinsClient(url, credential)

query_expression = 'SELECT * FROM digitaltwins'
query_result = service_client.query_twins(query_expression)
print('DigitalTwins:')
for key, twin in enumerate(query_result):
    print(key, twin)
    # if key <= 6:
        # relationships = service_client.list_relationships(twin['$dtId'])
        # for relationship in relationships:
            # print(relationship)
            # x = service_client.delete_relationship(relationship['$sourceId'], relationship['$relationshipId'])
        # service_client.delete_digital_twin(twin['$dtId'])
# service_client.delete_digital_twin("RoadSeg1")
# service_client.delete_digital_twin("Road2")
# service_client.delete_digital_twin("RoadSeg2")
# service_client.delete_digital_twin("vehicle1")