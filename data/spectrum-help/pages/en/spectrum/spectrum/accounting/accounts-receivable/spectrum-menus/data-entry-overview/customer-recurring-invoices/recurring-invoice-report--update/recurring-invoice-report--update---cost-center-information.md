---
title: "Recurring Invoice Report / Update - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-recurring-invoices/recurring-invoice-report--update/recurring-invoice-report--update---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-recurring-invoices/recurring-invoice-report--update/recurring-invoice-report--update---cost-center-information"
---

# Recurring Invoice Report / Update - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, when running the Recurring Invoice Edit Listing and Recurring Invoice Register Report, Spectrum will include invoices only if the operator requesting the report has permission to access the cost center assigned to the invoice. Spectrum compares the cost center assigned in the invoice header with cost centers in the operator's assigned scheme; if the invoice cost center is not included, then that invoice is not shown on the report. Because this report is based on cost centers assigned in the header portion of the invoice, it is possible that the report will include invoice information for invoices with detail assigned to allowed cost centers that the operator is not otherwise permitted to access. The cost centers assigned to invoices display on the edit listing.
If the 'Use entity-specific numbering?' installation option is selected for this company, entity-specific invoice numbers used for Accounts Receivable invoices will read for the cost center to be assigned to the new invoice. If the cost center is assigned to the 'main company entity' (blank), then get the 'Next invoice number' from Accounts Receivable Installation. If an entity is associated with the cost center, then read the new Entity Invoice Number Table for the 'Next invoice number' to be assigned to invoices in that entity.
