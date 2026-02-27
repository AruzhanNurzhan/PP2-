import json
with open('sample-data.json') as file:
    data = json.load(file)
print("Interface Status")
print("=" * 64)
print("DN".ljust(50),"Description ".ljust(20),"Speed".ljust(6),"MTU".ljust(6))
print("-" * 82)
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = str(attributes["mtu"])
    print(dn.ljust(50), "".ljust(20), speed.ljust(6), mtu.ljust(6))
