---
title: "Credit Card Reconciliation Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/credit-card-reconciliation-entry/credit-card-reconciliation-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/credit-card-reconciliation-entry/credit-card-reconciliation-entry---field-descriptions"
---

#  Credit Card Reconciliation Entry - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field/Button
Description

Header

Credit card account
Enter the credit account code. If you are not authorized to use the credit card account code you select, then an error message will appear and the entry will be cleared.
Note: The software verifies that the entry in this field is a
 credit card account. Entry of a bank account code is disallowed.

G/L date
Enter the General Ledger period-end date, or press
 Enter to accept the default. This date should
 always be the period-end date.
Based on this date, all the transactions for the selected credit card display through this year and period. This allows reconciliation to the period-end date for the General Ledger cash balance. The transactions that are not marked as cleared will be summed for the uncleared amount that is used for reconciling the General Ledger balance.

Statement date
Enter the credit card statement date. This date should always be the same as or before the General Ledger date.

Statement reconciliation

Opening balance
The opening bank account balance from the last posted statement ending balance displays.
After the first month has been reconciled for the credit card account, the opening balance for each subsequent month will default from the previous ending statement balance.

Ending balance
The ending bank account balance (per bank statement) displays.

Calculated balance
The calculated bank account balance (per reconciliation) displays.

Difference
The difference between the ending balance (per bank statement) and calculated balance (per reconciliation) displays.

General ledger
 reconciliation
G/L opening balance
The G/L balance appears.

G/L ending balance
The ending G/L balance displays.

Calculated balance
The calculated bank account balance (per reconciliation) displays.

Difference
The difference between the General Ledger balance and the Calculated balance (per reconciliation) displays.

Charges
 summary
Cleared
The total number of cleared charges and amounts will display in this row.
This information is stored in the Check Reconciliation Table (BR_CHECK_RECON_MC).

Uncleared
The total number of uncleared charges and amounts will display in this row.
This information is stored in the Check Reconciliation Table (BR_CHECK_RECON_MC).

Credits
 summary
Cleared
The total number of cleared credits and amounts will display in this row.
This information is stored in the Check Reconciliation Table (BR_CHECK_RECON_MC).

Uncleared
The total number of uncleared credits and amounts will display in this row.
This information is stored in the Check Reconciliation Table (BR_CHECK_RECON_MC).

Detail area
Card Detail
Click this button to open the Credit Card
 Reconciliation window to mark off transactions for the card
 that displays on the monthly statement.
