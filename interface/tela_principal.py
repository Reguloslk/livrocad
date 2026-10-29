import tkinter as tk
from tkinter import messagebox, ttk
from persistencia.repositorio_livro import RepositorioLivro
from dominio.livro import Livro


class TelaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("LivroCad - Cadastro de Livros")
        self.root.geometry("700x500")
        self.repo = RepositorioLivro()

        self._criar_widgets()
        self.atualizar_lista()

    def _criar_widgets(self):
        # Frame de cadastro
        frame_cadastro = tk.LabelFrame(self.root, text="Cadastrar Livro", padx=10, pady=10)
        frame_cadastro.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_cadastro, text="Título:").grid(row=0, column=0, sticky="w")
        self.entry_titulo = tk.Entry(frame_cadastro, width=40)
        self.entry_titulo.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_cadastro, text="Autor:").grid(row=1, column=0, sticky="w")
        self.entry_autor = tk.Entry(frame_cadastro, width=40)
        self.entry_autor.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(frame_cadastro, text="Ano:").grid(row=2, column=0, sticky="w")
        self.entry_ano = tk.Entry(frame_cadastro, width=10)
        self.entry_ano.grid(row=2, column=1, sticky="w", padx=5, pady=2)

        tk.Label(frame_cadastro, text="ISBN:").grid(row=3, column=0, sticky="w")
        self.entry_isbn = tk.Entry(frame_cadastro, width=20)
        self.entry_isbn.grid(row=3, column=1, sticky="w", padx=5, pady=2)

        tk.Label(frame_cadastro, text="Editora:").grid(row=4, column=0, sticky="w")
        self.entry_editora = tk.Entry(frame_cadastro, width=40)
        self.entry_editora.grid(row=4, column=1, padx=5, pady=2)

        tk.Label(frame_cadastro, text="Quantidade:").grid(row=5, column=0, sticky="w")
        self.entry_quantidade = tk.Entry(frame_cadastro, width=10)
        self.entry_quantidade.insert(0, "1")
        self.entry_quantidade.grid(row=5, column=1, sticky="w", padx=5, pady=2)

        tk.Button(frame_cadastro, text="Salvar", command=self.salvar_livro).grid(row=6, column=1, sticky="w", pady=5)

        # Frame da lista
        frame_lista = tk.LabelFrame(self.root, text="Livros Cadastrados", padx=10, pady=10)
        frame_lista.pack(fill="both", expand=True, padx=10, pady=5)

        columns = ("isbn", "titulo", "autor", "ano", "editora", "quantidade")
        self.tree = ttk.Treeview(frame_lista, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)
        self.tree.pack(fill="both", expand=True)

        tk.Button(frame_lista, text="Atualizar Lista", command=self.atualizar_lista).pack(pady=5)

    def salvar_livro(self):
        try:
            titulo = self.entry_titulo.get().strip()
            autor = self.entry_autor.get().strip()
            ano = int(self.entry_ano.get().strip())
            isbn = self.entry_isbn.get().strip()
            editora = self.entry_editora.get().strip()
            quantidade = int(self.entry_quantidade.get().strip())

            if not all([titulo, autor, isbn, editora]):
                messagebox.showwarning("Atenção", "Preencha todos os campos.")
                return

            livro = Livro(titulo, autor, ano, isbn, editora, quantidade)
            self.repo.salvar(livro)
            messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
            self.limpar_campos()
            self.atualizar_lista()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {e}")

    def limpar_campos(self):
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_isbn.delete(0, tk.END)
        self.entry_editora.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_quantidade.insert(0, "1")

    def atualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        livros = self.repo.listar_todos()
        for livro in livros:
            self.tree.insert("", tk.END, values=(
                livro.isbn, livro.titulo, livro.autor, livro.ano, livro.editora, livro.quantidade
            ))
