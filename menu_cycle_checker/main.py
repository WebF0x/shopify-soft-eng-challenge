import requests

SHOPIFY_CHALLENGE_API_URL = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json"


def get_challenge_json(id, page):
    payload = {"id": id, "page": page}
    response = requests.get(SHOPIFY_CHALLENGE_API_URL, payload)
    return response.json()


def main():
    challenge_json = get_challenge_json(1, 1)
    print(challenge_json)

if __name__ == "__main__":
    main()

