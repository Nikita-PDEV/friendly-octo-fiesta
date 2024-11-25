from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import NewsArticle
from .forms import NewsArticleForm, NewsArticleFilter

class NewsListView(ListView):
    model = NewsArticle
    paginate_by = 10
    template_name = 'news/news_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = NewsArticleFilter(self.request.GET, queryset=queryset)
        return filter.qs

class NewsCreate(CreateView):
    model = NewsArticle
    form_class = NewsArticleForm
    template_name = 'news/news_form.html'

    def form_valid(self, form):
        news_article = form.save(commit=False)
        news_article.article_type = NewsArticle.NEWS_TYPE  # Устанавливаем тип как новость
        news_article.save()
        return super().form_valid(form)

class NewsUpdate(UpdateView):
    model = NewsArticle
    form_class = NewsArticleForm
    template_name = 'news/news_form.html'

class NewsDelete(DeleteView):
    model = NewsArticle
    template_name = 'news/news_confirm_delete.html'
    success_url = '/news/'