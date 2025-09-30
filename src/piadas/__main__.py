import requests

def main():
    url_req = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        resp = requests.get(url_req)
        
        # Verifica se a resposta foi bem sucedida
        if resp.status_code != 200:
            print("Não encontrei nenhuma piada!")
            return
            
        joke = resp.json()
        
        # Verifica se os campos necessários existem e não são None
        if ("setup" in joke and joke["setup"] is not None and 
            "punchline" in joke and joke["punchline"] is not None):
            print("Piada do dia:")
            print(joke["setup"])
            print(joke["punchline"])
        else:
            print("Não encontrei nenhuma piada!")
            
    except requests.exceptions.RequestException:
        # Captura erros de rede, timeout, HTTP errors, etc.
        print("Não encontrei nenhuma piada!")
    except (ValueError, KeyError):
        # Captura erros de JSON decodificação e chaves faltando
        print("Não encontrei nenhuma piada!")
    except Exception:
        # Captura qualquer outra exceção inesperada
        print("Não encontrei nenhuma piada!")

if __name__ == "__main__":
    main()