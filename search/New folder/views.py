from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import inspect
from django.shortcuts import render
from .form import searchform
from .classaolw import findaol


# class home(TemplateView):
#    template_name = "index.html"


def home(request):
    context = inspect.objects.all()
    a = int(context.count())
    #   print(inspect.objects.count())
    #    print(context)
    return render(request, "index.html", {"context": context, "form": searchform()})


def search(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        print(request.META["REMOTE_ADDR"])
        form = searchform(request.POST)
        if form.is_valid():
            res = form.cleaned_data

            print(res)
        w = findaol(res["agent"])

        # check whether it's valid:

        ww = w.ww()
        wrs = w.wrs()
        wpn = w.wpn()

        wp = w.wp()[:-1]
        pmorpicaddress = w.wp()[-1]

        wv = w.wv()[:-1]
        vmorvideoaddress =w.wv()[-1]
        

        return render(
            request,
            "results.html",
            {"ww": ww, "wrs": wrs, "wpn": wpn, "wp": wp, "wv": wv,"vmorvideoaddress":vmorvideoaddress,"pmorpicaddress":pmorpicaddress},
        )

    # if a GET (or any other method) we'll create a blank form
    else:
        HttpResponse("nooooooooooooo")
