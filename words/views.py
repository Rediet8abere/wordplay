from django.shortcuts import render
from .models import Words
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
    ordering = ['date_posted'] # newst post to oldest post

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
