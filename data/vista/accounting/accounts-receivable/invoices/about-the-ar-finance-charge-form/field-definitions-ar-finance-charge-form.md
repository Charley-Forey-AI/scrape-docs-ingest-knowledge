---
title: "Field Definitions: AR Finance Charge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-finance-charge-form/field-definitions-ar-finance-charge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-finance-charge-form/field-definitions-ar-finance-charge-form"
---

# Field Definitions: AR Finance Charge Form

The following is a list of field descriptions for the AR Finance Charge form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq #

Enter the sequence number of an existing entry or enter N, New, or + to add a new sequence. The system will automatically assign the next available sequential number.

##  Customer

 Specify the customer for entering finance/service charges.

## Invoice #

For “A-Account” finance charge types:
Enter the finance/service charge invoice number, or if the system is assigning invoice numbers automatically, accept the default invoice number.
For “R-RecType” finance charge types:
Enter the original invoice number to which the finance/services charges are being applied. Use the F4 key to display a list of invoices for the selected customer.

##  Description

 This field initially defaults to either “Finance Charge” or “Service Charge”, depending on which of these charges you are using (defined in AR Company Parameters). You may override this description if desired.

##  RecType

 This field displays the Receivable Type for posting finance charges.
 If the customer's Finance Charge Type is “A-Account”, this field defaults the receivable type specified for finance charges in AR Company Parameters (Finance Charges tab). If you did not specify a finance charge receivable type, the system uses the AR Company Receivable Type (Info tab). Select the Allow Override of Receivable Type checkbox (AR Company Parameters) to override this field.
 If the customer's Finance Charge Type is “R-RecType”, this field is always accessible (regardless of how the Allow Override of Receivable Type checkbox is set), but defaults as blank. Enter the receivable type for restricting finance/service charge assessment. Only invoices with this receivable type will be included when calculating finance charges.
 If the customer's Finance Charge Type is “I-Invoice”, this field is always disabled (regardless of how Allow Override of Receivable Type is set), but defaults the receivable type from the invoice to which the finance charges are to be applied.

##  Inv/Trans Date

 Enter the invoice date for this transaction, or accept the current date default.

##  Due Date

 This field applies to Finance Charge Type “A-Account” or R-RecType” only.
 Specify the due date for this finance/service charge invoice. This field initially defaults a due date based on the customer's payment terms. If payment terms are not specified, this field defaults as blank.
 If you initialized finance charges (AR Calculate Finance Charge), the system bases the due date on the customer's payment terms unless you selected the "Set for DueDate to be same as TransDate" checkbox, in which case, the due date is the same as the transaction date. The system allows overrides to this field.

##  DueDateCutOff

 Specify the due date cutoff for this finance charge transaction. Unpaid invoices with a due date on or before this cutoff date will be included when calculating finance charges.
 Any difference between the due date cutoff and the paid date cutoff, represents a grace period in which customers may pay any overdue balance.

##  PaidDateCutOff

 Specify the paid date cutoff for this finance charge transaction. Invoices with a due date that falls on or before the specified due date cutoff, that have had a payment applied on or before this cutoff date, will be excluded when calculating finance charges.
 Any difference between the due date cutoff and the paid date cutoff, represents a grace period in which customers may pay any overdue balance.

## AR Line

Entry in this field depends on the Finance
 Charge Type specified for the customer (in AR Customers).
If the finance charge type is “A-Account”,
 enter '1' or 'New'.
If the finance charge type is “Invoice”, enter
 the line number of the original invoice to which you are applying this finance/service
 charge.
If the finance charge type is "RecType", press
 Ctrl+A, select File >  Create Finance
 Charge Detail, or click the Create FC Detail button. The system automatically locates all
 invoices posted to the receivable type that meet the Due Date Cutoff and Paid Date Cutoff
 criteria, and calculates finance charges as applicable.

##  Contract Item

 Specify the applicable contract item for this finance/service charge.

## Description

Enter a description for this transaction line, up to 30 characters.
If you calculate finance charges by receivable type (manually or automatically), this field defaults a description based on the original invoice's number, posted month, and transaction number.
For example:
Invoice #:  25500
Invoice Month: 06/21
Trans #: 250
In this case, the description would be 25500, 06/01/21, 250.
Note: You will note that the description uses a date (MMDDYY) in the description, rather
 than just the month. In all cases, the day will be '01'.

## GL Rev Account

This field initially defaults to the finance charge account (FinChg field in AR Receivable Types) for the invoice’s receivable type Rec Type field).

##  Amount

 If you had the system calculate finance charges automatically, this field defaults the calculated charge.
 If entering finance/service charges manually, enter the finance/service charge; the field does not default an amount.
