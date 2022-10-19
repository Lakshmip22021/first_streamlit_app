
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

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_row = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
streamlit.text("The Fruit Load List Contains:")
#streamlit.text(my_data_row)
streamlit.dataframe(my_data_row)

add_myfruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding ', add_myfruit)
my_cur.execute("insert into fruit_load_list values('from streamlit')")





