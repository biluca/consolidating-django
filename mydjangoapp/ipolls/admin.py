from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Questionary", {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["publication_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'publication_date', 'was_published_recently')
    list_filter = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
