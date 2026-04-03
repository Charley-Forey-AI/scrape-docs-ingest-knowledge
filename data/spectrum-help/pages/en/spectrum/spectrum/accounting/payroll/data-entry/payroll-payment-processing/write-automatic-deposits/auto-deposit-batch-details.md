---
title: "Auto Deposit Batch Details | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/auto-deposit-batch-details"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/auto-deposit-batch-details"
---

# Auto Deposit Batch Details

This window allows you to enter auto deposit batch codes.
Generally, the auto deposit batch setup only has to be completed once. It will be retained
 on file for use in preparing future auto deposits.
Note: If the last instance of a company is deleted in this
 window, the company will be deleted from the file that stores company defaults. This will
 allow new defaults to be set up when the company is re-added.
Fields/Buttons
Descriptions

Batch
Enter the batch number. Entry in this field must be numeric. This number is assigned in ascending sequence to each batch by the Sending Point in a given file of entries. If you are processing multi-company payroll transactions, each company will be assigned a subsequent batch number. Input here should be "0000001".
Note: When using 'ACH' setup from Cash Management, the software will never
 include other batches in the Auto Deposit File and the setting for 'Use
 NACHA service class code 200 and balanced file format?' is ignored.

Company
Enter the company code. Your three-digit company code will default into this field for Spectrum purposes.

Desc Date
Enter the company descriptive date in YYMMDD format, or press Enter to accept the system default (the check date from the Write Automatic Deposits screen).

Eff Entry Date
Enter the effective entry date in YYMMDD format, or press Enter to accept the system default (the check date from the Write Automatic Deposits screen). The effective entry date is the date specified by the Originator on which it intends a batch of entries to be settled. For credit entries, the effective entry date is either one or two banking days following the banking date of processing as established by the Originating ACH (your bank). For debit entries, the effective entry date should be one banking day following the processing date. This date will default to your system date; users should check with their bank for required entry in this field.

Company Name
Enter the company name. The value of this field is established by the Originator for purposes of further identifying the source of the entry and for descriptive purposes for the Receiver. Your company name will default into this field from the Company Installation. Press Enter to accept the default.

Company Desc
Enter the company entry description. The Originator establishes the value of this field to provide a description of the purpose of the entry to be displayed back to the Receiver. For example, "REG SALARY" may be used to describe PPD transactions.

Company ID
Enter the company id number: '1'+EIN, '3'+DUNS, or '9'+User-Assigned number. Originators are required to be identified by a unique identification number. The ANSI one-digit Identification Code Designators (ICDs) are used, followed by the nine-digit identification number.

Service Class Code
Enter a service class code, or press Enter to accept the system default.
200 Mixed Debit/Credit
220 Credits Only
225 Debits Only
The service class code identifies the general classification of dollar entries to be exchanged. The three possible entries available in PPD transactions are "200" (mixed debit and credit transactions), "220" (credit only transactions) and "225" (debit only transactions). Primarily, "200" will be input into this field; users should check with their bank for required input.

Originating DFI
Enter the originating DFI (the transit routing number of the original bank). Entry in this field is required. This Depository Financial Institution field should be input with the four-digit Transit/Routing number and four-digit ABA number of the ACH or originating DFI within a given batch. If multi-company payroll transactions are being processed, this may vary for each batch. If multi-company payroll transactions are not being processed, this will be the same as the Receiving ABA #.

Account Code
This field only displays if the Use Nacha service class code 200 and balanced file format checkbox is selected in the Payroll Installation – Defaults tab and 200 is entered in the Service class code field here. Enter the company's checking account code.
