import requests
import re
import settings

class RecipeFetcher:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url


    def fetch_ingredients(self, ingredients):
        full_url = f"{settings.base_url}?ingredients={','.join(ingredients)}&apiKey={settings.key}"
        r = requests.get(full_url)
        if r.status_code == 200:
            return r.json()
        else:
            print(f"Fetching wasn't possible: {r.status_code}")
            return None


class Recipe:
    def __init__(self, recipe_data):
        self.id = recipe_data["id"]
        self.title = recipe_data["title"]
        self.used_ingredients = recipe_data["usedIngredients"]
        self.missed_ingredients = recipe_data["missedIngredients"]
        self.unused_ingredients = recipe_data.get("unusedIngredients", [])
        self.missed_ingredient_count = recipe_data['missedIngredientCount']

    def recipe_url(self):
        formated_title = re.sub(r'[^a-zA-Z0-9 ]', '', self.title).replace(' ', '-').lower()
        return f"https://spoonacular.com/recipes/{formated_title}-{self.id}"
    
    def display(self):
        print(f"\nRecipe: {self.title}\n")

        

        print("Used Ingredients")
        for ingredient in self.used_ingredients:
            print(f"- {ingredient["name"]}, {ingredient["amount"]}, {ingredient["unit"]}")

        if self.missed_ingredients:
            print("Missed Ingredients:")
            for ingredient in self.missed_ingredients:
                print(f"- {ingredient["name"]}, {ingredient["amount"]}, {ingredient["unit"]}")

        if self.unused_ingredients:
            print("Unused Ingredients:")

            for ingredient in self.unused_ingredients:
                print(f"- {ingredient["name"]}, {ingredient["amount"]}, {ingredient["unit"]}")

        print(f"Recipe link: {self.recipe_url()}")
        

        
def main():

    ingredients = []

    print("type an ingredient or 'search' to get recipes")

    while True:
        ingr_inputs = input("Input ingredients: ")

        if ingr_inputs == 'search':
            break

        try:
            if not ingr_inputs.replace(' ', '').isalpha():
                raise ValueError("Ingredients must only contain letters.")
        
            ingredients.append(ingr_inputs)

            #print(f"ingredients: {ingredients}")
            
        
        except ValueError as e:
            print(e)

    fetcher = RecipeFetcher(api_key=settings.key, base_url=settings.base_url)
    data = fetcher.fetch_ingredients(ingredients)

    if data:
        for recipe_data in data:
            recipe = Recipe(recipe_data)
            if recipe.missed_ingredient_count <= 3:
                recipe.display()

if __name__ == '__main__':
    main()