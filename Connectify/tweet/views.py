from django.shortcuts import render
from .models import Tweet
from .forms import TweetFrom
from django.shortcuts import get_object_or_404,redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

def create_tweet(request):
    if request.method == 'POST':
        form = TweetFrom(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
        
    else:
        form = TweetFrom()
    return render(request, 'tweet_form.html', {'form': form})


def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user= request.user)
    if request.method == 'POST':
        form = TweetFrom(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
        pass
    else:
        form = TweetFrom(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})