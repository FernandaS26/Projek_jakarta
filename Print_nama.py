import json

with open('DatabaseName.json') as json_file:
    data = json.load(json_file)

name_list = data["name_list"]

print ("Nama Anggota Kelompok Jakarta")
for name in name_list:
    print(name)