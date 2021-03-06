from django.shortcuts import render

from rest_framework import viewsets

from rest_framework import permissions
from post.models import Post
from post.permissions import IsOwnerOrReadOnly
from post.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def post(self, request, format=None):
        import pdb; pdb.set_trace()
        return super(PostViewSet, self).post(request, format)

    def create(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        return super(PostViewSet, self).create(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(self).get_queryset()
        if self.request.query_params.get('username'):
            qs = qs.filter(author__username=self.request.query_params.get('username'))
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
