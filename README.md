Very simple sample of QA engine using vector store.


# How this works
- Split a input document into chunks
- Generate questions and the answers for each chunks
- Calculate embeddings for each questions
- Store the embeddings of questions with the answers
- Query vector store with embeddings calculated from user input texts.
- Return answer stored with the embedding.

# Problem
For the similar questions, like "when is the checkin time?" and "when is the checkout time?" Vector store does not return expected results. For instance, user is asking "checkout time" but vector store returns the embeddings of "What is the checkout time" as the closest vector.