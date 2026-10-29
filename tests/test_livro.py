import pytest
from dominio.livro import Livro, ItemAcervo


def test_livro_descricao():
    livro = Livro("Dom Casmurro", "Machado de Assis", 1899, "1234567890", "Editora XYZ", 2)
    assert "Dom Casmurro - Machado de Assis (1899)" in livro.descricao()
    assert livro.titulo == "Dom Casmurro"


def test_livro_emprestar():
    livro = Livro("1984", "George Orwell", 1949, "0987654321", "Editora ABC", 1)
    assert livro.disponivel is True
    livro.marcar_emprestado()
    assert livro.quantidade == 0
    assert livro.disponivel is False


def test_livro_heranca():
    livro = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "1111111111", "Editora", 3)
    assert isinstance(livro, ItemAcervo)
    assert livro.ano == 1943
