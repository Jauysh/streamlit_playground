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


st.write("Layouts, sidebar & slider. Left slidebar")
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted? selectbox',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values.   sidebar',
    0.0, 100.0, (25.0, 75.0)
)



st.write("Side-by-side content")
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")