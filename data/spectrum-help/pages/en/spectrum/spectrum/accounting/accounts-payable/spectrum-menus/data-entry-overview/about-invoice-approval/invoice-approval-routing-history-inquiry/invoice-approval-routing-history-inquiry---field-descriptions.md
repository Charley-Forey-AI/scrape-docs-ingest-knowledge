---
title: "Invoice Approval Routing History Inquiry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-approval-routing-history-inquiry/invoice-approval-routing-history-inquiry---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-approval-routing-history-inquiry/invoice-approval-routing-history-inquiry---field-descriptions"
---

# Invoice Approval Routing History Inquiry - Field Descriptions

A reference for using this screen.
Fields/ButtonsDescriptions
Edit (button)Select to make changes to a routing schedule which does not use Approval Limits.Note: If the Routing Code has Approval Limits assigned, the system prevents any changes.

StatusThe status of the invoice, from the perspective of the reviewer currently assigned to the invoice.

- Rejected invoices are routed back to the Originator.

- A reviewer could appear more than once in the grid if they first rejected it and later approved it.

- A reviewer can choose to set the status but not send it to the next reviewer.

ReviewerThe past and future assigned reviewers.
If Approval Limits exist:

- For an invoice not yet confirmed, a Routing Code which uses Approval Limits indicates which, if any, reviewers are to be skipped, based on the invoice Total amount.

- Each skipped reviewer is deleted from the approval history at the moment the invoice gets confirmed.

CodeThe reviewer's operator identification code displays.
NameThe reviewer's name displays based on the name that appears in Operator Maintenance for the assigned reviewer ID shown. If another operator performed the review on his/her behalf, that operator ID is shown in parenthesis.
Approval limitView only. Displays the reviewer schedule, and indicates which reviewers, if any, are to be skipped in the review cycle.If values appear, the invoice must be approved by all reviewers whose approval limit is equal to or below the invoice Total amount.
If no values appear, all reviewers in the grid must approve the invoice, regardless of the invoice amount.
If you need to make changes to the routing code, see [Edit an Unapproved Invoice Routing Code](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/edit-an-unapproved-invoice-routing-code).

DateThe date and time the reviewer completed their review.If the Routing Code uses Approval Limits, one or more reviewers may be flagged for being exempted. For invoices already confirmed, the system removes exempted reviewers from the history.

Time
New (button)Select to open the New Invoice Routing Note window.
CodeThe reviewer's operator identification code displays.
Routing notesRouting notes display, in order from oldest to newest.
