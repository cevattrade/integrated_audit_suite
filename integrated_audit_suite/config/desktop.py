from __future__ import annotations

MODULE_ICONS = {
    "ISO 9001": "fa fa-check-circle",
    "ISO 34000": "fa fa-shield",
    "ISO 13053": "fa fa-line-chart",
    "EFQM": "fa fa-star",
    "Accounting Audit": "fa fa-balance-scale",
}

def get_data() -> list[dict[str, object]]:
    """Return module definitions for the Integrated Audit Suite."""
    return [
        {
            "module_name": module,
            "color": "#1F4F8B",
            "icon": icon,
            "type": "module",
            "label": module,
        }
        for module, icon in MODULE_ICONS.items()
    ]
