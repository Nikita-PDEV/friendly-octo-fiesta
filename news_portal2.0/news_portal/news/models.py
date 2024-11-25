from django.db import models

class NewsArticle(models.Model):
    ARTICLE_TYPE = 'article'
    NEWS_TYPE = 'news'

    TYPE_CHOICES = [
        (ARTICLE_TYPE, 'Статья'),
        (NEWS_TYPE, 'Новость'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    article_type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title