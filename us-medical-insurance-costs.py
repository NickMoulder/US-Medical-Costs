#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs
# 
# The goal of this project is to determine 

# In[80]:


import csv

with open('insurance.csv') as insurances:
    reader = csv.DictReader(insurances)
    
    #Dictionary where regions are keys and all ages from that region are values stored in a list
    regions_and_ages = {}
    #Dictionary where regions are keys and all charges from that region are values stored in a list
    regions_and_charges = {}
    #Dictionary where smoker status are keys and all charges from that region are values stored in a list
    for row in reader:
        if row['region'] in regions_and_ages:
            
            regions_and_ages[row['region']].append(int(row['age']))
        else:
            regions_and_ages[row['region']] = [int(row['age'])]
            
        if row['region'] in regions_and_charges:
            regions_and_charges[row['region']].append(float(row['charges']))
        else:
            regions_and_charges[row['region']]= [float(row['charges'])]
            
        if row['smoker'] in smokers_and_charges:
            smokers_and_charges[row['smoker']].append(float(row['charges']))
        else:
            smokers_and_charges[row['smoker']]= [float(row['charges'])]
    


# In[81]:


def average_num_by_param(regions_dict):
    new_dict = {}
    for region in regions_dict:
        print(region)
        total = 0
        for nums in regions_dict[region]:
            total += nums
        average = total / len(regions_dict[region])
        new_dict[region] = average
    return new_dict

average_ages_by_region = average_num_by_param(regions_and_ages)
print(average_ages_by_region)


# It seems that there is not a significant difference in the average age of insurees by region.

# In[82]:


average_costs_by_region = average_num_by_param(regions_and_charges)
print(average_costs_by_region)
    


# In[83]:


def max_charges(average_costs):
    maxx = 0
    region = ""
    for charge in average_costs:
        if average_costs[charge] > maxx:
            maxx = average_costs[charge]
            region = charge
    return f"The {region} has the highest average charges with an average of {maxx} dollars."

print(max_charges(average_costs_by_region))


# In[84]:


average_costs_by_smoker = average_num_by_param(smokers_and_charges)
print(average_costs_by_smoker)


# In[85]:


def smoker_difference(smokers):
    diff = abs(smokers['yes']-smokers['no'])
    if smokers['yes'] > smokers['no']:
        return f"People who smoke are charged on average {diff} dollars more than non-smokers"
    else:
        return f"People who don't smoke are charged on average {diff} dollars more than smokers"

print(smoker_difference(average_costs_by_smoker))


# It seems as though between what region someone is from and whether they smoke or not, smoking status has the larger impact on one's insurance costs.
