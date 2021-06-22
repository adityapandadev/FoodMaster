from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from sweets.models import Sweetshop
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.http.response import HttpResponseRedirect
from django.core.mail import send_mail


# Create your views here.
"""Contact Function"""
def contact(req):
    sub = "FoodMaster Contact :: %s " % req.POST.get("Name")
    body = "Email = %s\nMessage = %s " % (req.POST.get("Email"),  req.POST.get("Message"))
    send_mail(
        sub,
        body,
        req.POST.get("Email"),      #from
        ['codergirl@gmail.com'],        #to
        fail_silently=False,
    )
    return HttpResponseRedirect("/sweets/home?msg=Submited Successfully")


class HomeView(TemplateView):
    template_name = "sweets/home.html"
    
class SweetshopListView(ListView):
    model = Sweetshop
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return Sweetshop.objects.filter(Q(name__icontains = si)| Q(rating__icontains = si)| Q(address__icontains = si)).order_by("-id")
             


class SweetshopDetailView(DetailView):
    model = Sweetshop

