from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Create
from .forms import CommentForm


class CreateView(generic.ListView):
    model = Create
    queryset = Create.objects.filter(status=1).order_by('-created_on')
    template_name = 'create.html'
    paginate_by = 6
