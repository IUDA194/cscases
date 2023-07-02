from django.shortcuts import render, HttpResponse
from cases.models import User, Cases, inventory, contract
import random, datetime

def get_item(item_list, user_id, used_items):
    items = []
    probabilities = []

    for item_chance in item_list:
        for item, chance in item_chance.items():
            items.append(item)
            probabilities.append(chance)

    for item in used_items:
        inventory.objects.filter(user_id=user_id, item=item)[0].delete()

    selected_item = random.choices(items, probabilities)[0]
    inventory.objects.create(user_id=user_id, item=selected_item, date=datetime.datetime.now())
    return selected_item

def insert_item_to_contract(request):
    if request.method == "POST":
        return HttpResponse("poST")
    if request.method == "GET":
        item_id = request.GET.get("item_id")
        can_drop = list(map(str, request.GET.get("can_drop").split(";")))
        chanse = list(map(int, request.GET.get("chanse").split(";")))
        if len(can_drop) == len(chanse):
            for i in range(len(can_drop)):
                contract.objects.create(item_id=item_id, can_drop=can_drop[i], chanse=chanse[i]).save()
            return HttpResponse(f"Всё круто отработало {can_drop} \n {chanse}")
        else:
            return HttpResponse("Соси тут разная длинна задаваемых масивов")

def start_contract(request):
    if request.method == "POST":
        return HttpResponse("poST")
    if request.method == "GET":
        user_id = request.GET.get("user_id")
        items = list(map(str, request.GET.get("items").split(";")))
        item_can_drop = []
        for name in items:
            contr = contract.objects.all()
            for i in contr.filter(item_id=name):
                item_can_drop.append({i.can_drop : i.chanse})
        psent_summ = 0
        for i in item_can_drop:
            psent_summ += float(i[list(i.keys())[0]])
        n_index = psent_summ / 100
        test_index = 0
        for i in item_can_drop:
            i[list(i.keys())[0]] = i[list(i.keys())[0]] / n_index
            test_index += i[list(i.keys())[0]]
        if test_index == 100.0: return HttpResponse(get_item(item_can_drop, user_id, items))
        return HttpResponse("Error Brooo")