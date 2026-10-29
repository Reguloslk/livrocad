import streamlit as st
import pandas as pd
from dominio.livro import Livro
from persistencia.repositorio_livro import RepositorioLivro

st.set_page_config(page_title="LivroCad", page_icon="📚", layout="wide")

st.title("📚 LivroCad")
st.markdown("Sistema de cadastro e gerenciamento de livros (POO + Streamlit)")

# Inicializa o repositório
if "repo" not in st.session_state:
    st.session_state.repo = RepositorioLivro()

repo = st.session_state.repo

tab1, tab2 = st.tabs(["📝 Cadastrar Livro", "📋 Lista de Livros"])

with tab1:
    st.subheader("Cadastrar novo livro")
    with st.form("form_livro"):
        col1, col2 = st.columns(2)
        with col1:
            titulo = st.text_input("Título *")
            autor = st.text_input("Autor *")
            ano = st.number_input("Ano *", min_value=1000, max_value=2100, value=2024)
        with col2:
            isbn = st.text_input("ISBN *")
            editora = st.text_input("Editora *")
            quantidade = st.number_input("Quantidade *", min_value=1, value=1)

        submitted = st.form_submit_button("Salvar Livro")

        if submitted:
            if not all([titulo, autor, isbn, editora]):
                st.error("Preencha todos os campos obrigatórios.")
            else:
                try:
                    livro = Livro(titulo, autor, int(ano), isbn, editora, int(quantidade))
                    repo.salvar(livro)
                    st.success(f"Livro '{titulo}' cadastrado com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao salvar: {e}")

with tab2:
    st.subheader("Livros cadastrados")
    livros = repo.listar_todos()

    if not livros:
        st.info("Nenhum livro cadastrado ainda.")
    else:
        dados = []
        for livro in livros:
            dados.append({
                "ISBN": livro.isbn,
                "Título": livro.titulo,
                "Autor": livro.autor,
                "Ano": livro.ano,
                "Editora": livro.editora,
                "Quantidade": livro.quantidade,
            })
        df = pd.DataFrame(dados)
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.caption(f"Total de livros: {len(livros)}")
