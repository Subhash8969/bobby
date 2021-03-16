import pandas as pd 
df=pd.read_csv("pokemon.csv")
#print(df.head(3))
#print(df.tail(5))
#print(df.columns)#reads headers
#print(df[["Name","Type 1","HP"]])#reds each columns
#print(df.iloc[0:6]) #read each row
#print(df.iloc[2,2]) #reads a specific location (r,c)
#for index,row in df.iterrows():
#    print(index,row)
#df.loc method
#t=df.loc[df["Type 1"]=="Fire"]
#print(t)
#s=df.describe()
#print(s)
#g=df.sort_values("Name")#alphabatical order
#print(g)
#h=df.sort_values("Name",ascending=False)#alphabatical order descending
#print(h)
#l=df.sort_values(["Type 1","Speed"],ascending=[1,0])
#print(l)
#               FILTERING DATA
#a=df.loc[(df["Type 1"]=="Grass") & (df["Type 2"]=="Poison")]
#print(a)
#d=df.loc[(df["Type 1"]=="Grass") | (df["Type 2"]=="Poison")]
#print(d)
#x=df.loc[(df["Type 1"]=="Grass") & (df["Type 2"]=="Poison")&(df["HP"]>50)]
#print(x)
#x.to_excel("filtered.xlsx")#new xcel file created as filtered.xlsx
#x=x.reset_index(drop=True)
#print(x)
'''k=df.loc[df["Name"].str.contains("Mega")]
print(k)'''#it gives name contains mega word in it
#r=df.loc[~df["Name"].str.contains("Mega")]
#print(r) #~ this give the output names which are not having Mega word
import re
'''n=df.loc[df["Type 1"].str.contains("fire|grass",flags=re.I,regex=True)]
print(n)'''
#m=df.loc[df["Name"].str.contains("^pi[a-z]*",flags=re.I,regex=True)]
#print(m)
#m.to_excel("pi_pokemon.xlsx")

# CONDITIONAL CHANGES
'''df.loc[df["Type 1"]=="Fire", "Type 1"]="Lava"
print(df)'''

'''df.loc[df["Type 1"]=="Lava", "Type 1"]="Fire"
print(df)'''

'''df.loc[df["Type 1"]=="Fire", "Legendary"]=True
print(df)'''

#ADDING COLUMN
'''df["Total"]=df["HP"]+df["Attack"]+df["Defense"]+df["Sp. Atk"]+df["Sp. Def"]+df["Speed"]
df.head(20)
print(df)
df.to_csv("new_col1.csv",index=False)'''

'''df=pd.read_csv("new_col1.csv")
#print(df)

df.loc[df["Total"]>500,["Generation","Legendary"]]=["Test1","Test2"]
print(df)'''
#AGGREGATE STATISTICS (GROUPBY) we can do mean(),sum(),count()
df=pd.read_csv("new_col1.csv")
#av=df.groupby(["Type 1"]).mean().sort_values("Defense",ascending=False)
#print(av)
#g=df.groupby(["Type 1"]).sum()
#print(g)
'''df["count"]=1
h=df.groupby(["Type 1","Type 2"]).count()["count"]
print(h)'''


#Access a data frame with boolean index values

import pandas as pd 
   
# dictionary of lists 
dict = {'name':["name1", "name2", "name3", "name4"], 
        'degree': ["degree1", "degree2", "degree3", "degree4"], 
        'score':[1, 2, 3, 4]} 
   
df = pd.DataFrame(dict, index = [True, False, True, False]) 
   
print(df) 






























