
import streamlit
import pandas

streamlit.title("🥣  My Parents New Healthy Diner")
#streamlit.title(" just to need to check")
streamlit.header(' My Menu in Diner')
streamlit.text('Healthy food options :🥣  Kale, Spinach Smoothie')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

