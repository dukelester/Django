from django.db import models

# Create your models here.

class Question(models.Model):
    ''' A simple question '''
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('Date published')

class Choice(models.Model):
    ''' The answer choice '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField('Number of votes', default=0)
    choice_text = models.CharField(max_length=200)
    update_at = models.DateTimeField()
