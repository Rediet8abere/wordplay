from django.shortcuts import render


vocab = [
    {
        'name': 'bobby',
        'noun': 'food',
        'verb': 'dr',
        'adjective': 'fruit'
     },
    {
         'name': 'luli',
         'noun': 'cat',
         'verb': 'jacky',
         'adjective': 'banaba'
      }
]

def index(request):
    context = {
        'vocab': vocab
    }
    return render(request, 'words/index.html', context)

def about(request):
    return render(request, 'words/about.html', {'title': 'about words'})
