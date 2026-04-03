---
title: "Bad-Debt Procedures | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/procedures-overview/bad-debt-procedures"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/procedures-overview/bad-debt-procedures"
---

# Bad-Debt Procedures

One-time steps:

- Set up a General Ledger account titled Bad Debt Expense in G/L Master File Maintenance.

- Set up a bad-debt transaction code in Transaction CodeFile Maintenance. The G/L account # should be the Bad Debt Expense account set up above. The G/L discount taken # should be your standard discounts account (this is required input but will not be used for bad debts). The A/R G/L account # should be the Accounts Receivable account.

When an invoice is not collectable:

- Make an adjusting entry for the amount of the invoice using Cash Receipts/Adjustment Entry. Use the bad debt transaction code, which was set up above. In the line transaction portion of the screen, position the cursor at the Discount field on the line to be written off as bad debt, and press Enter. At the Paid/adjusted field, type the invoice amount.

- Update the Cash Receipts Journal.
