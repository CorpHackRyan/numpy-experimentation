## Pandas overview - (6/3/22)
[(Link to the jupyter lab of pandas dataframes to assist with these notes )](https://github.com/CorpHackRyan/jupyter-experimention/blob/main/UsingPandas.ipynb)

## Creating a DataFrame
1. Using a two-dimensional list
2. Using a dictionary
3. Using the files / directly importing from a file

    
### Using two-dimensional lists
import pandas as pd<br>
import numpy as np

li = [[100, "ryan", 100000.5],
      [101, "Mike", 20000.5],
      [102, 'Jonny', 25000.6]]

// Convert list to array<br>
arr2d = np.array(li)

Now lets convert this list to a data frame instead of an array<br>
df = pd.DataFrame(li)

#### Series in a dataframe
In a data frame, each column is a series. In each series, everything is homogeneous. 
So, if something in that column is a string, then the rest of the column becomes a string. 
In pandas, when you check the data type of dataframe  column, and there's a string, then it 
will return a data type object of 'O' - which is object, which means string in pandas. 

Remember, in a list, each item in a row is the data in the row. The column is assigned automatically 
by the system with index numbers. 

### Using Dictionaries 
We can also convert a dictionary to a dataframe. Keep in mind when creating a dataframe from 
the dictionary, the dict must have all the same amount of values for each entry. 
Remember that each key in a dictionary is the column, and the values are the row data. 
Example:
<br>This is valid:<br>
dic = {'emp_no':[100,101,102], 'emp_name':['Ryan', 'Mike', 'Johnny'], 'emp_sal':[1000.5, 2000.5, 30000.6]}

<br> This is not valid: <br>
dic = {'emp_no':[100,101,102], 'emp_name':['Ryan', 'Mike', 'Johnny'], 'emp_sal':[1000.5, 2000.5, 30000.6, 4000.00]}
<br><br>This will not work because the salary has an extra entry and will throw an exception error.

### Using a file
You literally just read any type of file you want right into a data frame:
- csv = read_csv('/path/to/csv_file.csv')
- html = read_html('/path/to/html_file.html')

### Attributes of a DataFrame
- ndim
- shape
- size
- dtypes
- values
- columns
- index
- axes

### Important methods
- head()
- tail()