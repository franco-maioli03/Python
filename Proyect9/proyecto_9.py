import re
import os
import time
import datetime
from pathlib import Path
import math

start_time = time.time()

path = 'C:\\Users\\Franco\\OneDrive\\Desktop\\Courses\\Python\\Project9\\My_Big_Directory'

my_pattern = r'N\D{3}-\d{5}'

today = datetime.date.today()
numbers_found = []

files_found = []

def search_number(file, pattern):
    this_file = open(file, 'r')
    text = this_file.read()
    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''

def create_lists():
    for folder, subfolder, file in os.walk(path):
        for f in file:
            result = search_number(Path(folder, f), my_pattern)
            if result != '':
                numbers_found.append((result.group()))
                files_found.append(f.title())

def show_all():
    index = 0
    print('-' * 50)
    print(f'Search Date: {today.day}/{today.month}/{today.year}')
    print('\n')
    print('FILE\t\t\tSERIAL NO.')
    print('-----\t\t\t----------')
    for f in files_found:
        print(f'{f}\t{numbers_found[index]}')
        index += 1
    print('\n')
    print(f'Numbers found: {len(numbers_found)}')
    end_time = time.time()
    duration = end_time - start_time
    print(f'Search duration: {math.ceil(duration)} seconds')
    print('-' * 50)

create_lists()
show_all()
