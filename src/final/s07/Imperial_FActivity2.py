# -*- coding: utf-8 -*-
"""Imperial_FActivity2.ipynb

*De La Salle University – Dasmariñas* \
*College of Information and Computer Studies*

**S–CSIS312 — Natural Language Processing** \
Finals — Activity 2

**Name:** Luis Anton P. Imperial \
**CYS:** BCS32

# Finals Programming Activity 2: Tokenization in NLP with Python

## Case Scenario: Analyzing Customer Feedback for a Tech Company

A tech company has received a large volume of customer feedback via surveys, social media
posts, and support tickets. They need to analyze the feedback to identify common themes, key
opinions, and issues raised by customers. To do so, the company decides to preprocess the text
data and perform a basic analysis to understand the language used by customers.

The first step in this analysis is tokenization—the process of breaking the feedback text into
smaller units (tokens) such as words, phrases, and sentences. Tokenization is the foundational
task that helps further analyze text, such as extracting features, building word clouds, or
identifying sentiment.

In this activity, you will implement tokenization techniques using Python to preprocess the
customer feedback data.

## Objectives:

1. Use NLTK and spaCy to tokenize customer feedback.
2. Perform sentence and word tokenization.
3. Remove irrelevant words (stopwords) to focus on important information.
4. Extract useful entities (like product names or issues) from the feedback.

## Install Required Libraries:

1. If you haven't installed nltk or spaCy, do so now: `!pip install nltk spacy`
2. For spaCy, download the English model: `python -m spacy download en_core_web_sm`
3. Download NLTK Resources
  ```
  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')
  ```
"""

!pip install nltk spacy

!python -m spacy download en_core_web_sm

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

"""## Part 1: Tokenizing Customer Feedback

You will start by tokenizing some customer feedback text into words and sentences.

### Scenario Example:

Customer feedback text:

"Great product, but the software crashed twice in the last week. The customer support team was very helpful, though. Could improve the battery life."

a. **Tokenize the Feedback into Sentences and Words using NLTK** (Write functions to split the feedback into sentences and words using the NLTK library)
  - Sample Output:

b. **Tokenize the Feedback into Words using spaCy** (use spaCy to tokenize the same feedback into word)
"""

import random

def generate_feedback():
    feedbacks = [
        "The phone's camera quality is amazing!",
        "I'm having trouble connecting to the Wi-Fi network.",
        "The battery life of my new Galaxy S23 is impressive.",
        "Customer service was helpful, resolved the issue quickly.",
        "Disappointed with the latest update, it's buggy.",
        "The new features in iOS 16 are fantastic, especially the improved focus mode.",
        "The screen of my iPhone 14 is quite bright.",
        "I had a problem with the software, the support team from Apple was helpful but the issue was not completely solved",
        "Google Pixel 7's camera is excellent in low light.",
        "Overall, a great product from Samsung."
    ]
    return random.choice(feedbacks)

feedback_list = []

for _ in range(5):
    feedback_list.append(generate_feedback())

# Tokenize using NLTK
def nltk_tokenize(text):
  sentences = nltk.sent_tokenize(text)
  words = []
  for sentence in sentences:
    words.extend(nltk.word_tokenize(sentence))
  return sentences, words

nltk_results = []
for feedback in feedback_list:
    nltk_results.append(nltk_tokenize(feedback))

# Tokenize using spaCy
nlp = spacy.load("en_core_web_sm")

spacy_results = []
for feedback in feedback_list:
  doc = nlp(feedback)
  spacy_tokens = [token.text for token in doc]
  spacy_results.append(spacy_tokens)

# Print the results
for i, feedback in enumerate(feedback_list):
     print(f"Feedback {i+1}: {feedback}")
     print("NLTK Sentences:", nltk_results[i][0])
     print("NLTK Words:", nltk_results[i][1])
     print("spaCy Tokens:", spacy_results[i])
     print("-" * 20)

"""## Part 2: Removing Stopwords

Customer feedback often contains common words like “the,” “is,” and “it” that do not provide much useful information. To focus on meaningful content, we can remove stopwords.

a) **Remove Stopwords using NLTK** - Use NLTK’s list of stopwords to filter out
irrelevant words.

b) **Remove Stopwords using spaCy** (spaCy offers a built-in property (token.`is_stop`)
to check whether a token is a stopword)
"""

from nltk.corpus import stopwords
import spacy

# Remove stopwords using NLTK
stop_words_nltk = set(stopwords.words('english'))

def remove_stopwords_nltk(words):
  return [word for word in words if word.lower() not in stop_words_nltk]

