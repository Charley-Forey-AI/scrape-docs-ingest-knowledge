---
title: "Common Error Messages | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/troubleshooting/common-error-messages"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/troubleshooting/common-error-messages"
---

# Common Error Messages

The Common Error Messages section is
 a quick way to find solutions for some of the error messages in Spectrum®.

## Error - Equipment Code Entered is Not Available For Use

If a retired equipment code is entered, this message displays. This
 error message disallows further data entry.

1. To change the equipment's status, click Equipment Control > Maintenance > Equipment to open the Equipment
 File Maintenance screen.

1. In the Status field, enter
 a different status code, or press F4 or double-click in this field to select from a list of valid
 equipment status codes.

## Error - G/L Account Code Entered Is Not Available For Use

If a General Ledger account code with the status of Not used is entered, this message
 displays. This error message disallows further data entry.

1. To change the General Ledger account code's status, click
 General Ledger > Maintenance > Master File to open the G/L
 Master File Maintenance screen.

1. Select either Active or
 Inactive in the
 Status section.

## Error - Job Entered Has A Completed Status

If a job code with a status of Complete is entered, this message
 displays. This error message disallows further data entry.

1. To change the job code's status, click Job Cost > Maintenance > Job > Properties.

1. In the Status section,
 click either Active or
 Inactive.

## Error - Phase Code Entered Is Not Available For Use

If a phase code with a status of Complete is entered, this message
 displays. This error message disallows further data entry.

1. To change the phase's status, click Job Cost > Maintenance > Phase > Properties.

1. Select either Active or
 Inactive in the
 Status section.

## Error - Payroll Update to General Ledger is Not Complete

When errors are detected and you do not have access to the G/L Error Correction Screen,
 Spectrum will provide a warning box that states "Errors exist in the Payroll G/L summary
 file. You are not authorized to make corrections. Please review the Payroll G/L Report
 for details and contact your supervisor for assistance. All errors must be corrected
 before the update can be completed."
Even though you may not have security to make the corrections, the
 following procedure will assist you in locating the errors in the file.

1. Click OK to close the warning message box and return to the Payroll
 Payment Processing
 screen.

1. Click the Payroll
 Update button.

1. On the Payroll
 G/L Summary Report starting screen, select the Detail report version.

1. Click the Preview button. All errors in the file will have the word
 ERROR at the start of
 the line. Use the search function to locate the errors.

1. In the search box, type the word ERROR and press F4 or double-click on this field
 to open the search window.Note: If you press
 Enter after entering the search text, the preview
 window will automatically minimize.

1. Print only the screen(s) with errors on them.

1. Review the errors and contact you supervisor. Your supervisor
 will want to make these corrections.

1. Once the corrections have been made, go back to Payroll > Data Entry > Payment Processing and click the Payroll
 Update button.

1. If no more errors are found, the cycle will complete the
 update.

## Error - Operator or routing code is invalid...

When the user or routing code is not found Spectrum will provide a warning box that
 states "Error – Operator or routing code is invalid. The invoice is now assigned to your
 invoice approval queue. Click the Distribution button then use the routing sub-window in
 Invoice Approval to edit the routing list."
This error indicates that either the user is no longer active or that
 the routing code has been deleted from Spectrum. Any invoices associated with this
 invalid user or routing code will be transferred to Invoice Approval under your operator
 code.

1. Click OK on this message and continue updating the pay cycle.

1. Navigate to Accounts Payable > Data Entry > Invoice Entry.

1. Call up your approval queue.

1. Identify the invoices from the pay cycle by resorting the
 screen on invoice number. Remember that invoices created from payroll will start
 with PR.

1. Highlight the invoice and click the Distribution button.

1. Next, click the Routing button.

1. Enter the correct information in the Current Invoice Approval Routing
 window.

1. Click OK twice to save your changes.

## Error - Payroll Update - Create A/P Invoices Error Correction Screen

Invoices will be created for the following deductions in the Accounts Payable Invoice
 Approval screen. A routing code must be entered for each invoice before the update can
 be completed.
This screen will appear when a deduction to be sent to Accounts
 Payable exists without a routing code. This can happen if a deduction code was setup
 without a routing code prior to implementing Invoice Approval and there is no default
 routing code entered on the Accounts Payable Installation screen.

1. Enter the correct routing code that you want to assign to all
 detail lines with a blank routing code. Press F4 to view a list of valid
 routing codes.

1. When complete, click OK to continue updating the pay
 cycle.

## Error - No Changes to Auto Deposit Status Until New Cycle is Set

If you attempt to change the status of an auto deposit setting during payroll
 processing, this message displays. This error message disallows further data entry.
The Employees >  Properties > Auto Deposit window prevents changes to an employee's auto deposit status during
 certain portions of the payroll cycle. An employee's auto deposit status may still be
 changed up until checks are calculated, but after that no changes will be permitted
 until the cycle is cleared or the cycle is returned to Time Card Entry. This provides
 important protection to ensure that an employee does not receive a check while being
 included in the auto deposit file.

## Error - Errors exist in the Payroll G/L summary file

When errors are detected and you do not have access to the
 G/L Error Correction screen, Spectrum® will provide the
 following warning box. "Errors exist in the Payroll G/L summary file. You are not
 authorized to make corrections. Please review the Payroll G/L Report for details and
 contact your supervisor for assistance. All errors must be corrected before the update
 can be completed."
Even though you may not have security to make the corrections, the
 following procedure will assist you in locating the errors in the file.

1. In the Payroll
 Update to General Ledger is not complete window, click OK to open the Payment Processing screen.

1. Click the Payroll Update
 button.

1. On the G/L Summary Report
 screen, select the Detail
 report option.

1. Click the Preview button.
 In the previewed report, all errors in the file will have the word Error at the beginning of the line.

1. In the search field on the main toolbar (the white box next to
 the binoculars), type the word Error and click the binoculars icon to track down the file
 errors.Note: If you press Enter after
 typing the search text, the Preview window will
 automatically minimize.

1. Print only the screen(s) that contain errors.

1. Review the errors and contact you supervisor. Your supervisor will want to make
 these corrections.

1. Once the corrections have been made, return to Payroll > Data Entry > Payment > Processing and click the Update
 Payroll button. If no additional errors are found, the cycle will
 complete the update.

## Error - This Check Number Has Already Been Used and Updated

This error message displays when you click the Preview or Print buttons in the Print Checks screen and the check run
 includes a check number that has been used elsewhere in the software.
To clear this error, either re-print the check batch or complete the
 following steps to reprint one check at a time.

1. In the error message window, click OK to return to the Check Print screen.

1. In the Check number
 field, enter a new check number or press Enter to accept the software
 default of the next check number

1. Print the new check.
