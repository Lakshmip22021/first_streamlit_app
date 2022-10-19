
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(fruitchoice):
         fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruitchoice)
         # json response taken loaded into pandas dataframe
         fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
         return fruityvice_normalized
         


streamlit.title("🥣  My Parents New Healthy Diner")
#streamlit.title(" just to need to check")
streamlit.header(' My Menu in Diner')
streamlit.text('Healthy food options :🥣  Kale, Spinach Smoothie')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Banana','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
         streamlit.error("Please select a fruit to get information")
   else:
         back_from_function = get_fruityvice_data(fruit_choice)
         streamlit.dataframe(back_from_function)
except URLError as e:
      streamlit.error()

#streamlit.stop()
def get_fruit_load_list():
         with my_cnx.cursor() as my_cur:
                  my_cur.execute("select * from fruit_load_list")
                  return my_cur.fetchall()

if streamlit.button('Get the Fruit load List'):
         my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
         my_data_row = get_fruit_load_list()
         my_cnx.close()
         streamlit.dataframe(my_data_row)
#streamlit.stop()

#Allow end user to add fruit
def insert_fruit_to_list(new_fruit):
         with my_cnx.cursor() as my_cur:
                  my_cur.execute("insert into fruit_load_list values('"+new_fruit+"')")
                  return "Thanks for adding " + new_fruit 

add_myfruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
         my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
         back_from_function = insert_fruit_to_list(add_myfruit)
         my_cnx.close()
         streamlit.text(back_from_function)

         





