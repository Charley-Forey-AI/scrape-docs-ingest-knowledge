---
title: "About SM Work Order Lines on AP Invoices / Unapproved Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-sm-work-order-lines-on-ap-invoices--unapproved-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-sm-work-order-lines-on-ap-invoices--unapproved-invoices"
---

# About SM Work Order Lines on AP Invoices / Unapproved Invoices

You can associate AP invoice lines with an SM work order/item and have them generate work completed miscellaneous lines in SM Work Orders.

When you enter an invoice or unapproved invoice line that you want posted to an SM work order, use line type 8-SM Work Order. Once you post the invoice via AP Transaction Entry or AP Unapproved Invoice Posting (unapproved invoices), the system generates a work completed Misc line in SM Work Orders.
Note: Work order scopes referenced on a detail line must be assigned a call type, rate template, and/or phase (if a job work order) in SM Work Orders. If you enter a scope that is missing one or more of these values, you will be unable to post the invoice until the specified information is entered for the work order scope in SM Work Orders.Additionally, the work order scope must be open. If it is closed, you will be unable to post the invoice unless you reopen the scope or use a different (open) scope.

You can view the generated work completed Misc lines using the Work Completed grid or via the SM Work Completed Misc form (accessed from the SM Work Orders toolbar by selecting Work Competed > Miscellaneous).
For each invoice line, the Units, UC, and Gross values for the invoice line will become the cost values (Cost Qty, Cost UC and Cost Subtotal. If you entered taxes on the invoice line, those values become the Cost Tax Type, Cost Tax Code, Cost Tax Basis, and Cost Tax Amt. If you entered a Misc Amt, that amount is included in the work completed Misc line as follows:

- If you selected the Included checkbox for the invoice line, the resulting Misc work completed line includes the Misc Amt in the Cost UC, Cost Subtotal, Cost Rate, and Total Actual Cost amounts.

- If you did not select the Included checkbox, the resulting Misc work completed line excludes the Misc Amt from the Cost Rate and Total Actual Cost amounts; however, it does include the Misc Amt in the work completed line's Cost UC and Cost Subtotal amounts.

If you specify a job-related work order and the job associated with the work order has been soft or hard-closed, you are allowed to save the record, regardless of whether you allow posting to closed jobs. However, if you do not allow posting to soft or hard-closed jobs (that is, the Allow Posting to Hard-Closed Jobs and/or Allow Posting to Soft-Closed Jobs checkboxes are not selected in the JC Company Parameters form), you will be unable to post the invoice.
