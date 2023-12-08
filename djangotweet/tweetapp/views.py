from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect, render
from .models import Tweet
from .forms import AddTweetForm
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from tweetapp import models
def listtweet(request):
    nickname_filter = request.GET.get('nickname')

    if nickname_filter:
        filtered_tweets = Tweet.objects.filter(nickname=nickname_filter)
        tweet_dict = {"tweets": filtered_tweets}
    else:
        all_tweets = Tweet.objects.all()
        tweet_dict = {"tweets": all_tweets}

    nickname_list = Tweet.objects.values('nickname').distinct()  # Başlık listesi
    return render(request, 'tweetapp/listtweet.html', context={"tweets": tweet_dict['tweets'], "nickname_list": nickname_list})
@login_required(login_url="/login")
def addtweet(request):
    if request.method == 'POST':
        nickname = request.POST.get("nickname")
        message = request.POST.get("message")
        Tweet.objects.create(username=request.user, nickname=nickname, message=message)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request, 'tweetapp/addtweet.html')

def addtweetbyform(request):
    if request.method == 'POST':
        form = AddTweetForm(request.POST, request.FILES)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]
            image = form.cleaned_data["image"]
            Tweet.objects.create(username=request.user, nickname=nickname, message=message, image=image)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print("error in form!")
            return render(request, 'tweetapp/addtweetbyform.html', context={"form": form})
    else:
        form = AddTweetForm()
        return render(request, 'tweetapp/addtweetbyform.html', context={"form": form})

@login_required
def deletetweet(request,id):
    tweet = models.Tweet.object.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect('tweetapp:listtweet')

class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/singup.html"



