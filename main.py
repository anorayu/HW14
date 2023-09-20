import json

with open('ваш_файл.json', 'r') as file:
    data = json.load(file)

for i, dictionary in enumerate(data):
    with open(f'файл_{i}.json', 'w') as file:
        json.dump(dictionary, file)
