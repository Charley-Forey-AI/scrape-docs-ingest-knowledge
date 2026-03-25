---
title: "Check the Status of AP Invoices in the Approval Workflow | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/check-the-status-of-ap-invoices-in-the-approval-workflow"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/check-the-status-of-ap-invoices-in-the-approval-workflow"
---

# Check the Status of AP Invoices in the Approval Workflow

 Use the AP Unapproved Invoice Status form to select the types of invoices you want to review, by approval status.
The system uses a set of rules to determine which reviewer group's responsible person should see which invoices in the AP Unapproved Invoice Status form. If a reviewer group is assigned at the line level:

- the system displays the line status to that group's responsible person

- the responsible person of the header-level group will not see the invoice status on this form.

To review the approval status for invoices:

1. Enter the desired criteria in the Responsible Person, Reviewer, Reviewer Group, and/or Vendor fields (or by selecting from lists by pressing F4) to filter your search.Note: Only Reviewers and Reviewer Groups with an "Active" status in HQ Reviewers and/or HQ Reviewer Group can be added to either the Reviewer or Reviewer Group fields.

1. Select at least one additional filtering option from each of the Review Status and Invoice Status groups boxes:

- Show Rejected - to include rejected invoice lines in the grid. These rows appear with a red background.

- Show Unapproved - to include invoice lines without any approval or rejection action taken.

- Show Approved - to display all approved invoice lines in the grid. These rows appear with a blue background.

- Show Ready - to display all invoice lines that AP clerks have marked as ready for review to make them visible to their assigned reviewer(s).

- Show Not Ready - to display all invoice lines that AP clerks have not marked as ready for review; these are not visible to their assigned reviewer(s).

1. Click Refresh Grid to display all invoices that meet your filtering criteria.

1. If you want to view additional details associated with an invoice, and have security access to the AP Unapproved Invoice Entry form, highlight the invoice in the grid and click Invoice Setup. From here, you can view the invoice/lines or make any necessary changes. Note:When you select an invoice line in the grid, the system displays the invoice total in the Invoice Total display field. The Line display field shows information based on the line type:

- Job - job/phase/job cost type

- Equipment - equipment description/EM cost type, and EM cost code

- Inventory - inventory location/material

- Expense – material

- PO - purchase order/item number

- SL - subcontract order/item number/job/phase/cost type

1. If you want to email the reviewer about an invoice, select the appropriate line and click Email. Your email client will display with a message addressed to the email address associated with the reviewer in the VA User Profile form. The Subject line will default information about the invoice and the specific line.

1. If necessary, use the Reviewer Memo field to add notes to the reviewer record.

1. If an unapproved invoice is ready for posting, select File  >  Unapproved Invoice Post. The AP Unapproved Invoices Posting form is used to post unapproved invoices. For more information, see [Posting Approved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/posting-approved-invoices). Note: When you access AP Unapproved Invoice Posting this way, the system automatically selects the Restrict by Responsible Person checkbox and enters the responsible person’s ID in the Responsible Person field.
