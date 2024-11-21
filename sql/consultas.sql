SELECT
    Produto,
    Categoria,
    SUM(Quantidade * Preço) AS Total_Vendas
FROM
    data_clean
GROUP BY
    Produto, Categoria
ORDER BY
    Total_Vendas DESC;


SELECT
    Produto,
    Categoria,
    SUM(Quantidade * Preço) AS Total_Vendas
FROM
    data_clean
WHERE
    DATE(Data) >= '2023-06-01' AND DATE(Data) < '2023-07-01'
GROUP BY
    Produto, Categoria
ORDER BY
    Total_Vendas ASC;