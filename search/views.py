from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import inspect
from django.shortcuts import render
from .form import searchform
from .classaolw import findaol, findpage
from .classaolpic import findaolpic
from .classaolvid import findaolvid


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
        res=res["agent"]
        print(res)
        w = findaol(res)

        # check whether it's valid:

        end = w.ww()
        (wv, wp, wpn, wrs, ww) = end

        if len(wp) > 1:
            pmorpicaddress = wp[-1]
            wp = wp[:-1]
        else:
            pmorpicaddress = []
        if len(wv) > 1:
            vmorvideoaddress = wv[-1]
            wv = wv[:-1]
        else:
            vmorvideoaddress = []
        # save todatabase for request
        member = inspect(
            author_name=request.META["SERVER_NAME"],
            author_ip=request.META["REMOTE_ADDR"],
            searchitems=res,
            searchpages=wpn,
            webrelatedsearch=wrs,
            morevid =vmorvideoaddress,
            morepic =pmorpicaddress,
        )
        member.save()
        # END save todatabase for request
        return render(
            request,
            "results.html",
            {
                "ww": ww,
                "wrs": wrs,
                "wpn": wpn,
                "wv": wv,
                #"vmorvideoaddress": vmorvideoaddress,
                #"pmorpicaddress": pmorpicaddress,
                "wp": wp,

            },
        )

    # if a GET (or any other method) we'll create a blank form
    else:
        HttpResponse("nooooooooooooo")



def searchpages(request, pagenumber):
    print(request.META["REMOTE_ADDR"])
    entery = inspect.objects.filter(author_ip=request.META["REMOTE_ADDR"]).order_by("-date")

    n = entery.values()[0]["searchpages"]

    print(n, "22222222222222222" ,type(n))

    listurls =eval(n)
    print(len(listurls))
    url=listurls[int(pagenumber)-1]



    w = findpage(url)

    # check whether it's valid:

    end = w.ww()
    (wv, wp, wpn, wrs, ww) = end

    if len(wp) > 1:
        pmorpicaddress = wp[-1]
        wp = wp[:-1]
    else:
        pmorpicaddress = []
    if len(wv) > 1:
        vmorvideoaddress = wv[-1]
        wv = wv[:-1]
    else:
        vmorvideoaddress = []

    return render(
        request,
        "results.html",
        {
            "ww": ww,
            "wrs": wrs,
            "wpn": wpn,
            "wv": wv,
            "vmorvideoaddress": vmorvideoaddress,
            "pmorpicaddress": pmorpicaddress,
            "wp": wp,
        },
    )


def wrs(request,number):
    print(request.META["REMOTE_ADDR"])
    entery = inspect.objects.filter(author_ip=request.META["REMOTE_ADDR"]).order_by("-date")

    n = entery.values()[0]["webrelatedsearch"]

    print(n, "22222222222222222" ,type(n))

    listurls =eval(n)
    print(len(listurls))
    url=listurls[int(number)-1][1]
    res=listurls[int(number)-1][0]



    w = findpage(url)

    # check whether it's valid:

    end = w.ww()
    (wv, wp, wpn, wrs, ww) = end

    if len(wp) > 1:
        pmorpicaddress = wp[-1]
        wp = wp[:-1]
    else:
        pmorpicaddress = []
    if len(wv) > 1:
        vmorvideoaddress = wv[-1]
        wv = wv[:-1]
    else:
        vmorvideoaddress = []

    member = inspect(
            author_name=request.META["SERVER_NAME"],
            author_ip=request.META["REMOTE_ADDR"],
            searchitems=res,
            searchpages=wpn,
            webrelatedsearch=wrs,
            morevid =vmorvideoaddress,
            morepic =pmorpicaddress,
        )
    member.save()
    return render(
        request,
        "results.html",
        {
            "ww": ww,
            "wrs": wrs,
            "wpn": wpn,
            "wv": wv,
            "vmorvideoaddress": vmorvideoaddress,
            "pmorpicaddress": pmorpicaddress,
            "wp": wp,
        },
    )





def pic(request):
    w = findaolpic(request.META["REMOTE_ADDR"])

    # check whether it's valid:

    end = w.ww()

    return render(
        request,
        "resultspic.html",
        {
            "wp": end,
        },
    )


def vid(request ):
    w = findaolvid(request.META["REMOTE_ADDR"])

    # check whether it's valid:

    end = w.ww()

    return render(
        request,
        "resultsvid.html",
        {
            "wv": end,
        },
    )
