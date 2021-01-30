from django.shortcuts import render, redirect	# notice the import!
import random

def index(request):
    if 'MoneyGame_gold' in request.session:
        return render(request, "index.html")
    else:
        request.session['MoneyGame_gold'] = 0
        request.session["MoneyGame_transactions"] = []
        return render(request, "index.html")

def process_money(request, methods = ['POST'] ):
    previous_gold = request.session['MoneyGame_gold']
    if request.POST['type'] == "farm":
        gold = random.randint(10,21)
        request.session["MoneyGame_gold"] += gold
        request.session["MoneyGame_transactions"].append([previous_gold,gold, "Earned " + str(gold) +" gold from the farm!",request.session['MoneyGame_gold']])
    elif request.POST['type'] == "cave":
        gold = random.randint(5,10)
        request.session["MoneyGame_gold"] += gold
        request.session["MoneyGame_transactions"].append([previous_gold,gold, "Earned " + str(gold) +" gold from the cave!",request.session['MoneyGame_gold']])
    elif request.POST['type'] == "house":
        print("yesss")
        gold = random.randint(2,5)
        request.session["MoneyGame_gold"] += gold
        request.session["MoneyGame_transactions"].append([previous_gold,gold, "Earned " + str(gold) +" gold from the house!",request.session['MoneyGame_gold']])
        
    elif request.POST['type'] == "casino":
        gold = random.randint(-50,51)
        request.session["MoneyGame_gold"] += gold
        if gold > -1:
            request.session["MoneyGame_transactions"].append([previous_gold,gold, "Earned " + str(gold) +" gold from the casino!",request.session['MoneyGame_gold']])
        else:
            request.session["MoneyGame_transactions"].append([previous_gold,gold, "Lost " + str(gold) +" gold from the casino!",request.session['MoneyGame_gold']])
    context = {
        "previous_action": request.session["MoneyGame_transactions"][-1]
    }
    return render(request, "partials/action-realtime.html",context)

def clear(request):
    request.session.clear()
    return redirect("/")
