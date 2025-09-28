# Projeto piadas

Um projeto simples em **Python** que consome uma API pública de piadas utilizando a biblioteca [Requests](https://docs.python-requests.org/) e é gerenciado com [Poetry](https://python-poetry.org/) desenvolvido para aulas de C14, disciplina de Engenharia de Software.

---

## 📦 Requisitos

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/#installation)

---

## 🚀 Como rodar o projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/biancarsouza/piadas.git
   cd piadas
   ```

2. Instale as dependências com o Poetry:
   ```bash
   poetry install
   ```

3. Execute o programa:
   ```bash
   poetry run piadas
   ```

**Exemplo de saída:**
```
😂 Piada do dia:
Why don’t skeletons fight each other?
They don’t have the guts.
```

---

## ⚙️ Como gerar um build

Você pode criar um pacote instalável com:
```bash
poetry build
```

Os artefatos gerados ficarão no diretório `dist/`.

Para instalar o pacote:
```bash
pip install dist/piadas-0.1.0-py3-none-any.whl
```

E rodar diretamente com:
```bash
piadas
```

---

## 🛠 Estrutura do projeto

```
piadas/
 ├─ dist/              # artefatos de build
 ├─ src/piadas/        # código-fonte
 │   ├─ __main__.py    # ponto de entrada da aplicação
 │   └─ __init__.py
 ├─ tests/      
 │   ├─ __main__.py    # arquivo contendo os testes unitários desenvolvidos
 │   └─ __init__.py    
 ├─ pyproject.toml     # config do Poetry
 ├─ poetry.lock        # lockfile das dependências
 ├─ README.md          # documentação do projeto
 └─ .gitignore         # reponsável por não subir certos arquivos existentes no computador
```

---

## 📚 Dependências

- [requests](https://pypi.org/project/requests/) – para fazer chamadas HTTP.

---

## Testes unitários desenvolvidos

1. Casos positivos
- test_main_successful_response - Resposta bem-sucedida da API com piada completa
- test_main_different_joke - Diferentes formatos e conteúdos de piadas
- test_main_special_characters - Caracteres especiais e acentuação em piadas
- test_main_empty_strings - Strings vazias (caso extremo de validação)
- test_main_long_joke - Piadas com texto mais extenso
- test_main_multiple_calls - Múltiplas execuções consecutivas
- test_main_extra_fields - Resposta com campos extras no JSON
- test_main_numeric_values - Valores numéricos nos campos da piada
- test_main_no_exception - Verificação de ausência de exceções
- test_main_normal_operation - Operação padrão do programa

2. Casos negativos
- test_main_404_error - Simula erro HTTP 404 (Não Encontrado)
- test_main_500_error - Simula erro HTTP 500 (Erro Interno)
- test_main_timeout - Timeout na requisição à API
- test_main_connection_error - Erro de conexão com a API
- test_main_json_error - Erro na decodificação do JSON
- test_main_missing_setup - Campo 'setup' faltando na resposta
- test_main_missing_punchline - Campo 'punchline' faltando na resposta
- test_main_empty_json - Resposta com JSON vazio
- test_main_null_values - Valores null nos campos obrigatórios
- test_main_general_exception - Exceções genéricas inesperadas


Para executar os testes:
```bash
# Executar toda a suíte de testes
poetry run python -m unittest discover tests -v

# Executar apenas os testes do arquivo principal
poetry run python -m unittest tests/test_piadas.py -v
```

**Exemplo de saída:**
```
test_main_404_error (test_piadas.TestPiadas.test_main_404_error) ... ok
test_main_500_error (test_piadas.TestPiadas.test_main_500_error) ... ok
test_main_connection_error (test_piadas.TestPiadas.test_main_connection_error) ... ok
...
----------------------------------------------------------------------
Ran 20 tests in 0.025s

OK
```

---

## Resolução de conflitos

- Durante o desenvolvimento, eu e [Lavínia](github.com/laviniaribeiro) criamos alguns conflitos de Merge propositalmente. Tentamos alterar o nome da mesma variável, o que foi resolvido na hora de dar push na segunda alteração para que pudessemos dar merge.
- No desenvolvimento dos testes, [Lavínia](github.com/laviniaribeiro) alterou no arquivo "test_piadas.py" o nome do arquivo de onde estava localizada a main. Para resolver, voltei o nome para o original, já que alterar o nome do arquivo em si como ela colocou me faria alterar mais linhas de código.