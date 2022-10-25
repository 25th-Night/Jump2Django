from django.urls import path

from pybo.views import index2, detail, question_create, answer_create


app_name = "pybo"

urlpatterns = [
    path("", index2, name="index2"),
    path("<int:question_id>/", detail, name="detail"),
    path("question/create/", question_create, name="question_create"),
    path("answer/create/<int:question_id>/", answer_create, name="answer_create"),
]
