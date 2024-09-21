na = ["ingredient_name", "quantity", "measure"]

cook_book = {}
with open("recipes.txt", "r") as f:
    res = f.read()
    res = res.split("\n\n")
    for i in res:
        k, x, *v = i.split("\n")
        v = [dict(zip(na, j.split(" | "))) for j in v]
        cook_book[k] = v


def get_shop_list_by_dishes(dishes, person_count):
    ingres = {}
    if person_count < 1:
        return
    for i in dishes:
        for j in cook_book.get(i):
            ingre = j.get("ingredient_name")
            ex_item = int(j.get("quantity")) * person_count
            if ingre in ingres:
                ex_item += ingres.get(ingre)["quantity"]
            ingres[ingre] = {"measure": j.get("measure"), "quantity": ex_item}
    return ingres


# print(cook_book)
# print(get_shop_list_by_dishes(["Омлет"], 1))
# print(get_shop_list_by_dishes(["Омлет", "Фахитос"], 4))
# print(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2))
# get_shop_list_by_dishes(["Запеченный картофель", "Омлет", "Фахитос"], 2)