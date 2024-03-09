from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


monthly_challenges = {
    "january": "This works!",
    "february": "Hey! It's a leap year 2024 which means we have one extra day in feb.",
    "march": "This works!",
    "april": "Hey! It's a leap year 2024 which means we have one extra day in feb.",
    "may": "This works!",
    "june": "Hey! It's a leap year 2024 which means we have one extra day in feb.",
}

# def jan(request):
#     return HttpResponse("This works!")


# def feb(request):
#     return HttpResponse("Hey! It's a leap year 2024 which means we have one extra day in feb.")


# def monthly_challenge(request, month):
#     challenge_text = None
#     if month == "january":
#         challenge_text = "This works!"
#     elif month == "february":
#         challenge_text = "Hey! It's a leap year 2024 which means we have one extra day in feb."
#     else:
#         return HttpResponseNotFound("This month is not supported!")
#     return HttpResponse(challenge_text)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys)

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month  = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")



