# i have created this file - Anish
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')

    #check checkbox values
    removepunc = request.POST.get('removepunc','Off')
    fullcaps = request.POST.get('fullcaps','Off')
    newlineremover = request.POST.get('newlineremover','Off')
    extraspaceremover = request.POST.get('extraspaceremover','Off')


    # check which chckbox is on
    if removepunc == 'on':

        punctuations='''!()-[]{};:'"\,<>./?!@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps == 'on'):
        analyzed=''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'removed newlines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == 'on'):
        analyzed = ''
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose': 'removed extra spaces', 'analyzed_text': analyzed}

    if(removepunc !='on' and fullcaps !='on' and extraspaceremover !='on' and newlineremover!='on'):
        return HttpResponse('please select any operation and try agian')

    return render(request, 'analyze.html', params)


def about(request):
    return render(request,'about.html')
