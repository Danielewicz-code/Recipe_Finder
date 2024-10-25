# Recipe_Finder


## Recipe Finder

Recipe Finder is a Python-based program that allows users to input a list of ingredients they have on hand and receive recipe suggestions that utilize those ingredients. The program leverages the Spoonacular API to fetch recipes, filtering results to show recipes with three or fewer missing ingredients. Each recipe suggestion includes details on which ingredients are used, which are missing, and those unused. A link to the full recipe is also provided for easy access to instructions.

## Features

Ingredient-Based Recipe Search: Input ingredients to find recipes that best match your list, reducing food waste by using what's available.

Used, Missed, and Unused Ingredients: Displays which ingredients from your input are used in the recipe, which are missing, and which are unused.

Recipe URL Generation: Generates a link to the full recipe on Spoonacular’s website for further details and instructions.

Custom Filtering: Filters recipes to show those with three or fewer missing ingredients, ensuring that most required items are already on hand.

## Project Structure

RecipeFetcher Class: Handles interactions with the Spoonacular API, fetching recipes based on provided ingredients.

Recipe Class: Processes and formats recipe data, organizing it into used, missed, and unused ingredients and generating the recipe link.

Main Program: Gathers user input, fetches matching recipes, and displays relevant details.

