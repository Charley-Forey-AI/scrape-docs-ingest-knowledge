---
title: "Field Definitions: CM Accounts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-accounts/about-the-cm-accounts-form/field-definitions-cm-accounts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-accounts/about-the-cm-accounts-form/field-definitions-cm-accounts-form"
---

# Field Definitions: CM Accounts Form

The following is a list of field descriptions for the CM Accounts form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## CM Account

Enter a unique numeric code, up to 4 characters, to identify each cash account.

## Description

Enter the CM Account description, up to 30 characters.

## GL Account

Press F4 to select from a list of valid GL
 account codes. This GL account code will be affected each time entries are made to this CM
 account. The account description displays to the right.
This GL account must be a valid account in the GL Company specified in Company Parameters. If designating sub ledger codes in the GL Chart of Accounts form, then this account must be coded C-Cash.

##  Bank Account #

 Enter the bank account number for this CM account. This number will be used for EFT payments, such as Payroll Direct Deposits and AP EFT Payments.

## Beginning Check #

The Beginning Check # field on the CM Accounts form.
Enter a valid check number to use as the default beginning check number when printing computer checks in Accounts Payable and Payroll. Must be a number greater than zero, with no leading zeros or special characters. Up to 10-digits allowed.
When you run AP Check Print or PR Check Print, the system defaults this number in the Beginning Check # field of the applicable form when this CM account is specified. Once the check run is complete, the system updates this field with the last check number used plus one.
If you do not enter a value in this field, the system uses standard defaulting for check numbers; that is, the highest check number recorded in the system, plus one.
Note: The standard default method for check printing includes manually entered check numbers that may be out of the range of computer printed check numbers, which can result in the next default value being out of sync with the actual numbers available for computer printed checks. Entering a value in this field ensures that the system defaults the correct beginning check number when running a check print for this account.

## Immediate Destination (US)

(United States only) The Immediate Destination field on the CM Accounts form.
For Electronic Funds Transfers (EFTs).
Enter the transit routing number of the bank receiving and processing the ACH file. This is a 10-digit number (9-digit number preceded by a zero) provided by the bank.
Position: 04-13, File Header Record

## Immediate Origin (US)

(United States only) The Immediate Origin field on the CM Accounts form.
For Electronic Funds Transfers (EFTs).
Enter your company's bank account number. This is an up to 10-digit number, typically your bank account number or your company's Federal Tax ID number.
Position: 14-23, File Header Record

## Routing Transit # (US)

(United States only) The Routing Transit # field on the CM Accounts form.
For Electronic Funds Transfers (EFTs).
Enter the transit routing number of the bank receiving and processing the ACH file. This is a 9-digit number provided by the bank.
Note: This field is only used when the service class code is 200 (debits/credits).
Position: 4-12, Entry Detail Record

## Service Class (US)

(United States only) The Service Class field on the CM Accounts form.
For Electronic Funds Transfers (EFTs).
Enter the Service Class code as follows:

- Code 200 – Indicates the file contains a mix of debits and credits in the transaction.

- Code 220 – Indicates a transmission of credits only.

Position: 02-04, Batch Header Record

## Bank Name (US)

(United States only) The Bank Name field on the CM Accounts form.
For Electronic Funds Transfers (EFTs).
Enter the name of bank where this account resides (your bank). Allows up to 30 characters, but only the first 23 characters will be used in the file.
Position: 41-63, File Header Record

## Assign Bank Name (US)

(United States only) The Assign Bank Name field on the CM Accounts form.
For Electronic Funds Transfers (EFTs).
Enter the name of the sending party (generally the name of your company) as per bank's records, up to 23 characters. This name will be included in the EFT text file.
Position: 64-86, File Header Record

## Batch Header ID (US)

(United States only) The Batch Header ID field on the CM Accounts form.
For Electronic Funds Transfers (EFTs).
Enter the ACH header record label identification code/number as specified by the receiving bank for electronic funds transfers. Up to 94 characters allowed. This identification code/number will become the first line of the EFT text file. If left blank, this EFT line will not be created.
Note: This is an optional field; however, some banks may require an identification number in this field. Contact your bank representative for more information, if necessary.

## Company Discretionary (US)

