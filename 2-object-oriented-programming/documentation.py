def scale(data, factor):
    """Multiply all entries of numeric data list by the given factor"""
    for j in range(len(data)):
        data[j] *= factor 


def scale(data, factor):
    """Multiply all entries of numeric data llist by the given factor.

    data     an instance of any mutable sequence type (such as a list)
             containng numeric elements 
    
    factor   a number that serves as the multiplicative factor for scaling 
    """
    for j in range(len(data)):
        data[j] *= factor 
        