import streamlit as st
import pandas as pd

# Create sample data
data = pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': ['A', 'B', 'C']
})

# UI Elements
st.title("Streamlit UI Elements Demo")

st.header("Basic Widgets")
st.button('Hit me')
st.checkbox('Check me out')
st.radio('Pick one:', ['nose', 'ear'])
st.selectbox('Select', [1, 2, 3])
st.multiselect('Multiselect', [1, 2, 3])

st.header("Sliders")
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1, '2'])

st.header("Input Fields")
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')

st.header("Date/Time")
st.date_input('Date input')
st.time_input('Time entry')

st.header("Data Display")
st.write("### Editable Data Frame")
edited_data = st.data_editor(data)  # Correct data_editor usage

st.header("File Operations")
st.file_uploader('File uploader')
st.download_button(
    label="Download Data",
    data=data.to_csv().encode('utf-8'),
    file_name='data.csv',
    mime='text/csv'
)

st.header("Media")
st.camera_input("Say cheese!")
st.color_picker('Pick a color')
