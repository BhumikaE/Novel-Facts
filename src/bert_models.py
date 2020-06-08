import scipy
import numpy as np
import pickle
from sentence_transformers import models, SentenceTransformer


class Model:
    def __init__(self):
        self.model = SentenceTransformer("bert-base-nli-stsb-mean-tokens")

        # self.multilingual_model = SentenceTransformer('distiluse-base-multilingual-cased')

    def is_news_fake(self):
        # bert_stsb_model

        pass

    def create_corpus_embeddings(self, fake_news_data_set):
        self.corpus = fake_news_data_set["FakeNews"].tolist()
        filename = "./Data/corp_emb.pkl"
        infile = open(filename, "rb")
        stsb_model = pickle.load(infile)
        infile.close()
        self.corpus_embeddings = stsb_model

    def is_fake_news(self, query):
        closest_n = 3
        output = []
        queries = [
            query,
        ]
        query_embeddings = self.model.encode(queries)

        for query, query_embedding in zip(queries, query_embeddings):
            distances = scipy.spatial.distance.cdist(
                [query_embedding], self.corpus_embeddings, "cosine"
            )[0]

            results = zip(range(len(distances)), distances)
            results = sorted(results, key=lambda x: x[1])

            print("\n======================\n")
            print("Query:", query)
            print("\nTop 3 most similar sentences in corpus:")

            for idx, distance in results[0:closest_n]:
                sentence = [self.corpus[idx].strip(), (1 - distance)]
                print(self.corpus[idx].strip(), "(Score: %.4f)" % (1 - distance))
                output.append(sentence)

        return output
