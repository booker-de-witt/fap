import pandas as pd
import numpy as np
from numpy import random

# CAUTION , THERE ARE TOO MANY PRINT COMMANDS

# ==================================================================
# -----------------------PART ONE PANDAS----------------------------
# ==================================================================

#----------------LOAD THE DATASET-----------------------
# 1) read the csv
data_csv = pd.read_csv("california_housing_train.csv")
daf = pd.DataFrame(data_csv)

# 2) print the first five and last 10 datas
print(daf.head(5))
print(daf.tail(10))

# -------------DATA SUMMARY--------------------


# 2)print unique data in total_bedroom columns
unique_in_total_bedrooms = daf.nunique()["total_bedrooms"]
print(unique_in_total_bedrooms)


# --------------DATA TRANSFORMATION------------
# 1) adding a new column
daf["total_bedrooms_per_total_rooms"] = daf["total_bedrooms"]/daf["total_rooms"]

# 2) mean and standard deviation
da_mean = daf["total_bedrooms_per_total_rooms"].mean
da_std = daf["total_bedrooms_per_total_rooms"].std


# --------------DATA FILTERING----------------
# 1) dataset where median income is greater than 5
new_daf = daf.loc[daf["median_income"] > 5]

# 2) Create a subset of the data where the number of rooms (total_rooms) exceeds 10,000 and the median_house_value is below $150,000.

subset = daf.loc[(daf["total_rooms"] > 10000) & (daf["median_house_value"] < 150000)]
print(subset[["total_rooms", "median_house_value"]])


# --------EXPORT MODIFIED DATA------------

daf.to_csv("final.csv")


# ==================================================================
#------------------------PART 2 NumPY-------------------------------
# ==================================================================


# ------------ARRAY CREATION AND INDEXING-----------

arr = np.array(range(1,21))
evens_arr = arr[1::2]
random_arr = random.randint(10,100,size = (5,4))
extracted_arr = random_arr[:3,:2]


# ----------------ARRAY MANIPULATION--------------------

new_int_arr = arr.reshape(4,5)
new_rand_arr = random_arr.reshape(20)
print(new_rand_arr)

another_random_arr = random.randint(100,1000,size = (4,4))
matrix_multiply = np.dot(random_arr,another_random_arr)


# ---------------ARRAY INDEXING----------------------------

still_random_arr = random.randint(0 , 100 , size = 50)
da_mask = still_random_arr > 50
new_still_random_arr = still_random_arr[da_mask]

indices = [1,2,9,6,35]
fancy_indexing = still_random_arr[indices]


# --------------------STATISTICAL OPERATIONS---------------------

mean = np.mean(random_arr,axis=0)
median = np.median(random_arr, axis = 0)
mode = np.sum(random_arr,axis = 0)

da_mask_again = random_arr > mean
twodee_arr_with_mask = random_arr[da_mask_again]




# ==================================================================
# --------------------PART THREE PYTHON-----------------------------
# ==================================================================

# ---------Fibbonacci---------------
# 1) Creating Fibbonacci
fibbonacci = [1,1]

for i in range(1,100):
    fibbonacci.append(fibbonacci[i] + fibbonacci[i-1])

#2) Fizzbuzz
for x in fibbonacci:
    if x % 5 == 0 and x % 3 == 0:
        print("FizzBuzz")
    elif x % 5==0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")


# ------------Median-----------------
# 1) arguments as a list
def median_one(lst:list):
    max_count = 0
    for x in lst:
        if lst.count(x) > max_count:
            max_count = lst.count(x)
            med = x
    return med


# 2) variable number of arguments
def median_two(*args):
    max_count = 0
    med = 0
    for x in args:
        if args.count(x) > max_count:
            max_count = args.count(x)
            med = x

    return med

# ---------Error Handling-------------
def divide(a,b):
    print(a / b)

try:
    divide(1,0)
except ZeroDivisionError:
    print("Congrats! You just broke Maths")


# ==================================================================
# ------------------------BONUS-------------------------------------
# ==================================================================

threedee_arr = random.randint(0,1000, size= (20,5,10))

swapped_arr = np.swapaxes(threedee_arr,1,2)

sum_threedee_arr = np.sum(threedee_arr, axis = 1)

twodee_arr = random.randint(0,1000 , size = (6,12))
onedee_arr = random.randint(0,1000, size = 12)

broadcasted_arr = twodee_arr+onedee_arr

