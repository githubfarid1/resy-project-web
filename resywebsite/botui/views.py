from django.shortcuts import render
import os
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import ReservationType, Account, BotCommand, Proxy

# Create your views here.

def show_reservations(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {
    }
    return render(request=request, template_name='botui/show_reservations.html', context=context)

def reservation_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    reservations = ReservationType.objects.all()

    return render(request, 'botui/reservation_list.html', {
        'reservations': reservations,
    })
