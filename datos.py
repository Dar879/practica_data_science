import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

index_col=["año","pbi msoles","taza anual crecimiento",
           "poblacion","pbi por hab","tac","tac ndel"]
df=pd.DataFrame(pd.read_excel("pbi_peru.xlsx"))
df_pbi=df.iloc[7:35,[0,2,3,5,7,8,10]]
df_pbi.columns=index_col
df_pbi.drop(["año"],axis=1,inplace=True)
add_col=[]
for i in range(1995,2023):
    add_col.append(i)
df_pbi.insert(0,"año",add_col)


#plt.plot(df_pbi["año"],df_pbi["pbi msoles"])


plt.figure(figsize=(18,6))
#plt.plot(df_pbi["año"],df_pbi["pbi msoles"])
plt.plot(df_pbi["año"],df_pbi["tac ndel"])
plt.show()
