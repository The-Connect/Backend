# admin.py in your app
from django.contrib import admin
from .models import Question, FixedAnswer, UserResponse


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('Title_of_Question', 'answer_1', 'created_at')
    # You can customize the admin options for the Question model here.


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('answer_number', 'answer_choice', 'question_id')


# class AnswerInline(admin.TabularInline):
#     model = UserResponse.selected_answers.through
#     extra = 1

class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'answer', 'timestamp')
    # inlines = [AnswerInline]


admin.site.register(UserResponse, UserResponseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(FixedAnswer, AnswersAdmin)
