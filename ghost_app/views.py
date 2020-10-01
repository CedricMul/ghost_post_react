from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ghost_app.models import GhostPost
from ghost_app.serializers import GhostPostSerializer

class GhostPostViewSet(viewsets.ModelViewSet):
    queryset = GhostPost.objects.all()
    serializer_class = GhostPostSerializer

    @action(detail=False)
    def boasts(self, request):
        boasts = GhostPost.objects.filter(is_boast=True)
        serializer = self.get_serializer(boasts, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def roasts(self, request):
        roasts = GhostPost.objects.filter(is_boast=False)
        serializer = self.get_serializer(roasts, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.upvotes = post.upvotes + 1
        post.total_votes = post.total_votes + 1
        post.save()
        return Response({'status': 'Upvoted'})
    
    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        post = self.get_object()
        post.downvotes = post.downvotes + 1
        post.total_votes = post.total_votes - 1
        return Response({'status': 'Downvoted'})
    
    @action(detail=True, methods=['post'])
    def post_ghost(self, request):
        new_post = GhostPostSerializer(data=request.data)
        if serializer.is_valid():
            GhostPost.objects.create(
                is_boast=new_post.get('is_boast'),
                content=new_post.get('content'),
            )
            return Response({'status': 'Post created'})
