from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from ..models import Question


def index(request):
    # return redirect("/pybo")
    return redirect("pybo:index2")


def index2(request):
    page = request.GET.get("page", "1")  # 페이지
    question_list = Question.objects.order_by("-create_date")
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    print(paginator.count)
    max_index = len(paginator.page_range)
    page_obj = paginator.get_page(page)
    page_display_range = 3
    context = {
        "question_list": page_obj,
        "max_index": max_index,
        "page_display_range": page_display_range,
    }
    return render(request, "pybo/question_list.html", context)


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)
