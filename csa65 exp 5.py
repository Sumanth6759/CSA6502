from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Two sample documents
doc1 = "Artificial Intelligence is transforming education."
doc2 = "Artificial Intelligence is changing the education system."

# Convert text into numerical vectors
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform([doc1, doc2])

# Calculate cosine similarity
similarity = cosine_similarity(vectors)

# Display the similarity matrix
print("Cosine Similarity Matrix:")
print(similarity)

# Display similarity score
score = similarity[0][1]
print("\nSimilarity Score:", score)

# Interpret the score
if score > 0.8:
    print("Interpretation: The two documents are highly similar.")
elif score > 0.5:
    print("Interpretation: The two documents are moderately similar.")
else:
    print("Interpretation: The two documents are less similar.")
