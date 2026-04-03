---
title: "Cash Receipts Journal - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal/cash-receipts-journal---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal/cash-receipts-journal---field-descriptions"
---

# Cash Receipts Journal - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field
Description

Batch
Enter the customer batch code for unposted cash receipts, or enter ALL to include all transactions regardless of batch assignment.

Customer
Enter the customer you want included on the report, or press Enter to print ALL.

G/L dates
Enter the first and last General Ledger dates to be included, or press Enter to begin with the earliest date and end with the current A/R processing date.

Pay-when-paid
The Subcontract Payment Worksheets will print immediately following the Cash
 Receipts Journal if the "pay-when-paid" checkboxes are selected on the AR > Installation screen. Click the My Reports buttons to select a custom
 report.
If these checkboxes are not selected on the installation screen, the field text will alert the Operator that these worksheets are not available, and the My Reports buttons will be disabled.

Cost group
When a cost group or cost center is specified in the cash receipts header, the report will show only invoices assigned to that cost group/cost center. An option is also provided to sort primarily by cost center. The Cash Receipts Journal shows the cost center associated with each transaction line on the report.
Spectrum will include transactions only if you have permission to access the cost center assigned to the payment/adjustment. Spectrum compares the cost center assigned in the transaction with cost centers in your assigned scheme; if the invoice cost center is not included, then that item is not shown on the report.
Spectrum will determine whether all distribution lines of the
 payment/adjustment are assigned to the same cost center as in the
 transaction header. If there are multiple cost centers, then Spectrum will
 create balancing debit and credit entries for cost center inter-posting;
 cost center inter-posting account information is defined in the Accounts
 Receivable Installation screen. When the Enterprise Installation  >  Allow G/L account
 overrides by cost center checkbox is selected, Spectrum will assign retention, deferred
 retention, and inter-posting amounts to alternate General Ledger accounts by
 cost center, based on a list of override G/L accounts in the respective Accounts Receivable Installation > Override windows.
