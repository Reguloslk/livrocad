"""Regras de cadastro. A tela não acessa o banco diretamente."""

from database import RepositorioLivro
from models import Livro


class ErroValidacao(Exception):
    """Dados do formulário inválidos."""


class ServicoLivro:
    """Orquestra validação e persistência."""

    def __init__(self, repositorio: RepositorioLivro):
        self._repositorio = repositorio

    def cadastrar(self, titulo, autor, ano, isbn, editora, quantidade) -> Livro:
        titulo = (titulo or "").strip()
        autor = (autor or "").strip()
        isbn = (isbn or "").strip()
        editora = (editora or "").strip()
        if not all([titulo, autor, isbn, editora]):
            raise ErroValidacao("Preencha título, autor, ISBN e editora.")
        try:
            ano = int(ano)
            quantidade = int(quantidade)
        except (TypeError, ValueError) as exc:
            raise ErroValidacao("Ano e quantidade precisam ser números.") from exc
        if ano < 1000 or ano > 2100:
            raise ErroValidacao("Informe um ano entre 1000 e 2100.")
        if quantidade < 1:
            raise ErroValidacao("A quantidade deve ser pelo menos 1.")
        livro = Livro(titulo, autor, ano, isbn, editora, quantidade)
        self._repositorio.salvar(livro)
        return livro

    def listar(self):
        return self._repositorio.listar_todos()

    def remover(self, isbn: str) -> None:
        isbn = (isbn or "").strip()
        if not isbn:
            raise ErroValidacao("Informe o ISBN para remover.")
        if not self._repositorio.remover(isbn):
            raise ErroValidacao("Nenhum livro encontrado com esse ISBN.")
