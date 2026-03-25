---
title: "Field Definitions: AP Control Detail Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-control-detail-form/field-definitions-ap-control-detail-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-control-detail-form/field-definitions-ap-control-detail-form"
---

# Field Definitions: AP Control Detail Form

The following is a list of field descriptions for the AP Control Detail form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Hold/Release: Transaction Selection

The Entire Transaction / Select Line and Sequence radio buttons in the Hold Codes
 section of the AP Payment Control Detail form, Hold/Release tab.
Entire Transaction – Select this option to assign/release hold code for the entire transaction.
Select Line and Sequence – Select this option to assign/release a hold code for a specific line and sequence number on this transaction.

## Hold/Release: Line#

 The Line# field in the AP Payment Control Detail form, Hold/Release tab.
This field is enabled once you select the
 Select Line and Sequence radio button in the Hold Codes
 section.
Indicate the line on which to place or release
 the hold.
Note: You can only use this form to assign/remove non-retainage hold
 codes. Retainage holds are handled during transaction entry in AP Transaction Entry, AP
 Unapproved Invoice Entry, and AP Recurring Invoices. To release retainage holds, you
 must use AP Release Retainage. For more information, see [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice).

## Hold/Release: Seq#

The Seq# field in the AP Payment Control Detail form, Hold/Release tab.
This field is enabled once you select the Select Line and Sequence
 radio button in the Hold Codes section.
Indicate the sequence # on which to place or
 release the hold.
Note: You can only use this form to assign/remove non-retainage hold
 codes. Retainage holds are handled during transaction entry in AP Transaction Entry, AP
 Unapproved Invoice Entry, and AP Recurring Invoices. To release retainage holds, you
 must use AP Release Retainage. For more information, see [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice).

## Hold/Release: Hold Code

The Hold Code field on the AP Payment Control Detail form, Hold/Release
 tab.
Enter the hold code to assign or remove from
 the transaction or line/seq#, and press the Update button. If the hold code is already
 assigned to the transaction or line/seq#, it is removed and placed in the Unassigned Hold
 Codes box at the bottom of the screen.
If it has not been assigned, it is added to
 the transaction and placed in the Assigned Hold Codes box at the bottom of the screen.
