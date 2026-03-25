---
title: "GL Trial Balance Drilldown | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-general-reports/gl-trial-balance-drilldown"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-general-reports/gl-trial-balance-drilldown"
---

# GL Trial Balance Drilldown

You can use the GL Trial Balance Drilldown report by
 selecting General Ledger > Reports > GL Trial Balance Drilldown.
This drilldown report is similar to the GL Trial Balance report.
Required inputs are Company, Beginning Month, and Ending Month. Optional inputs are Beginning Account and Ending Account; Source Modules to include (one or more, comma-separated, or blank for all); Journal to include (one only, or blank for all); and flags to indicate whether to include year-end adjustments or inactive accounts, or to show zero balances.
Level 1 of the drilldown displays summary amounts by GL Account for the specified time period, including beginning balance, net activity (debit or credit) over the period, and ending balance.
Upon drilling into a specific GL Account, Level 2 displays summary amounts by month within the time period.
Upon drilling into a specific month, Level 3 presents that month's data by Journal and GL Reference, including the sum of debits and sum of credits for each GL Reference. The Journal sub-report, accessible at Level 3, displays all journal activity for the GL Reference, across all affected accounts.
Upon drilling into a specific GL Reference, Level 4 shows each GL transaction within that GL Reference (Batch ID), including the amount (debit or credit) of the transaction. Source detail for an individual GL transaction, when available, is displayed in the Source Detail sub-report, accessible at Level 4.
Note that the report is intended to be run for months that fall within a single fiscal year. If the inputs that you supply for Beginning Month and Ending Month fall within different fiscal years, the report displays a warning message, and may show inaccurate amounts for beginning balance and ending balance, particularly for income or expense accounts (which start each new fiscal year with a beginning balance of zero). The fiscal year that includes the Beginning Month input is used for purposes of calculating beginning balance amounts.
Note also that if you restrict the results to specific Source Modules or a specific Journal, the report does not print beginning balance amounts for accounts.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Beginning Account
Enter or press F4 to select a beginning GL account.

Ending Account
Enter or press F4 to select an ending GL account.

Beginning Month (Must be same Fiscal Year as Ending Month)
Enter beginning month (MM/YY).

Ending Month (Required)
Enter ending month (MM/YY).

Sources (AP, AR, etc.) Blank for All – n/a for (A)ccount
Enter source module(s) (separated by commas). Leave blank for all. This option is not available if printing by (A)ccount.

Journal (Blank for All) – n/a for (A)ccount
Click the Field Lookup
 button or press F4 to select journal. Leave blank for all. This
 option is not available if printing by (A)ccount.

Include Year End Adjustments?
Check this box to include year end adjustments. Leave unchecked to exclude year end adjustments.

Ending Balance By Month?
Check this box to show ending balance by month. Not applicable if printing by (A)ccount.

Include Inactive?
Check this box to include inactive accounts. Leave unchecked to exclude inactive accounts.

Show Zero Balances?
Check this box to include all accounts, including those with a zero balance. Leave unchecked to exclude accounts with a zero balance.
