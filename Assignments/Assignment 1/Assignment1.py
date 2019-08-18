"""
Mathematics and Statistics, Monsoon 2019
Assignment 1
Name: Jayitha. C
Roll No: 20171401
"""
import pandas as pd
import itertools
import warnings

warnings.filterwarnings("ignore")
columnNames = ["Economic Status", "Age", "Sex", "Survived"]
dummydf = pd.read_csv('titanic_dat.txt', delimiter = '        ', header=None)
df = pd.DataFrame(dummydf.values, columns = columnNames)

economicStatusIndex = ["crew", "first", "second", "third"]
ageIndex = ["child","adult"]
sexIndex = ["female", "male"]
survivedIndex = ["no", "yes"]

for i in range(4):
    df["Economic Status"] = df["Economic Status"].replace(i, economicStatusIndex[i])
for i in range(2):
    df["Age"]=df["Age"].replace([i], ageIndex[i])
    df["Sex"]=df["Sex"].replace(i, sexIndex[i])
    df["Survived"]=df["Survived"].replace(i, survivedIndex[i])


columnNames1 = ["Economic Status", "Sex", "Population Exposed to Risk","Number of Deaths","Deaths per 100"]
columnNames2 = ["Economic Status", "Age", "Population Exposed to Risk","Number of Deaths","Deaths per 100"]
df1 = pd.DataFrame(columns = columnNames1)
df2 = pd.DataFrame(columns = columnNames2)
sexIndex.append("both")
ageIndex.append("both")
df1["Economic Status"], df1["Sex"] = zip(*list(itertools.product(*[economicStatusIndex, sexIndex])))
df2["Economic Status"], df2["Age"] = zip(*list(itertools.product(*[economicStatusIndex, ageIndex])))

populationExposedtoRisk = []
numOfDeaths = []
deathsPer100Exposed = []
for t in zip(*[df1["Economic Status"],df1["Sex"]]):
    if not t[1] == "both":
        populationExposedtoRisk.append(df.loc[(df["Economic Status"]==t[0]) & (df["Sex"]==t[1])].shape[0])
        numOfDeaths.append(df.loc[(df["Economic Status"]==t[0]) & (df["Sex"]==t[1]) & (df["Survived"]=="no")].shape[0])
    else:
        populationExposedtoRisk.append(populationExposedtoRisk[-1]+populationExposedtoRisk[-2])
        numOfDeaths.append(numOfDeaths[-1] + numOfDeaths[-2])
    try:
        deathsPer100Exposed.append(numOfDeaths[-1]*100/populationExposedtoRisk[-1])
    except:
        deathsPer100Exposed.append(0)
df1["Population Exposed to Risk"] = populationExposedtoRisk
df1["Number of Deaths"] = numOfDeaths
df1["Deaths per 100"] = deathsPer100Exposed

del populationExposedtoRisk[:]
del numOfDeaths[:]
del deathsPer100Exposed[:]

for t in zip(*[df2["Economic Status"],df2["Age"]]):
    if not t[1] == "both":
        populationExposedtoRisk.append(df.loc[(df["Economic Status"]==t[0]) & (df["Age"]==t[1])].shape[0])
        numOfDeaths.append(df.loc[(df["Economic Status"]==t[0]) & (df["Age"]==t[1]) & (df["Survived"]=="no")].shape[0])
    else:
        populationExposedtoRisk.append(populationExposedtoRisk[-1]+populationExposedtoRisk[-2])
        numOfDeaths.append(numOfDeaths[-1] + numOfDeaths[-2])
    try:
        deathsPer100Exposed.append(numOfDeaths[-1]*100/populationExposedtoRisk[-1])
    except:
        deathsPer100Exposed.append(0)
df2["Population Exposed to Risk"] = populationExposedtoRisk
df2["Number of Deaths"] = numOfDeaths
df2["Deaths per 100"] = deathsPer100Exposed

print("\nTable I: Economic Status and Sex\n")
print(df1)
print("\n\nTableII: Economic Status and Age\n")
print(df2)
print("\nDone.")
