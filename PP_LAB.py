import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a)

print(type(a))

##2D array
b = np.array([[1, 2, 3], [4, 5, 6]])

##3D array
c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
 
##CHECKING DIMENSIONS
print(b.ndim)

##SPECIFYING DIMENSIONS
d = np.array([1, 2, 3, 4], ndmin=4)
print(d.ndim)

##INDEXING IN MULTI DIMENSION ARRAY
e = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(e[1,4])

f = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(f[0, 0, 2])

##SLICING ARRAYS
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, :4])
##SHAPE
G = np.array([[1, 2, 3,4], [5, 6, 7, 8]])

print(G.shape)


##pandas
print(df.info()) 
new_df = df.dropna() ##removing null values
df.fillna(130, inplace = True) ##inserting value into NA
df["C_name"].fillna(130, inplace = True)

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print(df.duplicated()) ##checking for duplicates
df.drop_duplicates(inplace = True) ##removing duplicates
df.corr()
#showing records with null value
pd.isnull(df["c1"])
df.notnull() #returns T/F
df.notna() #returns F for missing values
#showing not null values
pd.notnull(data["c1"])
##head/tail
df.head(n) // df.tail(n)
#desc
df.describe()
##ADDING COLUMN
# Declare a list that is to be converted into a column
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
  
# Using 'Address' as the column name
# and equating it to the list
df['Address'] = address

###dropping columns
ata.drop(["Team", "Weight"], axis = 1, inplace = True)
#renaming column
df.rename(coumns={'c1':'C2'}) #OPTIONAL INPLACE
#NUMBER OF UNIQUE VALUES
df.c_name.nunique(dropna=TRUE)
#UNIQUE VALUE IN A  COLUMN
df.c_name.unique()
#LOWERCASING A COLUMN
df[c]=df[c].str.lower()#/upper()
#Capitalizing first letter of column
df["c"]=df["c"].str.capitalize
#n largest/smallest value in a column
df.nlargest(n,["C_name"])
df.nsmallest(n,["C_name"])
#extracting rows
x=df.loc["arguement"] #what you want to extract eg:name
#extracting rows using index
x=df.iloc[i] #i=index
#sorting by column
df.sort_values("Name", axis = 0, ascending = True,
                 inplace = True, na_position ='last'/'first')
##values counts of each unique value in the given Series object.
df.value_counts()

# saving the dataframe
df.to_csv('file1.csv')
#UPDATING VALUE IN COLUMN
# updating the column value/data
df['Status'] = df['Status'].replace({'P': 'A'})
##Percentage of a column
df1['percent'] = (df1['Math_score'] / 
                  df1['Math_score'].sum()) * 100
##re-indexing after dropping
df.reset_index() #opt inplace=TRUE
