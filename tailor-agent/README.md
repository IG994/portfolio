# 🧵 Tailor Agent

An AI agent that makes getting clothes tailored easy - from a plain-language brief to a spec a tailor can actually work from.

## The problem

In many places, getting special clothes made by a tailor is very much the norm. I can recount the number of times I've stepped into a small tailor's shop to get a wedding outfit or graduation gown made from scratch. While the output feels more "you" than a large retailer, it's often a multi-step, high-friction process: figuring out the design, the fabric, the style, your measurements, finding a good tailor, and communicating all of it clearly. This projects focuses on the two parts that I have found the most challenging in the past:
- **Measurements** — these are difficult to know and can be everchanging, and giving them to a tailor is a hassle.
- **Communicating the design** to the tailor in a form they can actually use and bring to life. 

Example use case: *"I have a wedding coming up and need an outfit made."* → the agent takes it from idea to a tailor-ready brief.

## What it does

**Phase 1 (core — build first, no external API needed):**
1. **Brief → structured style spec** - the user describes the occasion (e.g., wedding), garment, vibe, colors, fabric, budget; the agent extracts a clean structured spec.
2. **Measurement estimation** - estimate measurements from the sizes/brands the user already wears (size-chart mapping) or from a garment that fits well. Always output as estimates with confidence + a "confirm at fitting" note. 
3. **Tailor-ready spec sheet** — design description + fabric + estimated measurements + construction notes, formatted the way a tailor expects.
4. **Evals** — score brief-adherence and measurement-estimate sanity.

**Phase 1 add-on (needs an image-generation API key):**
- Generate original design concepts + a moodboard from the spec.

**Phase 2 (later):**
- Match a tailor from a database → draft a WhatsApp message **+ an ElevenLabs voice note** (tailors work in voice notes) → simulated send.

## Try it

The measurement estimator runs with no dependencies and no API keys:

```bash
python3 src/measurements.py
```

Example — the user says *"I wear a US women's 8"* →

```json
{
  "bust_chest": 36.5, "waist": 28.5, "hip": 39.0,
  "source": "us_womens size 8",
  "confidence": "medium",
  "notes": [
    "Estimated from a standard size chart — real brand sizing varies.",
    "Confirm exact measurements with the tailor at a fitting before cutting fabric."
  ]
}
```

Every estimate carries a **confidence level** and a **"confirm at fitting" note** — the agent removes friction, it doesn't replace a fitting.

## Principles / guardrails

- **Generate, don't scrape** — original designs from an image model; never scrape Pinterest or other designers' images.
- **Real tailor data stays private** — the real tailor database is `.gitignore`d and never committed; the repo ships an anonymized sample only.
- **Measurements are always estimates** — clearly caveated; the agent reduces friction, it doesn't replace a fitting.
- **Never contacts real tailors** — outreach is generated and simulated, never actually sent to real people.
- **Honest scope** — mock/sample data is labeled as such.

## Status

🚧 Phase 1, in progress — starting with the brief → structured style spec.
