from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'ipolls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-publication_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'ipolls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'ipolls/results.html'

def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice_id = req.POST["choice"]
        choice = question.choice_set.get(pk=selected_choice_id)
    except (KeyError, Choice.DoesNotExist):
        return render(
            req,
            "ipolls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        choice.votes += 1
        choice.save()

    return HttpResponseRedirect(reverse("ipolls:results", args=(question.id,)))
