from django.shortcuts import render, get_object_or_404
# from datetime import timedelta, date
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView  # noqa
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # noqa
from django.http import HttpResponseRedirect
from .models import Review
from .forms import CommentForm, ReviewForm
# from django.urls import reverse


class ReviewList(ListView):
    '''
    This view will be rendered on the home page in a list view
    that paginates every 6 entries
    '''
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class ReviewDetail(View):
    '''
    This view will be rendered on the review detail page:
    User can see the content of posted reviews
    '''

    def get(self, request, pk, title, *args, **kwargs):
        '''
        User will be able to vote like, funny and insightful
        User can also see comments that have been made on the review
        '''

        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, pk=pk)
        comments = review.comments.filter(approved=True).order_by(
            "-created_on")

        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        funny = False
        if review.funny.filter(id=self.request.user.id).exists():
            funny = True

        insightful = False
        if review.insightful.filter(id=self.request.user.id).exists():
            insightful = True

        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "funny": funny,
                "insightful": insightful,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, pk, *args, **kwargs):
        '''
        User can also comment on the selected review
        This is posted to admin to be authorised bt admin
        '''

        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, pk=pk)
        comments = review.comments.filter(
            approved=True).order_by("-created_on")

        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        funny = False
        if review.funny.filter(id=self.request.user.id).exists():
            funny = True

        insightful = False
        if review.insightful.filter(id=self.request.user.id).exists():
            insightful = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
                "funny": funny,
                "insightful": insightful,
            },
        )


class ReviewLike(View):
    '''
    User can like a review and an icon changes to reflect that
    '''

    def post(self, request, pk, *args, **kwargs):
        '''
        User can like a review and an icon changes to reflect that
        But only if they are logged in as a registered user
        '''

        review = get_object_or_404(Review, pk=pk)
        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ReviewFunny(View):
    '''
    User can vote funny on a review and an icon changes to reflect that
    '''

    def post(self, request, pk, *args, **kwargs):
        '''
        User can vote funny a review and an icon changes to reflect that
        But only if they are logged in as a registered user
        '''

        review = get_object_or_404(Review, pk=pk)
        if review.funny.filter(id=request.user.id).exists():
            review.funny.remove(request.user)
        else:
            review.funny.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ReviewInsightful(View):
    '''
    User can vote insightful on a review and an icon changes to reflect that
    '''

    def post(self, request, pk, *args, **kwargs):
        '''
        User can vote insightful a review and an icon changes to reflect that
        But only if they are logged in as a registered user
        '''

        review = get_object_or_404(Review, pk=pk)
        if review.insightful.filter(id=request.user.id).exists():
            review.insightful.remove(request.user)
        else:
            review.insightful.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CreateReview(LoginRequiredMixin, CreateView):
    '''
    This renders the Create A Review page
    User can post a review of their own
    '''

    model = Review
    form_class = ReviewForm
    template_name = 'create_review.html'
    success_url = "posted_review.html"
    success_message = "You successfully created your own Review"

    def form_valid(self, form):
        form.instance.gamer = self.request.user
        form.save()
        form.instance.members.set([self.request.user.pk])
        self.success_url = "/posted_review/"

        return super().form_valid(form)
