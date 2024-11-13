# Чтение списка рецептов из файла и оформление результата в виде словаря
def recipes_load(file_recipes):
    cook_book = {}
    with open(file_recipes, "r", encoding='utf-8') as file_:
        file1 = filter(None, (line.rstrip() for line in file_))
        for line in file1:
            line = line.rstrip('\n')
            filtered = ''.join([x for x in line if x.isalnum()])
            if filtered.isalpha() and ('|' not in line):   
                cook_book[line] = []
                current_key = line
            else:
                if not line.isdigit():
                    name, count, measure = line.split(" | ")
                    ingredient = dict(ingredient_name=name, quantity=int(count), measure=measure)
                    cook_book[current_key].append(ingredient)
    return cook_book
  
        
# Функция для вывода полученного словаря на экран (в удобочитаемом виде)
def print_recipes(cook_book):
    print("cook_book = {")
    for dish in cook_book:
        print("  '", dish, "': [", sep='')
        for ingredient in cook_book[dish]:
            print("    ",ingredient, ",", sep='')
        print("    ],")
    print("  }")


# Функция для вывода словаря с названием ингредиентов и его количества (ингредиенты могут повторяться)
def get_shop_list_by_dishes(dishes, person_count):
    list_by_dishes = dict()
    for dish in dishes:
        value = cook_book.get(dish)
        if value is not None:
            for ingredient in cook_book[dish]:
                if ingredient["ingredient_name"] not in list_by_dishes:
                    list_by_dishes[ingredient["ingredient_name"]] = dict(measure=ingredient["measure"], quantity=ingredient["quantity"] * person_count)
                else:
                    list_by_dishes[ingredient["ingredient_name"]]["quantity"] += ingredient["quantity"] * person_count
        else:
            print(f'Блюдо "{dish}" отсутствует в списке блюд.')
    return list_by_dishes


cook_book = recipes_load('recipes.txt')
print()
print(cook_book)
print()
print_recipes(cook_book)
print()

list_by_dishes = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)
print(list_by_dishes)
print()
