"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np



df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})



st.write("Here's our first attempt at using data to create a table:")
st.write(df)



st.write("Numpy usage:")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)




st.write("Numpy highlights sths:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))


st.write("Table usage:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)


st.write("Chart usage:")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


st.write("Map usage:")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


st.write("Slider usage:")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


st.write("User Input usage:")
st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name


st.write("Show / Hide df:")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


st.write("Selectbox, options:")
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option