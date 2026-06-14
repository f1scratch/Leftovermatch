from database import all_recipes



def get_recommendations(Ingredients,Diet, Allergies ):
     recipes = all_recipes()
     results = []
     ingredients = Ingredients.lower().split(",")
     ingredients = [i.strip() for i in ingredients]

     diet = Diet.lower().strip()

     allergies = Allergies.lower().split(",")
     allergies = [a.strip() for a in allergies if a.strip() != ""]

     #matching system
     for r in recipes:
          can_continue = True
          for allergy in allergies:
               for recipe_ingredient in r["ingredients"]:
                    if allergy in recipe_ingredient.lower():
                         can_continue = False

          if diet == "vegan":
               if r["dietary_tag"] != "vegan":
                    can_continue = False

          elif diet == "vegetarian":
               if r["dietary_tag"] not in ["vegetarian", "vegan"]:
                    can_continue = False

          elif diet == "halal":
               if r["dietary_tag"] != "halal":
                    can_continue = False
                    

          if can_continue == True:
          
               total_ingredients = len(r["ingredients"])
               matched = []
               missing = []
               for ingredient in r["ingredients"]:
                    if ingredient in ingredients:
                         matched.append(ingredient)
                    else:
                         missing.append(ingredient)
          

               #scoring
               score = (len(matched)/total_ingredients)*(100)
               r["score"] = score
               r["matched"] = matched
               r["missing"] = missing
               results.append(r) #adds recipe to the results. it pased the filtering

     #sorting
     results.sort(
         key=lambda recipe: recipe["score"],
          reverse=True)
     

     return results


# #storing the recommendable recipes
# result = (get_recommendations(
#      "bread,cheese,butter,corn",
#      "vegetarian",
#      ""
# ))

# #displaying top 3 recipes
# for recipe in result[:7]:
#           print(recipe["name"])
#           print(f"Score: {int(recipe["score"])} %") #printing scores, maipulated number displaying format
#           print(f"Matched ingredients: {recipe["matched"]}")
#           print(f"Missing ingredients: {recipe["missing"]}")
#           print(f"Instructions: {recipe["instructions"]}")
#           print()

      





 