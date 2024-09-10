import Funcoes
import pyodbc as toSQL
import pandas as pd
import openpyxl

try:
    conexao = toSQL.connect(f'DRIVER={"{ODBC Driver 18 for SQL Server}"};'
                            f'SERVER={"ANTONIO"};'
                            f'DATABASE={"Pontes"}; Trusted_Connection=yes; TrustServerCertificate=yes;')
    cursor = conexao.cursor()
    nomeTabela1 = input("Insira o nome para a tabela das pontes da BR-174: ")
    nomeTabela2 = input("Insira o nome para a tabela das pontes da BR-230: ")
    nomeTabela3 = input("Insira o nome para a tabela das pontes da BR-319: ")
    Funcoes.criarTabelas(nomeTabela1, cursor)
    Funcoes.criarTabelas(nomeTabela2, cursor)
    Funcoes.criarTabelas(nomeTabela3, cursor)
    arquivo174 = pd.read_excel('C:\\Users\\anton\\Downloads\\LISTA ATUALIZADA OAES 2024 - BR-174 (1) (1).xlsx', engine='openpyxl')
    arquivo230 = pd.read_excel('C:\\Users\\anton\\Downloads\\Planilha sem título.xlsx', engine='openpyxl')
    #arquivo319 = pd.read_excel('', engine= 'openpyxl')

except toSQL.Error as e:
    print(f"Não foi possível se conectar ao servidor. Erro: {e}")

finally:
    if conexao:
        cursor.close()
        conexao.close()
        print("Conexão encerrada.")
