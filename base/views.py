from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required



# class IndexTemplateView(LoginRequiredMixin, TemplateView):

# @login_required(login_url='/login')
class IndexTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/account/login/'

    def get_template_names(self):
        return "index.html"

