from transformers import pipeline

chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

def get_response(question):
    return chatbot(question, max_length=100)[0]["generated_text"]