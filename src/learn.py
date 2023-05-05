from dotenv import load_dotenv
load_dotenv(verbose=True)
from gpt.gpt import get_questions, get_answer
from vector.chroma import ChromaClient
import uuid
from gpt.gpt import get_embeddings

id = str(uuid.uuid4())
print("ID: ", id)
chroma_client = ChromaClient(id)
chroma_client.create_collection()

# open file and read the content
with open('data.txt', 'r', encoding="utf-8") as f:
    data = f.read()

def split(data: str, max_characters: 1000) -> list:
    lines = data.split('\n')

    chunks = []
    chunk = ""
    for line in lines:
      if (len(chunk)) + len(line) > max_characters:
        chunks.append(chunk)
        chunk = line
      else:
        chunk += "\n" + line
    
    return chunks

chunks = split(data, 500)

questions = get_questions(chunks[0])
for q in questions:
    a = get_answer(q, chunks[0])
    print(q)
    print(a)
    if (a == "回答なし"):
        continue
    chroma_client.add(get_embeddings(q), [{ "answer": a }], [str(uuid.uuid4())])

chroma_client.persist()