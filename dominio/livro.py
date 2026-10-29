from abc import ABC, abstractmethod


class ItemAcervo(ABC):
    """Classe abstrata – demonstra abstração"""

    def __init__(self, titulo: str, ano: int):
        self._titulo = titulo          # encapsulamento
        self._ano = ano

    @abstractmethod
    def descricao(self) -> str:
        pass

    @property
    def titulo(self):
        return self._titulo

    @property
    def ano(self):
        return self._ano


class Livro(ItemAcervo):
    """Herda de ItemAcervo – demonstra herança e polimorfismo"""

    def __init__(self, titulo: str, autor: str, ano: int, isbn: str, editora: str, quantidade: int = 1):
        super().__init__(titulo, ano)
        self._autor = autor
        self._isbn = isbn
        self._editora = editora
        self._quantidade = quantidade
        self._disponivel = True

    @property
    def autor(self):
        return self._autor

    @property
    def isbn(self):
        return self._isbn

    @property
    def editora(self):
        return self._editora

    @property
    def quantidade(self):
        return self._quantidade

    @property
    def disponivel(self):
        return self._disponivel

    def descricao(self) -> str:          # polimorfismo
        return f"{self._titulo} - {self._autor} ({self._ano})"

    def marcar_emprestado(self):
        if self._quantidade > 0:
            self._quantidade -= 1
            self._disponivel = self._quantidade > 0
        else:
            raise ValueError("Sem exemplares disponíveis")

    def devolver(self):
        self._quantidade += 1
        self._disponivel = True

    def __str__(self):
        return self.descricao()
