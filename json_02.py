#Created a program which converts an JSON to python.

import json

data='{"name":"alex","age":20}'
result=json.loads(data)
print(result)