"""
TASK1 / PROBLEM STATEMENT

THe star wars API lists 82 characters in stars wars series. For the first task
we have to create a random number generator. The random number generator should
fetch numbers between 1-82. Using these random numbers we have to fetch random
15 characters from API using `requests` lib.
"""
from utils.randgen import produce_characters
import requests

start = 1
stop = 15

obj = produce_characters()
characters = []

for i in range(start, stop+1):
    characters.append(next(obj))


home_url = "https://swapi.dev"
relative = "/api/people/{0}"  # magic string



if __name__ == '__main__':
    print(__name__)
    print("current module getting executed")
    for num_ in characters:
        absolute_url = home_url + relative.format(num_)
        print(f"fetching details using - {absolute_url}  =>\n")
        response = requests.get(absolute_url)
        response = response.json()
        print(response)
        print("######" * 20)
