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


class CreateDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = GamerReview.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
       
        return render(
            request,
            "create.html",
            {
                "review": review,
                "review_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = GamerReview.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)

        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review_post = review_form.save(commit=False)
            review_post.create = review
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            "create.html",
            {
                "review": review,
            },
        )
