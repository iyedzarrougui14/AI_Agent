# prompts.py

def build_prompt(domain: str) -> str:
    return f"""
Tu es un expert en innovation d'entreprise. Génère 5 idées de business innovantes dans le domaine suivant : "{domain}".

Pour chaque idée, fournis :
1. **Nom de l’entreprise**
2. **Description courte**
3. **Public cible**
4. **Sources potentielles de revenus**

Présente les résultats dans un format lisible, structuré avec des titres clairs pour chaque idée.
"""
