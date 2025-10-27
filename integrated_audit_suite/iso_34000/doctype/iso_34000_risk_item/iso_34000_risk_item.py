from __future__ import annotations

from frappe import _
from frappe.model.document import Document

from integrated_audit_suite.iso_34000.risk_matrix import (
    DEFAULT_RISK_MATRIX,
    compare_risk_levels,
)


class ISO34000RiskItem(Document):
    """Risk register entry aligned with ISO 34000 principles."""

    def validate(self) -> None:
        self._sync_risk_evaluation()
        self._validate_residual_risk()

    def before_submit(self) -> None:
        if not self.risk_rating:
            raise ValueError("Risk Rating is required before submission.")

    def _sync_risk_evaluation(self) -> None:
        if not (self.likelihood and self.impact):
            return

        evaluation = DEFAULT_RISK_MATRIX.evaluate(self.likelihood, self.impact)
        self.risk_score = evaluation.score
        self.risk_rating = evaluation.rating

    def _validate_residual_risk(self) -> None:
        if not (self.residual_risk and self.risk_rating):
            return

        if compare_risk_levels(self.residual_risk, self.risk_rating) > 0:
            message = _("Residual risk cannot exceed the initial risk rating.")
            raise ValueError(message)
