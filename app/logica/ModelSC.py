import pickle

class ModelSC():

    def extract_features(self, words):
        return dict([(word, True) for word in words])


    def predictedSentiment(self, input_reviews):

        file = open(r'app/logica/classifier.pickle', 'rb')
        classifier = pickle.load(file)
        file.close()

        for review in input_reviews:
            probabilities = classifier.prob_classify(self.extract_features(self, review.split()))

        predicted_sentiment = probabilities.max()
        probability = round(probabilities.prob(predicted_sentiment), 2)

        return predicted_sentiment, probability


    def calificate(self, movie, predicted):
        if (predicted == 'Positive'):
            movie.likes += 1
        else:
            movie.dislikes += 1
        movie.save()
