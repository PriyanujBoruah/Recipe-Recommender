# Recipe Recommendation Engine

This project is a web application that helps users find recipes based on the ingredients they have. It's built using Python (Flask, Pandas) for the backend and HTML, CSS, and JavaScript for the frontend.  The application provides a user-friendly interface for searching recipes based on ingredients and browsing random recipe suggestions.


## Features

* **Ingredient-Based Search:** Enter a list of ingredients you have, and the app suggests recipes that use those ingredients.
* **Random Recipe Suggestions:** Explore a curated selection of random recipes for inspiration.
* **Recipe Details:** View complete recipe information, including ingredients, instructions, and an image (if available).
* **Responsive Design:**  The interface adapts to different screen sizes for optimal viewing.
* **Efficient Data Handling:** Utilizes Pandas DataFrames for efficient data manipulation and filtering.


## Technologies Used

* **Backend:** Python, Flask, Pandas
* **Frontend:** HTML, CSS, JavaScript
* **Data Storage:** CSV (or specify your data source and format)


## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PriyanujBoruah/Recipe-Recommender.git
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare your data:**
   * Place your preprocessed CSV file (`cuisines.csv` or whatever you named it) in the `data` directory.  Ensure your CSV has columns for `name`, `ingredients`, `instructions`, `image_url`, and `description` (adjust as needed based on your dataset).  Crucially, the `ingredients` column should contain comma-separated ingredient strings, pre-processed as described in the Data Preprocessing section.
   * If using a different directory, edit the `DATA_FILE_PATH` variable in `app.py`.

5. **Run the application:**
   ```bash
   python app.py
   ```
   The app should now be running at `http://127.0.0.1:5000/`.


## Data Preprocessing

This project requires preprocessing the recipe data, especially the `ingredients` column, for efficient ingredient-based searches.  If you're using a dataset that isn't already preprocessed, you should follow these steps, or similar depending on your data:

1. **Ingredient Parsing:** Extract individual ingredients from the `ingredients` column, which might be a free-form text string.
2. **Standardization:** Convert ingredient names to a standard format (lowercase, remove extra whitespace). This improves the accuracy of ingredient matching.

This preprocessing is not included in the application code itself (for simplicity and modularity).  Prepare the dataset once before running the app.



## Project Structure

```
recipe-recommendation-engine/
├── app.py             # Main Flask application file
├── templates/         # HTML templates
│   ├── index.html       # Homepage
│   ├── recommendations.html # Recommendations page
│   └── recipe_detail.html # Recipe details page
├── static/            # Static files (CSS, JavaScript)
│   └── style.css
└── data/
    └── cuisines.csv   # Your preprocessed recipe data (CSV or other format)
```


## Usage

1. **Homepage:**  The homepage displays a list of random recipes and an ingredient search form.
2. **Ingredient Search:** Enter ingredients (comma-separated) into the search form and click "Get Recommendations."
3. **Recommendations:**  The recommendations page displays recipes that match the entered ingredients.
4. **Recipe Details:**  Click on a recipe preview to view the full recipe details.
