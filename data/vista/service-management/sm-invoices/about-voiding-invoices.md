---
title: "About Voiding Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/about-voiding-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/about-voiding-invoices"
---

# About Voiding Invoices

You can use the Void Invoice option in SM Invoice Review and
 SM Agreement Invoice Review (File menu) to void invoices that you have already processed
 (i.e. sent to AR).
When you void an invoice, the system flags the invoice as 'Deleted' and
 reverses the invoiced amount in AR. Depending on the invoice type (work order or
 agreement), additional updates may occur.Note: Once you void an invoice, it cannot be
 undone.

## Work Order Invoices

When you void a work order invoice (those not associated with an agreement), the
 system reopens the work completed lines so they are available for billing later.
 Although the invoice will no longer display on the Invoices grid in any of the
 related forms (SM Customers, SM Service Sites, or SM Work Orders), it will still be
 included on certain reports (e.g. AR Invoice Detail, AR Invoice Listing, AR Customer
 Drilldown, etc.) with 0.00 values.

## Agreement Invoices

When you void an agreement invoice, the system reopens the agreement billing so it
 can be re-invoiced later. The invoice will continue to display in SM Invoices;
 however, the invoice amount and last printed date is cleared. The invoice will also
 display in SM Customers with a status of "Voided" and the Total Billed, Total Taxed,
 and Total Amount fields set to 0.00.
If you void an invoice that is associated with an agreement revision that is
 terminated due to an amendment, the billing and amortization schedules are removed
 from the terminated revision and a new billing and revenue recognition schedule
 created for each later revision for the same major version (does not apply to
 terminated revisions).
For example:
Version 1.0 - Scheduled Billing 1/1/19 for $1,000 is invoiced
Version 1.1 amendment is created and activated. It does not include the billing
 schedule for 1/1/19
Version 1.2 amendment is created and activated. It does not include the billing
 schedule for 1/1/19
Version 1.3 amendment is created but left in Quote status. It does not include the
 billing schedule for 1/1/19
Version 2.0 renewal is created by renewing the agreement.
You then void the $1,000 invoice for the 1/1/19 billing
The billing schedule and a revenue recognition for $1,000 shows as ready to bill for
 Version 1.2.
Version 1.1 was terminated, so it does not show the billing schedule and
 revenue recognition for $1,000
The system also creates a billing schedule and revenue recognition for the Version
 1.3 quote.
No changes are made to the Version 2.0 agreement.

Related tasks

- [Void an SM Invoice](/en/vista/vista/service-management/sm-invoices/about-voiding-invoices/void-an-sm-invoice)
