---
title: "GL Trial Balance By Profit Center | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-general-reports/gl-trial-balance-by-profit-center"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-general-reports/gl-trial-balance-by-profit-center"
---

# GL Trial Balance By Profit Center

You can use the GL Trial Balance By Profit Center report
 by selecting General Ledger > Reports > GL Trial Balance By Profit
 Center.
The GL Trial Balance by Profit Center has inputs for Beginning and Ending Month and Beginning and Ending Account, sources to print, whether to include year-end adjustments or not and which profit center Part 2 numbers to include in the report. 
If using Part 2 numbers, you will need to enter leading or trailing spaces for your Profit Centers (for example, if you use only one character of a right-justified, 2-character Profit Center, a leading space must be entered in the report parameter).
When no Profit Centers are selected, all accounts print. It can be run in a detail format giving one line each time the month and transaction number change, a more summarized level, one line each time the GL Reference number changes, or one line per GL Account.
If choosing to run the report by Account, you cannot further restrict by entering either Sources or Journals. When the report is run in detail format, a subtotal can be printed by month.
This report runs from a stored procedure, "brptGLFinDet".
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

Part 2s to Include
Enter part 2 codes to include, separated by commas (01,02, etc.). Leave blank for all.

Include Year End Adjustments?
Check this box to include year end adjustments. Leave unchecked to exclude year end adjustments.

Show Zero Balances?
Check this box to include all accounts, including those with a zero balance. Leave unchecked to exclude accounts with a zero balance.
