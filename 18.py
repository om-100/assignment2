"""Find a package in the Python standard library for dealing with
JSON. Import the library module and inspect the attributes of the
module. Use the help function to learn more about how to use the
module. Serialize a dictionary mapping 'name' to your name and 'age'
to your age, to a JSON string. Deserialize the JSON back into
Python."""

import json

data = {'name': 'om',
        'age': 24,
        'address': 'mulpani'}


json_data = json.dumps(data)

print("JSON Data: \n", json_data)

decoded_data = json.loads(json_data)

print("Decoded Data: \n", decoded_data)