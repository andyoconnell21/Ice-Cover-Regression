###############################################################################
## Semester:         CS 540 Spring 202
##
## This File:        ice_cover.py
## Author:           Andy O'Connell
## Email:            ajoconnell2@wisc.edu
## CS Login:         o-connell
##
###############################################################################
##                   fully acknowledge and credit all sources of help,
##                   other than Instructors and TAs.
##
## Persons:          N/A
##
## Online sources:   Lecture Notes and Piazza
##
###############################################################################

import math
import copy
from random import randrange

def get_dataset():
    data_list = []

    data_list.append([1855, 118])
    data_list.append([1856, 151])
    data_list.append([1857, 121])
    data_list.append([1858, 96])
    data_list.append([1859, 110])
    data_list.append([1860, 117])
    data_list.append([1861, 132])
    data_list.append([1862, 104])
    data_list.append([1863, 125])
    data_list.append([1864, 118])
    data_list.append([1865, 125])
    data_list.append([1866, 123])
    data_list.append([1867, 110])
    data_list.append([1868, 127])
    data_list.append([1869, 131])
    data_list.append([1870, 99])
    data_list.append([1871, 126])
    data_list.append([1872, 144])
    data_list.append([1873, 136])
    data_list.append([1874, 126])
    data_list.append([1875, 91])

    data_list.append([1876, 130])
    data_list.append([1877, 62])
    data_list.append([1878, 112])
    data_list.append([1879, 99])
    data_list.append([1880, 161])
    data_list.append([1881, 78])
    data_list.append([1882, 124])
    data_list.append([1883, 119])
    data_list.append([1884, 124])
    data_list.append([1885, 128])
    data_list.append([1886, 131])
    data_list.append([1887, 113])
    data_list.append([1888, 88])
    data_list.append([1889, 75])
    data_list.append([1890, 111])
    data_list.append([1891, 97])
    data_list.append([1892, 112])
    data_list.append([1893, 101])
    data_list.append([1894, 101])
    data_list.append([1895, 91])
    data_list.append([1896, 110])

    data_list.append([1897, 100])
    data_list.append([1898, 130])
    data_list.append([1899, 111])
    data_list.append([1900, 107])
    data_list.append([1901, 105])
    data_list.append([1902, 89])
    data_list.append([1903, 126])
    data_list.append([1904, 108])
    data_list.append([1905, 97])
    data_list.append([1906, 94])
    data_list.append([1907, 83])
    data_list.append([1908, 106])
    data_list.append([1909, 98])
    data_list.append([1910, 101])
    data_list.append([1911, 108])
    data_list.append([1912, 99])
    data_list.append([1913, 88])
    data_list.append([1914, 115])
    data_list.append([1915, 102])
    data_list.append([1916, 116])
    data_list.append([1917, 115])

    data_list.append([1918, 82])
    data_list.append([1919, 110])
    data_list.append([1920, 81])
    data_list.append([1921, 96])
    data_list.append([1922, 125])
    data_list.append([1923, 104])
    data_list.append([1924, 105])
    data_list.append([1925, 124])
    data_list.append([1926, 103])
    data_list.append([1927, 106])
    data_list.append([1928, 96])
    data_list.append([1929, 107])
    data_list.append([1930, 98])
    data_list.append([1931, 65])
    data_list.append([1932, 115])
    data_list.append([1933, 91])
    data_list.append([1934, 94])
    data_list.append([1935, 101])
    data_list.append([1936, 121])
    data_list.append([1937, 105])
    data_list.append([1938, 97])

    data_list.append([1939, 105])
    data_list.append([1940, 96])
    data_list.append([1941, 82])
    data_list.append([1942, 116])
    data_list.append([1943, 114])
    data_list.append([1944, 92])
    data_list.append([1945, 98])
    data_list.append([1946, 101])
    data_list.append([1947, 104])
    data_list.append([1948, 96])
    data_list.append([1949, 109])
    data_list.append([1950, 122])
    data_list.append([1951, 114])
    data_list.append([1952, 81])
    data_list.append([1953, 85])
    data_list.append([1954, 92])
    data_list.append([1955, 114])
    data_list.append([1956, 111])
    data_list.append([1957, 95])
    data_list.append([1958, 126])
    data_list.append([1959, 105])

    data_list.append([1960, 108])
    data_list.append([1961, 117])
    data_list.append([1962, 112])
    data_list.append([1963, 113])
    data_list.append([1964, 120])
    data_list.append([1965, 65])
    data_list.append([1966, 98])
    data_list.append([1967, 91])
    data_list.append([1968, 108])
    data_list.append([1969, 113])
    data_list.append([1970, 110])
    data_list.append([1971, 105])
    data_list.append([1972, 97])
    data_list.append([1973, 105])
    data_list.append([1974, 107])
    data_list.append([1975, 88])
    data_list.append([1976, 115])
    data_list.append([1977, 123])
    data_list.append([1978, 118])
    data_list.append([1979, 99])
    data_list.append([1980, 93])

    data_list.append([1981, 96])
    data_list.append([1982, 54])
    data_list.append([1983, 111])
    data_list.append([1984, 85])
    data_list.append([1985, 107])
    data_list.append([1986, 89])
    data_list.append([1987, 87])
    data_list.append([1988, 97])
    data_list.append([1989, 93])
    data_list.append([1990, 88])
    data_list.append([1991, 99])
    data_list.append([1992, 108])
    data_list.append([1993, 94])
    data_list.append([1994, 74])
    data_list.append([1995, 119])
    data_list.append([1996, 102])
    data_list.append([1997, 47])
    data_list.append([1998, 82])
    data_list.append([1999, 53])
    data_list.append([2000, 115])
    data_list.append([2001, 21])

    data_list.append([2002, 89])
    data_list.append([2003, 80])
    data_list.append([2004, 101])
    data_list.append([2005, 95])
    data_list.append([2006, 66])
    data_list.append([2007, 106])
    data_list.append([2008, 97])
    data_list.append([2009, 87])
    data_list.append([2010, 109])
    data_list.append([2011, 57])
    data_list.append([2012, 87])
    data_list.append([2013, 117])
    data_list.append([2014, 91])
    data_list.append([2015, 62])
    data_list.append([2016, 65])
    data_list.append([2017, 94])
    data_list.append([2018, 86])
    data_list.append([2019, 70])

    return data_list

