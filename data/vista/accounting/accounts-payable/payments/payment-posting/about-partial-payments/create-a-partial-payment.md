---
title: "Create a Partial Payment | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-partial-payments/create-a-partial-payment"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-partial-payments/create-a-partial-payment"
---

# Create a Partial Payment

You can create a partial payment for an invoice (in the AP Payment
 Control Detail form) when you need to split payments or when you need separate checks to pay the
 vendor and vendor/supplier.
 Partial payments are payments of anything less than
 the total invoice.A partial payment is implemented by splitting
 the transaction into two sequence numbers. You can create a partial payment for
 either the entire transaction, or at the line/sequence level.
Transactions that
 have retainage applied are automatically split into two sequences, one for the
 current amount, and one for the retainage portion, which is placed on hold. If you
 split a transaction that has retainage, a third sequence is created, which can also
 be placed on hold (non-retainage holds only).
You can also
 split released retainage into partial payments and put a portion of the retainage
 back on hold.
To create partial payments:

1. From the main menu, select Accounts Payable > Programs > AP Payment Workfile.

1. In the AP Payment
 Workfile form, select the transaction from the grid for creating a partial
 payment.If your grid does not have any transactions, enter Payment Selection Criteria in the fields at the top of the form, then select Fill Grid.

1. Select File > Additional Pay Control Functions.The AP Payment Control Detail
 form displays.

1. Select the Partial
 Payments tab.

1. In the Partial Payments
 section, select the appropriate radio button.

- Entire Transaction

- Select Line and Sequence

1. If you selected the
 Select Line and Sequence option, enter a line number and
 sequence number in the Line# and Seq# fields, respectively.

1. In the Amount field, enter the
 partial payment amount.The system enables the rest
 of the fields on the form.

1. If the partial payment
 is to be paid by a two-party check, enter the second party in the Supplier field.

1. If you want to place the
 remaining amount on hold:

1. Select the Put the original on hold
 checkbox.The system enables the Hold Code
 field.

1. In the Hold
 Code field, enter a non-retainage hold code. Press F4 to select from a list.Note: You can only enter non-retainage hold codes in this field; you cannot
 place a retainage hold on transactions/lines using this form.

1. If you want discount
 amounts distributed equally between the
 sequence numbers for the split transaction:

1. Select the Distribute
 Discounts checkbox.

1. Select the Distribute Tax checkbox to distribute the tax amount to
 each of the partial payments.Note:For Australian and Canadian
 companies only: If you released retainage, split it for
 payment, and plan to put a portion of it back on hold, *do not* select Distribute
 Tax. You want to keep all retainage tax on one
 of the sequence numbers and pay this portion first, putting the
 non-taxed retainage back on hold. If you
 put part of a split retainage with tax back on hold, you
 will most likely see an incorrect tax amount when you
 release the retainage in the future.
For more information, see [About Partial Payments for Split Released Retention / Holdback with
 Tax (AU and CA)](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-partial-payments/about-partial-payments-for-split-released-retention--holdback-with-tax-au-and-ca).

1. Click Update.

 The system splits the transaction into two sequence
 numbers. You can now pay each sequence as appropriate.Note:If you release retainage and split it for payment, but you put the retainage back on hold without paying any of the split, the batch posting action to put the retainage back on hold will automatically remove the split.

Related concepts

- [About Partial Payments](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-partial-payments)

Related tasks

- [Restore a Split Transaction](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/restore-a-split-transaction)

- [Change the Discount for an Invoice](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/change-the-discount-for-an-invoice)

- [Add or Remove a Supplier From an Invoice](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/add-or-remove-a-supplier-from-an-invoice)
