from dotenv import load_dotenv
load_dotenv(verbose=True)
from vector.chroma import ChromaClient
from gpt.gpt import get_embeddings

id = "e9af4eb0-8da1-4806-8718-128707a8f232"
chroma_client = ChromaClient(id)
chroma_client.use_collection()

while(True):
  user_input = input("ASK  : ")
  embeddings = get_embeddings(user_input)
  res = chroma_client.query(embeddings, 2)
  print("Answer1: ")
  print(res["metadatas"][0][0]["answer"])
  print("Answer2: ")
  print(res["metadatas"][0][1]["answer"])
  print("====================================")
  print("")