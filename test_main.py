import requests

url = "https://cs-361-sorting-microservice.onrender.com/sort"

simple_payload = {
    "arr": [3,2,1]
}

# Send the POST request
print("Sending request...")
response = requests.post(url, json=simple_payload)

# Check if the request was successful (HTTP Status 200)
if response.status_code == 200:
    print("\nSuccess! Here is the microservice output:")

    # .json() converts the server's JSON response back into a Python dictionary
    data = response.json()
    print(data)

else:
    print(f"\nFailed with status code: {response.status_code}")
    print(response.text)
