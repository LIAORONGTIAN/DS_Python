## 1. If Statements ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

header = apps_data[0]
apps_data = apps_data[1:]

free_apps_ratings = []
for row in apps_data:
    rating = float(row[7])
    price = float (row[4])
    
    if price == 0.0:
        free_apps_ratings.append(rating)
        
avg_rating_free  = sum(free_apps_ratings) / len(free_apps_ratings)

print (avg_rating_free)
        
    # Complete the code from here

## 2. Booleans ##

a_price = 0

if True: 
    print('This is free')
    
    
if a_price == 1:
    print ('This is not free')

## 3. The Average Rating of Non-free Apps ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

header = apps_data[0]
apps_data = apps_data[1:]

non_free_apps_ratings = []
for row in apps_data:
    rating = float(row[7])
    price = float(row[4])   
    if price != 0.0:
        non_free_apps_ratings.append(rating)
    
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)

print(avg_rating_non_free)

## 4. The Average Rating of Gaming Apps ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

header = apps_data[0]
apps_data = apps_data[1:]

non_games_ratings = []
for row in apps_data:
    rating = float(row[7])
    genre = row[11]
    
    if genre != 'Games':
        non_games_ratings.append(rating)
        
avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)

print(avg_rating_non_games)

## 5. Multiple Conditions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

header = apps_data[0]
apps_data = apps_data[1:]

free_games_ratings = []
for row in apps_data:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    
    if price == 0.0 and genre == 'Games':
        free_games_ratings.append(rating)
        
        
avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)

print(avg_rating_free_games)


    # Complete code from here

## 6. The or Operator ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    
    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)
        

avg_games_social = sum(games_social_ratings)/len(games_social_ratings)

print(avg_games_social)
    # Complete code from here
    

## 7. Combining Logical Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price != 0:
        non_free_games_social_ratings.append(rating)
        
avg_non_free = sum(non_free_games_social_ratings) / len(non_free_games_social_ratings)

# Non-free apps (average)

## 8. Comparison Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

header = apps_data[0]
apps_data = apps_data[1:]

more_9_apps = []
n_apps_more_9 = 0
n_apps_less_9 = 0
for row in apps_data:
    rating = float(row[7])
    price = float(row[4])
    
    if price > 9.0: 
        more_9_apps.append(rating)
    if price > 9.0:
        n_apps_more_9 = n_apps_more_9 + 1
    if price <=9.0:
        n_apps_less_9 = n_apps_less_9 + 1
        
           
avg_rating = sum(more_9_apps) / len(more_9_apps)

print(avg_rating)
print(n_apps_more_9)
print(n_apps_less_9)



 

## 9. The else Clause ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    
    if price == 0.0:
        app.append('free')
    else: 
        app.append('non-free')

apps_data[0].append('free_or_not')

print(apps_data[0:6])
    # Complete code from here

## 10. The elif Clause ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


for app in apps_data[1:]:
    price = float(app[4])
    
    if price == 0:
        app.append('free')
    elif price > 0 and price < 20:
        app.append('affordable')
    elif price >= 20 and price < 50:
        app.append('expensive')
    elif price >= 50:
        app.append('very expensive')
        
apps_data[0].append('price_label')
print(apps_data[:6])
    # Complete code from here