# LivroCad

Sistema web para cadastrar e consultar livros de um acervo. O projeto aplica Programação Orientada a Objetos, separa as responsabilidades em arquivos diferentes e grava os dados em SQLite.

## Funcionalidades

- Cadastro de livro (título, autor, ano, ISBN, editora e quantidade)
- Listagem do acervo
- Remoção por ISBN
- Validação dos dados e mensagens de erro, sem encerrar o programa
- Testes automáticos da regra de negócio

## Bibliotecas

| Nome | Versão | Uso |
| --- | --- | --- |
| Python | 3.10 ou superior | Linguagem |
| Streamlit | 1.39.0 | Interface web |
| pandas | 2.2.3 | Tabela do acervo |
| sqlite3 | incluso no Python | Banco de dados |
| pytest | 7.4.0 | Testes |

## Estrutura de pastas

```text
livrocad/
├── main.py            ponto de entrada
├── models.py          classes (POO)
├── controller.py      regras de cadastro
├── views.py           telas Streamlit
├── database.py        SQLite
├── requirements.txt
├── README.md
├── DOCUMENTACAO.md    documento técnico
├── apresentacao.html  slides no navegador
└── tests/
    └── test_livro.py
```

A tela não grava no banco. O controlador não desenha a página. O banco não decide se o formulário está válido.

## Como executar

```bash
git clone https://github.com/Reguloslk/livrocad.git
cd livrocad
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -v
streamlit run main.py
```

No Windows, ative o ambiente com `venv\\Scripts\\activate`.

## Publicação

O código fica neste repositório público. A interface web pode ser publicada de graça no Streamlit Community Cloud:

1. Acesse [share.streamlit.io](https://share.streamlit.io) e entre com a conta GitHub.
2. Em **Create app**, escolha o repositório `Reguloslk/livrocad`.
3. Arquivo principal: `main.py`.
4. Clique em **Deploy**.

## POO

- Encapsulamento: atributos com `_` e leitura por propriedades.
- Herança: `Livro` herda de `ItemAcervo`.
- Polimorfismo: `descricao()` é definido na classe filha.
- Abstração: `ItemAcervo` é abstrata e não pode ser instanciada.

## Autor

Artur LK — [Reguloslk](https://github.com/Reguloslk)
