# CS361-Sorting-Microservice
## Description
Sorts an input array of integers or a list of JSON objects by some value within each object, then returns the result.

## Calling the Microservice
Make an HTTP POST request to the microservice, specifying either the "sort_ints" or "sort_objects" endpoint. Include either the array of ints or array of objects as the POST payload.

Example sort_ints POST request:
```
import requests

url = "https://cs-361-sorting-microservice.onrender.com/sort_ints"

simple_payload = {
    "ints": [3, 2, 1]
}

response = requests.post(url, json=simple_payload)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"\nFailed with status code: {response.status_code}")
    print(response.text)
```

Example sort_objects POST request:
```
import requests

url2 = "https://cs-361-sorting-microservice.onrender.com/sort_objects"

complex_payload = {
    "objs": [
        {"rank": 1, "info": {"example_key": 1}},
        {"rank": 3, "info": {"example_key": 3}},
        {"rank": 4, "info": {"example_key": 4}},
        {"rank": 2, "info": {"example_key": 2}},
    ]
}

response = requests.post(url2, json=complex_payload)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"\nFailed with status code: {response.status_code}")
    print(response.text)
```

## Receiving Data
A JSON object will be returned.

Integer sorting example:
```
{'sorted_array':
    [1, 2, 3]
}
```

JSON sorting example:
```
{'objects':
    [
        {'rank': 1, 'info': {'example_key': 1}},
        {'rank': 2, 'info': {'example_key': 2}},
        {'rank': 3, 'info': {'example_key': 3}},
        {'rank': 4, 'info': {'example_key': 4}}
    ]
}
```