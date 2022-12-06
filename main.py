"""
Pull data for the first movie in star wars  # https://swapi.dev/api/films/1
Write the json data into a file named output.txt

SUBTASKS -
1. Output should be only list of names (first name & last name) of characters in the
movie.
2. Output should only print list of planet names used in the movie
3. Output should only print list of vehicle names used in the movie.
"""

import requests

character_name = []
planets_name = []
vehicle_name = []
response = {}
char_ = []
if __name__ == '__main__':
    print(__name__)
    absolute_url = "https://swapi.dev/api/films/1"
    response = requests.get(absolute_url)
    response = response.json()
    str_response = str(response)

    with open('output.txt', 'w') as f_obj:
        content = f_obj.write(str_response)
# print(response)


# character names
for key in response.keys():
    if key == 'characters':
        char_ = response[key]

for i in range(len(char_)):
    # print(char_[i])

    url = char_[i]
    char1 = requests.get(url)
    char1 = char1.json()
    character_name.append(char1['name'])
print("character names in film 1 :", character_name)
print("***"*20)

# planet names
for key in response.keys():
    if key == 'planets':
        char_ = response[key]

for i in range(len(char_)):
    # print(char_[i])

    url = char_[i]
    char1 = requests.get(url)
    char1 = char1.json()
    planets_name.append(char1['name'])
print("planet names in films 1: ", planets_name)
print("***"*20)


# vehicle names
for key in response.keys():
    if key == 'vehicles':
        char_ = response[key]

for i in range(len(char_)):
    # print(char_[i])

    url = char_[i]
    char1 = requests.get(url)
    char1 = char1.json()
    vehicle_name.append(char1['name'])
print("vehicle names in films 1: ", vehicle_name)
print("***"*20)