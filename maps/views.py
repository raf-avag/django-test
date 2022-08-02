from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import University, Subject
from .forms import UniversityForm


@login_required
def homePageView(request):
    universities = University.objects.all()
    context = {"universities": universities}
    form = UniversityForm(request.POST or None)  # , request.FILES or None
    if form.is_valid():
        u = form.cleaned_data.get("name")
        s = form.cleaned_data.get("subject")
        print(u, s)

        uni = University.objects.create(name=u)
        for i in s:
            uni.subject.add(i.id)
        # uni.save()
    return render(request, "home.html", {"universities": universities, "form": form})


@login_required
def uni(request, id):
    uni = University.objects.get(id=id)
    context = {"uni": uni}
    return render(request, "uni.html", context)


@login_required
def delete(request, id):
    uni = University.objects.get(id=id)
    uni.delete()
    return redirect("home")


def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")  # [] throw error
            user = authenticate(username=username, password=password)
            login(request, user)
            # print(username, password)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})
