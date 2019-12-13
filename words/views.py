from django.shortcuts import render, get_object_or_404
from .models import Words
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)



# def index(request):
#     context = {
#         'vocab': Words.objects.all()
#     }
#     return render(request, 'words/index.html', context)

class WordListView(ListView):
    model = Words
    template_name = 'words/index.html'
    context_object_name = 'vocab'
    ordering = ['-date_posted'] # newst post to oldest post
    paginate_by = 5

class PlayerWordListView(ListView):
    model = Words
    template_name = 'words/player_words.html'
    context_object_name = 'vocab'
    ordering = ['-date_posted'] # newst post to oldest post
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Words.objects.filter(player=user).order_by('-date_posted')


class WordDetailView(DetailView):
    model = Words
    # <app>/<model>_<viewtype>.html

class WordCreateView(LoginRequiredMixin, CreateView):
    model = Words
    fields = ['noun', 'define']
    # <app>/<model>_<viewtype>.html
    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)

class WordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Words
    fields = ['noun', 'define']
    # <app>/<model>_<viewtype>.html
    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)

    def test_func(self):
        voc = self.get_object()
        if self.request.user == voc.player:
            return True
        return False

class WordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Words
    success_url = '/'

    def test_func(self):
        voc = self.get_object()
        if self.request.user == voc.player:
            return True
        return False


def about(request):
    return render(request, 'words/about.html', {'title': 'about words'})
