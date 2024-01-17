import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df=pd.DataFrame(pd.read_excel("E:\proyectos\pbi\pbi_lima.xlsx",sheet_name="cuadro1"))
df.dropna(axis=0,inplace=True)
index_colu=["actividades"]
años=np.array(np.arange(2007,2022),dtype=str)
index_col=np.concatenate([index_colu,años],axis=0)
df.columns=index_col
df.drop(index=[5,20],axis=0,inplace=True)
df.set_index("actividades",inplace=True)
df_invert=df.transpose()


plt.style.use("_mpl-gallery-nogrid")
colors=plt.get_cmap("Blues")(np.linspace(0.2,0.8,len(df["2021"])))
fig,ax=plt.subplots()

ax.pie(df["2021"],colors=colors,labels=df.index)
plt.show()