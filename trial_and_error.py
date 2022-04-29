import json

#setting_dict = {'logging_encouragement': 2, 'logging_encouragement_counter': 2, 'reminder_start': 1}
# e.g. file = './data.json'
#with open('settings.json', 'w') as f:
#    json.dump(setting_dict, f)

with open('settings.json', 'r') as f:
    data = json.load(f)

print(data)

data['logging_encouragement'] = 1

with open('settings.json', 'w') as f:
    json.dump(data, f)

with open('settings.json', 'r') as f:
    read = json.load(f)

print("read ", read)
