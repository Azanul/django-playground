from django.db.models import Field, Lookup
from django.db import models


@Field.register_lookup
class LengthWithinLookup(Lookup):
    lookup_name = 'length_within'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        print(f"lhs: {lhs}, {lhs_params}")
        print(f"rhs: {rhs}, {rhs_params}")
        lower_limit, upper_limit = rhs_params[0][1:-1].split(", ")
        return f"LENGTH({lhs}) BETWEEN {lower_limit} AND {upper_limit}", []


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)