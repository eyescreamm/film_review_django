import requests
import os
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from dotenv import load_dotenv

from .models import User, Film, Review
from .forms import LoginForm, SignupForm, ReviewForm, SortForm

load_dotenv()

def get_all_films():
    film_list = []
    for obj in Film.objects.all():
        url = "http://www.omdbapi.com/?t=" + obj.title + "&apikey=" + os.environ['OMDB_API_KEY']
        response = requests.get(url).json()
        film = {
            "id" : obj.id,
            "title" : obj.title,
            "poster" : response["Poster"]
        }
        film_list.append(film)
    return film_list

def get_film_by_id(id):
    obj = Film.objects.filter(id=id)
    url = "http://www.omdbapi.com/?t=" + obj[0].title + "&apikey=" + os.environ['OMDB_API_KEY']
    response = requests.get(url).json()
    film = {
        "id": id,
        "count_reviews": obj[0].count_reviews,
        "title": response["Title"],
        "poster": response["Poster"],
        "year" : response["Year"],
        "runtime" : response["Runtime"],
        "plot": response["Plot"],
        "director": response["Director"],
        "genre" : response["Genre"]
    }
    return film

def get_rating_by_id(id):
    rating = 0
    film = Film.objects.filter(id=id).get()
    reviews = Review.objects.filter(film=film)
    for review in reviews:
        rating = rating + review.rating
    return 0 if len(reviews) == 0 else rating/len(reviews)

def get_film_by_option(sort, filter):
    film_list = []
    if sort == "title":
        films = Film.objects.order_by('title');
    if sort == "review":
        films = Film.objects.order_by('count_review');
    for obj in films:
        url = "http://www.omdbapi.com/?t=" + obj.title + "&apikey=" + os.environ['OMDB_API_KEY']
        response = requests.get(url).json()
        film = {
            "id" : obj.id,
            "title" : obj.title,
            "poster" : response["Poster"]
        }
        film_list.append(film)
    return film_list

def index(request):
    username = ""
    if 'authorized_user_login' in request.session:
        username = request.session["authorized_user_login"]
    sort = request.GET.get("sort")
    sort_list = ["title", "rating", "review"]
    filter = request.GET.get("filter")
    filter_list = ["5", "4", "3", "2", "1"]
    film_list = get_all_films
    option1 = ""
    option2 = ""
    if sort:
        option1 = sort
    if filter:
        option2 = filter 
    if sort or filter:
        film_list = get_film_by_option(option1, option2)
    return render(request, "index.html", {"film_list": film_list, "username": username, "sort_list": sort_list, "sort": sort, "filter_list": filter_list, "filter": filter})

def register_user(form):
    if not form.is_valid():
        raise RuntimeError("Error: " + str(form.errors))
    email = form.cleaned_data.get('email') 
    name = form.cleaned_data.get('name')
    password = form.cleaned_data.get('password')
    if len(User.objects.filter(email=email)) > 0:
        raise RuntimeError("This email is already exists.")
    if len(User.objects.filter(name=name)) > 0:
        raise RuntimeError("This username is already exists.")
    User.objects.create(name=name, email=email, password=make_password(password))
    

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        try:
            register_user(form)
        except RuntimeError as e:
            return render(request, 'signup.html', {'form': form, 'text': str(e)})
        return redirect('/')
    else:
        return render(request, 'signup.html', {'form': SignupForm()})

def auth_login(form):
    if not form.is_valid():
        raise RuntimeError("Error: " + str(form.errors))
    name = form.cleaned_data.get('name')
    password = form.cleaned_data.get('password')
    user = User.objects.filter(name=name)
    if len(user) == 1:
        if not(check_password(password, user[0].password)):
            raise RuntimeError("This password is not correct.")
        return user[0]
    else:
        raise RuntimeError("This username is not exists.")

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        text = ""
    else:
        form = LoginForm(request.POST)
        try:
            user = auth_login(form)
            request.session["authorized_user_login"] = user.name
            return redirect('/')
        except RuntimeError as e:
            text = str(e)
    return render(request, 'login.html', {'form': form, 'text': text})

def logout(request):
    try:
        del request.session['authorized_user_login']
    except KeyError:
        pass
    return redirect('/')

def film(request, id):
    if 'authorized_user_login' in request.session:
        username = request.session["authorized_user_login"]
    else:
        username = ""
    rating = get_rating_by_id(id)
    param = {
        'username': username,
        'film': get_film_by_id(id),
        'rating': rating,
        'rating_for_star': int(rating * 20),
        'review_list': Review.objects.filter(film=Film.objects.filter(id=id).get())
    }
    return render(request, 'film.html', param)

def register_review(form, film_id, username):
    if not form.is_valid():
        raise RuntimeError("Error: " + str(form.errors))
    rating = form.cleaned_data.get('rating') 
    comment = form.cleaned_data.get('comment')
    user = User.objects.filter(name=username)
    film = Film.objects.filter(id=film_id).get()
    count_reviews = film.count_reviews + 1
    if len(Review.objects.filter(film=film, user=user[0])) > 0:
        raise RuntimeError("This user's review is already exists.")
    Review.objects.create(user=user[0], film=film, rating=rating, comment=comment)
    Film.objects.update(count_reviews=count_reviews)

def review(request, id):
    if 'authorized_user_login' in request.session:
        username = request.session["authorized_user_login"]
    else:
        return redirect('login')
    if request.method == 'GET':
        form = ReviewForm()
        text=""
    else:
        form = ReviewForm(request.POST)
        try:
            register_review(form, id, username)
            return redirect(f'/film/{id}')
        except RuntimeError as e:
            text = str(e)
    param = {
        'form':form,
        'username': username,
        'film': get_film_by_id(id),
        'text': text,
    }
    return render(request, 'review.html', param)
