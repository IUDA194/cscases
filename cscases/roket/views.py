from django.shortcuts import render, HttpResponse
from cases.models import User, Cases, inventory
import django.middleware.csrf as csrf
import random
import json

def lose_in_roket(request):
    if request.method == "GET":
        user_id = request.GET.get("user_id")
        amount = float(request.GET.get("amount"))
        user = User.objects.all().filter(user_id=user_id)
        old_balance = user[0].balance
        user.update(balance=old_balance - amount)
        js_a = {"status" : "Done", "new_balance" : old_balance - amount, "lose_balance" : amount}
        ansver = json.dumps(js_a)
        return HttpResponse(ansver)

def win_in_roket(request):
    if request.method == "GET":
        user_id = request.GET.get("user_id")
        amount = float(request.GET.get("amount"))
        factor = float(request.GET.get("factor"))
        user = User.objects.all().filter(user_id=user_id)
        print(user[0].balance)
        old_balance = user[0].balance
        user.update(balance=old_balance + (amount * factor) - amount)
        js_a = {"status" : "Done", "new_balance" : old_balance + (amount * factor), "win_balance" : amount * factor}
        ansver = json.dumps(js_a)
        return HttpResponse(ansver)
    
def get_csrf(request):
    js_a = {"csrf" : csrf.get_token(request)}
    ansver = json.dumps(js_a)
    return HttpResponse(ansver)