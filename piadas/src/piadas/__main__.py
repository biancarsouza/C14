import requests

def main():
    URL = "https://official-joke-api.appspot.com/random_joke"
    resp = requests.get(URL)

    if resp.status_code == 200:
        joke = resp.json()
        print("Piada do dia:")
        print(joke["setup"])
        print(joke["punchline"])
    else:
        print("Não encontrei nenhuma piada!")

if __name__ == "__main__":
    main()
