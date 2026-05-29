import requests

url = "https://cs-361-sorting-microservice.onrender.com/sort_ints"
url2 = "https://cs-361-sorting-microservice.onrender.com/sort_objects"

simple_payload = {
    "ints": [3, 2, 1]
}

complex_payload = {
    "objs": [
        {"rank": 1, "info": {"example_key": 1}},
        {"rank": 3, "info": {"example_key": 3}},
        {"rank": 4, "info": {"example_key": 4}},
        {"rank": 2, "info": {"example_key": 2}},
    ]
}

# Send the POST request
print("Sending request...")
response = requests.post(url2, json=complex_payload)

# Check if the request was successful (HTTP Status 200)
if response.status_code == 200:
    print("\nSuccess! Here is the microservice output:")

    # .json() converts the server's JSON response back into a Python dictionary
    data = response.json()
    print(data)

else:
    print(f"\nFailed with status code: {response.status_code}")
    print(response.text)


