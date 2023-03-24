from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


# Умножить элементы списка на число порций, вернуть новый словарь
def multiply(ingredients, count=1):
    multiplied_ingrs = {}
    for key in ingredients.keys():
        # следующие проверки пришлось вставить, т.к. float после умножения
        # показывал некрасивые числа 0.30000000000004 и т.п.
        if type(ingredients[key]) is int:
            multiplied_ingrs[key] = ingredients[key] * count
        if type(ingredients[key]) is float:
            num = ingredients[key] * count
            multiplied_ingrs[key] = f'{num:.2f}'
    return multiplied_ingrs


def omlet(request):
    servings = int(request.GET.get('servings', 1))
    context = {'recipe': multiply(DATA['omlet'], servings)}
    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = int(request.GET.get('servings', 1))
    context = {'recipe': multiply(DATA['pasta'], servings)}
    return render(request, 'calculator/index.html', context)

def buter(request):
    servings = int(request.GET.get('servings', 1))
    context = {'recipe': multiply(DATA['buter'], servings)}
    return render(request, 'calculator/index.html', context)