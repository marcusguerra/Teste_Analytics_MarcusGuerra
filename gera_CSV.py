import csv
import random
from datetime import datetime, timedelta, time
import uuid


def gera_csv(arquivo_csv, produtos_categorias_quantidade, total_itens):

    #número máximo de itens é 20
    faixa_quantidade = (1, 20)

    data_inicial = datetime(2023, 1, 1)
    data_final = datetime(2023, 12, 31)

    with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as arquivo:
        csv_output = csv.writer(arquivo)
        csv_output.writerow(["ID", "Produto", "Categoria", "Preço", "Quantidade", "Data"])

        for i in range(1, total_itens):
            #Gera um ID aleatorio para a chave principal
            ID = str(uuid.uuid4())
            produto = random.choice(list(produtos_categorias_quantidade.keys()))
            categoria = produtos_categorias_quantidade[produto]["categoria"]


            preco = produtos_categorias_precos[produto]["preco"]

            #* descompacta os valores para poderem ser utilizados
            quantidade = random.randint(*faixa_quantidade)

            data = data_inicial + timedelta(days=random.randint(0, (data_final - data_inicial).days))

            #Como a loja só fica aberta das 8:00h até as 20:00h é importante que os horários
            #não passem disso
            hora = random.randint(8, 19)
            minuto = random.randint(0, 59)
            data_hora = data.replace(hour=hora, minute=minuto)

            csv_output.writerow([ID, produto, categoria, preco, quantidade, data_hora.strftime("%d/%m/%Y %H:%M")])

#Isso é base de todos os produtos, onde um produto está relacionado a uma
# categoria e a um preço
Produto_Categoria_Quantidade = produtos_categorias_precos = {
        "Samsung Galaxy S23": {"categoria": "Smartphones", "preco": 4000,},
        "iPhone 14 Pro": {"categoria": "Smartphones", "preco": 8000},
        "Notebook Dell": {"categoria": "Laptops", "preco": 5000},
        "MacBook Air": {"categoria": "Laptops", "preco": 12000},
        "Fone de Ouvido JBL": {"categoria": "Áudio", "preco": 400},
        "Teclado Mecânico Razer": {"categoria": "Acessórios", "preco": 700},
        "Mouse Razer": {"categoria": "Acessórios", "preco": 500},
        "Smart TV LG 4K 55''": {"categoria": "Eletrônicos", "preco": 3000},
        "Caixa de Som JBL": {"categoria": "Áudio", "preco": 2000},
        "Câmera Sony": {"categoria": "Fotografia", "preco": 7000},
        "Câmera Canon": {"categoria": "Fotografia", "preco": 9000}
}

gera_csv("data-sets/data_raw.csv", Produto_Categoria_Quantidade, 10000)