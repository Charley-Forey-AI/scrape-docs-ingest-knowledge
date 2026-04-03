---
title: "Making Corrections Using the G/L Error Correction screen | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/making-corrections-using-the-gl-error-correction-screen"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/making-corrections-using-the-gl-error-correction-screen"
---

# Making Corrections Using the G/L Error Correction screen

Errors shown on the G/L Error Correction screen must be
 corrected before the update can be completed.
Corrections can be made on this screen, or you may cancel out in order to make changes
 elsewhere in Spectrum to correct the problem. The following chart explains the different
 types of errors as well as suggestions on how to clear the error.
Error Message
Indicates
Suggestions for Resolution

INVALID G/L ACCOUNT
The G/L code entered does not exist in the General Ledger Master file.
Options include:

- Change to an existing G/L code.

- Exit the screen; in G/L, set up the code.

- Add the code on the fly (appropriate security required).

G/L ACCT NOT USED
G/L code does not have an Active or Inactive status.
Options include:

- Change to an Active or Inactive G/L code.

- Exit the screen; in G/L, change the status on the code.

- Change the code on the fly (appropriate security required).

INVALID YEAR & PER
Transaction not within processing dates.
Check the processing dates in all companies that the payroll posts to.
One Step Update:

- Cancel the update, review posting dates and restart the update.

Two Step Update:

- Open the date range to allow the transaction to post through. As the G/L is always the second update, we recommend that you allow the transactions to post in order to keep the other modules in balance with the G/L.
Note: In the event that this is an incorrect G/L period, make a
 manual journal entry to reclassify to the correct period.

G/L ACCT/COST CENTER MISMATCH
The G/L code used is not allowed for this cost center.
Options include:

- Cancel the update and add this cost center to the G/L code.

- Add the cost center to the G/L code on the fly (appropriate security required).

The G/L Error Correction screen is disabled when the post to G/L checkbox on the General Ledger Installation screen is cleared for a specific module.
For audit purposes, changes made in this window are recorded in a log
 file during the update to G/L. The G/L Error Correction Change Log is located on the General Ledger > Period End menu.
