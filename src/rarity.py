import json
import os
import re

import requests

from config import TIERS, TIER_THRESHOLDS


def _inat_query(plant_name: str) -> dict | None:
    try:
        r = requests.get(
            "https://api.inaturalist.org/v1/taxa",
            params={"q": plant_name, "rank": "species", "per_page": 1},
            timeout=12,
        )
        results = r.json().get("results", [])
        if results:
            t = results[0]
            return {
                "scientific_name": t.get("name", plant_name),
                "common_name": t.get("preferred_common_name") or plant_name,
                "observations_count": t.get("observations_count", 0),
            }
    except Exception:
        pass
    return None


def _count_to_tier(count: int) -> str:
    for tier, lo, hi in TIER_THRESHOLDS:
        if lo <= count < hi:
            return tier
    return "F"


def _claude_rank(plants: list[str], country: str) -> dict[str, str]:
    """Pide a Claude que clasifique plantas por rareza. Requiere ANTHROPIC_API_KEY."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("  [aviso] ANTHROPIC_API_KEY no definida. Asignando tier C por defecto.")
        return {p: "C" for p in plants}

    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        prompt = (
            f"Clasifica estas plantas de {country} por rareza en la naturaleza.\n"
            f"Tiers disponibles (de más rara a más común):\n"
            f"SS+ (críticamente en peligro / casi extinta)\n"
            f"SS (muy rara, pocas poblaciones)\n"
            f"S (rara, difícil de encontrar)\n"
            f"A (poco común)\n"
            f"B (moderadamente común)\n"
            f"C (bastante común)\n"
            f"D (muy común)\n"
            f"F (invasora / abundante en todo el país)\n\n"
            f"Plantas: {', '.join(plants)}\n\n"
            f"Responde SOLO con JSON válido: {{\"nombre planta\": \"tier\", ...}}"
        )
        msg = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}],
        )
        text = msg.content[0].text
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            data = json.loads(match.group())
            return {p: (data.get(p, "C") if data.get(p, "C") in TIERS else "C") for p in plants}
    except Exception as e:
        print(f"  [error Claude] {e}")

    return {p: "C" for p in plants}


def score_plants(plants: list[str], country: str) -> dict[str, tuple[str, str]]:
    """
    Retorna {nombre_original: (tier, nombre_mostrar)}
    Prioridad: iNaturalist → Claude fallback.
    """
    results: dict[str, tuple[str, str]] = {}
    needs_claude: list[str] = []

    for plant in plants:
        data = _inat_query(plant)
        if data and data["observations_count"] > 0:
            tier = _count_to_tier(data["observations_count"])
            display = data["common_name"].title()
            print(f"  ✓ {plant}: {data['observations_count']:,} obs → {tier}")
            results[plant] = (tier, display)
        else:
            print(f"  ? {plant}: sin datos iNaturalist → Claude")
            needs_claude.append(plant)

    if needs_claude:
        print(f"\n  Consultando Claude para {len(needs_claude)} plantas...")
        claude_tiers = _claude_rank(needs_claude, country)
        for plant in needs_claude:
            tier = claude_tiers.get(plant, "C")
            results[plant] = (tier, plant.split()[-1].title())

    return results
