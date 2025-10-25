from __future__ import annotations

from frappe.model.document import Document


class ISO34000RiskItem(Document):
    """Risk register entry aligned with ISO 34000 principles."""

    def before_submit(self) -> None:
        if not self.risk_rating:
            raise ValueError("Risk Rating is required before submission.")
