from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict

import opencc

from .models import TaiwanChineseDict

converter = opencc.OpenCC('s2t.json')


def index(request):
    return render(request, "zdict/index.html")


def search(request):
    keywords = request.GET.get('q')
    if keywords is None:
        keywords = converter.convert("国")
    else:
        keywords = converter.convert(str(keywords).strip())
    result = TaiwanChineseDict.objects.filter(term_name=keywords)
    content = []
    for e in result:
        content.append(model_to_dict(e))
    if len(content) == 0:
        content.append("None")
        return HttpResponse(keywords + "is not found.")
    # 使用"多音排序"字段进行排序
    content.sort(key=lambda x: x['polyphonic_sorting'])
    return render(request, "zdict/han_detail.html", {"content": content})
