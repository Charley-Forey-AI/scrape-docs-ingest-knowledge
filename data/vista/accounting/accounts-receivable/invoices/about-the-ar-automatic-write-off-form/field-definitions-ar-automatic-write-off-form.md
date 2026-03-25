---
title: "Field Definitions: AR Automatic Write-Off Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-automatic-write-off-form/field-definitions-ar-automatic-write-off-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-automatic-write-off-form/field-definitions-ar-automatic-write-off-form"
---

# Field Definitions: AR Automatic Write-Off Form

The following is a list of field descriptions for the AR Finance Charge form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Use Date or Days Older Than

Select the appropriate write-off option:

- Use Older Than Date – Use this option to write-off account balances, invoice balances, and finance charges older than the date specified in the Older Than Date field.

- Use Days Older Than – Use this option to calculate the "older than date" based on a specified number of days. The system calculates the
 “older than date” using the current date and subtracting the specified
 number of days. For example, if you enter 60 days, and the current date
 is 08/01/08, the “older than date” will default as 06/02/2008. This date
 is compared to 'I' (Invoice) type transactions only when determining
 which transactions should apply to this write-off process.

Note: If you enter a date in the Start Date field, the system uses the "older than date" (specified or calculated) in conjunction with the Start Date to determine transactions to include in the write-off process. For more information, see the [Start Date](/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-automatic-write-off-form/field-definitions-ar-automatic-write-off-form#concept-5292--en) F1 Help.

## Start Date

The Start Date field on the AR Automatic Write-Off form.
Enter the start date by which to filter write-off transactions. The system ignores all transactions dated before this date.
The system uses this date in conjunction with the Older Than Date or Older Than # of Days fields to determine transactions to include as follows:





- Older Than Date - The system writes off transactions with dates that fall on or after the start date, but are prior to the specified "older than date". For example, if the Start Date is 01/01/2017 and the Older than Date is 01/01/2018, the write-off process includes transactions with a date that falls on or after 01/01/2018 but prior to 01/01/2019.


- Older Than # of Days - With this option, the system calculates a date by subtracting the specified "Older Than # of Days" from the current date. The Older Than Date field then displays and defaults the calculated date. For example, if the current date is 01/01/2019 and you enter 180 in the Older Than # of Days field, the system defaults 07/05/2018 as the Older Than Date. The write-off process will then include transactions with a date that falls on or after 01/01/2018 but prior to 07/05/2018.

Leave this field blank to have the system include all transactions (meeting the selection criteria) with dates prior to the "older than date".

## Older Than Date / Older Than # of Days

The Older Than Date / Older Than # of Days field on the AR Automatic Write-Off form.
If you selected the
 Use
 Older Than Date radio option, this field displays as "Older Than Date". Enter the date to use in determining transactions to include in the write-off process. The system includes only those transactions with a date prior to this date.

If you selected the Use
 Days Older Than radio option, this field displays as "Older Than # of Days". Enter the number of days by which to calculate the "older than date". The system subtracts the number of days specified here from the current date to determine the “older than date”. For example, if you enter 60 days, and the current date
 is 08/01/08, the “older than date” defaults as 06/02/2008. This date
 is compared to 'I' (Invoice) type transactions only when determining
 which transactions should apply to this write-off process.
Note: If you enter a date in the Start Date field, the system uses the "older than date" (specified or calculated) in conjunction with the Start Date to determine transactions to include in the write-off process. For more information, see the [Start Date](/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-automatic-write-off-form/field-definitions-ar-automatic-write-off-form#concept-5292--en) F1 Help.

##  Beginning/Ending Customer Number

 Enter the beginning and ending customer in a range of customers for writing off balances.
Note: If you are also specifying an invoice range, the system restricts you to using a single customer, since multiple customers can have the same invoice number.

##  Beginning/Ending Invoice Number

For use with 'Write Off By Finance Charge' and 'Write Off By Invoice Balance' write off options only.
Enter the beginning and ending invoice in a range of invoices to write off. Once you enter the beginning invoice number, the ending invoice number automatically defaults the beginning invoice number.
 If you are using alpha-numeric invoice numbers, it is suggested that you limit the range to a single invoice number, as results can be unpredictable. You will receive a warning that processing a range of invoices containing alphanumeric characters can produce unexpected results, but you do have the option to continue.
Note: Because multiple customers can have the same invoice number, you will be restricted to a single customer when processing by invoice. As soon as you enter the beginning invoice number, the ending customer defaults the same as the beginning customer (overriding any previous entry), and field is disabled.

## Write Off Type

The Write-Off Type section on the AR Automatic Write-Off form.

- Write Off By Finance Charge – Select this option to write off finance charges (fully or partially). Selecting this option enables the "FC By (%), Apply to All Lines" and "FC By (%), Amt Applied Starting at Line 1" checkboxes below. How you set these options, along with the value entered in the FC Amount or FC Percentage field will determine how finance charges (invoice type "F") are written off. If neither of the "FC By (%).." options is selected and”

- The FC Amount or FC Percentage field’s amount is set to 0.00, the system will sum finance charges for each line. If there is a finance charge due for the line, the system will compare the finance charge due with the line's actual amount due (less retainage), and create a write-off transaction for the line either equal to the finance charge due or the line's actual amount due, whichever is less.

- The FC Amount or FC Percentage field’s amount is greater than 0.00, the system will distribute the write-off amount to each line beginning with line #1 and progressing to each successive line until the specified write-off amount has been fully distributed. Remaining lines will be left untouched.

For information on how the system writes off finance charges using the "FC By (%), Apply to All Lines" and "FC By (%), Amt Applied Starting at Line 1" options, see the F1 help for those checkboxes.

- Write Off By Invoice Balance – Select this option to write off individual invoice balances. Any invoices with a date less than the 'older than date' and a total amount due (including retainage) equal to or less than the 'balance less than' amount will be written off. Does not include 'on account' transactions.

- Write Off By Account Balance – Select this option to write off account balances. Sum the amounts due all eligible invoices (those with an invoice date less than the 'older than date'), and if the total amount due is equal to or less than the specified 'balance less than' amount, apply a 'write-off' transaction against any eligible invoice lines that are not paid in full. This will effectively write off the account balance.

##  FC By (%), Apply to All Lines

 Check this option to specify a write-off percent and have the write-off value apply to all lines. When selected, the percentage specified in the FC Amount or FC Percentage field will be multiplied against each line of the invoice equally. The write off amount for each line will be based on the line's amount and the percentage.
 Do not check this option if you do not want to write off finance charges by percent and have the value applied to all lines. Finance charges will be written off using one of the other methods.

##  FC By (%), Amt Applied Starting at Line 1

 Check this option to perform a partial write-off based on a write-off percent. When selected, the percentage specified in the FC Amount or FC Percentage field will be multiplied against the total remaining finance charge amount for the invoice to determine the dollar amount to be written off against each line. The write-off amount is then distributed beginning with line #1 and progressing to each successive line until the specified amount has been distributed in full. Remaining lines will be left untouched.
 Do not check this option if you do not want to write off finance charges by percent and have the value applied as allowable beginning with line 1. Finance charges will be written off using one of the other methods.

## FC Amount or FC Percentage/Balances Less Than Input Amount

The FC Amount or FC Percentage/Balances Less Than Input Amount field on the AR Automatic Write-Off form.
The title of this field changes depending on the Write-Off Type you selected.

### FC Amount or FC Percentage

This title displays when you select the Write-Off by Finance Charge type.
Specify the write-off amount or percentage. If you did not elect to use
 either of the 'FC By %...' options, this value represents a flat amount
 to write off. If you elected to use one of the 'FC By %…' options, this
 value represents a percentage of the finance charges to write off. See
 the F1 help for the 'Write Off by Finance Charge' options for information
 on how this value is applied.

### Balances Less Than Input Amount

This title displays when you select the Write-Off by Invoice Balance or Write-Off by Account Balance types.
Specify the amount to determine what balances will be written off. Balances that are equal to or less than this amount will be written off. Balances
 that are greater than this amount will be skipped.
The title of this field changes depending on the Write-Off Type you selected.
Note: The system regards this amount as an absolute value (i.e. ignores whether the value is negative or positive); therefore, if you specify $10.00 here, the system will write off any balance between –$10.00 and $10.00.
