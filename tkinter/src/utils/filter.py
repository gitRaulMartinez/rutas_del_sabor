def filter_ingredient(value,ingredient_search):
    for ingredient in value.ingredients:
        if ingredient_search.lower() in ingredient.lower():
            return True
    return False