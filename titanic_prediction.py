# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 13:41:53 2016

@author: Darragh
"""

import numpy as np
import pandas as pd
from IPython.display import display

import visuals as vs

#matplotlib inline

in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

#display(full_data.head())
# Store the 'Survived' feature in a new variable and remove it from the dataset
outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)

#display(data.head())

def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """
    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred):
        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    else:
        return "Number of predictions does not match number of outcomes"
        
#predictions = pd.Series(np.ones(5, dtype=int))
#print accuracy_score(outcomes[:5], predictions)


def predictions_0(data):
    """Model with no features. Always predict a passenger did not survive. """
    predictions = []
    for _, passenger in data.iterrows():
        # predict the survival of 'passenger'
        predictions.append(0)
    # return our predictions
    return pd.Series(predictions)

# Make predictions
#prediction_0 = predictions_0(data)
#print accuracy_score(outcomes, prediction_0)

#vs.survival_stats(data, outcomes, 'Sex')    

def predictions_1(data):
    """Model with one feature: 
        - Predict a passenger survived if they are female"""
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female':
            predictions.append(1)
        else:
            predictions.append(0)
    return pd.Series(predictions)
    
#prediction_1 = predictions_1(data)
#print accuracy_score(outcomes, prediction_1)

#vs.survival_stats(data, outcomes, 'Age', ["Sex == 'male'"])

def predictions_2(data):
    """ Model with two features: 
            - Predict a passenger survived if they are female.
            - Predict a passenger survived if they are male and younger than 10. """
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female':
            predictions.append(1)
        elif passenger['Sex'] == 'male' and passenger['Age'] < 10:
            predictions.append(1)
        else:
            predictions.append(0)                
    return pd.Series(predictions)
    
#prediction_2 = predictions_2(data)
#print accuracy_score(outcomes, prediction_2)

vs.survival_stats(data, outcomes, 'Embarked', ["Pclass == 2"])

def predictions_3(data):
    """ Model with multiple features.Makes a prediction with an accuracy of at least 80%. """
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female' and passenger['Age'] < 20 and passenger['Age'] > 50 and passenger['Pclass'] == 3:
            predictions.append(1)
        elif passenger['Sex'] == 'female' and passenger['Age'] >= 20 and passenger['Age'] <= 30 and passenger['Pclass'] == 3 and passenger['Parch'] > 1:
            predictions.append(1)
        elif passenger['Sex'] == 'female' and passenger['Pclass'] < 3:
            predictions.append(1)
        elif passenger['Sex'] == 'male' and passenger['Age'] < 10 and passenger['Pclass'] < 3:
            predictions.append(1)
        elif passenger['Sex'] == 'male' and passenger['Age'] > 20 and passenger['Age'] < 50 and passenger['Pclass'] == 1 and passenger['SibSp'] == 1:
            predictions.append(1)
        elif passenger['Sex'] == 'male' and passenger['Age'] >= 20 and passenger['Age'] <= 30 and passenger['Pclass'] == 3 and passenger['Parch'] == 1:
            predictions.append(1)
        else:
            predictions.append(0)                
    return pd.Series(predictions)
    
prediction_3 = predictions_3(data)
print accuracy_score(outcomes, prediction_3)
    