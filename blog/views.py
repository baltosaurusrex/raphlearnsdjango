from django.shortcuts import render

posts = [
    {
        'author':'Raph',
        'title':'first!',
        'content':'wow this is like rails, but a bit more hands on',
        'date_posted':'25 FEB 2019'
    },
    {
        'author':'Raph',
        'title':'second!!',
        'content':'wow this is like rails, but a bit more hands on',
        'date_posted':'26 FEB 2019'
    },
]

# Create your views here.
def home(request):
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'Abt'})
