```python
# Import necessary libraries
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MessageTemplateEngine:
    def __init__(self, templates):
        self.templates = templates
        self.vectorizer = TfidfVectorizer().fit_transform(self.templates)

    def generate_message(self, icp):
        """
        Generate a custom message based on the ICP.
        """
        # Tokenize the ICP
        icp_tokens = word_tokenize(icp)

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        icp_tokens = [w for w in icp_tokens if not w in stop_words]

        # Vectorize the ICP
        icp_vector = self.vectorizer.transform([' '.join(icp_tokens)])

        # Calculate cosine similarity between the ICP and templates
        cosine_similarities = cosine_similarity(icp_vector, self.vectorizer).flatten()

        # Get the index of the most similar template
        most_similar_index = cosine_similarities.argmax()

        # Return the most similar template
        return self.templates[most_similar_index]

# Example usage:
templates = [
    "Hello, I noticed that you're interested in {product}. Would you like to schedule a meeting to discuss it further?",
    "Hi, I saw that you've been looking at {product}. Can we set up a time to talk about it?",
    "Hey, I think {product} could really help your business. Would you be open to a meeting to discuss it?",
]

engine = MessageTemplateEngine(templates)
icp = "interested in product"
message = engine.generate_message(icp)
print(message)
```
