from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView, DeleteView

from  .models import Post

class Postlist(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'

class PostDetail(DeleteView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

