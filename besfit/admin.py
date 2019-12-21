from django.contrib import admin
from .models import result,questions


class result_fields(admin.ModelAdmin):
    list_display = ('category','user_name','user_email','total_questions','question_attempt','correct_answers')


admin.site.register(result,result_fields)
admin.site.register(questions)
