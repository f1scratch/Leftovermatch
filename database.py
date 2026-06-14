import sqlite3
import streamlit as st

def create_table():
    connection = sqlite3.connect("recipes.db")
    cursor = connection.cursor()

    #creating table in recipes.db
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ingredients TEXT NOT NULL,
        instructions TEXT NOT NULL,
        dietary_tag TEXT
        )""")
    
    connection.commit()
    connection.close()


#retrieving recipes
def all_recipes():
    connection = sqlite3.connect("recipes.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM recipes")

    rows = cursor.fetchall()

    connection.close()

    recipes = []

    for row in rows:
        recipe = {
            "id": row[0],
            "name": row[1],
            "ingredients": [i.strip().lower() for i in row[2].split(",")], #important, gets each ingredient seperatly.
            "instructions": row[3],
            "dietary_tag": row[4]
        }
        recipes.append(recipe)

    return recipes


create_table()


def add_recipe(name, ingredients, instructions, dietary_tag):
    connection = sqlite3.connect("recipes.db")
    cursor = connection.cursor()

    
    cursor.execute("SELECT * FROM recipes WHERE LOWER(name) = LOWER(?)",
    (name,))
    existing_recipe = cursor.fetchone()
    if existing_recipe:
        connection.close()
        return False
    else:

        cursor.execute("""INSERT INTO recipes (name, ingredients, instructions, dietary_tag) VALUES (?,?,?,?)""",
        (name,ingredients,instructions,dietary_tag))

        connection.commit()
        connection.close()
        return True



def search(name):
    recipes = all_recipes()

    for recipe in recipes:
        if recipe["name"].lower().strip() == name.strip().lower():
            return recipe
        
    return None


def delete(name):
    
    import os
    print("Deleting from:", os.path.abspath("recipes.db"))

    ...
    connection = sqlite3.connect("recipes.db")
    cursor = connection.cursor()

    cursor.execute(""" DELETE FROM recipes WHERE LOWER(name) = LOWER(?)""", (name,))
    
    connection.commit()

    recipe_deleted = cursor.rowcount
    connection.close()

    if recipe_deleted:
        return True
    else:
        return False




def update(name, new_name, ingredients, instructions, dietary_tag):
    connection = sqlite3.connect("recipes.db")
    cursor = connection.cursor()

    for recipe in all_recipes():
        if recipe['name'].lower().strip() == new_name.lower().strip() and recipe['name'].lower().strip() != name.lower().strip(): #what if the user didn't update name? then when all recipes are searche dit chould not count the og name as a duplicate
            connection.close()
            return False
        
    cursor.execute("""UPDATE recipes 
                   SET 
                   name = ?,
                   ingredients = ?,
                   instructions = ?,
                   dietary_tag = ?

                   WHERE LOWER(name) = LOWER(?)""",(new_name,ingredients,instructions,dietary_tag,name))

    connection.commit()
    connection.close()

    return True