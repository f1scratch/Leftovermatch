import streamlit as st
st.title("Recipe Details(❁´◡`❁)")

with st.container(border = True):
        if "selected_recipe" not in st.session_state:
                st.write("No recipe selected")
        else:
                recipe = st.session_state["selected_recipe"]

                st.subheader(recipe['name'])
                st.write(f"Score: {int(recipe['score'])}%")
                st.subheader("Ingredients you have ✅:" )
                for ingredient in recipe["matched"]:
                        st.write(f" • {ingredient}")
                st.subheader("Ingredients needed 🛒:")
                for ingredient in recipe["missing"]:
                        st.write(f"• {ingredient}")
                st.subheader("Instructions 👩‍🍳:")
                st.write(f"{recipe['instructions']}")
                st.subheader("Dietary-tag 🌱:")
                st.write(f"{recipe['dietary_tag']}")

col1, col2 = st.columns([1,5])

with col1:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

with col2:
      if st.button("Return to Results 🔙"):
        st.switch_page("pages/results.py")