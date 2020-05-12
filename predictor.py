import pandas as pd
import numpy as np
import tensorflow
from tensorflow import keras
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import models

#First, we're going to read in all previous plays in NCAA to get a scale
df = pd.read_csv('datasets/ncaaAll_binary.csv')

#Next, we'll vectorize it, scale it, and transform it
X = df.iloc[:,1:9]
y = df.iloc[:,9]
X = X.replace({True:1, False:0})
y = y.replace({'Rush':0, 'Pass':1})
y = to_categorical(y)
ss = StandardScaler()
numeric = ['score_differential', 'period', 'seconds_remaining', 'secondsInHalf', 'yardsToGoal', 'down', 'distance']
scaled_features = X.copy()
features = scaled_features[numeric]
scaler = ss.fit(features.values)
features = ss.transform(features.values)
scaled_features[numeric] = features
X = scaled_features

#Import the models we'll use to get a prediction
coaching = models.load_model('models/coachingModel.h5')
conference = models.load_model('models/conferenceModel.h5')
league = models.load_model('models/leagueModel.h5')

#Function to get a tuple of probabilities from the ensemble.
def ensemblePrediction(dataPoint):
  coach_prediction = coaching.predict(dataPoint)
  conference_prediction = conference.predict(dataPoint)
  league_prediction = league.predict(dataPoint)

  final_prediction = (0.5*coach_prediction + 0.3*conference_prediction + 0.2*league_prediction)
  runProb = final_prediction[0][0]
  passProb = final_prediction[0][1]
  return (runProb, passProb)

#A function to convert input data into features that the network will use for a prediction
def clean_data(oScore, dScore, quarter, minutes, seconds, yardsToGoal, dwn, dist):
  score_difference = oScore - dScore
  oneScoreGame = 1 if score_difference > -8 and score_difference < 8 else 0
  period = quarter
  seconds_remaining = ((4-quarter) * 15 * 60) + (minutes * 60) + seconds
  secondsInHalf = (seconds_remaining - 1800) if period < 2 else seconds_remaining
  yardsToGoal = yardsToGoal
  down = dwn
  distance = dist
  arrayed_data = np.array([score_difference, oneScoreGame, period, seconds_remaining, secondsInHalf, yardsToGoal, down, distance]).reshape(1,-1)
  return arrayed_data

#A function to scale each feature to all other plays and return dataframe
def scaleNewData(oScore, dScore, quarter, minutes, seconds, yardsToGoal, dwn, dist):
  predict_data = clean_data(oScore, dScore, quarter, minutes, seconds, yardsToGoal, dwn, dist)
  play_df = pd.DataFrame(data=predict_data, columns=['score_differential', 'oneScoreGame', 'period', 'seconds_remaining', 'secondsInHalf', 'yardsToGoal', 'down', 'distance'])
  scaled_features = play_df.copy()
  features = scaled_features[numeric]
  features = ss.transform(features.values)
  scaled_features[numeric] = features
  play = np.array(scaled_features)
  return play

#Finally, a function that gets a final prediction from input data
def getPrediction(oScore, dScore, quarter, minutes, seconds, yardsToGoal, dwn, dist):
  play = scaleNewData(oScore, dScore, quarter, minutes, seconds, yardsToGoal, dwn, dist)
  pred = ensemblePrediction(play)
  return pred
  