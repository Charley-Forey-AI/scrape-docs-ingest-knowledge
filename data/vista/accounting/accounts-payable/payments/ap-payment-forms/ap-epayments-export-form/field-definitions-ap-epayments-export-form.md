---
title: "Field Definitions: AP ePayments Export Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form/field-definitions-ap-epayments-export-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form/field-definitions-ap-epayments-export-form"
---

# Field Definitions: AP ePayments Export Form

The following is a list of field descriptions for the AP ePayments Export form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## CM Account

CM Account field in the AP ePayments Export
 form.
Enter the bank account to use for this payment. When you select Initialize, only payable transactions in
 this payment batch that are assigned this CM account will be added to the data file.
After selecting Initialize, you can opt to enter a new value in this field and then select
 Initialize again, repeating for as many CM accounts as needed. When
 you select Download, the system creates the ePayment data file and maintains your chosen
 CM account.

Related information

- [Credit Service CM Account Overwrite](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form/field-definitions-ap-epayments-export-form#ID-00006704--en)

## Credit Service CM Account
 Overwrite

Credit Service CM Account Overwrite field in the AP ePayments Export form.
The
 system enables this field only if your entry in this form's CM Account
 field matches what you have entered in the CM Acct field in the AP Company
 Parameters form (Payment Services tab). See [Credit Service CM Acct](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form/field-definitions-ap-company-parameters#ID-00005c0d--en) for additional information.
In
 most cases, you should simply re-enter into this field the same account number that you
 have just entered in the CM Account field immediately above.
This field provides an option to pay these invoices (the ones you are about to initialize) from a different CM account than what was originally intended by overwriting the pre-assigned CM account.
Important: If you take this option, you will need to
 reconcile any imbalances with a journal entry.

## Payment Methods

Payment Methods section in the AP ePayments Export form
You can choose which invoices from this payment batch to include in the ePay file you generate.

- ePayments only - Select this option to include only invoices (in this batch) with a payment method of N - ePayments in the generated file; invoices with any other payment method are excluded.

- Include all unpaid - Select this option to include all invoices in this payment batch, regardless of their payment method; the system will change their payment method to N - ePayments.

For requirements and instructions, see [AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form)

## Overwrite existing CM Reference# and
 Seq#

Overwrite existing CM Reference# and Seq# field in the AP ePayments Export form.
Only select this checkbox if you are
 re-initializing transactions intended for the ePayments data file.
Select this checkbox to remove
 already-assigned CM Reference and Sequence numbers and re-assign new ones when initializing ePayments transactions.
Leave this checkbox unselected to skip any payments that already have a CM Reference # assigned when initializing ePayments transactions.

## Use Multiple CM Reference #s

The Use Multiple CM Reference #s checkbox on the AP ePayments Export form.
Select this checkbox to have the system assign a unique CM reference number to each payment in the batch. When selected, a Starting CM Reference # field displays for specifying the number with which to begin CM reference number assignments.
Leave this checkbox unselected to assign the same CM reference number to all payments in the batch.

## CM Reference# / Starting CM Reference #

The CM Reference# / Starting CM Reference# field in the AP ePayments Export form.
The title of this field changes to "Starting CM Reference #" when you select the Use multiple CM Reference #s checkbox.
If you are not using multiple CM reference numbers, this number is assigned to each payment within this ePayments file and must be unique within the CM Account. This field is alphanumeric and allows up to 10 characters. To keep each payment record unique, the system appends a sequence number to the CM Reference #.
If you are using multiple CM reference numbers, enter the starting CM reference number (up to 10 digits) for payments in this ePayments file. The system assigns a separate CM reference number to each payment in the file, starting with the CM reference number specified here, and skipping any reference numbers already in use. The next time you run an export, the system defaults a starting CM reference number based on the last number used.

## Description

Description field in the AP ePayments Export
 form.
When you post this batch, if this particular
 payment includes more than one vendor, the description you enter appears in various reports
 and forms in the CM module. If you leave this field blank, the system uses "EFT Payment" as the description.
If this payment includes only one single
 vendor, the system inserts the vendor name in those same places in the CM module and any
 entry in this field is ignored.
This field accepts up to 10 characters.

## Created Date

Created Date field in the AP ePayments Export

 form.
Accept the default value (today's date) or modify the creation date for this ePay data
 file.
When you create the data file (by selecting Download), the value in this field supplies the "yyyymmdd" portion of the filename.

Related information

- [Download Filename](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form/field-definitions-ap-epayments-export-form#ID-00006749--en)

## Created Time

Created Time field in the AP ePayments Export

 form.
Accept the default value or modify the time stamp for this ePay data file.
When you create the data file (by selecting Download), the value in this field supplies the "hhmm" portion of the filename.

Related information

- [Download Filename](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form/field-definitions-ap-epayments-export-form#ID-00006749--en)

## Effective Date

 Effective Date field on the AP ePayments Export form.
Accept the default value (today's date), or enter the date all payments in this data file should be made effective (remitted) by Corpay. This date becomes the Paid Date when you download response files from Corpay and stores it to AP Payment History and to the CM module.
Note: If the effective date falls outside the payment/batch month and/or year, the system displays a warning, but allows the date.

## Download Filename

Download Filename field in the AP ePayments Export form.
Enter a file name or accept the default file name provided.
When you select Upload to create and upload the data file, the system appends the entry with a time stamp, formatted as filename_yyyymmdd_hhmm.
