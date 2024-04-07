from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def cakes(request):
    return render(request, 'cakes.html')
def order_online(request):
    return render(request, 'order_online.html')
def about_us(request):
    return render(request, 'about_us.html')
def customer_review(request):
    return render(request, 'customer_review.html')
def contact_us(request):
    return render(request, 'contact_us.html')