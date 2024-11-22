SELECT
    Produto,
    Categoria,  -- seleciona o Prduto e Categoria para visualizados posteriormente
    SUM(Quantidade * Preço) AS Total_Vendas -- gera a coluna total_vendas 
FROM
    data_clean -- seleciona a tabela
GROUP BY
    Produto, Categoria -- agrupa por produtos e categorias
ORDER BY
    Total_Vendas DESC; -- faz a ordenação descendente 


SELECT
    Produto,
    Categoria,  -- seleciona o Prduto e Categoria para visualizados posteriormente
    SUM(Quantidade * Preço) AS Total_Vendas -- gera a coluna total_vendas 
FROM
    data_clean
WHERE
    DATE(Data) >= '2023-06-01' AND DATE(Data) < '2023-07-01' -- é necessario passar a coluna Data para DATE por causa do horario dentro dela, após isso inclui apenas o mes de junho
GROUP BY
    Produto, Categoria
ORDER BY
    Total_Vendas ASC; -- ordena ascendente