# Remove stopwords using spaCy
nlp = spacy.load("en_core_web_sm")

def remove_stopwords_spacy(text):
    doc = nlp(text)
    return [token.text for token in doc if not token.is_stop]

# Print the results with stopwords removed
for i, feedback in enumerate(feedback_list):
    print(f"Feedback {i+1}: {feedback}")
    print("NLTK Words (no stopwords):", remove_stopwords_nltk(nltk_results[i][1]))
    print("spaCy Tokens (no stopwords):", remove_stopwords_spacy(feedback))
    print("-" * 20)

"""## Part 3: Extracting Named Entities

In customer feedback, named entities such as product names or locations are important for analysis. You can use spaCy to identify named entities.

a) **Extract Named Entities Using spaCy** - Modify your spaCy function to extract named entities (such as company names, products, or issues mentioned in the
feedback).
"""

def extract_entities(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    return entities

# Print the results with named entities
for i, feedback in enumerate(feedback_list):
    print(f"Feedback {i+1}: {feedback}")
    print("Named Entities:", extract_entities(feedback))
    print("-" * 20)

"""## Part 4: Evaluating and Reflecting on Tokenization

1. **Compare Tokenization Results** - Compare the results of NLTK and spaCy tokenization, and discuss their performance. Which method provides more
accurate results? Which one is easier to use?
2. ### Discussion
  1. What are the strengths and weaknesses of NLTK and spaCy tokenization methods?
  2. How did the removal of stopwords affect the tokenization results?
  3. Did spaCy do a better job at extracting named entities? Why or why not?
  4. How could you extend this process to analyze a larger set of customer feedback, such as identifying common themes or performing sentiment analysis?

#### What are the strengths and weaknesses of NLTK and spaCy tokenization methods?

NLTK offers a wider range of tokenization methods including word tokenization, sentence tokenization, and even regular expression-based tokenization. This makes it adaptable for different text processing scenarios.

However, NLTK can be slower compared to spaCy, especially when processing large volumes of text. Additionally, it relies on rule-based methods and might not be as accurate as spaCy, which uses statistical models trained on large datasets.

spaCy is known for its speed and efficiency in processing text, making it suitable for large datasets, but it can be resource-intensive, potentially requiring more memory and processing power.

#### How did the removal of stopwords affect the tokenization results?

The removal of stopwords eased the preparation process and subsequently now allows for the raw data to be consumed by natural language processing activities.

#### Did spaCy do a better job at extracting named entities? Why or why not?

No, because for smaller datasets that only use well-known entity names such as Google and Samsung, rule-based methods are enough.

#### How could you extend this process to analyze a larger set of customer feedback, such as identifying common themes or performing sentiment analysis?

We can use word-sense disambiguation (WSD) to understand the context behind each word, which necessarily requires tokenization.

## Submission Requirements:

1. Submit the Python script containing all your implementations for tokenization,
stopword removal, and named entity extraction.
2. ### Provide answers to the following questions:
  1. What are the advantages and limitations of NLTK and spaCy in text preprocessing?
  2. How can tokenization help with analyzing customer feedback?
  3. How does removing stopwords impact the analysis?
  4. Why is it important to extract named entities from customer feedback?
  5. What insights would you look for from tokenized feedback?

#### What are the advantages and limitations of NLTK and spaCy in text preprocessing?

NLTK offers a wider range of tokenization methods including word tokenization, sentence tokenization, and even regular expression-based tokenization. This makes it adaptable for different text processing scenarios.

However, NLTK can be slower compared to spaCy, especially when processing large volumes of text. Additionally, it relies on rule-based methods and might not be as accurate as spaCy, which uses statistical models trained on large datasets.

spaCy is known for its speed and efficiency in processing text, making it suitable for large datasets, but it can be resource-intensive, potentially requiring more memory and processing power.

#### How can tokenization help with analyzing customer feedback?

Tokenization can prepare words up to be absorbed by other activities done during natural language processing, such as word-sense disambiguation and sentiment analysis.

#### How does removing stopwords impact the analysis?

Removing stopwords helps improve the uniqueness of each word and cleans the list of any unnecessary parts of the sentence that don't contribute to further analysis.

#### Why is it important to extract named entities from customer feedback?

By identifying entities, we can link customer sentiments (positive or negative) to particular products, features, or aspects of their experience. For example, if many customers mention "battery life" with negative sentiment, it highlights a potential area for improvement.

#### What insights would you look for from tokenized feedback?

We can reveal common themes, topics and issues raised by customers. Aside from that, we can understand customers' overall sentiment towards each of our products, as well as segment them based on their interests and preferences.
"""