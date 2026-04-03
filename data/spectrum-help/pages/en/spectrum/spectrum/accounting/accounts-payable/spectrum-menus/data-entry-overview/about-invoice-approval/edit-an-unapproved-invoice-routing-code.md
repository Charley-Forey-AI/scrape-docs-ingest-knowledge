---
title: "Edit an Unapproved Invoice Routing Code | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/edit-an-unapproved-invoice-routing-code"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/edit-an-unapproved-invoice-routing-code"
---

# Edit an Unapproved Invoice Routing Code

You may need to occasionally alter a Routing Code by adding or removing a person in the routing sequence on an unapproved invoice.

- You must be assigned security level 3 (Job/Routing changes allowed) in order to use this procedure.

- Changes you make to Routing Codes affect only invoices created after your changes are made, not those that already exist.

To edit a Routing Code:

1. Navigate to Accounts Payable > Maintenance > Invoice Approval Routing.

1. Select Go.All existing Routing Codes appear in the grid.

1. Highlight the Routing code that you want to change and select Edit.The Edit Routing Code window opens.

1. Make the desired changes. If needed, see [New/Edit Routing Code - Field Descriptions](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/invoice-approval-routing-maintenance/newedit-routing-code---field-descriptions).

- Confirmation - This reviewer receives the invoice after all reviewers have approved it.Note: When [Approval Limits](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/approval-limits) are assigned, some reviewers may be exempted from having to review/approve the invoice. If this has happened, the confirming reviewer receives the invoice once it's been approved by all *required* reviewers.

- New - add a new reviewer in a new row.

- Insert - replace the currently selected reviewer with a different reviewer.

- Delete - remove the currently selected reviewer.

- Approval limit - if using Approval Limits, enter this reviewer's maximum approval amount. If all reviewers appearing in the grid should view and approve all invoices routed to this Routing Code, leave this field blank.Note:If using Approval Limits

- The amount in question is the Total amount, which includes Sales tax and VAT.

- Invoices amounts above this limit must be approved also by a reviewer with a higher limit.

- Invoice amounts lower than this limit will skip reviewers with higher limits.

- E-mail - Select if the reviewer should receive an email when the invoice is approved by all prior required reviewers.

1. Select OK to save your changes.
