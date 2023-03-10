from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe

stripe.api_key = "sk_test_51MJKXfC7xQ1zzbZ2Ipa85JLt0lpCbY2mWIqyy8tx9P9GtqLkj0HIMsK1efLUNhnM5Jjd3yqUu4YGMwLUSNKE8jEV005E6BTePM"

# Create your views here.

def index(request):
    return render(request, 'base/index.html')

def charge(request):
    amount = 5
    if request == "POST":
        print('Data: ', request.POST)
    return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
    amount = args
    return render(request, 'base/success.html', {'amount':amount})

