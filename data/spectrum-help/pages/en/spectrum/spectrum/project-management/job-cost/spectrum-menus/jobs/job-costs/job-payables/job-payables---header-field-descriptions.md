---
title: "Job Payables - Header Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-costs/job-payables/job-payables---header-field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-costs/job-payables/job-payables---header-field-descriptions"
---

# Job Payables - Header Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Total current payables
This is the total non-retention amounts for the current job that use the pay-when-paid terms. While it excludes credit memos, it includes open, unapproved and unposted invoices.

Total unreleased
This amount is a subset of 'Total current payables'. This represents the sum of all invoices that do not have a payment status of 'Released.'

Invoice button
Depending on where it is in the process, this button will open the highlighted vendor invoice:

-  Unposted or Unapproved: Displays in a new Spectrum tab.

- Posted: Displays in the Vendor Invoice Inquiry window.

Release button
Use the Release button to manually release the invoice for payment. Only vendor invoices with a 'Release' status may be selected for payment in Accounts Payable.
Clicking this button will store the operator code and date in the Pay-When-Paid Release Note window. Also, the 'Pay-when-paid?' checkbox is cleared on the invoice and the 'Payment due' date is set to the current date. Only the first operator and release date are stored.

Review button
Use this button to override the Payment Status of the invoice. Setting it to 'Flagged for review' indicates that the decision to release the invoice has not yet been made, yet some customer cash has been received.
The operator code and date that was stored in the Pay-When-Paid Release Note window are cleared when this status is used.

Waiting button
Click to set the Payment Status to 'Waiting for payment'. This is useful when an invoice is moved forward in the process in error and needs to be pushed back.
Any operator code and date that was stored in the Pay-When-Paid Release Note window are also cleared.
Note: If the transaction is currently selected for payment, the status cannot be switched.

Note button
Click to open the Pay-When-Paid Release Note window. The operator who released the invoice and the date is also stored here. When system-released, the invoice will state 'Auto-released during Cash Receipt Update.'
Note: This window allows release note and other 'payment' entries only while it is an open item.

Refresh button
Click to update the pay-when-paid policy and the totals on the screen.

Status button
Click to change the status filters to include items:

- Flagged for review

- Waiting for payment

- Released
