from __future__ import annotations

from integrated_audit_suite import (
    app_description as _app_description,
    app_email as _app_email,
    app_license as _app_license,
    app_name as _app_name,
    app_publisher as _app_publisher,
    app_title as _app_title,
)

app_name = _app_name
app_title = _app_title
app_publisher = _app_publisher
app_description = _app_description
app_email = _app_email
app_license = _app_license
app_logo_url = "/assets/integrated_audit_suite/logo.png"

app_include_js: list[str] = []
app_include_css: list[str] = []

doc_events: dict[str, dict[str, str]] = {}

fixtures: list[str] = []