def print_stats(data):
    #Length of dataset
    length = len(data)
    print(length)

    #Sample mean
    sum_of_numbers = 0

    for x in data:
        sum_of_numbers = sum_of_numbers + x[1]

    sample_mean = sum_of_numbers / length
    print(round(sample_mean, 2))

    #Standard Deviation
    sd_sum = 0
    for x in data:
        sd_sum = sd_sum + math.pow((x[1] - sample_mean), 2)
    
    standard_deviation = (1 / (length - 1)) * sd_sum
    sqrt_standard_deviation = math.sqrt(standard_deviation)
    print(round(sqrt_standard_deviation, 2))


def regression(beta_0, beta_1):
    data = get_dataset()

    sum_MSE = 0
    for x in data:
        sum_MSE = sum_MSE + math.pow((beta_0 + ((beta_1 * x[0]) - x[1])), 2)

    MSE_calc = (1 / len(data)) * sum_MSE

    return MSE_calc

def gradient_descent(beta_0, beta_1):
    data = get_dataset()
    l = len(data)

    sum_MSE = 0
    for x in data:
        sum_MSE = sum_MSE + (beta_0 + ((beta_1 * x[0]) - x[1]))
    pd1 = (2/l) * sum_MSE
    
    sum2_MSE = 0
    for x in data:
        sum2_MSE = sum2_MSE + ((beta_0 + ((beta_1 * x[0]) - x[1])) * x[0])
    pd2 = (2/l) * sum2_MSE

    return (pd1, pd2)

def iterate_gradient(T, eta):
    curr_iteration = 1
    beta0 = 0
    beta1 = 0

    #initial state
    MSE = gradient_descent(0, eta) 
    beta0 = 0 - (MSE[0] * eta)
    beta1 = 0 - (MSE[1] * eta)
    print(curr_iteration, round(beta0, 2), round(beta1, 2), round(regression(beta0, beta1), 2))
    curr_iteration += 1

    while curr_iteration <= T:
        MSE2 = gradient_descent(beta0, beta1)  

        temp1 = (MSE2[0] * eta)
        temp2 = (MSE2[1] * eta)
    
        beta0 = beta0 - temp1
        beta1 = beta1 - temp2

        print(curr_iteration, round(beta0, 2), round(beta1, 2), round(regression(beta0, beta1), 2))

        curr_iteration += 1


def compute_betas():
    data = get_dataset()
    length = len(data)

    #calculates y mean
    sum_of_numbers = 0
    for x in data:
        sum_of_numbers = sum_of_numbers + x[1]
    y_mean = sum_of_numbers / length

    #calculates x mean
    sum_of_numbers = 0
    for x in data:
        sum_of_numbers = sum_of_numbers + x[0]
    x_mean = sum_of_numbers / length

    numerator = 0
    #Calculates beta_1 numerator
    for x in data:
        numerator = numerator + ((x[0] - x_mean) * (x[1] - y_mean))
    
    denom = 0
    #Calculates beta_1 denomanator
    for x in data:
        denom = denom + math.pow((x[0] - x_mean), 2)
    
    beta1 = numerator / denom

    beta0 = y_mean - (beta1 * x_mean)

    MSE = regression(beta0, beta1)

    return (beta0, beta1, MSE)

