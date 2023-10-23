# admin.py in your app
from django.contrib import admin
from .models import Question, UserResponse

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('answer1', 'answer2', 'answer3', 'answer4', 'answer4', 'created_at')
    # You can customize the admin options for the Question model here.

class AnswerInline(admin.TabularInline):
    model = UserResponse.selected_answers.through
    extra = 1

class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'timestamp')
    inlines = [AnswerInline]

admin.site.register(UserResponse, UserResponseAdmin)
admin.site.register(Question, QuestionAdmin)
