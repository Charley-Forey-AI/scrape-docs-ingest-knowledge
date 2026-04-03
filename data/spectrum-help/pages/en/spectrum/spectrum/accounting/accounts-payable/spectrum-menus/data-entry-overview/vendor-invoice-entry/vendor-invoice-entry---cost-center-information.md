---
title: "Vendor Invoice Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/vendor-invoice-entry---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/vendor-invoice-entry---cost-center-information"
---

# Vendor Invoice Entry - Cost Center Information

If the cost center feature is enabled in the Enterprise
 Installation screen, the Cost center
 field displays just beneath the Remarks field to allow you to designate an invoice cost center (when
 applicable), even for job-specific invoices.
Because this cost center is also used when selecting the
 invoice for payment, this field will allow editing for all invoices (rather than
 display-only for subcontract invoices).The following hierarchy is
 used to determine the cost center in the invoice header when a subcontract is not
 specified:

1. The specified cost center is used if only one cost
 center is defined for this operator.

1. The specified cost center is used if only one cost
 center is defined for the vendor.

1. The last cost center entered for the current
 session.

[Invoice Entry Flow Chart of Cost Center Defaults](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-hierarchies/invoice-entry-flow-chart-of-cost-center-defaults).
Spectrum performs a series of cost
 center validations during entry:

- Spectrum allows your operator to add an invoice for a vendor
 only if you have permission to access that vendor. The software compares the vendor's
 list of shared cost centers with cost centers in your assigned cost center scheme,
 and if there are no common cost centers, then invoice entry for that vendor is not
 allowed.

- Also, when the Cash Management module is present, the bank
 account for any pre-paid checks must be compatible with the cost center of the
 invoice. If the invoice is "purchased with credit card," the credit card account must
 be compatible with the cost center already specified in the invoice header.

- When the Cash Management module is NOT present, the G/L account
 for the pre-paid check must be compatible with the cost center of the invoice.

When the operator changes the work order in the A/P Invoice
 Detail window, the software will automatically adjust the cost center assigned to the
 distribution line. Entry of a new work order will be disallowed if the Operator does not
 have permission for the new cost center.
