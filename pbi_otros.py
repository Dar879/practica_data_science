import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




ruta="E:\proyectos\pbi\pbi_otroserv.xlsx"
print("Nombre de las hojas",pd.ExcelFile(ruta).sheet_names)
x_labels=["Miles de soles","Estructura porcentual","Variación porcentual del índice de volumen físico",
          "Valores a Precios Corrientes Miles de soles","VPC Estructura porcentual","VPC ariación porcentual del índice de precios"]
dft=[]
for i in range(6):
    dft.append(pd.DataFrame(pd.read_excel(ruta,sheet_name=f"cuadro{i+1}",header=None)))

index_col=np.concatenate((["Departamento"],np.arange(2007,2022)),axis=0)
for i in range(6):
    dft[i].dropna(axis=0,inplace=True)
    dft[i].drop(index=[6,36],axis=0,inplace=True)
    dft[i].columns=index_col
    dft[i].set_index("Departamento",inplace=True)
    print(dft[i])
    
fig, axs = plt.subplots(3, 1, figsize=(15, 8))
    
for i in range(3):
    #plt.plot(dft[i].index,dft[i][f"2020"])
    axs[i].plot(dft[i].index,dft[i][f"2018"], label=f'grafica 2018 {i+1}')
    axs[i].plot(dft[i].index,dft[i][f"2019"], label=f'grafica 2019 {i+1}')
    axs[i].plot(dft[i].index,dft[i][f"2020"], label=f'grafica 2020 {i+1}')
    axs[i].plot(dft[i].index,dft[i][f"2021"], label=f'grafica 2021 {i+1}')
    
    axs[i].set_title(f'Gráfico {i+1}')
    axs[i].legend()


plt.show()