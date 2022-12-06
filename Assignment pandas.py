Q1. How do you load a CSV file into a Pandas DataFrame?
   Ans- CSV files contains plain text and is a well know format that can be read by everyone including Pandas
   df = pd.read_csv('xyz')
    df

Q2. How do you check the data type of a column in a Pandas DataFrame?
   ANs-pd.read_csv('xyz')
       pd.dtypes

Q3. How do you select rows from a Pandas DataFrame based on a condition?
#    Ans- it select tol 10 rows for data 
        pd.head(10)
        # bottom 5 rows
         df.tail()
         # bottom 10 rows
         df.tail(10)

Q4. How do you rename columns in a Pandas DataFrame?
   Ans-df2=fd.rename(columns={'Ticket':'Tokens'})
       df2

Q5. How do you drop columns in a Pandas DataFrame?
   Ans-#axis 0 -> rows and axis 1-> col
   fd.drop('Ticket',axis=1)

Q6. How do you find the unique values in a column of a Pandas DataFrame?
   Ans-# These represent the unique values in Ticket col
       fd['Ticket'].unique()

Q7. How do you find the number of missing values in each column of a Pandas DataFrame?
   Ans-#checking missing values
       fd.isnull()
         
      # checking the total number of missing values
      df.isnull().sum()

Q8. How do you fill missing values in a Pandas DataFrame with a specific value?
   Ans-# Want to fill 0 inall value then 
    #fd.fillna(0)
     fd.fillna({
    'Name':'None',
    'age':0,
    'Ticket':'Not confirmed'
   })
   #Carry forword upper value to lower NaN col
   fd2=fd.fillna(method='ffill')
   fd2
   #Carry forword lower value to upper NaN col
    fd2=fd.fillna(method='bfill')
     fd2

Q9. How do you concatenate two Pandas DataFrames?
   Ans-# using a .concat() method
        frames = [df, df1]
 
        res1 = pd.concat(frames)
        res1

Q10. How do you merge two Pandas DataFrames on a specific column?
   Ans-fd['New_col']=fd['Sex'] +'-'+ fd['Age'].astype (str)
       fd

Q11. How do you group data in a Pandas DataFrame by a specific column and apply an aggregation function?
    Ans-fd1=fd.groupby(['Sex'])['Sex'].agg('count')
         fd1
        # To find avg age of male and female
        fd1=fd.groupby(['Sex'])['Age'].agg({'mean'})
        fd1

Q12. How do you pivot a Pandas DataFrame?
   Ans-fd.pivot(index="xyz ",col="xyz",row="xyz")

Q13. How do you change the data type of a column in a Pandas DataFrame?
   Ans-# to change data type 
     fd['Sex']=fd['Sex'].astype('int64')
       
Q14. How do you sort a Pandas DataFrame by a specific column?
   Ans-fd.sort_values("PassengerId")

Q15. How do you create a copy of a Pandas DataFrame?
   Ans-fd.copy()

Q16. How do you filter rows of a Pandas DataFrame by multiple conditions?
   Ans-You can use df[df["Courses"] == 'Spark'] to filter rows by a condition in pandas DataFrame. 
   Not that this expression returns a new DataFrame with selected rows

Q17. How do you calculate the mean of a column in a Pandas DataFrame?
   Ans-#fd.describe() or fd.mean()
      To get column average or mean from pandas DataFrame use either mean() and describe() method

Q18. How do you calculate the standard deviation of a column in a Pandas DataFrame?
   Ans-#fd.std() It consider only col or row which have numeric value
       Standard deviation is calculated using the function . std()

Q19. How do you calculate the correlation between two columns in a Pandas DataFrame?
   Ans-#Find the correlation between col1 and col2 by using df[col1]. corr(df[col2]) 
        #and save the correlation value in a variable, corr. Print the correlation value, corr.
      fd1=fd['Fare'].corr(fd['Age'])
      fd1

Q20. How do you select specific columns in a DataFrame using their labels?
   Ans-This is the most basic way to select a single column from a dataframe, just put the string name of the column in brackets
        #fd['Name']

Q21. How do you select specific rows in a DataFrame using their indexes?
   Ans-You can select a single row from pandas DataFrame by integer index using df. iloc[n] .
      Replace n with a position you wanted to select
      #Access rows by indexs with iloc
      fd.iloc[[0,1,2],[1,2,3]]
                #rows   #col

Q22. How do you sort a DataFrame by a specific column?
   Ans-Sorting Your DataFrame on a Single Column. To sort the DataFrame based on the values in a single column, you'll use . sort_values() 
        #fd.sort_values(['Name'])
         
Q23. How do you create a new column in a DataFrame based on the values of another column?
   Ans-fd['new_col']=fd['Sex']+'-'+fd['Age']

Q24. How do you remove duplicates from a DataFrame?
   Ans-df.drop_duplicate()

Q25. What is the difference between .loc and .iloc in Pandas?
   Ans-loc[] is used to select rows and columns by Names/Labels
        iloc[] is used to select rows and columns by Integer Index/Position. zero based index position
      
