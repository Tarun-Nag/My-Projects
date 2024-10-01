import pandas as pd

# Load the dataset
file_path = r"C:\Users\tnag3\OneDrive\Desktop\dish_random.csv"
df = pd.read_csv(file_path)


# Clean the DataFrame (if necessary)
df.columns = df.columns.str.strip()  # Remove any leading/trailing spaces from column names


print("\n Namaste and Welcome to Tarun's Pakashala !!!\n I Would Love to share my Culinary Knowledge with YOU !! \n\n")
    

# Ensure the column names match exactly
if 'Ingredients' in df.columns and 'Detailed Process' in df.columns:
    # Create the 'full_recipe' column by combining 'Ingredients' and 'Detailed Process'
    df['full_recipe'] = df.apply(
    lambda row: f"\n\n Dish_Name: {row['Dish Name']} \n\n"
                f"State: {row['State']}\n\n"
                f"Cooking_Time: {row['Cooking Time']}\n\n"
                f"Ingredients: {row['Ingredients']}\n\n"
                f"Process: {row['Detailed Process']} \n\n"
                f"Serving_Suggestions: {row['Serving Suggestions']}\n\n",
                 axis=1)

    # Create a dictionary for quick lookup
    recipe_dict = dict(zip(df['Dish Name'].str.lower(), df['full_recipe']))

    # Function to get recipe by dish name
    def get_recipe(dish_name):
        dish_name_lower = dish_name.lower()  # Normalize the input to lowercase
        return recipe_dict.get(dish_name_lower, "Recipe not found.")

    # Example usage
    input_dish = input("Type in the name of the dish you'd like to learn about : ")
    predicted_recipe = get_recipe(input_dish)
    print(f"Recipe for {input_dish}: {predicted_recipe}")
else:
    print("The required columns 'Ingredients' and 'Detailed Process' are not present in the dataset.")
