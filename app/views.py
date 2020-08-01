from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics
from app import models
from app.logica.ModelSC import ModelSC
from app import serializers

class MoviList(generics.ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer

class MoviDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer

class CommetList(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

class MovieComments(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer
    def get_queryset(self):
        id = self.kwargs['movieid']
        return models.Comment.objects.filter(movie_fk_id=id)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class MovieView():
    
    def listMovies(request):
        movies = models.Movie.objects.all()

        print("movies", movies)
        return render(request, "index.html", {"movies": movies})

    def detailMovie(request, pk):
        input_reviews = []
        movie = models.Movie.objects.get(pk=pk)
        commets = models.Comment.objects.filter(movie_fk_id=movie.id).order_by('id').reverse
        if request.method == 'POST':
            comment = request.POST['comment']
            input_reviews.append(comment)

            predicted_sentiment, probability = ModelSC.predictedSentiment(ModelSC, input_reviews)
            # Print outputs
            #print("Predicted sentiment:", predicted_sentiment)
            #print("Probability:", probability)

            commentModel = models.Comment()
            commentModel.content = comment
            commentModel.predicted = predicted_sentiment
            commentModel.probability = probability
            commentModel.movie_fk = movie

            ModelSC.calificate(ModelSC, movie, predicted_sentiment)
            commentModel.save()

            return HttpResponseRedirect('/movie/'+str(pk)+'/')

        else:
            return render(request, "movie.html", {"movie": movie, "commets": commets})


