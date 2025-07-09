# main.py

import google.generativeai as genai
from prompts import build_prompt

# Configuration de l’API Gemini
genai.configure(api_key="AIzaSyBKn1h_kSWzXyuTB8PkWE343RZW0-ZLgpw")  # Remplacez par votre clé API Gemini

def generate_business_ideas(domain: str):
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Construction du prompt avec le domaine choisi
    prompt = build_prompt(domain)

    # Appel de l'API
    response = model.generate_content(prompt)

    # Affichage des idées générées
    print("\n=== Idées de business générées ===\n")
    print(response.text)

if __name__ == "__main__":
    domaine = input("Entrez un domaine d’activité (ex: 'mode durable', 'nutrition personnalisée') : ")
    generate_business_ideas(domaine)
