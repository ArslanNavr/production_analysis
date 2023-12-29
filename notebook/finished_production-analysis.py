#!/usr/bin/env python
# coding: utf-8

# In[30]:


import zipfile
import os
import json
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import datetime

####################

# Extracting zip
print(os.getcwd())

extract_path = '\data'
extract_path = '..\\..\\Data Science Cursus\\production_analysis\\data'

extracted_contents = os.listdir(extract_path)
extracted_contents.sort()
extracted_contents

####################

# Path to the daily_production folder and listing contents

daily_production_path = os.path.join(extract_path, 'daily_production')


daily_production_contents = os.listdir(daily_production_path)
daily_production_contents.sort()
daily_production_contents

####################

# Path to the BRU subfolder and listing the contents

bru_path = os.path.join(daily_production_path, 'BRU')

bru_contents = os.listdir(bru_path)
bru_contents.sort()
bru_contents

####################

# Selecting and displaying files from the bru_contents

random_file = random.choice(bru_contents)
sample_file_path = os.path.join(bru_path, random_file)

with open(sample_file_path, 'r') as file:
    sample_data = json.load(file)

sample_data

####################

# Simulate data with variation

def simulate_production(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    variation = random.uniform(0.8, 1.2)
    return data['production'] * variation

simulated_productions = [simulate_production(os.path.join(bru_path, file)) for file in bru_contents[:100]]

# Filtering out non-positive productions

simulated_productions = [prod for prod in simulated_productions if prod > 0]


# Simulation

plt.figure(figsize=(10, 6))
plt.hist(simulated_productions, bins=20, color='blue', edgecolor='black', density=True, range=(0, max(simulated_productions)))

sns.kdeplot(simulated_productions, bw_adjust=2, color='red', fill=True)

plt.title(' BRUSSEL HISTOGRAM')
plt.xlabel('SIMULATED PRODUCTION')
plt.ylabel('FREQ')
plt.xlim(0,)
plt.grid(True)
plt.show()

####################

####################

####################

# STO subfolder

sto_path = os.path.join(extract_path, 'daily_production', 'STO')

sto_contents = os.listdir(sto_path)
sto_contents.sort()

####################

# Selecting and displaying files from the sto_contents list

random_file = random.choice(sto_contents)
sample_file_path = os.path.join(sto_path, random_file)

with open(sample_file_path, 'r') as file:
    sample_data = json.load(file)

print(sample_data)

####################

# Simulate data with random variation for STO

def simulate_sto_production(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    variation = random.uniform(0.8, 1.2)
    return data['production'] * variation

simulated_sto_productions = [simulate_sto_production(os.path.join(sto_path, file)) for file in sto_contents[:100]]

# Filtering out non-positive productions

simulated_sto_productions = [prod for prod in simulated_sto_productions if prod > 0]

####################

# Histogram Simulation for STO

plt.figure(figsize=(10, 6))
plt.hist(simulated_sto_productions, bins=20, color='blue', edgecolor='black', density=True, range=(0, max(simulated_sto_productions)))

sns.kdeplot(simulated_sto_productions, bw_adjust=2, color='red', fill=True)

plt.title('STOCKHOLM HISTOGRAM')
plt.xlabel('SIMULATED PRODUCTION')
plt.ylabel('FREQ')
plt.xlim(0,)
plt.grid(True)
plt.show()

####################

# Creating a Time Series Line Plot for STO Production

# Parsing dates from filenames
dates = [datetime.datetime.strptime(file.split('.')[0], '%Y%m%d') for file in sto_contents[:100]]
production_data = [simulate_sto_production(os.path.join(sto_path, file)) for file in sto_contents[:100]]

plt.figure(figsize=(15, 6))
plt.plot(dates, production_data, color='red', marker='o', linestyle='-', linewidth=2, markersize=6)
plt.title('STOCKHOLM Production Over Time')
plt.xlabel('Date')
plt.ylabel('Production')
plt.grid(True)
plt.show()

####################


# In[ ]:




