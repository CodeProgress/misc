
import requests


def print_ratings_for_all_variants(json_req):
    for variant in json_req["perfs"]:
        print(variant, json_req["perfs"][variant]["rating"])

example_user = "https://en.lichess.org/api/user/thibault"

request = requests.get(example_user)

json_request = request.json()

print_ratings_for_all_variants(json_request)
