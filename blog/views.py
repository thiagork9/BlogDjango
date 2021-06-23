from django.views.generic import DetailView, ListView

from .models import Post

#classe para listagem de todos os posts
class PostListView(ListView):
    model = Post

#classe para post especifico 
class PostDetalView(DetailView):
    model = Post