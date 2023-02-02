from django.http import HttpResponse
from django.views import View

from .models import Question

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class RawSQL(View):
    def get(self, *args, **kwargs):
        field_map = {'due_date': 'pub_date'}
        notquestions = Question.objects.raw('SELECT * FROM polls_notquestion', translations=field_map)
        results = []
        for nq in notquestions:
            results += (nq.category, nq.question_text, str(nq.pub_date))
            results += "-----"
        return HttpResponse(", ".join(results))
