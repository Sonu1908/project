from django.http import HttpResponse


def home_page(request):

    print("home page request")
    return HttpResponse("<h1>This is home page of  Dtaviv Technologies </h1> ")