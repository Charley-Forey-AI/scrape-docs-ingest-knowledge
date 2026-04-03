---
title: "ACH Electronic Payment Setup (United States) - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/about-account-electronic-payment-additions-and-edits/about-ach-electronic-payments-and-nacha/ach-electronic-payment-setup-united-states---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/about-account-electronic-payment-additions-and-edits/about-ach-electronic-payments-and-nacha/ach-electronic-payment-setup-united-states---field-descriptions"
---

# ACH Electronic Payment Setup (United States) - Field Descriptions

Use this table for reference when the United States (ACH) electronic payment format is selected.
Note: All fields are required for ACH processing, unless otherwise noted.

FieldDescription
Company nameAccept or edit the company name that defaults from the Company Installation screen; max 16 characters.

Receiving ABA #Enter the four-digit transit routing number and the four-digit American Bankers Association (ABA) number of the ACH or receiving point (your bank).
Note: Data in this field automatically populates the Immediate dest name field.

Immediate dest nameEnter the name of the ACH or receiving point for which the file is destined (your bank).

Sending ABA #Enter the transit routing number of the ACH operator. Enter the four-digit transit routing number and the four-digit ABA number of the ACH or sending point of the file (your company).
Note: Data in this field automatically populates the Immediate origin field.

Immediate originAccept or edit the default text.

Immediate origin nameEnter the name of the ACH or sending point that is transmitting the file (your company).

Use NACHA service class code 200 and balanced file format?Select this checkbox to use a balanced file format. The National Automated Clearing House Association (NACHA) service class code 200 identifies ACH entries in a batch as mixed debits and credits. Note: If you select Use NACHA service class code 200 and balanced file format?, you must enter a secure account number.

Secure account numberInformation in this field does not display on other screens or reports, which allows the cash manager to record account numbers for electronic payments without revealing confidential information to unauthorized users.

Start the company discretionary data field with zeros?To accept the default company code, leave this box unselected. Select this checkbox to default three zeros in positions 21-23 of the Company/Batch Header Record in files exported from the [Export Electronic Payments](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/export-electronic-payments) and [Write Automatic Deposits](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits) screens. Refer to [Company/Batch Header Record (Record Type 5)](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/company--batch-header-record-record-type-5).

File ID modifierDefault value is "A". This entry displays in the File Header Record to distinguish multiple files created on the same date. See [File Header Record (Record Type 1)](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/company--batch-header-record-record-type-5).
Note: Only uppercase A-Z and numbers 0-9 are permitted in this field.

Priority codeAccept or edit the default text; max two characters.

Company IDThe originator, or company ID number begins with an American National Standards Institute (ANSI) one-digit Identification Code Designator (ICD) followed by a nine-digit identification number.

Originating DFIEnter the originating Depository Financial Institution (DFI), or the transit routing number of the original bank.

Reference code(Optional) Enter originator information. Note: Check with your bank for information they may desire in this field.

Company entry description(Optional) As the originator, your company can enter a description that displays to the receiver.
Electronic file name(Optional) Enter an automatic deposit file name for the export. Note: Text entered here defaults to the Export Electronic Payments screen. See [Export Electronic Payments](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/export-electronic-payments).
