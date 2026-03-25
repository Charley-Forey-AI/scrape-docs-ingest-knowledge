---
title: "Field Definitions: AP Check Print Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form/field-definitions-ap-check-print-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form/field-definitions-ap-check-print-form"
---

# Field Definitions: AP Check Print Form

The following is a list of field descriptions for the AP Check Print form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## CM Account

The CM Account field on the AP Check Print form.
 Enter the CM account for paying checks. The system only includes payable transactions assigned to this account in the check run.

Related information

- [AP Check Print Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form)

## Paid Date

The Paid Date field on the AP Check Print form.
 Specify the date to print on the checks in this check run. If the date does not fall within the batch month, the system displays a warning, but it will accept the date.

Related information

- [AP Check Print Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form)

## Print: Begin/End Printing With Sort Name

The Beginning / Ending Printing with Sort Name fields on the AP Check Print form, Print tab.
 If you are printing checks for only a portion of the batch, enter the vendor sort name to begin/end the check print. Otherwise, leave the field blank.

Related information

- [AP Check Print Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form)

## Print: Beginning Sequence #

The Beginning Sequence # field on the AP Check Print form, Print
 tab.
If you are printing checks for only a portion of the batch, enter
 the sequence number with which to begin printing checks. Use the AP Payment Preview
 with Compliance report to determine the correct sequence number to enter here. The report
 prints in order by vendor sort name; therefore, make sure you enter the sequence number of
 the first check (alphabetically) that you need to reprint.
Note: Although this number refers to the 'Batch Seq #', it will be shown as the
 'Payment Sequence' on the "Payment Preview" report.

## Print: Ending Sequence #

The Ending Sequence # field on the AP Check Print form, Print
 tab.
If you are printing checks for only a portion of the batch, enter
 the sequence number with which to end printing checks. Use the AP Payment Preview
 with Compliance report to determine the correct sequence number to enter here. The report
 prints in order by vendor sort name; therefore, make sure you enter the sequence number of
 the last check (alphabetically) that you need to reprint.
Note: Although this number refers to the 'Batch Seq #', it will be shown as the
 'Payment Sequence' on the "Payment Preview" report.

Related information

- [AP Check Print Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form)

## Print: Beginning/Ending Check#

The Beginning / Ending Check # fields on the AP Check Print form, Print tab.
Enter a check range for printing checks in the Beginning Check # and Ending Check # fields. Must be a numeric value greater than zero, with no leading zeros or special characters (such as a comma). Up to 10 digits allowed. These fields default as follows:

- Beginning Check # - Defaults to the next available check number as follows:

- If a Beginning Check # is entered in CM Accounts for the CM Account specified above, this field defaults that value.

- If a Beginning Check # is not specified in CM Accounts, this field defaults the next available check number based on the highest check number in the system.

- Ending Check # - Defaults based on the number of checks being printed for the CM Account/batch. For example, if the beginning check number is 100 and you are printing 10 checks, the ending check number defaults to 110.

Related information

- [AP Check Print Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form)

## Clear/Void: Beginning Check #

The Beginning Check # field on the AP Check Print form, Clear/Void
 tab.
Enter the beginning check number for the check print range to
 clear or void. Must be a numeric value greater than zero, with no leading zeros or special
 characters (such as a comma). Up to 10 digits allowed.

Related information

- [AP Check Print Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form)

## Clear/Void: Ending Check #

The Ending Check # field on the AP Check Print form, Clear/Void tab.
Enter the ending check number, up to 10 digits, for the check
 print range to clear or void. Must be a numeric value greater than zero, with no leading
 zeros or special characters (such as a comma). Up to 10 digits allowed.

Related information

- [AP Check Print Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form)

## Clear/Void Option

The Clear/Void Option section on the AP Check Print form, Clear/Void tab.
The Clear/Void Option section on the AP Check Print form, Clear/Void tab.
 Select the appropriate option:

- Clear existing Check #s - Select this option to clear the checks and allow the system to reuse the associated numbers.

- Void existing Check #s - Select this option to void the checks and prevent the system from reusing the associated numbers.

Related information

- [AP Check Print Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form)

## Clear/Void: Void Memo

The Void Memo field on the AP Check Print form, Clear/Void tab.
This field is enabled only when you select the Void existing Check #s option.
Enter a note or memo regarding this voided payment, up to 255 characters.
Note:This memo is updated to AP Payment History; the first 30 characters are used as the CM Detail transaction description.

Related information

- [AP Check Print Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form)
