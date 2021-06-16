import math

''' x
    y
    xy
    x^2
    y^2
'''
def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def correlation(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    
    avg_x = average(x)
    avg_y = average(y)
    
    x_y_product = 0
    sum_x_square = 0
    sum_y_square = 0
    
    for i in range(n):
        x_ = x[i] - avg_x
        y_ = y[i] - avg_y
        x_y_product += x_ * y_
        sum_x_square += x_ * x_
        sum_y_square += y_ * y_

    return x_y_product / math.sqrt(sum_x_square * sum_y_square)

  
correlation([1,2,3], [1,5,7])
