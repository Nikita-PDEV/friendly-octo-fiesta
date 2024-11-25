from django import forms
from .models import NewsArticle
import django_filters

class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['title', 'content', 'author']

class NewsArticleFilter(django_filters.FilterSet):
    created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = NewsArticle
        fields = ['title', 'author', 'created_after']