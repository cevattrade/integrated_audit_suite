from __future__ import annotations

from frappe.model.document import Document


class AccountingAuditChecklist(Document):
    """Checklist for accounting audit procedures and findings."""

    def validate(self) -> None:
        if not self.status:
            raise ValueError("Status is required for the audit checklist item.")
