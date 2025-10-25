from __future__ import annotations

from frappe.model.document import Document


class EFQMAssessment(Document):
    """Self-assessment record for the EFQM excellence model."""

    def validate(self) -> None:
        if self.score is not None and not 0 <= self.score <= 1000:
            raise ValueError("Score must be between 0 and 1000.")
