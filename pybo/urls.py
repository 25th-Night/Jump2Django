from django.urls import path

from .views.base_views import index2, detail
from .views.question_views import question_create, question_modify, question_delete
from .views.answer_views import answer_create, answer_modify, answer_delete


app_name = "pybo"

urlpatterns = [
    path("", index2, name="index2"),
    path("<int:question_id>/", detail, name="detail"),
    path("question/create/", question_create, name="question_create"),
    path("question/modify/<int:question_id>/", question_modify, name="question_modify"),
    path("question/delete/<int:question_id>/", question_delete, name="question_delete"),
    path("answer/create/<int:question_id>/", answer_create, name="answer_create"),
    path("answer/modify/<int:answer_id>/", answer_modify, name="answer_modify"),
    path("answer/delete/<int:answer_id>/", answer_delete, name="answer_delete"),
]
