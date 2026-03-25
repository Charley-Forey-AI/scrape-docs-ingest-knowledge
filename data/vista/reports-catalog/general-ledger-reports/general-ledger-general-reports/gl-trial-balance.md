---
title: "GL Trial Balance | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-general-reports/gl-trial-balance"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-general-reports/gl-trial-balance"
---

# GL Trial Balance

You can use the GL Trial Balance report by selecting
 General Ledger > Reports > GL Trial Balance.
The GL Trial Balance has inputs for Beginning and Ending Month and Beginning and Ending Account, sources to print (Sources are 2 characters separated by a comma, example AP,CM,JC), and whether to include year-end adjustments. It can be run in a detail format giving one line each time the month and transaction number change, a more summarized level, one line each time the GL Reference number changes, or one line per GL Account. When the report is run in detail format, a subtotal can be printed by month. This report runs from a stored procedure, "brptGLFinDet". If choosing to run the report by Account, you cannot further restrict by entering either Sources or Journals. When defining Sources, the report will not print a value for beginning balance for the account. If balances are entered using the program Prior Year Balances, the report must be run by 'A' Account level to get correct ending balances.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

(D)etail, (R)eference, (A)ccount
Enter D, R, or A.

Beginning Account
Enter or press F4 to select a beginning GL account.

Ending Account
Enter or press F4 to select an ending GL account.

Beginning Month (Must be same Fiscal Year as Ending Month)
Enter beginning month (MM/YY).

Ending Month (Required)
Enter ending month (MM/YY).

Sources (AP, AR etc.) Blank for All – n/a for (A)ccount
Enter source module(s) (separated by commas). Leave blank for all. This option is not available if printing by (A)ccount.

Journal (Blank for All) – n/a for (A)ccount
Click the Field Lookup
 button or press F4 to select journal. Leave blank for all. This
 option is not available if printing by (A)ccount.

Include Year End Adjustments?
Check this box to include year end adjustments. Leave unchecked to exclude year end adjustments.

Ending Balance By Month?
Check this box to show ending balance by month. Not applicable if printing by (A)ccount.

Show Zero Balances?
Check this box to include all accounts, including those with a zero balance. Leave unchecked to exclude accounts with a zero balance.
