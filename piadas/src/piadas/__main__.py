import requests

def main():
    url = "https://official-joke-api.appspot.com/random_joke"
    resp = requests.get(url)

    if resp.status_code == 200:
        joke = resp.json()
        print("😂 Piada do dia:")
        print(joke["setup"])
        print(joke["punchline"])
    else:
        print("Erro ao buscar piada!")

if __name__ == "__main__":
    main()
