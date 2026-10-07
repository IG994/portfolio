"""
measurements.py — estimate body measurements so the user doesn't have to.

One of the most annoying parts of getting something tailored is producing your
measurements. Most people DON'T know theirs — but they DO know what size they
wear ("I'm a US 8", "a medium at Zara"). This module turns that into an
estimated measurement set the tailor can start from.

IMPORTANT (honesty): these are ESTIMATES from standard size charts. Real brand
sizing varies a lot, and bodies don't match charts exactly. Every result is
returned with a confidence level and a "confirm at fitting" note. The goal is to
remove friction and give the tailor a strong starting point — NOT to replace a
final fitting.
"""

from dataclasses import dataclass, field, asdict
from typing import Optional


# --- The measurement set we produce -----------------------------------------

@dataclass
class Measurements:
    """Estimated body measurements, in inches, plus honesty metadata."""
    bust_chest: Optional[float] = None
    waist: Optional[float] = None
    hip: Optional[float] = None
    source: str = ""            # how we arrived at these (e.g. "US women's size 8")
    confidence: str = "low"     # "high" | "medium" | "low"
    notes: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)


# --- Standard size charts (approximate, in inches) --------------------------
# These are common US retail values. They vary by brand, so we treat them as a
# starting estimate only. New charts (brands, men's, EU/UK) can be added here.

SIZE_CHARTS: dict[str, dict[str, dict[str, float]]] = {
    # Women's US numeric sizing -> bust / waist / hip
    "us_womens": {
        "0":  {"bust_chest": 32.0, "waist": 24.0, "hip": 34.5},
        "2":  {"bust_chest": 33.0, "waist": 25.0, "hip": 35.5},
        "4":  {"bust_chest": 34.0, "waist": 26.0, "hip": 36.5},
        "6":  {"bust_chest": 35.0, "waist": 27.0, "hip": 37.5},
        "8":  {"bust_chest": 36.5, "waist": 28.5, "hip": 39.0},
        "10": {"bust_chest": 38.0, "waist": 30.0, "hip": 40.5},
        "12": {"bust_chest": 39.5, "waist": 31.5, "hip": 42.0},
        "14": {"bust_chest": 41.0, "waist": 33.0, "hip": 43.5},
    },
    # Men's alpha sizing (tops) -> chest / waist (hip left blank)
    "us_mens": {
        "XS": {"bust_chest": 34.0, "waist": 28.0},
        "S":  {"bust_chest": 36.0, "waist": 30.0},
        "M":  {"bust_chest": 39.0, "waist": 33.0},
        "L":  {"bust_chest": 42.0, "waist": 36.0},
        "XL": {"bust_chest": 45.0, "waist": 39.0},
    },
}


def estimate_from_size(chart: str, size: str) -> Measurements:
    """Estimate measurements from a standard size the user already wears.

    chart: which size chart to use, e.g. "us_womens" or "us_mens".
    size:  the size within that chart, e.g. "8" or "M".
    """
    chart = chart.lower().strip()
    size = size.upper().strip() if chart == "us_mens" else size.strip()

    if chart not in SIZE_CHARTS:
        return Measurements(
            source=f"unknown chart '{chart}'",
            confidence="low",
            notes=[f"No size chart named '{chart}'. Available: {', '.join(SIZE_CHARTS)}."],
        )

    table = SIZE_CHARTS[chart]
    if size not in table:
        return Measurements(
            source=f"{chart} size {size}",
            confidence="low",
            notes=[f"Size '{size}' not in the {chart} chart. Available: {', '.join(table)}."],
        )

    values = table[size]
    return Measurements(
        **values,
        source=f"{chart} size {size}",
        confidence="medium",  # a standard chart is a decent estimate, not exact
        notes=[
            "Estimated from a standard size chart — real brand sizing varies.",
            "Confirm exact measurements with the tailor at a fitting before cutting fabric.",
        ],
    )


def estimate_from_reference_garment(
    bust_chest: Optional[float] = None,
    waist: Optional[float] = None,
    hip: Optional[float] = None,
) -> Measurements:
    """Use measurements taken from a garment the user says fits them well.

    This is the most reliable input we can take without a tape measure on the
    body: measure a shirt/trousers that already fit, and we carry those through
    as the starting point (still to be confirmed at fitting).
    """
    provided = {k: v for k, v in
                {"bust_chest": bust_chest, "waist": waist, "hip": hip}.items()
                if v is not None}
    if not provided:
        return Measurements(
            source="reference garment",
            confidence="low",
            notes=["No garment measurements were provided."],
        )
    return Measurements(
        **provided,
        source="a garment the user says fits well",
        confidence="high",  # measured from a real garment that fits
        notes=[
            "Taken from a well-fitting garment the user already owns.",
            "Still confirm with the tailor at a fitting.",
        ],
    )


# --- Quick demo: run `python src/measurements.py` ---------------------------

if __name__ == "__main__":
    import json

    print("Example 1 — user says 'I wear a US women's 8':")
    print(json.dumps(estimate_from_size("us_womens", "8").as_dict(), indent=2))

    print("\nExample 2 — user says 'I'm a men's L':")
    print(json.dumps(estimate_from_size("us_mens", "L").as_dict(), indent=2))

    print("\nExample 3 — user measured a shirt that fits (chest 38, waist 32):")
    print(json.dumps(
        estimate_from_reference_garment(bust_chest=38, waist=32).as_dict(),
        indent=2,
    ))
