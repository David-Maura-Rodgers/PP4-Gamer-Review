from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, View, CreateView
from django.http import HttpResponseRedirect
from .models import Review
from .forms import CommentForm, ReviewForm


class ReviewList(ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class ReviewDetail(View):

    def get(self, request, pk, title, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, pk=pk)
        comments = review.comments.filter(approved=True).order_by("-created_on")
       
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

        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, pk=pk)
        comments = review.comments.filter(approved=True).order_by("-created_on")
        
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
    
    def post(self, request, pk, *args, **kwargs):
        review = get_object_or_404(Review, pk=pk)
        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ReviewFunny(View):
 
    def post(self, request, pk, *args, **kwargs):
        review = get_object_or_404(Review, pk=pk)
        if review.funny.filter(id=request.user.id).exists():
            review.funny.remove(request.user)
        else:
            review.funny.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ReviewInsightful(View):
  
    def post(self, request, pk, *args, **kwargs):
        review = get_object_or_404(Review, pk=pk)
        if review.insightful.filter(id=request.user.id).exists():
            review.insightful.remove(request.user)
        else:
            review.insightful.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'create.html'
