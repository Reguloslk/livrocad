"""Modelos de domínio do LivroCad."""

from abc import ABC, abstractmethod


class ItemAcervo(ABC):
    """Classe abstrata de um item do acervo."""

    def __init__(self, titulo: str, ano: int):
        self._titulo = titulo
        self._ano = ano

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def ano(self) -> int:
        return self._ano

    @abstractmethod
    def descricao(self) -> str:
        """Texto curto do item. Cada subclasse define o próprio formato."""


class Livro(ItemAcervo):
    """Livro do acervo. Herda de ItemAcervo."""

    def __init__(
        self,
        titulo: str,
        autor: str,
        ano: int,
        isbn: str,
        editora: str,
        quantidade: int = 1,
    ):
        super().__init__(titulo, ano)
        self._autor = autor
        self._isbn = isbn
        self._editora = editora
        self._quantidade = quantidade

    @property
    def autor(self) -> str:
        return self._autor

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def editora(self) -> str:
        return self._editora

    @property
    def quantidade(self) -> int:
        return self._quantidade

    @property
    def disponivel(self) -> bool:
        return self._quantidade > 0

    def descricao(self) -> str:
        return f"{self._titulo} - {self._autor} ({self._ano})"

    def marcar_emprestado(self) -> None:
        if self._quantidade <= 0:
            raise ValueError("Sem exemplares disponíveis.")
        self._quantidade -= 1

    def devolver(self) -> None:
        self._quantidade += 1

    def __str__(self) -> str:
        return self.descricao()
