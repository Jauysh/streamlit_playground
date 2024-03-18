"""
# Basics
## My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np
import time


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})



st.write("1. Here's our first attempt at using data to create a table:")
st.write(df)



st.write("2. Numpy usage:")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)




st.write("3. Numpy highlights sths:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))


st.write("4. Table usage:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)


st.write("5. Chart usage:")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


st.write("6. Map usage:")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


st.write("7. Slider usage:")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


st.write("8. User Input usage:")
st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name


st.write("9. Show / Hide df:")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


st.write("10. Selectbox, options:")
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option


st.write("11. Layouts, sidebar & slider. Left slidebar")
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



st.write("12. Side-by-side content")
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")



st.write("13. Show progress")

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.06)

'...and now we\'re done!'