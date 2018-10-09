import json

#block IDs
with open('block_ids.json', 'r') as data_file:
    json_data = data_file.read()
data = json.loads(json_data)

f = open('block_ids_out.json','w+')
for id in data.keys():
    f.write('"' + id + '",\r\n')
f.close()

#item IDs
with open('block_ids.json', 'r') as data_file:
    json_data = data_file.read()
data = json.loads(json_data)

f = open('item_ids_out.json','w+')
for id in data.keys():
    f.write('"' + id + '",\r\n')
f.close()
