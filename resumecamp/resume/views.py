from django.shortcuts import render
from django.http import HttpResponse


def viewresume(request, username):
    return HttpResponse("hallo " + username);
