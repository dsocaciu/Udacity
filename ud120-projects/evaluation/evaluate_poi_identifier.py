#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


### it's all yours from here forward!  

from sklearn import tree
from sklearn.cross_validation import train_test_split

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30, random_state=42)

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)

print len(features_test)
print len(labels_test)

print clf.predict(features_test)

print clf.score(features_test,labels_test)

precision_score(features_test,labels_test,average=None)

recall_score(features_test,labels_test,average=None)

clf2 = tree.DecisionTreeClassifier()
clf2.fit(features,labels)

#print clf2.predict(features_test)


