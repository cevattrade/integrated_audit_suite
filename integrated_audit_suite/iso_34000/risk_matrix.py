"""Risk evaluation helpers for ISO 34000 assessments."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

LIKELIHOOD_WEIGHTS: Mapping[str, int] = {
    "Rare": 1,
    "Unlikely": 2,
    "Possible": 3,
    "Likely": 4,
    "Almost Certain": 5,
}

IMPACT_WEIGHTS: Mapping[str, int] = {
    "Insignificant": 1,
    "Minor": 2,
    "Moderate": 3,
    "Major": 4,
    "Severe": 5,
}

RISK_THRESHOLDS: Mapping[str, range] = {
    "Low": range(1, 5),
    "Medium": range(5, 13),
    "High": range(13, 20),
    "Critical": range(20, 26),
}


@dataclass(frozen=True)
class RiskEvaluation:
    """Calculated score and label for a risk exposure."""

    score: int
    rating: str


class RiskMatrix:
    """Simple multiplicative risk matrix used for ISO 34000 style scoring."""

    def __init__(
        self,
        likelihood_weights: Mapping[str, int] | None = None,
        impact_weights: Mapping[str, int] | None = None,
        thresholds: Mapping[str, range] | None = None,
    ) -> None:
        self._likelihood_weights = dict(likelihood_weights or LIKELIHOOD_WEIGHTS)
        self._impact_weights = dict(impact_weights or IMPACT_WEIGHTS)
        self._thresholds = dict(thresholds or RISK_THRESHOLDS)

    def evaluate(self, likelihood: str, impact: str) -> RiskEvaluation:
        """Return the risk score and qualitative rating for the provided values."""

        try:
            likelihood_weight = self._likelihood_weights[likelihood]
        except KeyError as exc:  # pragma: no cover - defensive programming
            raise KeyError(f"Unknown likelihood level: {likelihood}") from exc

        try:
            impact_weight = self._impact_weights[impact]
        except KeyError as exc:  # pragma: no cover - defensive programming
            raise KeyError(f"Unknown impact level: {impact}") from exc

        score = likelihood_weight * impact_weight
        rating = self._determine_rating(score)
        return RiskEvaluation(score=score, rating=rating)

    def _determine_rating(self, score: int) -> str:
        for label, valid_range in self._thresholds.items():
            if score in valid_range:
                return label
        raise ValueError(f"Score {score} does not fall into any configured threshold range.")


DEFAULT_RISK_MATRIX = RiskMatrix()


def compare_risk_levels(primary: str, secondary: str) -> int:
    """Compare two risk labels based on the configured rating order."""

    order = {label: index for index, label in enumerate(RISK_THRESHOLDS, start=1)}
    return (order.get(primary, 0) > order.get(secondary, 0)) - (
        order.get(primary, 0) < order.get(secondary, 0)
    )

