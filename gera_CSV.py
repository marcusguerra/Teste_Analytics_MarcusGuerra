import csv
import random
from datetime import datetime, timedelta
import uuid


def gera_csv(arquivo_csv, produtos_categorias_quantidade, totalItens):

    #número máximo de itens é 20
    faixa_quantidade = (1, 20)

    data_inicial = datetime(2023, 1, 1)
    data_final = datetime(2023, 12, 31)

    with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as arquivo:
        csv_output = csv.writer(arquivo)
        csv_output.writerow(["ID", "Produto", "Categoria", "Preço", "Quantidade", "Data"])

        for i in range(1, totalItens):
            #Gera um ID aleatorio para a chave principal
            ID = str(uuid.uuid4())
            produto = random.choice(list(produtos_categorias_quantidade.keys()))
            categoria = produtos_categorias_quantidade[produto]["categoria"]


            #Como os preços variam de acordo com o tempo do ano, foi decidido fazer com que os
            #preços respeitem um intervalo de limites
            if isinstance(produtos_categorias_precos[produto]["preco"], tuple):
                preco = random.randint(*produtos_categorias_precos[produto]["preco"])
            else:
                preco = produtos_categorias_precos[produto]["preco"]

            #* descompacta os valores para poderem ser utilizados
            quantidade = random.randint(*faixa_quantidade)
            data = data_inicial + timedelta(days=random.randint(0, (data_final - data_inicial).days))

            csv_output.writerow([ID, produto, categoria, preco, quantidade, data.strftime("%d/%m/%Y")])


#Isso é base de todos os produtos, onde um produto está relacionado a uma
# categoria e a um preço
Produto_Categoria_Quantidade = produtos_categorias_precos = {
        "Samsung Galaxy S23": {"categoria": "Smartphones", "preco": (4000, 5000)},
        "iPhone 14 Pro": {"categoria": "Smartphones", "preco": (7000, 9000)},
        "Notebook Dell": {"categoria": "Laptops", "preco": (3000, 6000)},
        "MacBook Air": {"categoria": "Laptops", "preco": (8000, 12000)},
        "Fone de Ouvido JBL": {"categoria": "Áudio", "preco": (200, 400)},
        "Teclado Mecânico Razer": {"categoria": "Acessórios", "preco": (500, 1000)},
        "Mouse Razer": {"categoria": "Acessórios", "preco": (200, 500)},
        "Smart TV LG 4K 55''": {"categoria": "Eletrônicos", "preco": (2500, 4000)},
        "Caixa de Som JBL": {"categoria": "Áudio", "preco": (1500, 2000)},
        "Câmera Sony": {"categoria": "Fotografia", "preco": (8000, 9000)},
        "Câmera Canon": {"categoria": "Fotografia", "preco": (8000, 7000)}
}

gera_csv("produtos_precos_fixos.csv", Produto_Categoria_Quantidade, 20)