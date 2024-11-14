import sqlite3

# Etapa 1 - Preparação DB
# Conexão e criação da base de dados
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Criação da tabela de livros
cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    ano_publicacao INTEGER NOT NULL)''')
conn.commit()

# Etapa 2 - Funcionalidades
# Função para inserir um novo livro
def inserir_livro(titulo, autor, ano_publicacao):
    cursor.execute('INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (?, ?, ?)',
                   (titulo, autor, ano_publicacao))
    conn.commit()
    print(f"Livro '{titulo}' inserido com sucesso.")

# Função para atualizar informações de um livro
def atualizar_livro(id, novo_titulo=None, novo_autor=None, novo_ano_publicacao=None):
    if novo_titulo:
        cursor.execute('UPDATE livros SET titulo = ? WHERE id = ?', (novo_titulo, id))
    if novo_autor:
        cursor.execute('UPDATE livros SET autor = ? WHERE id = ?', (novo_autor, id))
    if novo_ano_publicacao:
        cursor.execute('UPDATE livros SET ano_publicacao = ? WHERE id = ?', (novo_ano_publicacao, id))
    conn.commit()
    print(f"Livro com ID {id} atualizado com sucesso.")

# Função para remover um livro
def remover_livro(id):
    cursor.execute('DELETE FROM livros WHERE id = ?', (id,))
    conn.commit()
    print(f"Livro com ID {id} removido com sucesso.")

# Função para listar livros publicados após um determinado ano
def listar_livros_apos_ano(ano):
    cursor.execute('SELECT * FROM livros WHERE ano_publicacao > ?', (ano,))
    livros = cursor.fetchall()
    if livros:
        print("Livros publicados após o ano", ano)
        for livro in livros:
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano de Publicação: {livro[3]}")
    else:
        print(f"Nenhum livro encontrado após o ano {ano}.")


# Etapa 3 - Aplicação
# Exemplos de uso:
# Inserir um novo livro
inserir_livro("Harry Potter e a Pedra Filosofal", "----", 2000)

# Atualizar informações de um livro
# atualizar_livro(1, novo_titulo="O Hobbit")

# Remover um livro
# remover_livro(1)

# Listar livros publicados após um determinado ano
listar_livros_apos_ano(1958)

# Fechar a conexão
conn.close()

