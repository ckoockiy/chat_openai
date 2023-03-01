import openai
import os
from textToSpeech import convertir_texto_a_voz

# Configura la API Key de OpenAI
api_key = os.environ["OPENAI_API_KEY"]
openai.api_key = api_key

# Función para generar respuesta
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        temperature=0.7
    )
    message = completions.choices[0].text
    return message.strip()

# Define la función principal del chatbot
def chat():
    # Inicia el loop del chatbot
    while True:
        prompt = input("> ")
        response = generate_response(prompt)
        print(response)
        convertir_texto_a_voz(response)

# Inicia el chatbot
chat()
