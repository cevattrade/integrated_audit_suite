from __future__ import annotations

import frappe
from frappe.model.document import Document


class ISO9001Clause(Document):
    """DocType representing an ISO 9001 clause compliance record."""

    def validate(self) -> None:
        """Ensure a clause number is provided and unique per site."""
        if not self.clause_number:
            frappe.throw("Clause Number is required.")

        existing = frappe.db.exists(
            self.doctype,
            {"name": ("!=", self.name), "clause_number": self.clause_number},
        )
        if existing:
            frappe.throw("Clause Number must be unique.")
