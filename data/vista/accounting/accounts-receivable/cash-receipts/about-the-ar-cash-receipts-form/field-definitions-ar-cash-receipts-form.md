---
title: "Field Definitions: AR Cash Receipts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/field-definitions-ar-cash-receipts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/field-definitions-ar-cash-receipts-form"
---

# Field Definitions: AR Cash Receipts Form

The following is a list of field descriptions for the AR Cash Receipts form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq #

Enter the sequence number of an existing entry or enter N, New, or + to add a new sequence. The system will automatically assign the next available sequential number.

##  Customer

 Enter the customer that applies to this payment transaction.

##  Trans Date

 Enter the transaction date for this payment, or accept the current date default. The system records this date as the “paid date”, which is typically the date payment was received. This date is used in the calculation of finance/service charges (if applicable) and is part of the aging routine if payments after the aging date are excluded.

##  Check #

 Enter the check number for this transaction.

##  Check Date

 Enter the date of the check. The system uses this date as a reference only. Aging routines use the transaction date.

##  Check Amount

 Enter the total amount of the check.

##  CM Co

 Enter the Cash Management company for the depositing bank account.

##  CM Account

 Enter the CM bank account to deposit the check to.

## Deposit #

Enter the reference number for this deposit. This number is the transaction number of the deposit, which you can use to create deposit slips and to modify deposits within Cash Management. Use F4 to view all available deposit numbers, either posted or in process.
Consider using a combination of the date and a sequence number to create the deposit number. For example, the first deposit made on April 16 could be deposit #0416-1.
Note: The system interfaces the accumulation of all transactions entered with the same deposit number as a single deposit to the CM module. The batch audit list includes a separate page for each unique deposit, with all transactions detailed. You might provide this detail to the bank along with the deposit slip.

## SM Co

SM Co field on the Info tab of the AR Miscellaneous Receipt
 Lines form.
Enter the SM Co or press F4 for a list of valid SM
 companies.

## WO

WO field on the Info tab of the AR Miscellaneous Receipt Lines
 form.
Enter the SM work order that applies to this timecard line. Press F4 for a
 list of valid work orders.

## Scope

Scope field on the Info tab of the AR Miscellaneous Receipt
 Lines form.
Enter a scope code or press F4 to select one from
 a list.

## Cost Type

Cost Type field on the Info tab of the AR Miscellaneous
 Receipt Lines form.
Enter a cost type or press F4 to select a cost type from a
 list.

## Total Applied

This column displays the total amount of payment applied.
If you initialize payments, the system automatically applies the payment to the first invoice with a balance in the Current Due column. If the payment exceeds the Current Due value, the system automatically forwards the remaining balance to subsequent invoices in the same manner. Override this amount as necessary.
If you are manually applying payments, or overriding an initialized amount, enter the total amount of the payment to apply to this invoice. Press Ctrl + A to automatically set this amount to the Current Due value. If a discount is active, do not subtract that amount. The system automatically adjusts the Total paid (displayed in the Total field in the header) once you enter the discount amount.
Note: Pressing Ctrl + A also accomplished the following actions:

- The Tax Applied column is set to the amount in the UnPaid Tax field (Invoice Totals section of the form).

- The FC Applied column is set to the amount in the UnPaid FC field.

- The Disc Taken column is set to the available discount amount (Disc Offered field minus the Disc Taken field)

- The Tax Disc column is set to the amount in the Avail Tax Disc field.

 For information on other shortcuts (e.g. tax reversal, apply retainage, etc.) that can be implemented from this field, see Posting Shortcuts below.

[](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/posting-shortcuts)Posting Shortcuts

##  Tax Applied

 This field defaults the ‘unpaid tax’ amount for the invoice (initialized or manually applied payments) or the amount of the payment, whichever is greater. For example, if the payment amount is $1000.00, but the Current Due is $25,000.00 and the UnPaid Tax is $1,500.00, this field will default 1000.00. You can override this as necessary.
 If you override the default amount, specify any amount of the payment to apply towards the tax amount, as long as it does not exceed the amount in the Unpaid Tax field. To override this restriction, select the Remove Input Restrictions checkbox in AR Payment Detail.
