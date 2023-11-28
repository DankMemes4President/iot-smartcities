from azure.digitaltwins.core import DigitalTwinsClient
from azure.identity import DefaultAzureCredential
import random
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
random_number = random.randint(1, 20)
number_of_cars = []
print("Random Number:", random_number)
spotStatus = ['Reserved', 'Occupied', 'Vacant']
carType = ['EV', 'ICE']
vacant = []
reserved = []
occupied = []
incompatible = []
digital_twin_id = 'ParkingCar'
patch = [{
        "op": "replace",    
        "path": "/isEv",
        "value": random.choice(list(carType))
    }
    ]

updated_twin = service_client.update_digital_twin(digital_twin_id, patch)
print('Updated Digital Twin')
for i in range(1,11):
    digital_twin_id = f'ParkingSpot{i}'
    patch = [{
        "op": "replace",
        "path": "/status",
        "value": random.choice(list(spotStatus)),
    }
    ]

    updated_twin = service_client.update_digital_twin(digital_twin_id, patch)
    print(f'Updated Digital Twin {i}:')
get_twin = service_client.get_digital_twin('ParkingCar')
print(get_twin)
for key, twin in enumerate(query_result):
    print("hi")  
    if "ParkingSpot" in twin["$dtId"]:
        if(get_twin["isEv"] == twin["Type"]):
            if(twin["status"] == "Vacant"):
                vacant.append(twin)
            elif(twin["status"] == "Occupied"):
                occupied.append(twin)
            elif(twin["status"] == "Reserved"):
                reserved.append(twin)
        else: 
            incompatible.append(twin)
            
print(vacant)
print(incompatible)
#     roads = ['RoadA', 'RoadB', 'RoadC']
#     random_road = random.choice(roads)
#     print("Random Road:", random_road)
#     myRelationship = {
#         "$relationshipId": f"RoadVehicle {i}",
#         "$sourceId": random_road ,
#         "$relationshipName": "is_on",
#         "$targetId":  f"Vehicle{i}"
#         }
#     print(myRelationship)
#     service_client.upsert_relationship(
#         myRelationship["$sourceId"],
#         myRelationship["$relationshipId"],
#         myRelationship
#     )  

# for road in roads:
#     relationships = service_client.list_relationships(road)
#     relationships_list = list(relationships)
#     print("Number of Relationships:", len(relationships_list))
#     number_of_cars.append(len(relationships_list))

# max_value = max(number_of_cars)
# max_indices = [i for i, value in enumerate(number_of_cars) if value == max_value]
# if len(max_indices) > 1:
#     selected_road = random.choice(max_indices)
#     print(f"Traffic light for road {chr(ord('A') + selected_road)} has turned green")
# else:
#     max_index = number_of_cars.index(max_value)
#     print(f"Traffic light for road {chr(ord('A') + max_index)} has turned green")   
    # for
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