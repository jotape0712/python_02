
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73] # Lista dada nas instruções do codigo.


for i in range(len(glicemia)):
    nivel = "Hipoglicemia" if glicemia[i] <= 70 else "Normal" if glicemia[i] > 70 and glicemia[i] < 100 else "Alterada" if glicemia[i] > 100 and glicemia[i] < 126 else "Diabetes"
    print(nivel)