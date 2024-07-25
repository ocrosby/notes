# This illustrates how to make an http request using the Python standard library
# This illustrates how to make an http request using the Python standard library

import http.client

# Step 2: Establish a connection
conn = http.client.HTTPSConnection("www.example.com")

# Step 3: Send a GET request
conn.request("GET", "/")

# Step 4: Get the response
response = conn.getresponse()

# Step 5 & 6: Read and decode the response content
data = response.read().decode("utf-8")

# Print the response content
print(data)
