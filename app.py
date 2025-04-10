import streamlit as st
from transformers import pipeline

classifier = pipeline('text-classification', model='./model/final')

def predict(text):
    prediction = classifier(text)
    match prediction[0]['label']:
        case "LABEL_0":
            condition = "anxious"
        case "LABEL_1":
            condition = "normal"
        case "LABEL_2":
            condition = "depressed"
        case "LABEL_3":
            condition = "suicidal"
        case "LABEL_4":
            condition = "stressed"
        case "LABEL_5":
            condition = "a personality disorder"
        case "LABEL_6":
            condition = "bipolar"
    output = f"You are feeling {condition} ({round((prediction[0]['score'] * 100), 2)}% confidence)"
    return output

st.title('Say something...')

input = st.text_input('input', placeholder='Your text here...', label_visibility='hidden')
st.write(f"### {predict(input)}")