def predict(year):
    betas = compute_betas()
    beta_0 = betas[0]
    beta_1 = betas[1]

    #copmuter prediction value
    predict_value = beta_0 + (beta_1 * year)

    return predict_value

def iterate_normalized(T, eta):
    #Normalizes the x values
    data = get_dataset()
    x_counter = 0
    x_counter_2 = 0
    std_x = 0
    normal_x = 0
    l = len(data)
    data_copy = copy.deepcopy(data)

    #Finds mean of X: CORRECT
    for x in data:
        x_counter = x[0] + x_counter
    temp_x = (1/l) * x_counter

    #Finds sd of X: SLIGHTLY OFF
    sd_sum = 0
    x_value = 0
    for x in data:
        x_value = math.pow((x[0] - temp_x), 2) 
        sd_sum = sd_sum + x_value
  
    standard_deviation = (1 / (l - 1)) * sd_sum
    sqrt_standard_deviation = math.sqrt(standard_deviation)

    #Normalize all X values: 
    for x in data_copy:
        x[0] = (x[0] - temp_x) / sqrt_standard_deviation
        
    #calculate iterate_gradient()
    curr_iteration = 1
    beta0 = 0
    beta1 = 0

    #initial state
    MSE = norm_gradient_descent(0, eta, data_copy) 
    beta0 = 0 - (MSE[0] * eta)
    beta1 = 0 - (MSE[1] * eta) #BETA_1 IS SLIGHTLY OFF
    

    print(curr_iteration, round(beta0, 2), round(beta1, 2), round(norm_regression(beta0, beta1, data_copy), 2))
    curr_iteration += 1

    #Calculates iterations after
    while curr_iteration <= T:
        MSE2 = norm_gradient_descent(beta0, beta1, data_copy)  

        temp1 = (MSE2[0] * eta)
        temp2 = (MSE2[1] * eta)
    
        beta0 = beta0 - temp1
        beta1 = beta1 - temp2

        print(curr_iteration, round(beta0, 2), round(beta1, 2), round(norm_regression(beta0, beta1, data_copy), 2))

        curr_iteration += 1

 
def sgd(T, eta):
    data = get_dataset()
    n = len(data)
    rand_num = randrange(n)
    
    #Normalize dataset
    #Normalizes the x values
    x_counter = 0
    x_counter_2 = 0
    std_x = 0
    normal_x = 0
    l = len(data)
    data_copy = copy.deepcopy(data)

    #Finds mean of X: CORRECT
    for x in data:
        x_counter = x[0] + x_counter
    temp_x = (1/l) * x_counter

    #Finds sd of X: SLIGHTLY OFF
    sd_sum = 0
    x_value = 0
    for x in data:
        x_value = math.pow((x[0] - temp_x), 2) 
        sd_sum = sd_sum + x_value
  
    standard_deviation = (1 / (l - 1)) * sd_sum
    sqrt_standard_deviation = math.sqrt(standard_deviation)

    #Normalize all X values: 
    for x in data_copy:
        x[0] = (x[0] - temp_x) / sqrt_standard_deviation


    #Gets x,y from random number
    temp = data_copy[rand_num]
    

    #Run iterate_normalized
    curr_iteration = 1
    beta0 = 0
    beta1 = 0
    MSE = norm_gradient_descent(0, eta, data_copy) 
    beta0 = temp[0] - (MSE[0] * eta)
    beta1 = temp[1] - (MSE[1] * eta) #BETA_1 IS SLIGHTLY OFF
    

    print(curr_iteration, round(beta0, 2), round(beta1, 2), round(norm_regression(beta0, beta1, data_copy), 2))
    curr_iteration += 1

    #Calculates iterations after
    while curr_iteration <= T:
        MSE2 = norm_gradient_descent(beta0, beta1, data_copy)  

        temp1 = (MSE2[0] * eta)
        temp2 = (MSE2[1] * eta)
    
        beta0 = beta0 - temp1
        beta1 = beta1 - temp2

        print(curr_iteration, round(beta0, 2), round(beta1, 2), round(norm_regression(beta0, beta1, data_copy), 2))

        curr_iteration += 1


def norm_gradient_descent(beta_0, beta_1, data):
    l = len(data)

    sum_MSE = 0
    for x in data:
        sum_MSE = sum_MSE + (beta_0 + ((beta_1 * x[0]) - x[1]))
    pd1 = (2/l) * sum_MSE
    
    sum2_MSE = 0
    for x in data:
        sum2_MSE = sum2_MSE + ((beta_0 + ((beta_1 * x[0]) - x[1])) * x[0])
    pd2 = (2/l) * sum2_MSE

    return (pd1, pd2)

def norm_regression(beta_0, beta_1, data):
    sum_MSE = 0
    for x in data:
        sum_MSE = sum_MSE + math.pow((beta_0 + ((beta_1 * x[0]) - x[1])), 2)

    MSE_calc = (1 / len(data)) * sum_MSE

    return MSE_calc
