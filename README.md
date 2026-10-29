# LivroCad

Sistema de cadastro e gerenciamento de livros desenvolvido em Python aplicando os princípios de Programação Orientada a Objetos (POO): encapsulamento, herança, polimorfismo e abstração.

A aplicação foi adaptada para rodar na **web com Streamlit**, facilitando a publicação e demonstração.

## Bibliotecas utilizadas

| Nome | Versão | Uso |
|------|--------|-----|
| Python | 3.10+ | Linguagem principal |
| Streamlit | 1.39.0 | Interface web |
| pandas | 2.2.3 | Exibição da tabela de livros |
| sqlite3 | incluso no Python | Banco de dados local |
| pytest | 7.4.0 | Testes unitários |

## Estrutura de pastas

```
livrocad/
├── app.py                    # Aplicação Streamlit (interface web)
├── main.py                   # Versão desktop (Tkinter) - opcional
├── README.md
├── requirements.txt
├── dominio/
│   ├── __init__.py
│   └── livro.py
├── persistencia/
│   ├── __init__.py
│   └── repositorio_livro.py
└── tests/
    └── test_livro.py
```

## Como executar localmente

```bash
git clone https://github.com/Reguloslk/livrocad.git
cd livrocad

pip install -r requirements.txt

# Executar a versão web
streamlit run app.py
```

## Publicação no Streamlit Community Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io)
2. Faça login com sua conta GitHub
3. Clique em **New app**
4. Selecione o repositório `Reguloslk/livrocad`
5. Defina o arquivo principal como `app.py`
6. Clique em **Deploy**

## Princípios de POO aplicados

- **Encapsulamento**: Atributos protegidos com `_` e acesso via properties.
- **Herança**: `Livro` herda de `ItemAcervo`.
- **Polimorfismo**: Método `descricao()` sobrescrito na classe filha.
- **Abstração**: Classe `ItemAcervo` é abstrata e não pode ser instanciada.

## Autor

Reguloslk / Artur LK
