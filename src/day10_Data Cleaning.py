# STEP 1 — Import pandas
import pandas as pd

# STEP 2 — Create messy dataset (added Date + messy City + duplicate row)
Data = {
    "CustomerID": [101,102,103,104,105,106,107,107,108,109],
    "Name": ["Amit","Sara","John",None,"Priya","David","Meena","Meena","Ali","Riya"],
    "Age": [25,None,30,22,None,28,35,35,None,26],
    "City": [" Bangalore","Mumbai ","Delhi",None,"Bangalore","Chennai","Mumbai","Mumbai","Delhi"," Bangalore "],
    "OrderAmount": [2500,1800,None,2200,3000,None,1500,1500,2700,None],
    "PaymentMethod": ["UPI","Card","Cash","Card",None,"UPI","Cash","Cash","Card","UPI"],
    "Date": ["2024-01-05","2024-01-10","2024-02-01","2024-02-05","2024-03-01",
             "2024-03-05","2024-03-10","2024-03-10","2024-04-01","2024-04-05"]
}


df = pd.DataFrame(Data)

# STEP 3 — Inspect dataset
print("First rows:\n", df.head())
print("\nDataset info:")
print(df.info())

# STEP 4 — Check missing values
print("\nMissing values per column:")
print(df.isna().sum())

# STEP 5 — Fill missing values (statistical approach)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["OrderAmount"] = df["OrderAmount"].fillna(df["OrderAmount"].mean())
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["PaymentMethod"] = df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0])
df["Name"] = df["Name"].fillna("Unknown")

# STEP 6 — Check data types before conversion
print("\nData types BEFORE conversion:")
print(df.dtypes)

# STEP 7 — Convert data types
df["Age"] = df["Age"].astype(int)
df["Date"] = pd.to_datetime(df["Date"])

print("\nData types AFTER conversion:")
print(df.dtypes)

# -------------------------------------------------
# NEW PART — STRING CLEANING
# -------------------------------------------------

# Strip extra spaces from City names
df["City"] = df["City"].str.strip()

# Convert City names to lowercase
df["City"] = df["City"].str.lower()

print("\nCity column after cleaning:")
print(df["City"])

# -------------------------------------------------
# NEW PART — DUPLICATE HANDLING
# -------------------------------------------------

# Check duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\nShape after removing duplicates:", df.shape)

# FINAL CLEAN DATASET
print("\nFinal cleaned dataset:")
print(df.head())


#task 1
import csv
import numpy as np
data1=pd.read_csv("customer_order.csv")
df1=pd.DataFrame(data1)
print("shape before cleaning",df1.shape)
#report missing values
print(df1.isna().sum())
#filling missing values

numeric_cols = df1.select_dtypes(include=[np.number]).columns

df1[numeric_cols] = df1[numeric_cols].fillna(df1[numeric_cols].median())

df1=df1.drop_duplicates()
print("Shape after cleaning",df1.shape)
print(df1)


#task 2
import pandas as pd
data2={
       "Date":["2026-01-01","2026-01-02","2026-01-03","2026-01-04"],
       "Price":["$100.50","$200.75","$300.20","$400.10"]
       }
df2=pd.DataFrame(data2)
print(df2)
#data types
print(df2.dtypes)
#converting data types
df2["Price"]=df2["Price"].str.replace("$","",regex=False).astype(float)#removing dollar
print(df2)
print(df2.dtypes)#changed datatype

df2["Date"]=pd.to_datetime(df2["Date"])
print(df2)
print(df2.dtypes)



#task 3
import pandas as pd
data3={
       "Location":[" New York","new york","NEW YORK ","New York"]
       }
df3=pd.DataFrame(data3)
print(df3)
#before cleaning
df3.groupby("Location").size()
print(df3["Location"].unique())
#cleaning
df3["Location"]=df3["Location"].str.strip()
df3["Location"]=df3["Location"].str.title()#or you can use str.lower
#after cleaning
print(df3["Location"].unique())
df3.groupby("Location").size()


