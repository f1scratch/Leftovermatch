import streamlit as st

st.title("Recommended Recipes╰( *°▽°* )╯")

if "results" not in st.session_state:
     st.write("No searches yet")
else:
     with st.container(border = True):
          for recipe in st.session_state["results"][:1]:
               st.subheader(recipe["name"])
               st.write(f"🥇Score: {int(recipe['score'])}% Match")
               if st.button(f"View details - {recipe['name']}"): 
                    st.session_state["selected_recipe"] = recipe
                    st.switch_page("pages/recipe_details.py")
               
     with st.container(border = True):
          for recipe in st.session_state["results"][1:2]:
               st.subheader(recipe["name"])
               st.write(f"🥈Score: {int(recipe['score'])}%")
               
               if st.button(f"View details - {recipe['name']}"): 
                    st.session_state["selected_recipe"] = recipe
                    st.switch_page("pages/recipe_details.py")

     with st.container(border = True):
          for recipe in st.session_state["results"][2:3]:
               st.subheader(recipe["name"])
               st.write(f"🥉Score: {int(recipe['score'])}%")
               
               if st.button(f"View details - {recipe['name']}"): 
                    st.session_state["selected_recipe"] = recipe
                    st.switch_page("pages/recipe_details.py")

     with st.container(border = True):
          for recipe in st.session_state["results"][3:7]:
               st.subheader(recipe["name"])
               st.write(f"Score: {int(recipe['score'])}%")
               
               if st.button(f"View details - {recipe['name']}"): 
                    st.session_state["selected_recipe"] = recipe
                    st.switch_page("pages/recipe_details.py")

col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Home"):
        st.switch_page("app.py")