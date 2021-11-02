import numpy as np
import pickle
import pandas as pd
import joblib
import streamlit as st
def load():
    global __model
    with open('model.pkl', 'rb') as f:
            __model = joblib.load(f)
def main():
    text=st.text_area('enter news to find fake or real')
    m=pd.Series(data=text)
    if st.button('predict'):
        k=__model.predict(m)
        if k==1:
            st.success('Real News')
        else:
            st.error('Fake News')
        x='akhil'
        #st.write(x)
        #st.write(tt)
if __name__ == '__main__':
    # cursor=tweepy.Cursor(api.user_timeline,id=user).items(10)
    load()
    main()
