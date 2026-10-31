
import requests
import tkinter as tk
from tkinter import messagebox, ttk

# Lista de produtos
produtos_carregados = []


# ==========================================
# FUNÇÃO DE PESQUISA
# ==========================================

def buscar_produtos(event=None):

    termo = campo_busca.get().strip().casefold()

    # Limpar tabela
    tabela.delete(*tabela.get_children())

    # Percorrer produtos
    for produto in produtos_carregados:

        id_produto = str(produto['id'])
        nome = produto['title']
        categoria = produto['category']
        preco = produto['price']

        # Filtrar por ID, nome ou categoria
        if (
            termo in id_produto.casefold()
            or termo in nome.casefold()
            or termo in categoria.casefold()
        ):

            tabela.insert(
                '',
                'end',
                values=(
                    id_produto,
                    nome,
                    categoria,
                    f'R$ {preco:.2f}'
                )
            )

    # Atualizar contador
    contador.config(
        text=f'Produtos encontrados: {len(tabela.get_children())}'
    )


# ==========================================
# FUNÇÃO PARA CARREGAR PRODUTOS
# ==========================================

def carregar_produtos():

    try:

        resposta = requests.get(
            'https://fakestoreapi.com/products',
            timeout=15
        )

        resposta.raise_for_status()

        produtos = resposta.json()

        # Atualizar lista
        produtos_carregados.clear()
        produtos_carregados.extend(produtos)

        # Exibir produtos
        buscar_produtos()

    except (requests.RequestException, ValueError, KeyError) as erro:

        messagebox.showerror(
            'Erro',
            f'Não foi possível carregar os produtos:\n{erro}'
        )


# ==========================================
# JANELA PRINCIPAL
# ==========================================

janela = tk.Tk()

janela.title('Produtos da Fake Store API')
janela.geometry('1050x550')
janela.configure(bg='blue')


# ==========================================
# ESTILIZAÇÃO
# ==========================================

estilo = ttk.Style()

estilo.theme_use('clam')

estilo.configure(
    'Fundo.TFrame',
    background='yellow'
)

estilo.configure(
    'Fundo.TLabel',
    background='red',
    foreground='white',
    font=('Arial', 11, 'bold')
)

estilo.configure(
    'Treeview',
    background='#222222',
    fieldbackground='#222222',
    foreground='white',
    rowheight=30,
    font=('Arial', 10)
)

estilo.configure(
    'Treeview.Heading',
    background='red',
    foreground='white',
    font=('Arial', 10, 'bold')
)

estilo.map(
    'Treeview',
    background=[('selected', 'blue')],
    foreground=[('selected', 'white')]
)


# ==========================================
# TÍTULO
# ==========================================

ttk.Label(
    janela,
    text='LISTA DE PRODUTOS',
    font=('Arial', 18, 'bold'),
    style='Fundo.TLabel'
).pack(pady=15)


# ==========================================
# CAMPO DE PESQUISA
# ==========================================

ttk.Label(
    janela,
    text='Buscar produto, ID ou categoria:',
    style='Fundo.TLabel'
).pack(anchor='w', padx=10)

campo_busca = ttk.Entry(
    janela,
    font=('Arial', 12)
)

campo_busca.pack(fill='x', padx=10, pady=5)

campo_busca.bind(
    '<KeyRelease>',
    buscar_produtos
)


# ==========================================
# FRAME DA TABELA
# ==========================================

frame = ttk.Frame(
    janela,
    style='Fundo.TFrame'
)

frame.pack(
    fill='both',
    expand=True,
    padx=10,
    pady=10
)


# ==========================================
# CRIAR TABELA
# ==========================================

colunas = ('id', 'produto', 'categoria', 'preco')

tabela = ttk.Treeview(
    frame,
    columns=colunas,
    show='headings'
)

# Cabeçalhos
tabela.heading('id', text='ID')
tabela.heading('produto', text='PRODUTO')
tabela.heading('categoria', text='CATEGORIA')
tabela.heading('preco', text='PREÇO')

# Largura das colunas
tabela.column('id', width=50, anchor='center')
tabela.column('produto', width=550, anchor='w')
tabela.column('categoria', width=200, anchor='center')
tabela.column('preco', width=100, anchor='e')


# ==========================================
# BARRA DE ROLAGEM
# ==========================================

barra_rolagem = ttk.Scrollbar(
    frame,
    orient='vertical',
    command=tabela.yview
)

tabela.configure(
    yscrollcommand=barra_rolagem.set
)

tabela.pack(
    side='left',
    fill='both',
    expand=True
)

barra_rolagem.pack(
    side='right',
    fill='y'
)


# ==========================================
# CONTADOR
# ==========================================

contador = ttk.Label(
    janela,
    text='Produtos encontrados: 0',
    style='Fundo.TLabel'
)

contador.pack(pady=10)


# ==========================================
# CARREGAR E EXECUTAR
# ==========================================

carregar_produtos()

janela.mainloop()
