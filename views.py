"""Interface web do LivroCad."""

import streamlit as st

from controller import ErroValidacao, ServicoLivro
from database import ErroBanco, RepositorioLivro


def _servico() -> ServicoLivro:
    if "servico" not in st.session_state:
        st.session_state.servico = ServicoLivro(RepositorioLivro("livros.db"))
    return st.session_state.servico


def render() -> None:
    st.set_page_config(page_title="LivroCad", page_icon="📚", layout="wide")
    st.title("LivroCad")
    st.caption("Cadastro de livros com Programação Orientada a Objetos e SQLite.")

    try:
        servico = _servico()
    except ErroBanco as exc:
        st.error(str(exc))
        return

    aba_cadastro, aba_lista = st.tabs(["Cadastrar livro", "Acervo"])

    with aba_cadastro:
        _formulario(servico)
    with aba_lista:
        _lista(servico)


def _formulario(servico: ServicoLivro) -> None:
    st.subheader("Novo livro")
    with st.form("form_livro", clear_on_submit=True):
        coluna_a, coluna_b = st.columns(2)
        with coluna_a:
            titulo = st.text_input("Título")
            autor = st.text_input("Autor")
            ano = st.number_input("Ano", min_value=1000, max_value=2100, value=2024)
        with coluna_b:
            isbn = st.text_input("ISBN")
            editora = st.text_input("Editora")
            quantidade = st.number_input("Quantidade", min_value=1, value=1)
        enviado = st.form_submit_button("Salvar livro")

    if not enviado:
        return
    try:
        livro = servico.cadastrar(titulo, autor, ano, isbn, editora, quantidade)
    except ErroValidacao as exc:
        st.warning(str(exc))
    except ErroBanco as exc:
        st.error(str(exc))
    except Exception:
        st.error("Ocorreu um erro inesperado. O cadastro não foi concluído.")
    else:
        st.success(f"Livro salvo: {livro.descricao()}")


def _lista(servico: ServicoLivro) -> None:
    st.subheader("Livros cadastrados")
    try:
        livros = servico.listar()
    except ErroBanco as exc:
        st.error(str(exc))
        return
    except Exception:
        st.error("Não foi possível carregar o acervo.")
        return

    if not livros:
        st.info("Nenhum livro cadastrado ainda.")
        return

    st.dataframe(
        [
            {
                "ISBN": livro.isbn,
                "Título": livro.titulo,
                "Autor": livro.autor,
                "Ano": livro.ano,
                "Editora": livro.editora,
                "Quantidade": livro.quantidade,
            }
            for livro in livros
        ],
        use_container_width=True,
        hide_index=True,
    )
    st.caption(f"Total de livros: {len(livros)}")

    with st.form("form_remover"):
        isbn = st.text_input("ISBN para remover")
        confirmar = st.form_submit_button("Remover livro")
    if not confirmar:
        return
    try:
        servico.remover(isbn)
    except ErroValidacao as exc:
        st.warning(str(exc))
    except ErroBanco as exc:
        st.error(str(exc))
    except Exception:
        st.error("Não foi possível remover o livro.")
    else:
        st.success("Livro removido.")
        st.rerun()
