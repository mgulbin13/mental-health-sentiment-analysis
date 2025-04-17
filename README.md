# Mental Health Sentiment Analysis using Machine Learning
By Matthew Gulbin

## Table of Contents
[Overview](#overview)

[Data Summary](#datasummary)

[Initial Model](#initialmodel)

[Neural Network Implementation](#neuralnetworkimplementation)

[Hyperparameter Tuning](#hyperparametertuning)

[Final Implementation](#finalimplementation)

[Web App](#webapp)

[Conclusion/Future Work](#conclusionfuturework)

[Build Guide](#buildguide)

## Overview

For this project, I decided to research social media sentiment analysis, particularly through the lens of mental health. To that end, I trained machine learning models to try to predict mental health conditions (anxiety, depression, etc.) based on text input from a user. 

This project is made up primarily by two files: a Jupyter notebook, where I performed the data cleaning, modeling, and tuning, and a Python file for a web app that I built using Streamlit that allows the user to enter text and receive a prediction from the model.

<a id="datasummary"></a>

## Data Summary 

I used the sentiment analysis on social media dataset from [Kaggle](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health/data). It contains 53k social media posts collected from Reddit and Twitter/X that are labeled with one of the following:
- Normal
- Anxiety
- Depression
- Suicidal
- Stress
- Bipolar
- Personality Disorder

<a id="initialmodel"></a>

## Initial Model

I implemented the initial model using Multinominal Naive Bayes. It performed horribly, with a F1 score of 0.17, due to semantic overlap between categories such as anxiety and stress.

<a id="neuralnetworkimplementation"></a>

## Neural Network implementation

For a Neural Network implementation of this model, I chose to use BERT (Bidirectional Encoder Representations from Transformers) to encode and model the dataset. I utilized HuggingFace's python libraries, which include pretrained implementations of BERT for NLP classification problems.

<a id="hyperparametertuning"></a>

## Hyperparameter Tuning

The key hyperparameters that I tuned to maximize model performance were learning rate, weight decay, and sample size. After tuning, the model achieved a F1 score of 0.73.

<a id="finalimplementation"></a>

## Final Implementation

For the final implementation of the model, I decided to undersample the training dataset to solve the underlying class imbalance problem. Training the model on this data resulted in an improved F1 score of 0.81.

<a id="webapp"></a>

## Web App

I also built a simple web app using Streamlit that allows users to input text and recieve a mental health label prediction based on the trained model. 

<a id="conclusionfuturework"></a>

## Conclusion/Future Work

In conclusion, this model could be used to help diagnose mental health conditions based on social media posts. Given more time, I would like to improve this project in the following ways:
- Research the semantic subtleties between very coorelated mental health conditions, such as anxiety and stress.
- Deploy the web app so that internet users will be able to use it without a complicated setup.
- Gather more modern social media posts to keep the model up to date.


____

<a id="buildguide"></a>

## Build Guide
### Dependencies:
- Python 3.10+
- Pandas
- Streamlit
- HuggingFace Transformers, Datasets, Evaluate
- Scikit-learn
- Seaborn
- Matplotlib

### How to Run Web App:
1. In the project directory, open a terminal window and type ``` streamlit run app.py ```
2. Your web browser should automatically open the app