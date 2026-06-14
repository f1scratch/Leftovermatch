import streamlit as st
from database import add_recipe
from database import search
from database import delete
from database import update

st.title("Recipe Control Panel (⌐■_■)")
col1,col2 = st.columns(2)

with col1:
     with st.container(border = True):
          st.subheader("➕ New Recipes:")
          name = st.text_input("Enter recipe name")


          ingredients = st.text_area("Enter ingredients:")


          instructions = st.text_area("Enter instructions:")

          dietary_tag = st.selectbox("Select diet:",["","halal","vegetarian","vegan"])


          if st.button("Add recipe 📥"):

               success = add_recipe(name, ingredients, instructions, dietary_tag)

               if success:
                    st.success("The recipe is added!") #built in streamlit theme/function "success button"
               else:
                    st.error("This recipe already exists.") #built in streamlit "error button"

with col2:
     with st.container(border = True):
          st.subheader("✨Modify Recipes:")
          search_name = st.text_input("Search for recipes")

          if st.button("Search🔎"):
               searched_recipe = search(search_name)
               if searched_recipe:
                    st.success("recipe found")
                    st.write(searched_recipe['name'])
                    st.write("Ingredients:", ", ".join(searched_recipe["ingredients"]))
                    st.write(f"instructions: {searched_recipe['instructions']}")
                    st.write(f"Dietary-tag: {searched_recipe['dietary_tag']}")

                    st.session_state["searched_recipe"] = searched_recipe
               else:
                    st.error("Recipe does not exist.")

          if "searched_recipe" in st.session_state:

               recipe = st.session_state["searched_recipe"]

               name = recipe["name"]
               new_name = st.text_input("Name", value = recipe["name"])

               ingredients = st.text_input("Ingredients", value = ",".join(recipe["ingredients"]))

               instructions = st.text_input("Instructions", value = recipe["instructions"])

               tags = ["", "halal", "vegetarian", "vegan"]
               current_index = tags.index(recipe["dietary_tag"].lower())

               dietary_tag = st.selectbox("Dietary Tag", tags, current_index)

               col1,col2,col3 = st.columns(3)
               with col1:
                   
                    if st.button("Update Recipe💾"):
                         action = update(name, new_name, ingredients, instructions, dietary_tag)

                         if action:
                              st.success("Recipe is updated ✅")
                              st.session_state["searched_recipe"] = {
                                   "name": new_name,
                                   "ingredients": [i.strip() for i in ingredients.split(", ")], #to avoid spacing
                                   "instructions": instructions,
                                   "dietary_tag": dietary_tag
                              }
                         else:
                              st.error("Recipe name already exists. Enter a different recipe name.")
               with col2:
                    if st.button("Delete Recipe 🗑️"):
                         action = delete(st.session_state["searched_recipe"]["name"])

                         if action:
                              st.success("Recipe deleted ✅")
                         else:
                              st.error("Recipe cannot be deleted")
               
              

               
if st.button("🏠 Home"):
        st.switch_page("app.py")
