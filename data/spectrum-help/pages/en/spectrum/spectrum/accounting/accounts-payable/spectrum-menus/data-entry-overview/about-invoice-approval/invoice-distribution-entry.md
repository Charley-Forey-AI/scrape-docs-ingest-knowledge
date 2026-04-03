---
title: "Invoice Distribution Entry | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-distribution-entry"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-distribution-entry"
---

# Invoice Distribution Entry

Use this window to change invoice distribution by assigning or editing the phase and cost type, based on existing security authorization.
Changes to invoice approval security can be made in Operator Maintenance or Accounts Payable Installation.
On the Invoice Approval screen, select a record in the distribution portion of the screen and select the Assign Phases button.
The columns that display in this window are the same as those found in the [Vendor Invoice Entry](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry) grid. This window shows all rows on the invoice, although changes can only be made to direct job cost rows, and only to the Phase and Cost type columns. As in Vendor Invoice Entry, when entering a standard transaction, the originator can leave the phase and cost type fields blank to indicate 'unclassified'. This allows the first reviewer to code job costs prior to approval and further routing.
If this is a sub-job transaction set up on a master job, double-click on this field to search phases for the sub-job. This makes it easy to select a phase set up on a master job, but not present on the sub-job.
Spectrum will add a new phase to the sub job if all these conditions apply:

- the current job is a sub-job of a valid master job

- the phase lengths of both jobs match

- the Phase + Cost type combination for the current job is valid and not 'Complete'

When the Cost type on the distribution row is edited, you can also reset the G/L account. All validations offered in Vendor Invoice Entry for the G/L account are provided including status restrictions, cost type/G/L account restrictions in General Ledger, cost type/G/L account restrictions in Job cost, department/division restrictions and cost center restrictions. When multiple qualifying G/L accounts are present, the software displays a simple window that allows you to select the desired code.
When edits are made in this window, it is possible that the Tax Classification sales and use tax codes may be reset (due to phase changes). In this case, the application automatically allocates tax as it does in Vendor Invoice Entry.
