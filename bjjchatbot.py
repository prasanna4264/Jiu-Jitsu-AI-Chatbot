#Imports
import os
import json
import faiss
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
from typing import List, Tuple
from langchain_openai import OpenAIEmbeddings

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Define a mini knowledge base
jiu_jitsu_kb = [
    {
        "technique": "Triangle Choke",
        "context": "Opponent postures up in closed guard",
        "steps": "Break posture, pull arm across, shoot legs up, lock triangle, adjust angle, pull head",
        "role": "Coach",
        "tags": "guard,submission"
    },
    {
        "technique": "Hip Bump Sweep",
        "context": "Opponent leans forward in closed guard",
        "steps": "Sit up, trap arm, post hand, bump hips, roll to mount",
        "role": "Coach",
        "tags": "guard,sweep"
    },
    {
        "technique": "Mount Escape (Trap and Roll)",
        "context": "Opponent has high mount with hands on mat",
        "steps": "Trap one arm, bridge hard, roll opponent into guard or mount",
        "role": "Coach",
        "tags": "mount,escape"
    }
]

# Prepare documents and metadata
documents = [f"{entry['technique']} - {entry['context']}: {entry['steps']}" for entry in jiu_jitsu_kb]
metadata = [
    {
        "technique": entry["technique"],
        "context": entry["context"],
        "steps": entry["steps"],
        "role": entry["role"]
    } for entry in jiu_jitsu_kb
]

# Embed and store vectors
embedding_model = OpenAIEmbeddings(openai_api_key=api_key)
embeddings = embedding_model.embed_documents(documents)
embedding_matrix = np.array(embeddings).astype("float32")
index = faiss.IndexFlatL2(len(embedding_matrix[0]))
index.add(embedding_matrix)

# Semantic search
def semantic_search(query: str, top_k=1) -> Tuple[dict, float]:
    query_embedding = embedding_model.embed_query(query)
    D, I = index.search(np.array([query_embedding]).astype("float32"), top_k)
    return metadata[I[0][0]], D[0][0]

# Prompt builder
def build_prompt(entry: dict, user_input: str) -> str:
    return (
        f"You are a Jiu-Jitsu {entry['role']}.\n"
        f"Technique: {entry['technique']}\n"
        f"Context: {entry['context']}\n"
        f"Steps: {entry['steps']}\n"
        f"User Question: {user_input}"
    )

# Ask GPT (min token usage)
def ask_gpt(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.3,
        messages=[
            {"role": "system", "content": "You are a concise and technical Jiu-Jitsu instructor."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Chat Loop
def run_chat():
    print("Jiu-Jitsu Chatbot ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Oss! See you on the mats.")
            break
        result, score = semantic_search(user_input)
        if score > 1.0:
            print("Not sure how to help. Try rephrasing or being more specific.")
            continue
        prompt = build_prompt(result, user_input)
        answer = ask_gpt(prompt)
        print(f"\n {answer}\n")


print("Jiu-Jitsu chatbot code loaded.")


if __name__ == "__main__":
    run_chat()