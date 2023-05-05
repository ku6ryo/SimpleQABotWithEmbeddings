Very simple sample of QA engine using vector store.


# How this works
- Split a input document into chunks
- Generate questions and the answers for each chunks
- Calculate embeddings for each questions
- Store the embeddings of questions with the answers
- Query vector store with embeddings calculated from user input texts.
- Return answer stored with the embedding.