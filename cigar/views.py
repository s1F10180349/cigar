from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from cigar.models import Article
import random

# Create your views here.

def index(request):
    context = {
        "articles": Article.objects.all()
    }
    return render(request, 'cigar/tabaco.html', context)

def  index1(request):
    a = ["ラキスト", "マルボロ", "ホープ", "ハイライト", "メビウス", "アメスピ", "セブンスター", ]
    b = ["レギュラー", "メンソール"]
    choice = random.choice(a)
    choice1 = random.choice(b)
    date = {
        'name': choice,
        'RorM': choice1,
    }
    return render(request, 'cigar/today.html', date)

def redirect_t(request):
    return redirect(index)

def detail(request, article_id):
    context = {
        'article_id': article_id
    }
    return render(request, 'cigar/tabaco.html', context)

def update(request, article_id):
    context = {
        'article_id': article_id
    }
    return render(request, 'cigar/tabaco.html', context)

def delete(request, article_id):
    return redirect(index)