(United States only) The Company Discretionary field on the CM Accounts form.
This field is for your company's internal use, and no specific format is required. You may enter any alphanumeric value, up to 20 characters. The information in this field displays in the export file created when using the Download tab in PR EFT Payments.
Note: Some banks may require information in this field. Contact your bank representative for more information, if necessary.
Position: 21-40, Batch Header Record

## Company ID# (US)

(United States only) The Company ID# field on the CM Accounts form.
For Electronic Funds Transfers (EFTs).
Enter your 10-digit company identification number. This will typically be either your bank account number or your Federal Tax ID preceded by a '1'.
Position: 41-50, Batch Header Record

## Originating DFI (US)

(United States only) The Originating DFI field on the CM Accounts form.
For Electronic Funds Transfers (EFTs).
Enter your bank's routing transit number. Allows up to 10 digits; however, the file will only use the first 8 digits. This will typically be the your 9-digit routing number, minus the last digit.
Position: 80-87, Batch Header Record

## Account Type (US)

(United States only) The Account Type options on the CM Accounts form.
For Electronic Funds Transfers (EFTs).
Specify the type of this account:

- Checking – Select this option if this is a checking account.

- Savings – Select this option if this is a savings account.

## Account Name (AU)

(Australia only) The Account Name field on the CM Accounts form.
Enter the name of the account’s financial institution.

## BSB # (AU)

(Australia only) The BSB # field on the CM Accounts form.
Enter the Bank/State/Branch number for the account. This number defines the individual branch of your financial institution.

## Customer # (AU)

(Australia only) The Customer # field on the CM Accounts form.
Enter the customer number for this account.

## Bank Short Name (AU)

(Australia only) The Bank Short Name field on the CM Accounts form.
Enter the three character abbreviation for the financial institution.

## Reference (AU)

(Australia only) The Reference field on the CM Accounts form.
Enter the description for account entries, up to 12 characters.

## Contra Required (AU)

(Australia only) The Contra Required checkbox on the CM Accounts form.
Select this checkbox to indicate that EFTs are a mix of debits and credits.
 Do not select this checkbox if EFTs are credits only.

## PBA Type (AU)

(Australia only) PBA Type drop down in the CM Accounts form.
If this bank account is a PBA trust account, select the correct type from the list.

The system uses this value for validation when assigning CM Accounts to contracts and/or when posting subcontract claim payments and principle contract payments.

## Originator's ID (CA)

(Canada only) The Originator's ID field on the CM Accounts form.
Enter the originator ID number, as provided by your financial institution. This field allows up to 10 digits.

## Destination Data Centre (CA)

(Canada only) The Destination Data Centre field on the CM Accounts form.
Enter the unique ID for the destination financial institution.

## Short Name (CA)

(Canada only) The Short Name field on the CM Accounts form.
Enter your organization's name for participants' statements.

## Long Name (CA)

(Canada only) The Long Name field on the CM Accounts form.
Enter your organization's name for participants' statements.

## Currency Code (CA)

(Canada only) The Currency Code drop-down on the CM Accounts form.
Select the currency code for this account. The following options are available:

- CAD - Canada

- USA - U.S.A

## Direct Payment Routing # (CA)

(Canada only) The Direct Payment Routing # field on the CM Accounts form.
Enter the account number that transactions should be posted to if returned.

## EFT Format (CA)

(Canada only) The EFT Format drop-down on the CM Accounts form.
Note: This field displays only for Canadian companies
 (specified in HQ Company Setup, Default County field).
Select the bank/format to use when creating an EFT file for this account. If you are unsure of which format to use, check with your financial institution.
The following options are available:

- HSBC Bank

- RBC Bank

- TD Bank

- Scotia Bank

- Montreal Bank

- Chase

- CIBC Bank

- Concentra Financial

- Canadian Western

- CPA 005

## RBC File Descriptor (CA)

(Canada only) The RBC File Descriptor field on the CM Accounts form.
The system enables this field when you select
 RBC
 Bank from the EFT Format field.
Enter a file descriptor if you are using the web-based file transfer option for RBC bank. The system will add this value to the text file that is generated in either PR (PR EFT Payments) or AP (AP EFT Download).
