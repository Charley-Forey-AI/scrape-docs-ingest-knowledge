---
title: "Reverse Work Order Billing - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/reverse-work-order-billing/reverse-work-order-billing---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/reverse-work-order-billing/reverse-work-order-billing---cost-center-information"
---

# Reverse Work Order Billing - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen for this company, the A/R credit memo that is created during this update uses the same cost center assigned to the original invoice on both the header and detail lines.
If an A/R credit memo is created for a Service Contract Manufacturer (from the Service Contract module on a work order being reversed), then the site cost center is assigned to the invoice's header and detail lines. If an A/R invoice was originally created for a warranty manufacturer, then the same cost centers as the original invoice are assigned to the reversing credit memo.
If the 'Use entity-specific numbering?' installation option is selected for this company, entity-specific invoice numbers used for Accounts Receivable invoices will read for the cost center to be assigned to the new invoice. If the cost center is assigned to the 'main company entity' (blank), then get the 'Next invoice number' from Accounts Receivable Installation. If an entity is associated with the cost center, then read the new Entity Invoice Number Table for the 'Next invoice number' to be assigned to invoices in that entity.
