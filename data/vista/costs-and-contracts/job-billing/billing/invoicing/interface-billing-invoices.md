---
title: "Interface Billing Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/interface-billing-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/interface-billing-invoices"
---

# Interface Billing Invoices

Using the JB Interface form, you can interface, change, and
 re-interface invoices to AR and to update the billing amounts in GL and JC.
The GL Close form does not allow a month to close if there are any
 invoices that require interfacing for the month. If you have permissions, you can
 change and re-interface billings that are in a closed month. However, closed month
 billings must re-interface to a month that is open in both JC and AR.
Because the Batch Selection form in JB Interface automatically
 defaults the closed month, you must change the batch month to an open month before
 interfacing. For more information about changing closed-month billings, see [About Changing Interfaced or Closed-Month Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-changing-interfaced-or-closed-month-billings).
On the JB Interface form, the grid on
 the Interface tab displays invoices that require interfacing. Use the grid filtering
 options to view and select invoices to interface.
The status column in the invoice grid displays the status for each invoice. Valid
 status codes include:

- A: Active invoice


- C: Previously
 interfaced invoice with changes

- D: Previously
 interfaced invoice marked for deletion

Note: Changing the notes on an invoice causes the transaction
 status to become C-Change and display on the grid.
 Re-interface the invoice to update the changes.

1. From the JB Interface
 form, enter a bill month to restrict interfacing to in the Bill
 Month field.

1. Optional: Check the Restrict by
 Process Group box to display a specific process group’s
 invoices. Enter the process group in the Process Group field.

1. Optional: Check the Include
 Billings with Blank Invoice Numbers box to see all invoices
 (both T&M and Progress) without an assigned invoice number. This is useful
 for tracking non-interfaced billings, which cause errors when trying to close a
 month in GL (due to missing invoice numbers). While this box is checked, the
 system disables the Post button as well as the Interface checkbox for each item in the grid.

1. Check the Interface box for each invoice in the grid that you want to
 interface. You can also check the Interface all bills box to
 automatically check the Interface box for all
 invoices in the grid.

1. Select Post. The Batch Selection form
 opens.

1. Create a new batch with
 the appropriate batch month and process the batch as normal. All the invoices
 that you selected no longer display in the grid. Note: The Batch Selection form automatically
 defaults the month of the interfacing batch. If you are interfacing billings
 from a closed month, change the default month to an open month (must be open
 in both JC and AR). Otherwise, an error will display. For more information
 about changing closed-month bills, see [About Changing Interfaced or Closed-Month Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-changing-interfaced-or-closed-month-billings).

For more information about the JB Interface form, see [JB Interface Form](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-interface-form#ID-00014dd7--en__ID-00014dd7).
