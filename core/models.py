# models.py in your app
from django.db import models
from django.contrib.auth.models import User


# look here for inspiration - https://github.com/tomwalker/django_quiz/blob/master/quiz/models.py

class FixedAnswer(models.Model):
    answer_number = models.SmallIntegerField(blank=True, null=True)
    answer_choice = models.CharField(max_length=25, blank=True, null=True)
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'answer_choice'

    def __str__(self):
        return self.answer_choice


class Question(models.Model):
    Title_of_Question = models.TextField()
    answer_1 = models.ForeignKey(FixedAnswer, on_delete=models.CASCADE, related_name='answer', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'question'

    def __str__(self):
        # This needs to match one of the fields so django knows what to name it.
        return self.Title_of_Question


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(FixedAnswer, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'user_response'
