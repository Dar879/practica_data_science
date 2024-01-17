import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

index_col=["Departamentos"]
for i in range(2007,2022):
    index_col.append(i)



df_ml=pd.DataFrame(pd.read_excel("E:\proyectos\pbi\pbi_regiones.xlsx",sheet_name="cuadro1"))
df_ml=df_ml.iloc[7:34,0:17]
df_ml.columns=index_col
df_ml.drop(index=[21,22,23],axis=0,inplace=True)

df_ml=df_ml.set_index("Departamentos")
df=df_ml.transpose()

print(df)


plt.figure()
for i in df:
    
    plt.plot(df[f"{i}"],label=f"{i}")

plt.title("PBI por regiones")
plt.xlabel("Año")
plt.ylabel("PBI en soles")
plt.ticklabel_format(style='plain', axis='y')
plt.legend()
plt.show()


def plote():
    plt.figure(figsize=(18,9))
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(df_ml[2021])))
    fig, ax= plt.subplots()
    ax.pie(df_ml[2021],labels=df_ml["Departamentos"], colors=colors, radius=3, center=(4, 4),
        wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 8), yticks=np.arange(1, 8))
    plt.show()
