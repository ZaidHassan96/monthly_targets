from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse


monthly_targets = {
    "January": "Read a new book every week",
    "February": "Exercise for at least 30 minutes every day",
    "March": "Learn a new skill or hobby",
    "April": "Cook a new recipe every week",
    "May": "Plant a garden or start a small indoor plant collection",
    "June": "Go for a walk in nature every weekend",
    "July": "Try a digital detox - limit screen time",
    "August": "Volunteer for a local community service",
    "September": "Write a journal entry every day",
    "October": "Take a photo of something beautiful every day",
    "November": "Practice gratitude - write down three things you're thankful for each day",
    "December": None
}

def targets_list(request):
    months = list(monthly_targets.keys())
    return render(request, "targets/index.html", {"months_list": months})

def targets_by_num(request, month): 
    months = list(monthly_targets.keys())
    if month > len(months):
        return HttpResponseNotFound("Does not exist")

    redirect_month = months[month - 1]
    redirect_url = reverse("month_target", args=[redirect_month])
    return HttpResponseRedirect(redirect_url)





def targets(request,month): 
    uppercase_month = month.capitalize()
    monthly_statement = monthly_targets[uppercase_month]

    return render(request, "targets/targets.html", {"text": monthly_statement, "month": month} )