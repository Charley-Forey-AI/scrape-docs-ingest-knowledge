---
title: "Write Automatic Deposits - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/write-automatic-deposits---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/write-automatic-deposits---field-descriptions"
---

# Write Automatic Deposits - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Period end date
The period end date displays.

Check/cheque date
The check date for the current pay cycle displays.

Bank account
The Cash Management bank account assigned to this pay cycle displays.
Note: This field only displays if Cash Management is installed and is based on
 the bank account specified during Set Payroll Cycle on the 'Electronic
 Payment' tab of the Edit Account window in [Account Code File Maintenance](/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/account-code-file-maintenance/addedit-electronic-payment-account-information).

Electronic format
Select the electronic payment format or accept the default selection, based on the bank account setup.
Note: This field only displays if Cash Management is installed and is based on
 the bank account specified during Set Payroll Cycle on the 'Electronic
 Payment' tab of the Edit Account window in [Account Code File Maintenance](/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/account-code-file-maintenance/addedit-electronic-payment-account-information).

Clear Auto Deposit Cycle
Once the export update has been performed, click this button to clear the auto deposit cycle. This allows you to make changes to auto deposit settings without having to wait until a new payroll cycle is initiated. Once cleared, you can then modify the Employee Auto Deposit page.
Important: If changes are made to the employee's auto deposit
 information and the auto file is exported again, the new settings will be
 used.

Header ID info

Priority code
Enter the NACHA priority code (for example, 01) or press Enter to leave blank. This field is included to allow for some future scheme for priority handling of files. At present, it should be filled with "01".
This field is display-only when the bank account is set up for ACH file format.

Receiving ABA #
Enter the transit routing number of the receiving point, or press Enter to accept the system default. Entry in this field is required. (This field should be input with the four-digit Transit/Routing number and four-digit ABA number of the ACH or receiving point to which the file is being sent (your bank). Your input in this field will be used to fill in the Immediate destination field.)
This field is display-only when the bank account is set up for ACH file format.

Immediate destination
The immediate destination (the receiving aba#) displays. No entry is allowed. This 10-character field begins with a blank in the first position, your bank's four-digit Transit/Routing number and four-digit ABA number, and the Check digit. This field will be calculated by Spectrum.
This field is display-only when the bank account is set up for ACH file format.

Immediate dest name
Enter the immediate destination name. Entry in this field is required. This field contains the name of the ACH or receiving point for which this file is destined (your bank).
This field is display-only when the bank account is set up for ACH file format.

Sending ABA #
Enter the transit routing number of the sending point, or press Enter to accept the system default. Entry in this field is required. This field should be input with the four-digit Transit/Routing number and four-digit ABA number of the ACH or sending point of the file (your company). Input in this field will be used to fill the Immediate Origin.
This field is display-only when the bank account is set up for ACH file format.

Immediate origin
The immediate origin (the sending aba#) displays. This 10-character field begins with a blank in the first position, the user's company four-digit Transit/Routing number and four-digit ABA number, and the Check Digit. This field will be calculated by Spectrum, but may be overwritten by the operator as necessary.
This field is display-only when the bank account is set up for ACH file format.

Immediate origin name
Enter the immediate origin name. Entry in this field is required. This field contains the name of the ACH or sending point that is sending the file (your company).
This field is display-only when the bank account is set up for ACH file format.

File creation date
Enter the transmission date in YYMMDD format with no slashes or other punctuation (that is, 990801 translates to the first day of the eighth month of the year 1999), or press Enter to accept the system current date default. This field is the date on which the file is prepared by an ODFI (ACH input files) or the exchange date on which a file is transmitted from ACH to ACH. This field defaults on today's system date in the YYMMDD format.

File creation time
Enter the transmission time in HHMM format with no slashes or other punctuation (for example, 1136 translates to the thirty-sixth minute of the eleventh hour of the day). This field is the time on which the file is prepared by an ODFI (ACH input files) or the exchange date on which a file is transmitted from ACH to ACH. This field defaults to today's system time in the HHMM 24-hour clock format.

File ID modifier
Enter the file id modifier if desired, or press Enter to accept the system default. This field is included in the File Header Record to permit multiple files created on the same date and between the same participants to be distinguished. Only upper-case A-Z and number 0-9 are permitted. Since this is just a PPD file being created, the default is A.

Reference code
Enter the reference code, if desired. This field is reserved for information pertinent to the Originator (your company) and is an optional, not required, input field. Check with your bank for information they may desire in this field.

Write to

Export file
Enter the automatic deposit file name for the export.

Batch setup

Co. desc date
Enter the default company descriptive date or press Enter to accept the default (the Check date entered above). The originator establishes this field as the date it would like to see displayed to the Receiver for descriptive purposes. This field cannot be used to control timing of any computer or manual operation, and is an optional input field. For example, "JAN 15" or "JAN 05" may be used to describe payments for payroll through January 15th.

Entry date
Enter the effective entry date in YYMMDD format, or press Enter to accept the default (the Check date entered above). The effectiveness entry date is the date specified by the Originator on which it intends a batch of entries to be settled. For credit entries, the effective entry date is either one or two banking days following the banking date of processing as established by the Originating ACH (your bank). For debit entries, the effective entry date should be one banking day following the processing date. This date will default to your system date; check with your bank for required entry in this field.

Enter Detail button
Click this button to open the [Auto Deposit Batch Details](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/auto-deposit-batch-details) window. Generally, the auto deposit batch setup only has to be completed once. It will be retained on file for use in preparing future auto deposits.
This button does not display when the setup is from the Cash Management bank account.

Auto deposit log
Select the Preview auto deposit log checkbox to preview the Auto Deposit Report, otherwise leave this checkbox clear.
If the 'Use secure download page for electronic files' option on the Payroll Installation screen is selected, the Checking Account Code, Account Type and ABA # will be masked on the report.
