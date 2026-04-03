---
title: "Print Checks - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/print-checks/print-checks---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/print-checks/print-checks---field-descriptions"
---

# Print Checks - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Print options
Select the File copy checkbox if you want to print a file copy of the Crystal printed checks following the check print.

Auto deposit check format
Select which auto deposit check format you want Spectrum to use.

- No bank account details This format resembles a regular check, except that it is marked with "VOID."

- Multi-account format #1 This format displays information about the bank accounts that the funds were deposited to.

- Multi-account format #2 This is the same as multi-account format #1, except that it accommodates envelopes with a lower window.

To comply with Wage Theft laws, the three plain paper formats of the Auto Deposit Remittance Advice include the company name, address and telephone number on the form. This information displays in the 'check stub' portion of the form, above the alphabetic payment amount and the 'Pay to the order of' name.

Reprint options
Select Regular checks to print checks only, Auto deposits to print automatic deposit information, or press Enter to accept the system default and print Both checks and automatic deposit statements.
This radio group is only available after the original checks have been printed
 or previewed. The system now allows the user an alternate option when
 reprinting checks. You can reprint either by job number or employee code.
 This radio group is only available if the checks for the current payroll
 cycle have been previewed or printed, and if the Use plain paper
 for auto deposit check stub checkbox is select on the Payroll Installation > Printing tab.

Add-on options
Select any add-on options for the layoff check:

- Auto-signature
 check: Select this checkbox if you are using the
 Auto-signature check option. The Auto-Signature
 Setup screen defines Operators who have access to the
 Auto-Signature options on the Payroll and Accounts Payable check print
 process, the operator code's specific Accounts Payable check limit,
 and a secure signature file to be linked to an operator code.

- MICR check: Select
 this checkbox if you are using MICR checks. The MICR Bank
 Account Setup screen defines the check information for
 the existing Cash Management Bank Accounts needed to print in a check,
 the Bank Accounts that have been set up to print on the Accounts
 Payable and/or Payroll checks, and the location to print the MICR
 Account Code Setup Listing, the Blank Check, the Blank Check Log and
 the Blank Check Log Report.

- MICR check w/ auto-signature: If you have the combined MICR with Auto-Signature Checks product, you will still need to complete the MICR Bank Account Setup as well as the Auto-Signature Setup.

Selections

Check number
Enter the check number on the next check form to be printed. Spectrum validates the check number entered here and a message displays if any duplicate checks are found. The validation is based on the bank account specified in Set Payroll Cycle when the Cash Management module is used.

Pay cycle message
Enter any message text to appear on the pay stub. For example, an employer may want to enter a state ID number in this field. This message will also appear on auto deposit forms, replacement checks, layoff checks and the Employee Kiosk earning statement. If the reprint feature is used, the pay cycle message will be stored on all checks in the pay cycle, and content will be from the latest reprint.
To comply with state requirements, you can also add up to five user-defined fields to appear on the check stub. To include employee user-defined fields in the pay cycle message, enter percent sign + number (ex. %1), separated by commas. Text may also be included. Anything over 100 characters will be truncated.

Spoiled checks
Select this checkbox if spoiled checks should be recorded after checks print. Otherwise, leave blank.
 If this checkbox is selected, after printing checks the system will display
 the Spoiled Check Entry window, allowing entry of the
 numbers for all spoiled checks.
These checks are then recorded by the system as void checks in the Payroll Check Reconciliation file. To add, edit, or delete items already entered, click the applicable button. This is particularly useful when reprinting checks.

Partial SSN in place of employee code?
Select this checkbox to show the last four digits of the employee's Social Security Number in place of the employee code on the payroll check.

Starting check
Entry in these fields is permitted only when the reprinting checks and the
 Print checks sorted by
 field on the Payroll Installation > Printing tab is set to Job/alpha or Alpha reference.

Ending check
Entry in these fields is permitted only when the reprinting checks and the
 Print checks sorted by
 field on the Payroll Installation > Printing tab is set to Job/alpha.

Preview/Export/My Reports buttons
