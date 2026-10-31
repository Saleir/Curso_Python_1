
import requests
import tkinter as tk
from tkinter import ttk, messagebox

# ==========================================
# 1. BUSCAR DADOS NA API FAKESTORE
# ==========================================

try:
    resposta = requests.get(
        'https://fakestoreapi.com/products',
        timeout=10
    )

    resposta.raise_for_status()
    produtos = resposta.json()

except requests.RequestException as erro:
    produtos = []
    print(f'Erro ao acessar API: {erro}')


# ==========================================
# 2. CRIAR JANELA PRINCIPAL
# ==========================================

janela = tk.Tk()
janela.title('CATÁLOGO DE PRODUTOS - FAKE STORE')
janela.geometry('1100x650')
janela.configure(bg='#1e293b')

# ==========================================
# 3. TÍTULO
# ==========================================

titulo = tk.Label(
    janela,
    text='CATÁLOGO DE PRODUTOS',
    font=('Arial', 22, 'bold'),
    bg='#1e293b',
    fg='white'
)

titulo.pack(pady=20)


# ==========================================
# 4. CAMPO DE PESQUISA
# ==========================================

frame_pesquisa = tk.Frame(janela, bg='#1e293b')
frame_pesquisa.pack(fill='x', padx=25, pady=10)

label_pesquisa = tk.Label(
    frame_pesquisa,
    text='Pesquisar produto:',
    font=('Arial', 11, 'bold'),
    bg='#1e293b',
    fg='white'
)

label_pesquisa.pack(side='left', padx=5)

campo_pesquisa = tk.Entry(
    frame_pesquisa,
    font=('Arial', 12),
    width=45
)

campo_pesquisa.pack(side='left', padx=10, ipady=5)


# ==========================================
# 5. FRAME DA TABELA
# ==========================================

frame_tabela = tk.Frame(janela, bg='#1e293b')
frame_tabela.pack(fill='both', expand=True, padx=25, pady=10)

colunas = ('ID', 'PRODUTO', 'PREÇO R$')

tabela = ttk.Treeview(
    frame_tabela,
    columns=colunas,
    show='headings'
)

# Cabeçalhos
tabela.heading('ID', text='ID')
tabela.heading('PRODUTO', text='PRODUTO')
tabela.heading('PREÇO R$', text='PREÇO R$')

# Largura das colunas
tabela.column('ID', width=70, anchor='center')
tabela.column('PRODUTO', width=800, anchor='w')
tabela.column('PREÇO R$', width=130, anchor='center')

# Estilização
estilo = ttk.Style()
estilo.theme_use('clam')

estilo.configure(
    'Treeview',
    background='#f1f5f9',
    foreground='#1e293b',
    rowheight=35,
    font=('Arial', 10)
)

estilo.configure(
    'Treeview.Heading',
    background='#2563eb',
    foreground='white',
    font=('Arial', 10, 'bold')
)

estilo.map(
    'Treeview',
    background=[('selected', '#93c5fd')],
    foreground=[('selected', '#000000')]
)

# Barra de rolagem
scroll = ttk.Scrollbar(
    frame_tabela,
    orient='vertical',
    command=tabela.yview
)

tabela.configure(yscrollcommand=scroll.set)

tabela.pack(side='left', fill='both', expand=True)
scroll.pack(side='right', fill='y')


# ==========================================
# 6. FUNÇÃO PARA EXIBIR PRODUTOS
# ==========================================

def exibir_produtos(lista):

    # Limpar tabela
    for item in tabela.get_children():
        tabela.delete(item)

    # Inserir produtos
    for produto in lista:

        id_produto = produto['id']
        nome = produto['title']
        preco = produto['price']

        tabela.insert(
            '',
            'end',
            values=(
                id_produto,
                nome,
                f'R$ {preco:.2f}'
            )
        )

    # Atualizar contador
    contador.config(
        text=f'Produtos encontrados: {len(lista)}'
    )


# ==========================================
# 7. FUNÇÃO DE PESQUISA
# ==========================================

def pesquisar_produto(event=None):

    pesquisa = campo_pesquisa.get().strip().lower()

    resultados = []

    for produto in produtos:

        nome = produto['title'].lower()
        id_produto = str(produto['id'])

        if pesquisa in nome or pesquisa in id_produto:
            resultados.append(produto)

    exibir_produtos(resultados)


# ==========================================
# 8. FUNÇÃO LIMPAR PESQUISA
# ==========================================

def limpar_pesquisa():

    campo_pesquisa.delete(0, tk.END)

    exibir_produtos(produtos)


# ==========================================
# 9. BOTÕES DE PESQUISA
# ==========================================

botao_pesquisar = tk.Button(
    frame_pesquisa,
    text='PESQUISAR',
    font=('Arial', 10, 'bold'),
    bg='#2563eb',
    fg='white',
    activebackground='#1d4ed8',
    command=pesquisar_produto,
    cursor='hand2'
)

botao_pesquisar.pack(side='left', padx=5, ipady=5)

botao_limpar = tk.Button(
    frame_pesquisa,
    text='LIMPAR',
    font=('Arial', 10, 'bold'),
    bg='#64748b',
    fg='white',
    activebackground='#475569',
    command=limpar_pesquisa,
    cursor='hand2'
)

botao_limpar.pack(side='left', padx=5, ipady=5)


# ==========================================
# 10. PESQUISAR AUTOMATICAMENTE AO DIGITAR
# ==========================================

campo_pesquisa.bind(
    '<KeyRelease>',
    pesquisar_produto
)


# ==========================================
# 11. CONTADOR DE PRODUTOS
# ==========================================

contador = tk.Label(
    janela,
    text='',
    font=('Arial', 11, 'bold'),
    bg='#1e293b',
    fg='white'
)

contador.pack(pady=15)


# ==========================================
# 12. CARREGAR PRODUTOS NA ABERTURA
# ==========================================

exibir_produtos(produtos)


# ==========================================
# 13. EXECUTAR A APLICAÇÃO
# ==========================================

if not produtos:
    messagebox.showwarning(
        'Aviso',
        'Não foi possível carregar os produtos da API.'
    )

janela.mainloop()
