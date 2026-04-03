---
title: "Sales Journal / Update - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/sales-journal--update/sales-journal--update---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/sales-journal--update/sales-journal--update---field-descriptions"
---

# Sales Journal / Update - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field
Description

Customer
Enter the customer you want to include on this report, or press Enter to print ALL.

Job
Enter the job you want to include on this report, or press Enter to print ALL.

Batch
Enter the batch code, or press Enter to accept the operator code that defaults.

Invoice
Enter the invoice number to include on this report, or press Enter to print ALL.

G/L date
Enter the first and last General Ledger dates you want to include on this report, or press Enter to begin with the earliest date in the software and end with the current Accounts Receivable processing date.

Cost Center information
If the cost center feature is enabled in the Enterprise Installation screen, this screen includes the Cost group field. When a cost group or cost center is specified, then the report will show only invoices and credit memos assigned to cost centers in that group. When the operator specifies a cost center on the starting screen, Spectrum verifies that the operator has permission to access that cost center's information before proceeding.
The Sales Journal will include invoices only if the operator requesting the report has permission to access the associated cost center. The cost center used for comparison purposes with the operator's allowed codes is the cost center recorded on the main screen of Invoice Entry.
The Sales Journal includes the cost center assignment for each detail line.
Spectrum will determine whether all distribution lines of the invoice are
 assigned to the same cost center as in the invoice header. If there are
 multiple cost centers, then Spectrum will create balancing debit and credit
 entries for cost center inter-posting; cost center inter-posting account
 information is defined in the Accounts Receivable Installation screen. When
 cost centers are used and the Allow G/L account overrides by cost center
 checkbox is selected on the Enterprise Installation screen, Spectrum will
 assign inter-posting amounts to multiple General Ledger accounts, by cost
 center based on the list of override G/L accounts in the Accounts Receivable Installation > Inter-posting Overrides window.
