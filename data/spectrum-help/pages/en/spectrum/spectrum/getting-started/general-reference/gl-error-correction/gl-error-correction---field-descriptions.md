---
title: "G/L Error Correction - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/getting-started/general-reference/gl-error-correction/gl-error-correction---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/getting-started/general-reference/gl-error-correction/gl-error-correction---field-descriptions"
---

# G/L Error Correction - Field Descriptions

Use the table below for reference when completing the
 fields on this screen.
Fields
Descriptions

Seq
The sequence number assigned by the software displays.

Comp
The company code displays.

Date
The transaction date displays, but changes are
 allowed. Click the Expand button to display the Year and Period fields.
 Be sure to record the same period for all lines where you amend the date.
 The software will verify Debits = Credits for each period before
 permitting the update to proceed. When the period is changed for a
 transaction posting to a direct job cost or direct equipment cost
 account, the General Ledger balances will be posted to the new period.
 Payroll transactions recorded in the subsidiary ledger have already been
 recorded for the prior period.

Account code
The G/L account code displays, but changes are
 allowed.
If the G/L account code is invalid on a particular
 line, but the Year and Period fall within the current processing date
 range, you will only have access to the G/L account field.
When changing account codes, a warning message will
 display if a 'Not Used' account is reset and the direct cost setting of
 the new account does not match the old account.

Employee code, Debit, Credit
The employee code, debit amount, and credit amount
 display.

Memo - G/L
One of the following messages will display in this
 column:

- Invalid G/L Account

- G/L Account Not Used

- Invalid Year and Period – If this message
 displays the Errors for current line field will display the module
 and company that is being validated.


- Multiple Errors – This message displays when
 both the G/L account is invalid and when it is not used, and when
 the date is outside the processing date range.

Expand
Clicking this button displays the fiscal Year and
 Period associated with the transaction date.

Errors for current line
This box lets you know exactly where you need to make
 corrections before you proceed to preview the report and run the update.
 Errors include: "G/L account not used," "Invalid G/L account," and
 "Invalid Year and Period." If the cost center feature is enabled in the
 Enterprise Installation screen, then the "G/L Account/Cost Center
 Mismatch" error can display.

Making Error Corrections
Errors shown on the G/L Error Correction screen must be corrected
 before completing the update. Corrections can be made on this screen, or you may cancel
 out of the screen to make changes elsewhere in Spectrum. The chart below shows the
 different error types along with suggestions on how to clear them.
Error Message
Indicates
Resolution Suggestions

INVALID G/L ACCOUNT
The G/L code entered does not exist in the General
 Ledger Master file.
Options include:

- Change to an existing G/L code.

- Exit the screen; in the General Ledger module,
 set up the code.

- Add the code on the fly (appropriate security
 required).


G/L ACCT NOT USED
G/L code does not have an Active or Inactive
 status.
Options include:

- Change to an Active or Inactive G/L code.


- Exit the screen; in the General Ledger module,
 change the status on the code.


- Change the code on the fly (appropriate security
 required).


INVALID YEAR & PER
Transaction not within processing dates.
Check the processing dates in all companies that the
 payroll posts to.
One Step
 Update:
Cancel the update, review posting dates and restart
 the update.
Two Step
 Update:
Open the date range to allow the transaction to post
 through. As the G/L is always the second update, we recommend that you
 allow the transactions to post in order to keep the other modules in
 balance with the G/L.
Note:
 In the event that this is an incorrect G/L period,
 make a manual journal entry to reclassify to the correct period.


G/L ACCT/COST CENTER MISMATCH
The G/L code used is not allowed for this cost
 center.
This error can display if the cost center feature is
 enabled in the Enterprise Installation screen.
Options include:

- Cancel the update and add this cost center to
 the G/L code.


- Add the cost center to the G/L code on the fly
 (appropriate security required).
