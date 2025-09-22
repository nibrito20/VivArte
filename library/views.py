from django.shortcuts import render

def booklist(request):
    return render(request, 'library/booklist.html')