#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


poi = 0

for i in enron_data:
	if enron_data[i]["poi"] == 1:
		poi=poi+1


print poi

names = open("../final_project/poi_names.txt", "r")

name_file = names.readline()

#print(len(name_file))

total= 0 
email = 0
salary = 0

#print enron_data["PRENTICE JAMES"]
for key in  enron_data:
    total = total+1
    if enron_data[key]["total_payments"]!="NaN" and enron_data[key]["poi"]:
        salary = salary + 1

#print total


print salary
print poi
print float(salary)/float(poi)

#print enron_data["SKILLING JEFFREY K"]["total_payments"]
#print enron_data["LAY KENNETH L"]["total_payments"]
#print enron_data["FASTOW ANDREW S"]["total_payments"]