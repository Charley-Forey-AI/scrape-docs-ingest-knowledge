---
title: "Sales Tax Report - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/reports-overview/sales-tax-report/sales-tax-report---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/reports-overview/sales-tax-report/sales-tax-report---cost-center-information"
---

# Sales Tax Report - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, the starting screen includes a selection for a cost group. When a cost group or cost center is specified, the report will show only invoices assigned to that cost group/cost center. When the operator specifies a cost center on the starting screen, Spectrum verifies that the operator has permission to access the cost center's information before proceeding.
When running the Sales Tax Report for Accounts Receivable invoices, Spectrum will include invoice amounts only if the operator requesting the report has permission to access the cost center assigned to the A/R invoice. Spectrum compares the cost center assigned in the invoice header with cost centers in the operator's assigned scheme; if the invoice cost center is not included, then that invoice is not shown on the report. Because this report is based on cost centers assigned in the header portion of the invoice, it is possible that the report will include invoice information for invoices with detail assigned to cost centers that the operator is otherwise not permitted to access.
When running the Sales Tax Report for Order Processing invoices, Spectrum will include invoices with sales tax only if the operator requesting the report has permission to access the cost center assigned in the header of the Order Processing invoice. Spectrum compares the cost center assigned in the invoice with cost centers in the operator's assigned scheme; if the invoice cost center is not included, then that invoice is not included on the report. Because this report is based on cost centers assigned in the header portion of the invoice, it is possible that the report will include invoice information for invoices that the operator is not otherwise permitted to access.
