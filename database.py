"""Persistência dos livros em SQLite."""

import sqlite3

from models import Livro


class ErroBanco(Exception):
    """Falha ao gravar ou ler o banco."""


class RepositorioLivro:
    """Acesso à tabela livros. Não valida regra de negócio."""

    def __init__(self, db_path: str = "livros.db"):
        try:
            self.conn = sqlite3.connect(db_path, check_same_thread=False)
            self._criar_tabela()
        except sqlite3.Error as exc:
            raise ErroBanco("Não foi possível abrir o banco de dados.") from exc

    def _criar_tabela(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS livros (
                isbn TEXT PRIMARY KEY,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano INTEGER NOT NULL,
                editora TEXT NOT NULL,
                quantidade INTEGER NOT NULL
            )
            """
        )
        self.conn.commit()

    def salvar(self, livro: Livro) -> None:
        try:
            self.conn.execute(
                """
                INSERT INTO livros
                    (isbn, titulo, autor, ano, editora, quantidade)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(isbn) DO UPDATE SET
                    titulo = excluded.titulo,
                    autor = excluded.autor,
                    ano = excluded.ano,
                    editora = excluded.editora,
                    quantidade = excluded.quantidade
                """,
                (
                    livro.isbn,
                    livro.titulo,
                    livro.autor,
                    livro.ano,
                    livro.editora,
                    livro.quantidade,
                ),
            )
            self.conn.commit()
        except sqlite3.Error as exc:
            self.conn.rollback()
            raise ErroBanco("Não foi possível salvar o livro.") from exc

    def listar_todos(self) -> list:
        try:
            cursor = self.conn.execute(
                """
                SELECT isbn, titulo, autor, ano, editora, quantidade
                FROM livros
                ORDER BY titulo
                """
            )
            return [self._para_livro(row) for row in cursor.fetchall()]
        except sqlite3.Error as exc:
            raise ErroBanco("Não foi possível listar os livros.") from exc

    def remover(self, isbn: str) -> bool:
        try:
            cursor = self.conn.execute(
                "DELETE FROM livros WHERE isbn = ?",
                (isbn,),
            )
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as exc:
            self.conn.rollback()
            raise ErroBanco("Não foi possível remover o livro.") from exc

    @staticmethod
    def _para_livro(row) -> Livro:
        return Livro(
            titulo=row[1],
            autor=row[2],
            ano=row[3],
            isbn=row[0],
            editora=row[4],
            quantidade=row[5],
        )
