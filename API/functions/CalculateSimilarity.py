from numpy import ndarray
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class CalculateSimilarity:

    @staticmethod
    def calculateSimilarity(media_table) -> ndarray:
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(media_table['combined_features'])

        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

        return cosine_sim