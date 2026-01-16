import os


FILE_NAME = "recipes.txt"
SEPARATOR = "---RECIPE_END---"
def load_recipes():
    recipes = []
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            content = file.read()

        raw_recipes = content.split(SEPARATOR)

        for raw_recipe in raw_recipes:
            raw = raw.strip()
            if not raw:
                continue

            parts = raw.split('\n\n')
            if len(parts) >= 3:
                title = parts[0].replace("Назва: ", "").strip()
                ingredients = parts[1].replace("Інгредієнти:\n", "").strip()
                instructions = parts[2].replace("Інструкції:\n", "").strip()

                recipes.append({
                    'title': title,
                    "ingredients": ingredients,
                    "instructions": instructions
                })

    except FileNotFoundError:
        print("файл із рецептами не знайдено. Створюємо новий файл.")
    except Exception as e:
        print(f"Сталася помилка при завантаженні рецептів: {e}")
    
    return recipes




def save_recipe(recipes):
    try:
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            for recipe in recipes:
                file.write(f"Назва: {recipe['title']}\n\n")
                file.write(f"Інгредієнти:\n{recipe['ingredients']}\n\n")
                file.write(f"Інструкції:\n{recipe['instructions']}\n")
                file.write(f"{SEPARATOR}\n\n")
        print("Рецепт успішно збережено!")
    except Exception as e:
        print(f"Сталася помилка при збереженні рецептів: {e}")

def add_new_recipe():
    print("\n--- Додати новий рецепт ---")
    title = input("Введіть назву рецепту: ").strip()
    ingredients = input("Введіть інгредієнти (розділені комами): ").strip()
    instructions = input("Введіть інструкції приготування: ").strip()

    if title and ingredients and instructions:
        new_recipe = {
            'title': title,
            'ingredients': ingredients,
            'instructions': instructions
        }
        recipes.append(new_recipe)
        print(f"Рецепт '{title}' додано успішно!")
    else:
        print("помилка не можна додати рецепт з порожніми полями.")

recipes = load_recipes()


def view_recipes_titles(recipes):
    if not recipes:
        print("Немає доступних рецептів.")
        return False

    print("\n--- Список рецептів ---")
    for index, recipe in enumerate(recipes, start=1):
        print(f"{index}. {recipe['title']}")
    print("-----------------------")
    return True
def view_single_recipe(recipes):
    if not view_recipe_titles(recipes):
        return
    try:
        recipe_num = int(input("Введіть номер рецепту, який хочете переглянути: "))

        if 1 <= recipe_num <= len(recipes):
            recipe = recipes[recipe_num - 1]
            print(f"\n--- Рецепт: {recipe['title']} ---")
            print(f"Інгредієнти:\n{recipe['ingredients']}\n")
            print(f"Інструкції:\n{recipe['instructions']}\n")
            print("-----------------------")
        else:
            print("Невірний номер рецепту.")

    except ValueError:

        print("Будь ласка, введіть дійсний номер рецепту.")

    except Exception as e:
        print(f"Сталася помилка: {e}")



def main():
    recipes = load_recipes()

    while True:
        print("\n--- Меню Рецептів ---")
        print("1. Переглянути всі рецепти")
        print("2. Додати новий рецепт")
        print("3. Вийти")
        choice = input("Оберіть опцію (1-3): ").strip()

        if choice == '1':
            view_single_recipe(recipes)
        elif choice == '2':
            add_new_recipe()
            save_recipe(recipes)
        elif choice == '3':
            print("Вихід з програми. До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, оберіть опцію від 1 до 3.")


if __name__ == "__main__":
    main()