---
title: "A/P Transaction Register | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-transaction-register"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-transaction-register"
---

# A/P Transaction Register

The A/P Transaction Register prints
 a list of invoices and credit memos recorded in A/P Vendor Invoice Entry since the last
 update. It is followed by the A/P Transaction
 Update screen, providing the option to update the items included on the
 register. During the PO Receiving step, the register will display the previously accrued
 amount and the true-up amount for job PO costs. If the PO contains multiple rows, the true-up
 amount will be the summation of all rows.
There are many report variations, all of which include drill-down functionality for Document Imaging attachments.

- If the multi-company feature is being used, the report will screen break between each company.

- If the Post Detail checkbox is selected in Job Cost > Cost Type File
 Maintenance screen, the job cost history records will be updated with one history
 record per distribution line. For example, if an invoice contained multiple lines on
 the same job, phase, and cost type, each distribution line will be separated out in
 history rather than being summarized into one history record. If the cost type being
 posted is not set for detail posting, then one history record will be created per
 invoice per job, phase and cost type.

- If you attempt to update while another user is "in progress," the software displays the operator ID performing the update. You must wait until the operator shown has completed use of the screen before proceeding.

Spectrum validates the transaction details during this report/update's
 compilation process. If an error is found during the compilation, the [G/L Error Correction](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/gl-error-correction) screen
 automatically displays, allowing you to enter the necessary changes. Once you close the
 G/L Error Correction screen, Spectrum will recompile the data and
 apply the corrections; the report will reprint automatically.
When a related-party vendor is entered, the override retention payable
 G/L account will default in the A/P retention field. If left blank,
 the G/L account from the General Ledger
 Installation screen will default.
Note: If you cancel out of the A/P Transaction
 Report/Update screen before completing the update, the changes made in the
 G/L Error Correction screen will not be saved to the A/P G/L
 distribution history file.
Important: This report should be retained as a permanent
 audit record of the company.

Related information

- [A/P Batch Won't Print or Update](/en/spectrum/spectrum/accounting/accounts-payable/troubleshooting/ap-batch-wont-print-or-update)