You can repeat this process until all hold
 codes have been assigned or released for the specified transaction (or line/seq#).
Note: You can only use this form to assign/remove non-retainage hold
 codes. Retainage holds are handled during transaction entry in AP Transaction Entry, AP
 Unapproved Invoice Entry, and AP Recurring Invoices. To release retainage holds, you
 must use AP Release Retainage. For more information, see [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice).

## Partial Payments: Transaction Selection

The Entire Transaction / Select Line and Sequence radio buttons in the Partial
 Payments section of the AP Payment Control Detail form, Partial Payments tab.
Entire Transaction – Select this option if you want to create a partial payment on the entire transaction.
Select Line and Sequence – Select this option if you want to create a partial payment for a specific line and sequence number on the transaction.

## Partial Payments: Line#

The Line# field on the AP Payment Control Detail form, Partial Payments
 tab.
 Indicate the line for which to create a
 partial payment.
Note: You can only split the non-retainage portion of a transaction; you cannot split a
 retainage line/sequence. If you need to perform a partial release of retainage, use the
 AP Release Retainage form. For more information, see [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice).

## Partial Payments: Seq#

 The Seq# field on the AP Payment Control Detail form, Partial Payments
 tab
This field is enabled once you select the Select Line and Sequence radio button in the Partial Payments section.
Indicate the sequence number for which to
 create the partial payment.
Note: You can only use this form to create a partial payment for a
 non-retainage line/sequence. To perform a partial release on a retainage hold, you must
 use AP Release Retainage. For more information, see [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice).

## Partial Payments: Amount

The Amount field in the AP Payment Control Detail form, Partial Payments
 tab.
Enter the partial payment amount. If you are
 not assigning a supplier, placing the remaining amount on hold, or distributing discount
 amounts, you can click the Update button now. The amount specified here will then be
 subtracted from the original entry, and a second sequence will be created for the partial
 payment amount.
Example:
You have a transaction with a single expense
 line (Seq #1) for $1,000, and you want to create a partial payment of $600. The transaction
 would be split, and Seq #1 would be reduced by $600, changing its amount to $400. A second
 sequence (#2) would be created for the partial payment amount of $600.
Note: You can only split the non-retainage portion of a transaction; you cannot split a
 retainage line/sequence. If you need to perform a partial release of retainage, use the
 AP Release Retainage form. For more information, see [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice).

## Partial Payments: Supplier

 If the partial payment is to be paid by a 2-party check, enter the second party here. If you are not placing the remaining amount on hold or distributing discount amounts, you can click the Update button now to perform the split and create the partial payment.

## Partial Payments: Put the Original on Hold

The Put the Original on Hold checkbox on the AP Payment Control Detail form, Partial
 Payments tab.
Select this checkbox to place the remaining
 amount (the original sequence) on hold.
Clear this checkbox if not placing the
 remaining amount on hold.

## Partial Payments: Hold Code

The Hold Code field on the AP Payment Control Detail form, Partial Payments
 tab.
Indicate the hold code for the remaining
 amount. If you are not distributing discount amounts, you can click the Update button now
 to perform the split and create the partial payment.
Note: You can only assign non-retainage hold codes to a split payment.

## Partial Payments: Distribute Discounts

The Distribute Discounts checkbox on the AP Payment Control Detail form, Partial
 Payments tab.
Select this checkbox to distribute discount
 amounts when the transaction is split. When the split is performed and the partial payment
 created, the discount amounts are distributed proportionately, based on the discount amount
 and the split amount.
For example, for a transaction of $1000, with a partial payment of $600, and a discount amount of $50, the result would be as follows:

- Seq #1 ($400) – discount amount would be $20 ($50 x $400/$1000)

- Seq #2 ($600) – discount amount would be $30 ($50 x $600/$1000)

Clear this checkbox if not distributing the
 discount amounts. The discount amount will be taken from the partial payment.

## Partial Payments: Distribute Tax

Check this box to distribute the tax amount
 equally between the two sequence numbers for a split transaction. The system enables this
 field when you enter an amount in the Amount field.

## Restore Tab

The Restore tab on the AP Payment Control Detail form.
Use the Restore tab of AP Payment Contol Detail to restore and entire transaction or selected line to its original state. By restoring a transaction/line, all of the unpaid and uncleared entries by line and pay type are consolidated into a single sequence. All amounts are accumulated, and any splits created for partial payments are removed. If suppliers or hold codes were assigned to parts of a transaction or sequences of a line, they are lost for all but the first sequence for each pay type.
The following instructions detail how to restore a split transaction.

1. Select one of the options in the Partial Payments section of the form:

- Entire Transaction – Select this option to restore the entire
 transaction. Any splits made for partial payments will be removed, and
 all of the unpaid and uncleared sequences by line and pay type will be
 consolidated into one sequence.

- Select Line and Sequence – Select this option to restore a selected line. Any
 splits made for partial payments will be removed, and all of the unpaid
 and uncleared sequences for this line by pay type will be consolidated
 into one sequence.
If you select this option, the system enables the Line# field.

1.

If you chose Select Line and Sequence, enter the line to restore in the Line# field.

1.
Click Update.The system removes splits made for partial payments and all sequences by pay type are consolidated into a single sequence.

.

## Discounts Tab

The Discounts tab on the AP Payment Control Detail form.
Use the Discounts tab of AP Payment Control Detail to change an invoice's total discount offered and or discount taken amounts. When you change a discount amount, the new amount is distributed proportionately to all lines on the transaction, based on each line's gross amount. You can also use this feature to change both the discount offered and discount taken amounts to zero.

The system only enables the fields on this tab if you have unchecked the Post Discounts Offered to GL and Net Amounts to Subledgers box in AP Company Parameters (Pay Types/Discounts/ICR tab).

The following instructions detail how to change the discount for an invoice/transaction.

1. If you want to change the discount amount, check the Select Discount Amount box. The system enables the Discount Amt field. Enter the amount in the Discount Amt field.

1. If you want to change the discount percentage, check the Select Discount Percentage box. The system enables the Discount % field. Enter the percentage in the Discount % field.

1. Check the Change Discount Offered box to change the discount offered amount by the amount or percentage that you specified.

1. Check the Change Discount Taken box to change the discount taken amount by the amount or percentage that you specified.

1. Click Update.The system distributes the new amount proportionately to all invoice lines, based on each line's gross amount.

## Supplier Tab

The Supplier tab on the AP Payment Control Detail form.
Use the Supplier tab of AP Payment Control Detail to assign or remove a supplier from all lines of an invoice.

You can specify suppliers when the invoice is entered in AP Transaction Entry or AP Recurring Invoices. When you add or remove a supplier in AP Payment Control Detail, it is done by pay type, and applies to all unpaid detail of an invoice.

If
 you are adding a supplier, the existing supplier is not overridden. You
 must remove the existing supplier first, then add the new supplier.

The following instructions detail how to add or remove a supplier from an invoice.

1. Select one of the options in the Supplier section of the form.

- Add Supplier - Select this option to add the specified supplier to all unpaid invoice lines, based on the pay type.

- Remove Supplier - Select this option to remove the specified supplier from all unpaid invoice lines for the pay type.

1.

Enter the supplier you want to add or remove in the Supplier field. Press F4 for a list of suppliers.

1.
Select a pay type from the Select Pay Types grid.

1.
Click Update.The system adds/removes the supplier from all invoice lines that have the specified pay type assigned.
