from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from .models import Tweet
from .forms import TweetModelForm
# Create your views here.

class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = "/tweet/create/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)

class TweetDetailView(DetailView):
    #template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Tweet, pk=pk)
        return obj
        
class TweetListView(ListView):
    #template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        print(context)
        context["another_list"] = Tweet.objects.all()
        return context


# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)
#     print(obj)
#     context = {
#         "object": obj
#     }
#     return render(request, "tweets/detail_view.html", context)

# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print(queryset)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "tweets/list_view.html", context)