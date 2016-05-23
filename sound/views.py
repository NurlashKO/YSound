from django.shortcuts import render
from .getAudioFromYoutube import getAudioFromYoutube
def index(request):

    if(request.GET.get('sdownload')):
        getAudioFromYoutube(str(request.GET.get('soundname')))

    return render(request, 'sound/index.html')
