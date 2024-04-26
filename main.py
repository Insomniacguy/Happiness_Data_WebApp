import streamlit as st
import pandas as pd
import plotly.express as px
from functions import get_data

# df = pd.read_csv("happy.csv")
# st.write(df)

st.title("In Search For Happiness")

options1 = st.selectbox("Select the data for x-axis", ("Happiness", "GDP", "Generosity"))
options2 = st.selectbox("Select the data for y-axis", ("Happiness", "GDP", "Generosity"))

st.subheader(f"{options1.capitalize()} and {options2.capitalize()}")

x1, y1 = get_data(options1, options2)
# st.write(x1)
# st.write(x2)

fig = px.scatter(x=x1, y=y1, labels={"x": options1, "y": options2})
st.plotly_chart(fig)
