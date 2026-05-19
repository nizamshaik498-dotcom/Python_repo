#created a program using json into file.

import json

flights={"name":"Emirates Airbus","model":"A380"}
with open("flights.json","w") as file:
    json.dump(flights, file)


with open("flights.json","r") as file:
    flights=json.load(file)
    print(flights)