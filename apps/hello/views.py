from django.http import HttpResponse

def hello_view(request):
    # Возвращаем обычный текст в ответ на HTTP-запрос
    return HttpResponse("Hello, Natali!")