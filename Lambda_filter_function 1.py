#Created aprogram using lambda filter function which prints only the names which starts with letter "a".

names=["nizam",",bruce","akshaya","miachel","sam"]
result=list(filter(lambda n:n.startswith("a"),names))
print(result)