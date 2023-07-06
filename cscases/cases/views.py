from django.shortcuts import render, HttpResponse
from .models import User, Cases, inventory
import random
import datetime 
import json
import asyncio


def test(requerst):

    # получаем все объекты
    people = User.objects.all()
    print(people.query)
    
    # получаем объекты с именем Tom
    people = people.filter(user_id = "Tom")
    print(people.query)
    
    # получаем объекты с возрастом, равным 31
    print(people.query)

    for person in people:
        return HttpResponse(f"{person.id}.{person.user_id} - {person.balance}")

    # Create your views here.

def append_case(request):
    if request.method == "GET":
        return render(request, "append.html")
    if request.method == "POST":
        case_name = request.POST.get("case_name")
        if case_name == None:
            ansver = json.dumps({"error" : "'case_name' is not exist"})
            return HttpResponse(ansver)
        items = request.POST.getlist("items", ['python'])
        if items == None or type(items) != list:
            ansver = json.dumps({"error" : "'items' is not exist or dot have list type"})
            return HttpResponse(ansver)
        for i in range(len(items)):
            Cases.objects.create(name=case_name, item=items[i], item_id=i)
        return HttpResponse(f"Case name: {case_name}, items: {items}")

def open_case(request):
    if request.method == "GET":
        case = request.GET.get("case")
        user = request.GET.get("user_id")
        if user == None and case == None:
            ansver = json.dumps({"error" : "'user_id' and 'case' is not entered"})
            return HttpResponse(ansver)
        elif case == None:
            ansver = json.dumps({"error" : "'case' is not entered"})
            return HttpResponse(ansver)
        elif user == None:
            ansver = json.dumps({"error" : "'user_id' is not entered"})
            return HttpResponse(ansver)

        all_cases = Cases.objects.all()
        selected_case = all_cases.filter(name=case)
        if len(selected_case) <= 0:
            ansver = json.dumps({"error" : "No such case exists."})
            return HttpResponse(ansver)
        items = []
        for i in selected_case:
            items.append(i.item)
        drop = items[random.randint(0, len(items)) - 1]
        inventory.objects.create(user_id=user, item=drop, date=datetime.datetime.now() )
        js_a = {"user" : user, "drop" : drop, "time" : str(datetime.datetime.now()), "case_name" : case}
        ansver = json.dumps(js_a)
        return HttpResponse(ansver)

