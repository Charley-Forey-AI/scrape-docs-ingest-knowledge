---
title: "Approval Limits | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/approval-limits"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/approval-limits"
---

# Approval Limits

You can assign approval limits to all of a Routing Code's reviewers to excuse certain reviewers in that Routing Code from having to review and approve the invoice.
Based on each reviewer's assigned approval limit, the system determines who does and does not need to review the invoice. Reviewers are skipped when the invoice amount is less than or equal to an earlier reviewer's approval limit.
In determining which reviewers are to be exempted from reviewing an invoice, the system compares each reviewer's approval limit to the value in the Total amount field of the invoice. The system doesn't route invoices to later reviewers on those instances where an earlier reviewer has approved an invoice whose amount is under their approval limit.
If you want to assign Approval Limits to your existing Routing Codes, see [Edit an Unapproved Invoice Routing Code](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/edit-an-unapproved-invoice-routing-code). Changes you make will take effect on all subsequently entered invoices.

## Approval Limit Setup

Set approval limits in the Edit Routing Code window using these guidelines.

- If you assign an Approval limit to any one reviewer, then you must assign one to all reviewers in the same Routing Code. You may delete rows which don’t have an Approval limit, but you cannot leave the field blank.

- Each reviewer's approval limit amount must be equal to or higher than the limit amount entered for a previous reviewer.

- Any one reviewer cannot appear in the routing grid more than once.

- To grant a reviewer authority to approve invoices of any amount, enter 999,999,999.99 as the Amount limit.

- The system prevents entry of negative numbers in the Amount limit field.

- For Routing Codes with Approval Limits, the Edit button is disabled in the Invoice Approval Routing History Inquiry window.
