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
 ├─ tests/             # pasta vazia para futuros testes
 ├─ pyproject.toml     # config do Poetry
 ├─ poetry.lock        # lockfile das dependências
 └─ README.md          # documentação do projeto
```

---

## 📚 Dependências

- [requests](https://pypi.org/project/requests/) – para fazer chamadas HTTP.