Note: If you are using the Distribute Tax to Retainage feature (AR Company Parameters), this amount will not include retainage tax. Retainage tax is included in the UnPaid Retg amount and paid when retainage is paid.
Tip: To reverse an invoice's tax amount, press Ctrl + T. See Posting Shortcuts in Related Topics for more information.  
[](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/posting-shortcuts)Posting Shortcuts

## Disc Taken

If you initialized payments and selected the
 Apply Discounts checkbox (in AR Initialize Receipt), this field defaults the available
 discount amount (Disc Offered field minus the Prev DiscTaken field), as long as you
 apply payment before the Discount Date and it covers the entire balance due of the invoice;
 otherwise, this field defaults as 0.00. Override this amount as necessary.
If you are applying payments manually, this field defaults the available discount amount, as long as the transaction date is equal to or less than the invoice's discount date and the Total Applied value fully covers the current amount due for the invoice. Otherwise, the field defaults to 0.00.
If you override the default amount, specify any discount amount, as long as it does not exceed the available discount amount. To override this restriction, select the Remove Input Restrictions checkbox in AR Payment Detail.
Note: You can also auto apply the discount taken by pressing
 Ctrl + A in the Total Applied column (after the payment amount is entered). If the payment
 date is greater than the discount date, auto-apply the discount by pressing Ctrl + W. These
 options are only available if the invoice has an offered discount. For more information,
 refer to Posting Shortcuts in Related Topics below.
[](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/posting-shortcuts)Posting Shortcuts

##  Tax Disc

 If you initialized payments and selected the Apply Discounts checkbox (in AR Initialize Receipt), this field defaults the offered tax discount amount (Disc Offered field), as long as the payment is applied before the Discount Date and covers the entire balance due of the invoice; otherwise, this field defaults as 0.00. Override this amount as necessary.
 If you are applying payments manually, this field defaults the available tax discount amount (Avail Tax Disc field) as long as the transaction date is equal to or less than the invoice's discount date and the Total Applied amount fully covers the current due for the invoice. Otherwise, default will be 0.00.
 If you override the default amount, specify any tax discount amount, as long as it does not exceed the available tax discount amount. To override this restriction, select the Remove Input Restrictions checkbox in AR Payment Detail.
Note: You can also auto-apply the tax discount by pressing Ctrl + A in the Total Applied column (after the payment amount is entered). If the payment date is greater than the discount date, auto-apply the tax discount by pressing Ctrl + E. These options are only available if the invoice has an offered discount. For more information, refer to Posting Shortcuts in Related Topics below.  
[](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/posting-shortcuts)Posting Shortcuts

##  Retg Applied

 If you initialized payments and selected the Include Retainage checkbox (in AR Initialize Receipt), this field defaults the unpaid retainage amount (if any), as long as the payment is sufficient to cover both the unpaid retainage and total amount due (invoice amount, tax, and finance charges, if applicable). Otherwise, this field defaults as 0.00. Override the amount as necessary.
Note: If you are using the Distribute Tax to Retainage feature (AR Company Parameters), the UnPaid Retg amount includes retainage tax.
 If manually applying payments, or if overriding the default-applied retainage, specify any amount of the payment to apply to retainage, as long as it does not exceed the amount in the UnPaid Retainage field. To override this restriction, select the Remove Input Restrictions checkbox in AR Payment Detail.
Note: You can also auto-apply payment to unpaid retainage by pressing Ctrl + G in the Total Applied column. For more information, refer to Posting Shortcuts in Related Topics below.  
[](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/posting-shortcuts)Posting Shortcuts

##  FC Applied

 If you initialized payments and did not select the Exclude Finance Charges checkbox, this field defaults unpaid finance charges (if any). If the payment is not sufficient enough to cover the total finance charge amount (after taxes are paid), this field defaults the remaining available amount of the payment. Override this default as needed.
 If manually applying payments, or if overriding the default-applied finance charge, specify any amount of the payment to apply to the finance charges, as long as it does not exceed the amount in the UnPaid FC field. To override this restriction, select the Remove Input Restrictions checkbox in AR Payment Detail.
Note: The finance charge portion of the invoice does not update to JC. Only the invoice amount updates to JC.
