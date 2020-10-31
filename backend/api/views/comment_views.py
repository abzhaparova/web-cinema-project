from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from datetime import datetime
from ..models import Comment, CommentPage, User
from ..serializers import CommentSerializer


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_comments(request, page_id):
    try:
        comment_page = CommentPage.objects.get(id=page_id)
        comments = list(comment_page.comments.values())
        serializer = CommentSerializer(data=comments, many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except CommentPage.DoesNotExist:
        return Response('Page does not exist', status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def post_comment(request, page_id):
    try:
        comment_page = CommentPage.objects.get(id=page_id)
        comment = Comment()
        comment.message = request.data
        comment.username = request.user.username
        comment.date_posted = datetime.now()
        comment.comment_page = comment_page
        comment.score = 0
        comment.save()
        return Response()
    except CommentPage.DoesNotExist:
        return Response('Page does not exist', status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def change_score(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
        comment.score += int(request.data)
        comment.save()
        return Response()
    except Comment.DoesNotExist:
        return Response('Comment does not exist', status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated, ))
def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
        if comment.username != request.user.username:
            return Response('Not an owner of comment', status=status.HTTP_400_BAD_REQUEST)
        else:
            comment.delete()
            return Response()
    except Comment.DoesNotExist:
        return Response('Comment does not exist', status=status.HTTP_404_NOT_FOUND)