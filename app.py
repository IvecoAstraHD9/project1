import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
st.title('Hello World!')
st.write("This is my first Streamlit app.")
with st.sidebar:
    st.write('This is a sidebar')

with st.expander('Expand'):
    st.write('This is expandable')


text = st.text_input("Enter text")
number = st.number_input("Enter number", step=1)
date = st.date_input("Enter date", datetime.now())        
# Sample data
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

st.title('Charts and Graphs')

# Line chart
st.line_chart(data)

# Area chart
st.area_chart(data)

# Bar chart
st.bar_chart(data)