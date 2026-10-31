"""Testes das classes de domínio e da regra de cadastro."""

from controller import ErroValidacao, ServicoLivro
from database import RepositorioLivro
from models import ItemAcervo, Livro


def test_livro_descricao_e_heranca():
    livro = Livro("Dom Casmurro", "Machado de Assis", 1899, "123", "Garnier", 2)
    assert isinstance(livro, ItemAcervo)
    assert livro.descricao() == "Dom Casmurro - Machado de Assis (1899)"
    assert livro.disponivel is True


def test_marcar_emprestado_atualiza_quantidade():
    livro = Livro("1984", "George Orwell", 1949, "456", "Secker", 1)
    livro.marcar_emprestado()
    assert livro.quantidade == 0
    assert livro.disponivel is False


def test_cadastro_rejeita_campo_vazio(tmp_path):
    servico = ServicoLivro(RepositorioLivro(str(tmp_path / "livros.db")))
    try:
        servico.cadastrar("", "Autor", 2020, "999", "Editora", 1)
        raise AssertionError("deveria recusar título vazio")
    except ErroValidacao:
        pass


def test_cadastro_grava_e_lista(tmp_path):
    servico = ServicoLivro(RepositorioLivro(str(tmp_path / "livros.db")))
    servico.cadastrar("O Cortiço", "Aluísio Azevedo", 1890, "789", "Martin Claret", 3)
    livros = servico.listar()
    assert len(livros) == 1
    assert livros[0].titulo == "O Cortiço"
    servico.remover("789")
    assert servico.listar() == []
