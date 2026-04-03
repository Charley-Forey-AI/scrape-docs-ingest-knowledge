---
title: "G/L Error Correction Screen | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/troubleshooting/gl-error-correction-screen"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/troubleshooting/gl-error-correction-screen"
---

# G/L Error Correction Screen

The G/L Error Correction screen captures issues in General Ledger transactions. This screen does not display in the General Ledger module. The modules that display the G/L Error Correction screen are listed below:

- Accounts Payable > Data Entry > Invoice/Credit Memo Entry > Update

- Accounts Payable > Data Entry > Invoice/Credit Memo Entry > Reverse > Reverse Open Invoice Entry / Update

- Accounts Payable > Data Entry > Payments G/L Detail Report/Update

- Accounts Receivable > Data Entry > Invoice / Credit Memo Entry > Update

- Accounts Receivable > Data Entry > Cash Receipts / Adjustments Entry > Update

- Human Resources > Data Entry > Vac/Hol/Sick G/L Accrual Report/Update

- Human Resources > Data Entry > Reverse Vac/Hol/Sick G/L Accrual / Update

- Inventory Control > Data Entry > Inventory Transaction Report / Update

- Payroll > Data Entry > Payment Processing > Update Payroll

Errors shown on the G/L Error Correction screen must be corrected before completing the update. Corrections can be made on this screen, or you may cancel out of the screen to make changes elsewhere in Spectrum. The chart below shows the different error types along with suggestions on how to clear them.
Error Message
Indicates
Suggestions on How to Resolve

INVALID G/L ACCOUNT
The G/L code entered does not exist in the General Ledger Master file.
Options include:
• Change to an existing G/L code.
• Exit the screen; in the General Ledger module, set up the code.
• Add the code on the fly (appropriate security required).

G/L ACCT NOT USED
G/L code does not have an Active or Inactive status.
Options include:
• Change to an Active or Inactive G/L code.
• Exit the screen; in the General Ledger module, change the status on the code.
• Change the code on the fly (appropriate security required).

INVALID YEAR & PER
Transaction not within processing dates.
Check the processing dates in all companies that the payroll posts to.
One Step Update:
Cancel the update, review posting dates and restart the update.
Two Step Update:
Open the date range to allow the transaction to post through. As the G/L is always the second update, we recommend that you allow the transactions to post in order to keep the other modules in balance with the G/L.
Note: In the event that this is an incorrect G/L period, make a manual journal entry to reclassify to the correct period.

G/L ACCT/COST CENTER MISMATCH
The G/L code used is not allowed for this cost center.
This error can display if the cost center feature is enabled in the Enterprise Installation screen.
Options include:
• Cancel the update and add this cost center to the G/L code.
• Add the cost center to the G/L code on the fly (appropriate security required).

The G/L Error Correction screen is disabled when the post to G/L checkbox on the General Ledger Installation screen is cleared for a specific module.
For audit purposes, changes made in this window are recorded in a log
 file during the update to G/L. The G/L Error Correction Change Log is located on the General Ledger > Period End menu.
Note: Note Regarding Security: Enhanced security is provided for the G/L Error Correction screen. If the user initiating the update does not have level 8 security authorization, a warning message displays. It is recommended that the user review the updated report; searching for the word, ERROR helps identify the records in question. The user will then need to contact the supervisor for assistance.
