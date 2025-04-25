
vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883),
           ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544),
             ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471),
             ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)] # Lista de tuplas dada nas intruções do projeto.
 
vendas_maiores = []
for i in range(len(vendas)):
    dados = [vendas_maiores.append(vendas[i]) if int(venda) > 6000 else '' for venda in vendas[i]] 

print(vendas_maiores)