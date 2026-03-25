---
title: "GL Statement of Cash Flow | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-general-reports/gl-statement-of-cash-flow"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-general-reports/gl-statement-of-cash-flow"
---

# GL Statement of Cash Flow

You can use the GL Statement of Cash Flow report by
 selecting General Ledger > Reports > GL Statement of Cash Flow.
Accounts are selected for this Cash Flow report when one of the two following conditions are met:

- The account is assigned to a Minor Category that has Cash Flow Statement Order filled in.

- The account is assigned to a Major Category that has Income Statement Order filled in (these accounts appear in the first group "Cash Flow from Operating Activities").

The Cash Flow statement groups accounts into the following categories:
Cash Flow from Operating Activities - Any accounts assigned to a Major Category with Income Statement Order filled in, or any accounts assigned to a Minor Category with Cash Flow Statement Order filled in with a value between 100-199.
Adjustments to Reconcile to Net Income to Net Cash Flow - Any accounts assigned to a Minor Category with Cash Flow Statement Order filled in with a value between 200-299.
Decrease (Increase) in Current Assets - Any accounts assigned to a Minor Category with Cash Flow Statement Order filled in with a value between 300-399.
Increase (Decrease) in Current Liabilities - Any accounts assigned to a Minor Category with Cash Flow Statement Order filled in with a value between 400-499.
Cash Flow from Investing Activities - Any accounts assigned to a Minor Category with Cash Flow Statement Order filled in with a value between 500-599.
Cash Flow from Financing Activities - Any accounts assigned to a Minor Category with Cash Flow Statement Order filled in with a value between 600-699.
This report ignores the Cash Flow Statement Order value on the Major Category. Minor Categories are required for the Cash Flow Statement for all accounts other than the Income Statement accounts.
This report excludes Header and Memo type accounts.
The groups on this report can be customized by updating the "Major Group Name" formula in the Crystal report.
The report will round an amount to the nearest whole dollar. Because of this, discrepancies may appear between the amounts displayed and their calculated totals.
More information for setting up GL Account Parts for the Statement of Cash Flow can be found under the GL help topic for Major Categories.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Through Month
Enter through month (MM/YY).
