import requests

# Create user

USERNAME = "ward"
TOKEN = "perfectminigolfscore"
GRAPH = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"

user = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user)
# print(response.text)


# Create graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Python graph",
    "unit": "projects",
    "type": "int",
    "color": "ichou"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Create pixel in a graph

pixel_graph_config = {
    "date": "20231004",
    "quantity": "4"
}

pixel_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

response = requests.post(url=pixel_graph_endpoint, json=pixel_graph_config, headers=headers)

print(response.text)
