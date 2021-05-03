from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text' , 'default')
    print(djtext)
    removepunc = request.POST.get('punc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    removenewline = request.POST.get('removenewline', 'off')
    removeextraspace = request.POST.get('removeextraspace', 'off')
    count = request.POST.get('count', 'off')

    if(removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze = ""
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char

        param = {'purpose' : "Remove Punctuations", 'analyzed_text' : analyze}
        return render(request, 'analyze.html', param)

    elif(uppercase == 'on'):
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()
        param = {'purpose': "UpperCase", 'analyzed_text': analyze}
        return render(request, 'analyze.html', param)

    elif(removenewline == 'on'):
        analyze = ""
        if djtext != '\n':
            analyze = analyze + djtext
        param = {'purpose': "Remove New Line", 'analyzed_text': analyze}
        return render(request, 'analyze.html', param)

    elif (removeextraspace == 'on'):
        analyze = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == "  "):
                analyze = analyze + char
        param = {'purpose': "Remove Extra Space", 'analyzed_text': analyze}
        return render(request, 'analyze.html', param)

    elif (count == 'on'):
        counting = 0
        for char in djtext:
            if char != " ":
                counting = counting + 1
        param = {'purpose': "count", 'analyzed_text': counting}
        return render(request, 'analyze.html', param)
    else:
        return HttpResponse("error")