---
title: "G/L Error Correction | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/getting-started/general-reference/gl-error-correction"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/getting-started/general-reference/gl-error-correction"
---

# G/L Error Correction

The G/L Error Correction screen displays automatically if
 any errors are encountered during the printing of certain G/L update reports.
The G/L Error Correction screen is disabled when
 the post to G/L checkbox on the
 General Ledger Installation screen is cleared for a specific
 module.
Use this screen to make any necessary corrections before proceeding with
 the report printing and update. The errors for current line box helps you locate errors
 that need correcting, and clicking the Expand button displays the year and period associated with the transaction
 date.
Note: If you do not have level 8 security for that module, you will receive an error message. If you do not have adequate security to correct these errors, it is recommended that you review the update report. Searching for the word ERROR will help identify the records in question. You will then need to contact your supervisor for assistance.
The modules and data entry screens that display the G/L
 Error Correction screen are listed below:

## Accounts Payable

- Vendor Invoices > Update

- Vendor Invoices > Reverse > Reverse Open Invoice Entry / Update

- Payments G/L Detail Report/Update

## Accounts Receivable

- Customer Invoices > Update

- Cash Receipts / Adjustments Entry > Update

## Human Resources

Any of the following accrual exceptions may cause the G/L Error
 Correction screen to open in Human Resources:

- An employee's current home department is not set up in G/L
 Department File Maintenance.

- The specified accrual G/L account codes are not set up in G/L
 Department File Maintenance.

- The accrual date stored in the Employee file is later than the accrual date
 specified on the Vac/Hol/Sick G/L Accrual starting screen;
 the date specified in the Employee file will display on exceptions report.

- Vac/Hol/Sick G/L Accrual Report/Update

- Reverse Vac/Hol/Sick G/L Accrual / Update

## Inventory Control

- Inventory Transaction Report / Update

## Payroll

- Payment Processing > Update Payroll

- After corrections are recorded, click OK, and a new copy of the
 Payroll G/L Report will be produced automatically. If all errors have been
 resolved, the Payroll G/L Summary Update screen will then display.

For audit purposes, changes made in this window are recorded in a log file
 during the update to G/L. The G/L Error Correction Change Log is located on the General Ledger > Period End menu.
Note: Enhanced security is provided for the G/L Error
 Correctiong screen. If the user initiating the update does not have
 level 8 security authorization, a warning message displays. It is recommended that
 the user review the updated report; searching for the word,
 ERROR helps identify the records in question. The user will
 then need to contact the supervisor for assistance.

Related information

- [G/L Error Correction Change Log](/en/spectrum/spectrum/getting-started/general-reference/gl-error-correction-change-log)
