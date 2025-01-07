from flask import Flask, render_template, request, url_for, redirect, abort, jsonify
import pandas as pd
import json
import os

app = Flask(__name__)

# Data file path (using os.path.join for robustness)
DATASET_FILE = 'cuisine_updated.csv'
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key


# Load the DataFrame (executed only once)
try:
    recipes_df = pd.read_csv(DATASET_FILE)
    recipes_df['lower_ingredients'] = recipes_df['ingredients'].str.lower()
    print("CSV file loaded successfully into Pandas DataFrame.")
except FileNotFoundError:
    print(f"Error: CSV file not found at {DATASET_FILE}. Exiting...")
    exit()
except Exception as e:  # Catching other potential errors during CSV loading
    print(f"An error occurred while loading the CSV: {e}. Exiting...")
    exit()



# Recommendation logic (moved from recommendation.py)
def filter_recipes(ingredients_list):
    if not ingredients_list:
        return []
    try:
        filtered_recipes = recipes_df[
            recipes_df['lower_ingredients'].apply(lambda x: all(ing.strip() in x for ing in ingredients_list))
        ]
        return filtered_recipes.to_dict(orient='records')
    except Exception as e:
        print(f"Error filtering recipes: {e}")
        return []



# --- Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredients = request.form.get('ingredients')
        if ingredients:
            ingredients_list = [ing.strip().lower() for ing in ingredients.split(',')]
            recipes = filter_recipes(ingredients_list)
            return render_template('recommendations.html', recipes=recipes, selected_ingredients=ingredients)
        else:
            error_message = "Please enter at least one ingredient."
            return render_template('index.html', error_message=error_message) # Pass the error message
    else:
        random_recipes = recipes_df.sample(n=12).to_dict('records')
        recipes_json = json.dumps(recipes_df.sample(n=8).to_dict("records"))
        return render_template('index.html', recipes_json=recipes_json, all_recipes=random_recipes)

@app.route('/recipe/<recipe_name>')  # Dynamic route for recipe details
def recipe_details(recipe_name):
    recipe = recipes_df[recipes_df['name'] == recipe_name].to_dict('records')
    if recipe: # Check if the recipe was found
        return render_template('recipe_detail.html', recipe=recipe[0]) # Render detail
    else:
        return "404: Page not found", 404
        #abort(404)  # Or redirect to a custom 404 page

# Error Handlers
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404 # Return your custom 404 page instead of a string

@app.errorhandler(500)
def internal_server_error(error):
    return "500: Internal server error", 500

if __name__ == '__main__':
    app.run(debug=True)