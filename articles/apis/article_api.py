from rest_framework.generics import ListCreateAPIView
from articles.serializers.articles_serializer import *
from articles.models import *
from rest_framework.response import Response
from django.http import Http404


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Article.objects.all()
    genre = request.GET.get('genre')

    if is_valid_queryparam(genre):
        qs = qs.filter(genre__name=genre)

    return qs

class ArticlesView(ListCreateAPIView):
    serializer_class = ArticlesSerializer
    queryset = Article.objects.select_related("genre").all().order_by('-date')

    def get_queryset(self):
        qs = filter(self.request)
        return qs

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk="", format=None):
        if pk == '':
            data = self.get_queryset()
            serializer = ArticlesSerializer(data, many=True)
        else:
            data = self.get_object(pk)
            serializer = ArticlesSerializer(data)
        return Response(serializer.data)

class SuggestionsView(ListCreateAPIView):
    serializer_class = SuggestionSerializer
    queryset = Suggestions.objects.all()

class Comments(ListCreateAPIView):
    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()

    def get(self, request, post_id="", format=None):
        if post_id == '':
            data = Comment.objects.all()
            serializer = CommentsSerializer(data, many=True)
        else:
            data = Comment.objects.filter(post=post_id).values()
            return Response(data)
        return Response(serializer.data)
