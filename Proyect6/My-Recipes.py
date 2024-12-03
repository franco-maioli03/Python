import os
from pathlib import Path
from os import system

# Definir el directorio de recetas relativo al script actual
current_dir = Path(__file__).parent
my_path = Path(current_dir, "Recipes")


def count_recipes(path):
    counter = 0
    for txt in Path(path).glob("**/*.txt"):
        counter += 1
    return counter


def start():
    system('cls')
    print('*' * 50)
    print('*' * 5 + " Welcome to the Recipe Manager " + '*' * 5)
    print('*' * 50)
    print('\n')
    print(f"Recipes are located at {my_path}")
    print(f"Total recipes: {count_recipes(my_path)}")

    menu_choice = 'x'
    while not menu_choice.isnumeric() or int(menu_choice) not in range(1, 7):
        print("Choose an option:")
        print('''
        [1] - Read a recipe
        [2] - Create a new recipe
        [3] - Create a new category
        [4] - Delete a recipe
        [5] - Delete a category
        [6] - Exit the program''')
        menu_choice = input()

    return int(menu_choice)


def show_categories(path):
    print("Categories:")
    category_path = Path(path)
    category_list = []
    counter = 1

    for folder in category_path.iterdir():
        folder_str = str(folder.name)
        print(f"[{counter}] - {folder_str}")
        category_list.append(folder)
        counter += 1

    return category_list


def choose_category(category_list):
    correct_choice = 'x'

    while not correct_choice.isnumeric() or int(correct_choice) not in range(1, len(category_list) + 1):
        correct_choice = input("\nChoose a category: ")

    return category_list[int(correct_choice) - 1]


def show_recipes(path):
    print("Recipes:")
    recipe_path = Path(path)
    recipe_list = []
    counter = 1

    for recipe in recipe_path.glob('*.txt'):
        recipe_str = str(recipe.name)
        print(f"[{counter}] - {recipe_str}")
        recipe_list.append(recipe)
        counter += 1

    return recipe_list


def choose_recipe(recipe_list):
    recipe_choice = 'x'

    while not recipe_choice.isnumeric() or int(recipe_choice) not in range(1, len(recipe_list) + 1):
        recipe_choice = input("\nChoose a recipe: ")

    return recipe_list[int(recipe_choice) - 1]


def read_recipe(recipe):
    print(Path.read_text(recipe))


def create_recipe(path):
    exists = False

    while not exists:
        print("Enter the name of your recipe: ")
        recipe_name = input() + '.txt'
        print("Write your new recipe: ")
        recipe_content = input()
        new_path = Path(path, recipe_name)

        if not os.path.exists(new_path):
            Path.write_text(new_path, recipe_content)
            print(f"Your recipe {recipe_name} has been created")
            exists = True
        else:
            print("Sorry, that recipe already exists")


def create_category(path):
    exists = False

    while not exists:
        print("Enter the name of the new category: ")
        category_name = input()
        new_path = Path(path, category_name)

        if not os.path.exists(new_path):
            Path.mkdir(new_path)
            print(f"Your new category {category_name} has been created")
            exists = True
        else:
            print("Sorry, that category already exists")


def delete_recipe(recipe):
    Path(recipe).unlink()
    print(f"The recipe {recipe.name} has been deleted")


def delete_category(category):
    Path(category).rmdir()
    print(f"The category {category.name} has been deleted")


def go_back_to_start():
    back_choice = 'x'

    while back_choice.lower() != 'v':
        back_choice = input("\nPress V to return to the menu: ")


end_program = False

while not end_program:
    menu = start()

    if menu == 1:
        my_categories = show_categories(my_path)
        my_category = choose_category(my_categories)
        my_recipes = show_recipes(my_category)
        my_recipe = choose_recipe(my_recipes)
        read_recipe(my_recipe)
        go_back_to_start()
    elif menu == 2:
        my_categories = show_categories(my_path)
        my_category = choose_category(my_categories)
        create_recipe(my_category)
        go_back_to_start()
    elif menu == 3:
        create_category(my_path)
        go_back_to_start()
    elif menu == 4:
        my_categories = show_categories(my_path)
        my_category = choose_category(my_categories)
        my_recipes = show_recipes(my_category)
        my_recipe = choose_recipe(my_recipes)
        delete_recipe(my_recipe)
        go_back_to_start()
    elif menu == 5:
        my_categories = show_categories(my_path)
        my_category = choose_category(my_categories)
        delete_category(my_category)
        go_back_to_start()
    elif menu == 6:
        end_program = True
