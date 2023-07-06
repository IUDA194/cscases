from django.shortcuts import render, HttpResponse
from cases.models import User, Cases, inventory, contract
import random, datetime
import json

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
        if item_id == None:
            ansver = json.dumps({"error" : "'item_id' is not exist"})
            return HttpResponse(ansver)
        can_drop = list(map(str, request.GET.get("can_drop").split(";")))
        if can_drop == None:
            ansver = json.dumps({"error" : "'can_drop' is not exist"})
            return HttpResponse(ansver)
        chanse = list(map(int, request.GET.get("chanse").split(";")))
        if chanse == None:
            ansver = json.dumps({"error" : "'chanse' is not exist"})
            return HttpResponse(ansver)
        if len(can_drop) == len(chanse):
            for i in range(len(can_drop)):
                contract.objects.create(item_id=item_id, can_drop=can_drop[i], chanse=chanse[i]).save()
            ansver = json.dumps({"status" : "success", "error" : "None"})
            return HttpResponse(ansver)
        else:
            ansver = json.dumps({"error" : "Different lengths of given arrays"})
            return HttpResponse(ansver)

def start_contract(request):
    if request.method == "POST":
        return HttpResponse("poST")
    if request.method == "GET":
        user_id = request.GET.get("user_id")
        if user_id == None:
            ansver = json.dumps({"error" : "'user_id' is not exist"})
            return HttpResponse(ansver)
        items = list(map(str, request.GET.get("items").split(";")))
        if items == None:
            ansver = json.dumps({"error" : "'items' is not exist"})
            return HttpResponse(ansver)
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
        else: return HttpResponse(json.dumps({"error" : "Interest calculation error"}))