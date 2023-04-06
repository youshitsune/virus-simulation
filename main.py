import streamlit as st
import pandas as pd

st.write("# Virus simulator")

infect_rate = st.slider("How much people can one person infect?", min_value=0, max_value=10)
days = st.slider("For how many days?", min_value=2, max_value=20)
death_rate = st.slider("What is death rate?", min_value=0, max_value=100)
if infect_rate == 0:
    st.write("Choose an infect rate")
else:
    number_infection = [1]
    dead = [0]
    infected = 1
    for i in range(1,days):
        infected = infected + infected*infect_rate
        number_infection.append(infected)
        if (death_rate/100)*sum(number_infection) < 1:
            dead.append(0)
        else:
            number_infection[-1] -= int((death_rate/100)*sum(number_infection))
            dead.append(int((death_rate/100)*sum(number_infection)))

    tbl = pd.DataFrame(data={"Infected people": number_infection, "Deaths": dead}, index=[x for x in range(0, days)])
    st.table(tbl)
    st.line_chart(tbl)
