import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return f"{self.question_text}"

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        return self.publication_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.choice_text}"
