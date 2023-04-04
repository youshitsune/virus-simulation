import streamlit as st
import pandas as pd

st.write("# Virus simulator")

a = st.slider("How much people can one person infect?", min_value=0, max_value=10)
b = st.slider("For how many days?", min_value=2, max_value=20)

if a == 0:
    st.write("Choose a number")
else:
    number_infection = [1]
    infected = 1
    for i in range(1,b):
        infected = infected + infected*a
        number_infection.append(infected)
    
    tbl = pd.DataFrame(data=number_infection,columns=["Infected people"],index=[x for x in range(1, b+1)])
    st.table(tbl)
    st.line_chart(tbl)
