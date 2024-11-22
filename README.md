# Teste Analytics Marcus Guerra

Este repositório contém um conjunto de scripts e notebooks voltados para análise de dados e geração de relatórios utilizando datasets específicos. Ele abrange tarefas relacionadas a manipulação de dados, execução de consultas SQL, e visualização por meio de Jupyter Notebooks.

## Estrutura do Projeto

- **`data-sets/`**: Diretório contendo os conjuntos de dados utilizados no projeto.
- **`notebooks/`**: Notebooks do Jupyter para exploração e análise de dados.
- **`sql/`**: Scripts SQL para consulta e manipulação dos dados.
- **`gera_CSV.py`**: Script Python que gera o CSV utilizado durante o projeto.

## Suposições

A primeira etapa de qualquer projeto envolvendo um conjunto de dados é entender esse conjunto, para isso é importante contactar o cliente e esclarecer quaisquer dúvidas pertinentes pois uma coluna mal interpretada pode gerar problemas no futuro.
Neste caso, como fui eu quem criou o dataset, presumi que estava atuando como o cliente.

Sobre a qualidade dos dados, como é possivel observar na seção abaixo, os dados foram gerados aleatoriamente, a qualidade deles tende a ser inferior, o que atrapalha as analises, pois
dados de baixa qualidade leva a resultados imprecisos e conclusões equivocadas, comprometendo a confiabilidade das análises e decisões baseadas neles. Contudo, ainda foi possivel tirar insights interessantes como observado no pdf. 

Outra suposição importante feita durante a limpeza dos dados foi que, se uma entrada no arquivo CSV possui todos os campos idênticos, exceto o UUID, ela é considerada uma duplicata e, portanto, deve ser removida.

## Notebooks

Para esse projeto foram criados 2 notebook para manter uma melhor organização dos dados. 

O primeiro `notebooks/1 - Limpeza e Análise de Dados de Vendas.ipynb`, foca na primeira parte do desafio, onde ele realiza uma limpeza no conjunto de dados e também cria a coluna Vendas que será utilizada posteriormente, gerando o arquivo `data-sets/data_clean.csv`.

O segundo `notebooks/2. Análise Exploratória de Dados de Vendas.ipynb`, foca na análise dos dados, onde para uma melhor organização, visualização e reaproveitamento de código. Foi decidido criar uma seção para as funções que geram os gráficos.

## Criação do Conjunto de Dados

O script `gera_CSV.py` gera um conjunto de dados fictício para análises. Como ele é de utilização única, ele só não fui excluido pois é necessário para a entrega do projeto.
Ele utiliza produtos pré-definidos com suas categorias e preços para criar registros que incluem:

- **ID**: Identificador único gerado aleatoriamente atravéz do uuid4.
- **Produto e Categoria**: Informações sobre o item, onde um mesmo Produto sempre está associado a uma mesma Categoria.
- **Preço e Quantidade**: Preços fixos e quantidades aleatórias entre 1 e 20.
- **Data e Hora**: Registro gerado em um intervalo entre 01/01/2023 e 31/12/2023, com horários aleatórios entre 8h e 20h.

Os produtos disponíveis são os seguintes:

| Produto                 | Categoria      | Preço  |
|-------------------------|----------------|--------|
| Samsung Galaxy S23      | Smartphones    | 4000   |
| iPhone 14 Pro           | Smartphones    | 8000   |
| Notebook Dell           | Laptops        | 5000   |
| MacBook Air             | Laptops        | 12000  |
| Fone de Ouvido JBL      | Áudio          | 400    |
| Teclado Mecânico Razer  | Acessórios     | 700    |
| Mouse Razer             | Acessórios     | 500    |
| Smart TV LG 4K 55       | Eletrônicos    | 3000   |
| Caixa de Som JBL        | Áudio          | 2000   |
| Câmera Sony             | Fotografia     | 7000   |
| Câmera Canon            | Fotografia     | 9000   |

Para gerar o CSV, configure os parâmetros `produtos_categorias_quantidade` e `total_itens` no script, e execute-o.

## Execução

Para a execução, primeiramente é importante lembrar de não executar o arquivo `gera_CSV.py` novamente, pois irá criar um csv novo e alterar todos os notebooks.

Também é imporante alterar os caminhos para a leitura e escrita do csv caso for executar o código novamente, todas as células onde esta ação deve ser realizada estão marcadas com o comentário #Mudar caminho absoluto.

A escolha de fazer referência ao caminho absoluto da máquina local, em vez de usar o link do GitHub, foi por dois motivos: primeiro, como o arquivo CSV precisa ser escrito, não é possível utilizar o caminho do GitHub e misturar caminhos do GitHub com da maquina pode gerar confusão; segundo, para evitar problemas relacionados à conexão de internet, é mais seguro usar o caminho local. No entanto, em projetos maiores, com várias pessoas acessando o sistema simultaneamente, essa abordagem não é recomendada.

## Pré-requisitos

- Python 3.9+
- Bibliotecas: numpy, matplotlib, pandas, seaborn, uuid, datetime, csv, random
- mysql workbench ou outra ferramenta para sql.
