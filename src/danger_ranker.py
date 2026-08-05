import json
import os
import re

import requests


def rank_dangerous_plants(country: str) -> list[str]:
    """Uses Claude to get 10 dangerous plants for a country, least → most dangerous."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY no definida. Necesaria para países sin lista predefinida.")

    import anthropic
    client = anthropic.Anthropic(api_key=api_key)
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": (
                f"Dame exactamente 10 plantas peligrosas que se encuentren en {country}, "
                f"ordenadas de MENOS peligrosa (posición 1) a MÁS peligrosa (posición 10).\n"
                f"Incluye plantas con toxicidad para humanos (irritantes, venenosas, letales).\n"
                f"Usa sus nombres científicos más conocidos.\n\n"
                f"Responde SOLO con un JSON array de 10 nombres científicos en orden:\n"
                f'["planta 1 (menos peligrosa)", ..., "planta 10 (más peligrosa)"]'
            ),
        }],
    )
    text = msg.content[0].text
    match = re.search(r"\[.*?\]", text, re.DOTALL)
    if match:
        return json.loads(match.group())
    raise ValueError(f"No se pudo parsear respuesta de Claude: {text}")


def get_display_name(scientific_name: str) -> str:
    """Returns common name from iNaturalist, or falls back to scientific name."""
    try:
        r = requests.get(
            "https://api.inaturalist.org/v1/taxa",
            params={"q": scientific_name, "rank": "species", "per_page": 1},
            timeout=10,
        )
        results = r.json().get("results", [])
        if results:
            common = results[0].get("preferred_common_name")
            if common:
                return common.title()
    except Exception:
        pass
    return scientific_name
