---
title: "Print Draw Request Billing - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/print-draw-request-billing/print-draw-request-billing---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/print-draw-request-billing/print-draw-request-billing---cost-center-information"
---

# Print Draw Request Billing - Cost Center Information

When the Enterprise InstallationUse cost centers option is set to Yes for this
 company, then the Print Draw Request Billing starting screen includes a
 selection for a cost group. When a cost group or cost center is specified, then the report
 will show only invoices assigned to that cost group/cost center. An option is also provided to
 sort primarily by cost center.
When the operator specifies a cost center on the starting screen, the software verifies the operator has permission to access that cost center before proceeding.
When printing the Draw Billing Worksheet, Spectrum will include the job only if the operator has permission to access the job. Spectrum compares the cost center assigned to the job with cost centers in the operator's assigned scheme; if the cost center is not included, then that job will not be shown.
When the operator's scheme includes override settings for 'Job' entries in
 Cost Center Scheme Maintenance, this report will validate the
 cost center assigned to the job based on these overrides. The override cost center(s)
 supersede the cost center list defined for the scheme in general. Spectrum will compare
 the cost center assigned to the job with 'Job' override cost centers in the operator's
 assigned scheme; if the cost center is not included, then the job will not be shown on
 the report.
Spectrum will also verify that the operator requesting the report has permission to access the contract. Spectrum compares the contract's assigned cost center with cost centers in the operator's assigned scheme; if the cost center is not present, then quantity transactions for that contract will not be included.
When the operator's scheme includes override settings for 'Contract' entries
 in Cost Center Scheme Maintenance, this report will validate the
 cost center assigned to the contract based on these overrides. The override cost
 center(s) supersede the cost center list defined for the scheme in general. Spectrum
 will compare the cost center assigned to the contract with 'Contract' override cost
 centers in the operator's assigned scheme; if the cost center is not included, then that
 contract will not be shown on the report.
When the operator is authorized to access the job and contract, all billing items for that contract are included on the report, including ones for disallowed cost centers.
