---
title: "Restore a Split Transaction | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/payment-posting/restore-a-split-transaction"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/payment-posting/restore-a-split-transaction"
---

# Restore a Split Transaction

You can restore a transaction or line to its original state,
 as long as it is still unpaid.
When you restore a transaction/line, all of the unpaid and
 uncleared entries by line and pay type are consolidated into a single sequence. All
 amounts are accumulated, and any splits created for partial payments are removed. If
 suppliers or hold codes were assigned to parts of a transaction or sequences of a line,
 they are removed for all but the first sequence for each pay type.Note:If you release retainage and split it for payment, but you put the retainage back on hold without paying any of the split, the batch posting action to put the retainage back on hold will automatically remove the split.  In this scenario, you will not have to manually restore
 the split transaction.

The following instructions detail
 how to restore a split unpaid transaction.

1. In the AP Payment
 Workfile form, select the split transaction from the grid.

1. Select File > Additional Pay Control Functions.The AP Payment Control Detail
 form displays.

1. Select the Partial
 Payments tab.

1. In the Partial Payments section of
 the form, select one of these
 options:

- Entire Transaction – Select this option to restore the
 entire transaction. Any splits made for partial payments will be removed,
 and all of the unpaid and uncleared sequences by line and pay type will be
 consolidated into one sequence.

- Select Line and Sequence – Select this option to restore a
 selected line. Any splits made for partial payments will be removed, and all
 of the unpaid and uncleared sequences for this line by pay type will be
 consolidated into one sequence. If you select this option, the system
 enables the Line# field.

1. If you chose Select Line and
 Sequence, enter the line to restore in the Line# field.

1. Click Update.

The system removes splits made for partial payments and
 all sequences by pay type are consolidated into a single sequence.

Related concepts

- [About Partial Payments](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-partial-payments)

- [AP Payment Control Detail Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-control-detail-form)

Related tasks

- [Create a Partial Payment](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-partial-payments/create-a-partial-payment)

- [Change the Discount for an Invoice](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/change-the-discount-for-an-invoice)

- [Add or Remove a Supplier From an Invoice](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/add-or-remove-a-supplier-from-an-invoice)
