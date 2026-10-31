# Documento técnico — LivroCad

## 1. Objetivo

O LivroCad é um sistema de cadastro de livros. A bibliotecária ou o aluno informa os dados do livro, o sistema valida, grava no banco e permite consultar e remover itens do acervo.

## 2. Requisitos atendidos

- Repositório público no GitHub, com vários commits.
- Programação Orientada a Objetos.
- Arquivos separados: `main.py`, `models.py`, `views.py`, `controller.py` e `database.py`.
- Interface web funcional.
- Banco SQLite operacional.
- Tratamento de erros para dados inválidos e falha de banco.
- README com instalação, execução e funcionalidades.

## 3. Arquitetura

| Arquivo | Responsabilidade |
| --- | --- |
| `main.py` | Sobe a aplicação |
| `views.py` | Formulário e tabela. Não contém SQL |
| `controller.py` | Valida os dados e chama o repositório |
| `models.py` | Classes `ItemAcervo` e `Livro` |
| `database.py` | Cria a tabela, grava, lista e remove |

Fluxo: a tela chama o serviço, o serviço cria um `Livro` e pede ao repositório para gravar.

## 4. Modelo conceitual

Entidade **Livro**

- isbn: identificador único (**PK**)
- titulo
- autor
- ano
- editora
- quantidade

Não há outra tabela, então não existe chave estrangeira (**FK**).

## 5. Modelo físico

SGBD: **SQLite**

```sql
CREATE TABLE IF NOT EXISTS livros (
    isbn TEXT PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    editora TEXT NOT NULL,
    quantidade INTEGER NOT NULL
);
```

As consultas usam parâmetros (`?`), então o texto digitado não é concatenado no SQL.

## 6. POO

- **Abstração:** `ItemAcervo` declara `descricao()` sem implementar.
- **Herança:** `Livro` recebe título e ano da classe pai.
- **Encapsulamento:** `_titulo`, `_isbn` e os demais atributos só são lidos por propriedades.
- **Polimorfismo:** quem usa um `ItemAcervo` chama `descricao()` sem precisar saber se o objeto é um livro.

## 7. Tratamento de erros

- Campo vazio, ano fora do intervalo ou quantidade menor que 1 geram `ErroValidacao`. A tela mostra um aviso.
- Falha ao abrir ou gravar o SQLite gera `ErroBanco`. A tela mostra o erro e continua aberta.
- Qualquer outra falha inesperada é capturada na interface para o processo não encerrar.

## 8. Testes

O arquivo `tests/test_livro.py` cobre herança, descrição, empréstimo de exemplar, recusa de cadastro vazio e gravação no banco temporário.

```bash
pytest -v
```

## 9. Como executar

```bash
pip install -r requirements.txt
pytest -v
streamlit run main.py
```

## 10. Publicação

Repositório: https://github.com/Reguloslk/livrocad

A aplicação web é publicada no Streamlit Community Cloud, com o arquivo principal `main.py`.

## 11. Limitações

O SQLite fica no arquivo `livros.db` da máquina que executa o programa. Em uma hospedagem gratuita, o arquivo pode ser recriado quando o servidor reinicia. Para um uso contínuo com muitos usuários, o próximo passo seria um banco hospedado.
