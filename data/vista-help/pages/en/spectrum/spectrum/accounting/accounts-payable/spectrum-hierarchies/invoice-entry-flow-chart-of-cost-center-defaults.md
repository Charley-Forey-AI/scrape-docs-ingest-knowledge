---
title: "Invoice Entry Flow Chart of Cost Center Defaults | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-hierarchies/invoice-entry-flow-chart-of-cost-center-defaults"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-hierarchies/invoice-entry-flow-chart-of-cost-center-defaults"
---

# Invoice Entry Flow Chart of Cost Center Defaults

The following are invoice entry workflows for Cost Center
 defaults.

## Header Cost Center Defaults

## Detail Area Cost Center Defaults

## Cost Center Information - Subcontract Invoices

If cost centers are enabled for the current company, use the cost center
 defined on the Subcontract Defaults screen. If this field is left
 blank, the default cost center from the Accounts Payable
 Installation screen will default instead.
When setting up a new subcontract, both you and the vendor must have access to
 the job's cost center. If you enter an override cost center in the
 Subcontracts Default screen, the vendor must have access to
 the entered cost center.

## Cost Center Information - Unapproved Invoices

If the cost center feature is enabled in the Enterprise
 Installation screen, the Cost center field appears just beneath the Remarks field to allow you to
 designate an invoice cost center (when applicable), even for job-specific invoices.
 Because this cost center is also used when selecting the invoice for payment, this field
 will allow editing for all invoices (rather than display-only for subcontract
 invoices).
Spectrum allows you to add an unapproved invoice for a vendor only if your operator has permission to access that vendor. Spectrum compares the vendor's list of shared cost centers with cost centers in the your assigned cost center scheme, and if there are no common cost centers, then invoice entry for that vendor will not be allowed.
If the invoice is "purchased with credit card," the credit card account to be assigned to the invoice must be compatible with the cost center already specified for the invoice.
Spectrum also compares the cost center assigned in the invoice with cost centers in your operator's assigned cost center scheme, and if the invoice cost center is not included, then access to that invoice is not allowed.

## Cost Center Information - Document Tracking Reports and Lien Releases

If cost centers are being used, when printing this report Spectrum compares the vendor's list of shared cost centers with cost centers in your operator's assigned cost center scheme, and if there are no common cost centers, then tracking information for that vendor will not be included on the report.
For subcontract tracking, Spectrum validates that the cost center assigned to the job is an authorized cost center for your operator. Spectrum compares the cost center assigned to the job with cost centers in your assigned cost center scheme, and if the job's cost center is not present, then subcontracts for that job will be omitted.
For lien releases, Spectrum also compares the cost center assigned to the payment cycle with cost centers in your assigned cost center scheme, and if there are no common cost centers, then lien releases for that payment are not included on the report.
