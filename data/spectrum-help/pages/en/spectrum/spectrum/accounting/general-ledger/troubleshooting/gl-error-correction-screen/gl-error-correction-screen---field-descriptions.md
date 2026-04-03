---
title: "G/L Error Correction Screen - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/troubleshooting/gl-error-correction-screen/gl-error-correction-screen---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/troubleshooting/gl-error-correction-screen/gl-error-correction-screen---field-descriptions"
---

# G/L Error Correction Screen - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field/Button
Description

Seq
The sequence number assigned by the system displays.

Comp
The company code displays.

Date
The transaction date displays. If changes need to be made here, enter the correct date, or press F4 or double-click on this field to select a date from the Date Change window. In addition, you can click the Expand button to display the Year and Period fields. Be sure to record the same period for all lines where you amend the date. The system will verify Debits = Credits for each period before permitting the update to proceed. When the period is changed for a transaction posting to a direct job cost or direct equipment cost account, the General Ledger balances will be posted to the new period. Payroll transactions recorded in the subsidiary ledger have already been recorded for the prior period.

Account code
The G/L account code displays. If changes need to be made here, enter the correct code or press F4 or double-click on this field to select from a list of available account codes.
 If the G/L account code is invalid on a particular line, but the Year and Period fall within the current processing date range, you will only have access to the G/L account field.
When changing account codes, a warning message will display if a 'Not Used' account is reset and the direct cost setting of the new account does not match the old account.

Employee code
The employee code displays.

Debit
The debit amount displays.

Credit
The credit amount displays.

Memo - G/L
One of the following messages will display in this column:

- Invalid G/L Account

- G/L Account Not Used

- Invalid Year and Period – If this message displays the Errors for current line box will display the module and company that is being validated. This box lets you know where exactly you need to make corrections before you proceed to print the report and run the update. Errors include: "G/L account not used," "Invalid G/L account," and "Invalid Year and Period." If the cost center feature is enabled in the Enterprise Installation screen, then the "G/L Account/Cost Center Mismatch" error can display.

- Multiple Errors – This message displays when both the G/L account is invalid and when it is not used, and when the date is outside the processing date range.
