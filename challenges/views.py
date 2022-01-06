from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
monthandchallenges = {
    "january":"Hustle 5 hr a day",
    "february":"Run for some time",
    "march":"Learn new things",
    "april":"research on stocks in stockmarket",
    "may":"Lear Django for 20 min",
    "june":"Eat no meat",
    "july":"No need to worry",
    "august":"Whatever is proclaimed for you will be delivered",
    "september":"Everythings gonna be fine",
    "october":"Gotcha homie",
    "november":"Do or die",
    "december":"Choose wisely, one day or day one"
}

def index(request):
    months = list(monthandchallenges.keys())
    list_month=""
    for month in months:
        month_path = reverse("month-challenge",args=[month])
        capitalized_month = month.capitalize()
        list_month = list_month + (f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>")

    response_data = f"<ul>{list_month}</ul>"
    return HttpResponse(response_data)

    
def challenge_for_no(request, month):
    months = list(monthandchallenges.keys())
    
    if(month > len(months)):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month])
    
    return HttpResponseRedirect(redirect_path)

def challenge_function(request, month):
    challenge_text = None
    try:
        challenge_text = monthandchallenges[month]
        return HttpResponse(f"<h1>{challenge_text}</h1>")
    except:
        return HttpResponseNotFound("<h1>this is not a valid month</h1>")
