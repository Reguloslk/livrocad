import sqlite3
from dominio.livro import Livro


class RepositorioLivro:
    def __init__(self, db_path="livros.db"):
        self.conn = sqlite3.connect(db_path)
        self._criar_tabela()

    def _criar_tabela(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                isbn TEXT PRIMARY KEY,
                titulo TEXT,
                autor TEXT,
                ano INTEGER,
                editora TEXT,
                quantidade INTEGER
            )
        """)
        self.conn.commit()

    def salvar(self, livro: Livro):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO livros (isbn, titulo, autor, ano, editora, quantidade)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (livro.isbn, livro.titulo, livro.autor, livro.ano, livro.editora, livro.quantidade))
        self.conn.commit()

    def listar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT isbn, titulo, autor, ano, editora, quantidade FROM livros")
        rows = cursor.fetchall()
        livros = []
        for row in rows:
            livro = Livro(
                titulo=row[1],
                autor=row[2],
                ano=row[3],
                isbn=row[0],
                editora=row[4],
                quantidade=row[5]
            )
            livros.append(livro)
        return livros

    def buscar_por_isbn(self, isbn: str):
        cursor = self.conn.cursor()
        cursor.execute("SELECT isbn, titulo, autor, ano, editora, quantidade FROM livros WHERE isbn = ?", (isbn,))
        row = cursor.fetchone()
        if row:
            return Livro(
                titulo=row[1],
                autor=row[2],
                ano=row[3],
                isbn=row[0],
                editora=row[4],
                quantidade=row[5]
            )
        return None

    def deletar(self, isbn: str):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM livros WHERE isbn = ?", (isbn,))
        self.conn.commit()
        return cursor.rowcount > 0

    def fechar(self):
        self.conn.close()
