from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import NewsArticle

class NewsListView(ListView):
    model = NewsArticle
    template_name = 'news/news_list.html'

class NewsCreate(CreateView):
    model = NewsArticle
    template_name = 'news/news_form.html'
    fields = ['title', 'content', 'author']

class NewsUpdate(UpdateView):
    model = NewsArticle
    template_name = 'news/news_form.html'
    fields = ['title', 'content', 'author']

class NewsDelete(DeleteView):
    model = NewsArticle
    template_name = 'news/news_confirm_delete.html'
    success_url = reverse_lazy('news-list')

class NewsSearchView(ListView):
    model = NewsArticle
    template_name = 'news/news_search.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        author = self.request.GET.get('author')
        created_after = self.request.GET.get('created_after')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if created_after:
            queryset = queryset.filter(created_at__date__gte=created_after)

        return queryset