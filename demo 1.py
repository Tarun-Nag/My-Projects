import tkinter
from tkinter import font
import pandas as pd
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox,PhotoImage

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
        axis=1
    )
    
    # Create a dictionary for quick lookup
    recipe_dict = dict(zip(df['Dish Name'].str.lower(), df['full_recipe']))

    # Create a simple GUI using Tkinter
    root = tk.Tk()
    root.title("Tarun's Pakashala")
    root.geometry()

    # Input field
    icon=tkinter.PhotoImage(file=r"C:\Users\tnag3\OneDrive\Pictures\Naruto\xyz.png")
    label=tkinter.Label(root,image=icon)
    label.pack()
    Label(root, text="Hello and Welcome to Tarun's Pakashala", font=("Times New Roman Bold",30)).pack(pady=30)
    Label(root, text="Enter the name of the dish you'd like to learn about:" , font=("Arial Italic",20)).pack(pady=10)
    custom_font=font.Font(size=14)
    entry = Entry(root,width=50,font="Arial")
    entry.pack()

    # Label to display the recipe
    recipe_label = Label(root, text="", wraplength=400, justify="left")
    recipe_label.pack(pady=10)

    # Button to get the recipe
    def on_button_click():
        dish_name = entry.get().lower()  # Get the user input
        recipe = recipe_dict.get(dish_name, "Recipe not found.")

        # Update recipe label
        recipe_label.config(text=recipe)

    Button(root, text="Get Recipe", command=on_button_click).pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

else:
    print("The required columns 'Ingredients' and 'Detailed Process' are not present in the dataset.")
