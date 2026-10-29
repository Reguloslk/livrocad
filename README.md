# LivroCad

Sistema de cadastro e gerenciamento de livros desenvolvido em Python aplicando os princípios de Programação Orientada a Objetos (POO): encapsulamento, herança, polimorfismo e abstração.

A aplicação permite cadastrar livros, listá-los e gerenciar o acervo de forma simples, com interface gráfica em Tkinter e persistência em SQLite.

## Bibliotecas utilizadas

| Nome | Versão | Uso |
|------|--------|-----|
| Python | 3.10+ | Linguagem principal |
| tkinter | incluso no Python | Interface gráfica |
| sqlite3 | incluso no Python | Banco de dados local |
| pytest | 7.4.0 | Testes unitários |

## Estrutura de pastas

```
livrocad/
│
├── main.py                  # Ponto de entrada da aplicação
├── README.md
├── requirements.txt
│
├── dominio/                 # Lógica de negócio (POO)
│   ├── __init__.py
│   └── livro.py             # Classes ItemAcervo (abstrata) e Livro
│
├── persistencia/            # Acesso ao banco de dados
│   ├── __init__.py
│   └── repositorio_livro.py # Repositório SQLite
│
├── interface/               # Interface gráfica (Tkinter)
│   ├── __init__.py
│   └── tela_principal.py    # Tela principal de cadastro e listagem
│
└── tests/
    └── test_livro.py        # Testes das classes de domínio
```

## Como executar

```bash
# Clone o repositório
git clone https://github.com/Reguloslk/livrocad.git
cd livrocad

# (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows

# Instale as dependências (apenas pytest)
pip install -r requirements.txt

# Execute os testes
pytest -v

# Inicie a aplicação
python main.py
```

## Princípios de POO aplicados

- **Encapsulamento**: Atributos protegidos com `_` e acesso via properties.
- **Herança**: `Livro` herda de `ItemAcervo`.
- **Polimorfismo**: Método `descricao()` sobrescrito na classe filha.
- **Abstração**: Classe `ItemAcervo` é abstrata e não pode ser instanciada.

## Prints do programa funcionando

*(Adicione aqui os prints da tela de cadastro, lista de livros e resultado dos testes)*

## Autor

Reguloslk / Artur LK
