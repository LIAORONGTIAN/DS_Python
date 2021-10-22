## 1. Functions ##

a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]

sum_manual = 0 
for row in a_list:
    sum_manual += row
    
    
print(sum_manual)
sum(a_list)
   

## 2. Built-in Functions ##

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']

content_ratings = {}

for key in ratings:
    if key in content_ratings:
        content_ratings[key]+= 1
        
    else:
        content_ratings[key] =1

print (content_ratings)

## 3. Creating Our Own Functions ##

def square_1(number):
    square_number = number * number
    return square_number

squared_10 = square_1(number = 10)
squared_16 = square_1(number = 16)

print (squared_10)
print (squared_16)

## 4. The Structure of a Function ##

def add_10(a_number):
    add_on = a_number + 10
    return add_on

add_30 = add_10(a_number=30)
add_90 = add_10(a_number=90)

print(add_30)
print(add_90)

## 5. Parameters and Arguments ##

def square_2(number):
    return number * number

squared_6 = square_2(6)
squared_11 = square_2(11)

print(squared_6)
print(squared_11)

## 6. Extract Values from Any Column ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
header = apps_data[0]
apps_data = apps_data[1:]

def extract(elec):
    ratings = []
    for row in apps_data:
        ratings.append(row[elec])
    return ratings

genres = extract(11)

print(genres)

## 7. Creating Frequency Tables ##

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
header = apps_data[0]
apps_data = apps_data[1:]

def extract(elec):
    ratings = []    
    for row in apps_data:
        ratings.append(row[elec])    
    return ratings

genres = extract(11)


def freq_table(gen):
    gen_table = {}
    for row in gen:
        if row in gen_table:
            gen_table[row]+= 1
        else: 
            gen_table[row] =1
    return gen_table

genres_ft=freq_table(genres)

     
    

## 8. Writing a Single Function ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
header = apps_data[0]
apps_data=apps_data[1:]

def freq_table(index_num):
    frequency_table = {}
    for row in apps_data:
        genre_value = row[index_num]
        if genre_value in frequency_table:
            frequency_table[genre_value]+= 1
        else:
            frequency_table[genre_value]=1
    return frequency_table
    
ratings_ft = freq_table(7)
print(ratings_ft)
                    

## 9. Reusability and Multiple Parameters ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(index,gener_list):
    
    frequency_table = {}
    
    for row in apps_data[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

ratings_ft = freq_table(index=7,gener_list=apps_data)
print(ratings_ft)

## 10. Keyword and Positional Arguments ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table

content_ratings_ft = freq_table(apps_data,10)
ratings_ft = freq_table(data_set=apps_data,index=7)
genres_ft = freq_table(index = 11, data_set=apps_data)

## 11. Combining Functions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# function for extract
def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

# function for sum
def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

# function for list
def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length
# def mean, which is using the extrac function to find the column value first and then use 
# sum and length to calc mean 
# would need to have a better understanding of the steps 
def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum (column) / find_length(column)

avg_price = mean(apps_data, 4)
    
print(avg_price)

## 12. Debugging Functions ##

def extract(data_set, index):
    column = []
    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)

print (avg_price)
print (avg_rating)