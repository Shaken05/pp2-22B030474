import json

file = open('data.json', 'r')
data = json.load(file)

print("Interface Status\n\
================================================================================")
print("""DN                                                 Description           Speed    MTU \n\
-------------------------------------------------- --------------------  ------  ------ """)

for i in data["imdata"] :
    print(i["l1PhysIf"]["attributes"]["dn"], end="       \t")
    print(i["l1PhysIf"]["attributes"]["descr"], end="         \t")
    print(i["l1PhysIf"]["attributes"]["speed"], end="   ")
    print(i["l1PhysIf"]["attributes"]["mtu"], end="\n")
    
"""print("{DN:50}{Speed:>30}{MTU:>6}".format(DN=i["l1PhysIf"]["attributes"]["dn"],) Speed=(i["l1PhysIf"]["attribut""es"]["descr"])"""
