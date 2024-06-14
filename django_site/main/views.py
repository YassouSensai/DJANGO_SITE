import openai

from .models import Article
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

openai.api_key = settings.OPENAI_API_KEY

def article_list(request):
    articles = Article.objects.all()
    return render(request, "main/article_list.html", {"articles": articles})


def chatbot(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return JsonResponse({'answer': answer})
    return render(request, 'main/chatbot.html')