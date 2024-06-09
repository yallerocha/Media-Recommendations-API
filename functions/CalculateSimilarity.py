from numpy import ndarray
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class CalculateSimilarity:

    @staticmethod
    def calculate_similarity(movies) -> ndarray:
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(movies['combined_features'])

        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

        return cosine_sim