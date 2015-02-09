from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from models import Resume


def viewresume(request, username):
    user = get_object_or_404(User, username=username)
    resume = get_object_or_404(Resume, owner=user)
    return render(request, 'resume/view.html', {
        'resume': resume
    })
