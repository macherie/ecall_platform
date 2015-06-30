from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from post_service.forms import LoginForm
from post_service.models import Post


def post_list(request):
    template = get_template('post_list.html')
    context = Context({'post_list': Post.objects.all()})

    return HttpResponse(template.render(context))


def login(request):
    template = get_template('login_form.html')
    context = Context({'login_form': LoginForm()})

    return HttpResponse(template.render(context))