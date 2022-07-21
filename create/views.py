from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import GamerReview
from .forms import ReviewForm


class CreateView(generic.ListView):
    model = GamerReview
    queryset = GamerReview.objects.filter(status=1).order_by('-created_on')
    template_name = 'create.html'
    paginate_by = 6
