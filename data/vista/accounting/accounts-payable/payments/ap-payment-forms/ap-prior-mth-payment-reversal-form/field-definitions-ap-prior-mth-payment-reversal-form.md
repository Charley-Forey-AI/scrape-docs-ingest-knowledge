---
title: "Field Definitions: AP Prior Mth Payment Reversal Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-prior-mth-payment-reversal-form/field-definitions-ap-prior-mth-payment-reversal-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-prior-mth-payment-reversal-form/field-definitions-ap-prior-mth-payment-reversal-form"
---

# Field Definitions: AP Prior Mth Payment Reversal Form

The following is a list of field descriptions for the AP Prior Mth Payment Reversal form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Payment Method

The Payment Method field on the AP Prior Mth Payment Reversal form.

Specify the type of payment to reverse.

- C-Check

- S-Credit Service

- N-ePayments

- E-EFT

 The reversal process works the same for all payment types.

## CM Account

 Enter the CM account from which the check you wish to reverse was paid.

## Check / EPay #

The Check / Epay # field on the AP Prior Mth Payment Reversal form.

Enter the number of the check, credit service payment, ePayment, or EFT to reverse. The payment must be "outstanding" in CM Detail (it cannot be cleared), it must exist in AP Payment History, and it cannot be void; however, its Paid Month may be open or closed.

## Seq#

Indicate the sequence number of the payment to be reversed. Typically this is zero.

## PrePaid Date

Required.
Specify the prepaid date for this check reversal transaction. Initially defaults the last day of the reversal batch month (e.g., if batch month is 04/XX, prepaid date will default as 04/30/XX). You may override this default; however, if you change to a date outside the batch month, a warning is displayed indicating that the prepaid date is not in the same month as the batch month. Entry will be allowed, but results in the Actual Date (in CMDT) differing from the GL Month (in GLDT).

## Reverse all Seqs

The Reverse all Seqs checkbox on the AP Prior Mth Payment Reversal form.

Enabled only if the payment method is N-ePayment or E-EFT.
Select this checkbox to reverse all payment sequences on the EFT / ePayment transmission.
If you are only reversing a single payment sequence on the EFT / ePayment transmission, leave this checkbox unselected and then use the EFT Seq # field to specify the payment sequence to reverse (required).

## EFT Seq #

The EFT Seq # field on the AP Prior Mth Payment Reversal form.

Enabled only if the payment method is N-ePayments or E-EFT and you did not select the Reverse all Seqs checkbox.
Required.
Enter the payment sequence to reverse or press F4 to select from a list of valid payment sequences for the specified.

## Create Open Transaction(s) in Batch Month

The Create Open Transaction(s) in Batch Month checkbox on the AP Prior Mth Payment
 Reversal form.
Select this checkbox to have the system
 automatically create new open transactions (in the current batch month) matching the
 previously paid entries. Once you post the batch (via this form or the AP Transaction Entry
 form), the transactions become available for payment like any other expense transaction.
Leave this checkbox unselected if you want to
 reverse the original payment, but do not want to set up new transactions.
Note: If you leave this checkbox unselected, when you click the Update button, the system
 displays a warning that a reversal batch will be created without open transactions. If
 you want open transactions created, select No to cancel the
 update, select the checkbox, and then click Update again. Only select
 Yes if you want to proceed with creating the reversal batch
 without open transactions.
