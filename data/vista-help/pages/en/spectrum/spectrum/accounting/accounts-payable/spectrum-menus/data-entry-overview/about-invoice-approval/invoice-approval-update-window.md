---
title: "Invoice Approval Update window | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-approval-update-window"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-approval-update-window"
---

# Invoice Approval Update window

Use this window to set the status for this invoice, and to send the
 invoice to the next reviewing operator.

- If you want to accept the defaults as they appear and to close the window, press
 Enter.

- When confirming invoices, Spectrum evaluates whether the each invoice was
 purchased with a credit card; if it was, the software stores the G/L date from the
 Invoice Approval confirmation window as the credit card
 transaction date. The transaction date is automatically set to the G/L date assigned
 during confirmation when using Invoice Approval.

FieldsDescriptions
VendorThe vendor code and name displays.
Entry typeThe entry type displays (invoice or credit memo).
Invoice no.The invoice number displays.
Reviewer 2The operator ID and name for the next reviewer displays. The prompt text also
 indicates the reviewer number in the routing queue; for example, "Reviewer
 2."
StatusThe status of the invoice displays based on the button you selected on the
 Invoice Approval screen.Example of how the Invoice Approval status works:

1. Reviewer #1 'Approves' the invoice.

1. Now it is in Reviewer #2's queue. The status is 'Unapproved' because this reviewer (#2) needs to do something. To have arrived at this condition, it is implied that reviewer #1 has Approved it (or it would not be here).

1. If Reviewer #2 'Approves' this invoice and sends it along to the next reviewer, it will be 'Unapproved' yet again because Reviewer #3 has yet to review the invoice.

1. If instead of approving the invoice, Reviewer #2 rejects it, the invoice will reappear in Reviewer #1's queue and will be 'Unapproved' because this reviewer has to perform some new action.

1. If an invoice is 'Rejected' all the way back to the originator, the status will say 'Rejected' right when it arrives.In all cases, an operator can choose to set the status but not send it along to the next reviewer. In this case, the reviewer has still performed an action and the software saves this new information.

Complete reviewSelect one of the following options to complete the review:

- Review is complete. Send to next operator.

- Review pending. Set current status but do not send.
