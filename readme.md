## NumPy Overview - (June 2, 2022)

### NumPy is nothing but provides all the libraries to deal with the linear algebra.
- NumPy, which stands for Numerical Python
- NumPy is the foundational package for mathematical computing
- Mathematical and logical operations on arrays
- Operations related to linear algebra. NumPy has inbuilt functions for
linear algebra and random generation
- ndarray is the core object in NumPy

### Numpy arrays 
- Are great alternatives to Python Lists. Some of the key advantages of Numpy arrays are that they are fast, 
easy to work with, and give users the opportunity to perform calculations across entire arrays.

### Basics ndarray
- multidimensional array
- homogenous collection of values (all the same)
- fast and efficient
- support for mathematical functions
- primary container for data exchange between python algorithms

## Attributes of an ndarray object
### Ndarray.ndim
- the number of axes (dimensions) of the array, the
number of dimensions is referred to as rank
### Ndarray.shape 
- the dimensions of the array. This is tuple of integers indicating the size of the array in each dimension. For a matrix within
rows and m columns, the shape will be (n,m)
### Ndarray.size 
- the total number of elements of the array. This is equal to the product of the elements of shape

### Ndarray.dtype
- an object describing the type of the elements in the array

## Datatypes and Precedence
- Str (highest precedence)
- Complex
- Float
- Int
- Bool (lowest precedence)<br>

This means that if there is 100 items in an array, and only one item is a string, then the entire array object 
becomes a string. Again, NumPy arrays are homogeneous objects. Also, this is why its important to pre-process you data. 

## Special functions
- np.arange()
- np.zeros()
- np.ones()
- np.eye()
- np.empty()
- np.copy()
- np.reshape()

## Operations

Something worth noting: Array multiplication is not matrix multiplication:

- Comparisons
- Array-wise comparisons
- Logical Operations
- Transcedental functions (sin, log, exp)
- Transposition (triu)
  - transposition is a view
- Linear algebra (.linalg implements basic linear algebra, such as linear systems, singular value decomposition)
- You can sum rows and columns (sum)
- Other reductions (.min, .max, .argmin, .argmax, .all, .any)
- In Statistics: .mean, .median, .mode, .std (standard deviation)

The argmin() and argmax() give you the index of the corresponding value

# Quantile
In statistics and probability, quantiles are cut points dividing the range of 
a probability distribution into continuous intervals with equal probabilities, 
or dividing the observations in a sample in the same way.

# Working with files in NumPy


























