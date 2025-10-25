from __future__ import annotations

from frappe.model.document import Document


class ISO13053Project(Document):
    """Lean Six Sigma project tracker aligned with ISO 13053."""

    def validate(self) -> None:
        if self.end_date and self.start_date and self.end_date < self.start_date:
            raise ValueError("End Date cannot be before Start Date.")
