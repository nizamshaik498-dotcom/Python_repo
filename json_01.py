#Created a program using JSON .

import json

student={"name":"Alex","age":25,"course":"CSE"}
result=json.dumps(student)
print(result)
