import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

embedding_model = "text-embedding-ada-002"
gpt_model = "gpt-3.5-turbo"

def get_embeddings(text: str):
    res = openai.Embedding.create(input=text, model=embedding_model)
    embeddings = res['data'][0]['embedding']
    return embeddings


def chat_completion(messages: list):
    res = openai.ChatCompletion.create(
        model=gpt_model,
        messages=messages,
        temperature=0,
    )
    return res["choices"][0]["message"]["content"]

def get_questions(doc: str):
    res = chat_completion([{
        "role": "user",
        "content": f"以下の文書のに回答があるような質問を１０つ生成してください。\n\n{doc}"
    }])
    return res.split("\n")

def get_answer(q: str, doc: str):
    return chat_completion([{
        "role": "user",
        "content": f"以下の質問に与えられた参考文書から回答を見つけてください。回答が文書の中に見つからないときには「回答なし」と答えてください。\n\n\n質問: {q} \n\n\n文書:{doc}\n\n\n回答: "
    }])