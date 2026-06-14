# Main application
import streamlit as st
from recommendation import get_recommendations

st.set_page_config(layout = "wide") #zooms in. the page contents are not small
st.title("LeftoverMatch🥘")
st.markdown("Turn Leftovers into Meals!  Search done, meal done.")


col1,col2,col3 = st.columns(3) #creates 3 columns
with st.form("search_form"):
     with col1:
          with st.container(border = True):
               st.subheader("Ingredients 🛒")
               ingredients = st.text_area("Enter ingredients seperated with commas")
     with col2:
          with st.container(border = True):
               st.subheader("Dietary preference 😋")
               diet = st.radio("Choose an option",["None","Halal","Vegetarian","Vegan"])
     with col3:
          with st.container(border = True):
               st.subheader("Allergies ✍")
               allergies = st.text_area("Enter allergies, seperating them with commas")

     col1,col2,col3,col4,col5 = st.columns(5)
     with col3:
          submit = st.form_submit_button("Find Recipes 🍽️")

if submit:
     results = get_recommendations(ingredients, diet.lower(), allergies)
     st.session_state["results"] = results #creating soemthing like a global variable across files/pages
     st.switch_page("pages/results.py")
     

