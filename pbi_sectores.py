import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




df=pd.DataFrame(pd.read_excel("E:\proyectos\pbi\pbi_sectores.xlsx",header=None,sheet_name="MillonesSoles"))
df.dropna(axis=0,inplace=True)
df.drop(3,axis=0,inplace=True)
df.columns=["year","PBI","extractive","transformation","services"]
df.at[76,"year"]=2020
df.at[77,"year"]=2021
df.at[78,"year"]=2022
df.set_index("year",inplace=True)


fig,ax=plt.subplots(nrows=1,ncols=5,figsize=(20,5))

colors=["red","blue","green","orange"]
for i in range(4):
    ax[i].plot(df.index,df.iloc[:,i],color=colors[i],label="PBI")
    ax[i].legend()
    ax[i].set_xlabel("year")
    ax[i].set_ylabel("millones de soles")
    ax[i].grid()
    ax[i].set_title(df.columns[i])
    ax[4].plot(df.index,df.iloc[:,i],color=colors[i],label=f"{df.columns[i]}")
ax[4].set_xlabel("Year")
ax[4].set_ylabel("Millones de soles")
ax[4].grid()
ax[4].set_title("Comparacion")
ax[4].legend()
plt.show()