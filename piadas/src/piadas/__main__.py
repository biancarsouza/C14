import requests

def main():
    url_req = "https://official-joke-api.appspot.com/random_joke"
    resp = requests.get(url_req)

    if resp.status_code == 200:
        joke = resp.json()
        print("Piada do dia:")
        print(joke["setup"])
        print(joke["punchline"])
    else:
        print("Não encontrei nenhuma piada!")

if __name__ == "__main__":
    main()
