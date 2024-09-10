def criarTabelas(nomePonte, cursor):
    atividade = f'CREATE TABLE {nomePonte}(' \
                f'  ITEM INT Primary Key,' \
                f'  RODOVIA VARCHAR(10) NOT NULL UNIQUE,' \
                f'  MATERIAL VARCHAR(50) NOT NULL UNIQUE,' \
                f'  NOME VARCHAR(100) NOT NULL UNIQUE,' \
                f'  KM DECIMAL(10,8),' \
                f'  EXTENSAO DECIMAL(10,8),' \
                f'  LARGURA DECIMAL (10,8));'
    cursor.execute(atividade)
    cursor.commit()


def inserirValoresNoSQL(nomeTabela, arquivoExcel, cursor):
    atividade = f"""INSERT INTO {nomeTabela} (ITEM, RODOVIA, MATERIAL, NOME, KM, EXTENSÃO, LARGURA)
    (?, ?, ?, ?, ?, ?, ?)"""
