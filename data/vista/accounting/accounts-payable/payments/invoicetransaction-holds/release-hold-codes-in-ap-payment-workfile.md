---
title: "Release Hold Codes in AP Payment Workfile | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/invoicetransaction-holds/release-hold-codes-in-ap-payment-workfile"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/invoicetransaction-holds/release-hold-codes-in-ap-payment-workfile"
---

# Release Hold Codes in AP Payment Workfile

You can release a single non-retainage hold code from a
 transaction or line directly from the AP Payment Workfile grid.
 When you remove a hold code from a transaction, the
 system removes the same hold code from all associated line items. This method only works when
 a single, non-retainage hold code has been applied to a transaction/line. Note: To release a retainage hold code from a transaction, you must use the AP Release
 Retainage form. For more information, see [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice).

1. Open the AP Payment Workfile form.

1. Select the transaction from the grid that you want to
 release a hold code.If your grid does not have any transactions, enter Payment Selection Criteria in the fields at the top of the form, then select Fill Grid. Alternatively, you can manually enter the transaction to be released.

1. Select the Release Hold Code checkbox for the appropriate
 transaction or line.The system displays a message that the hold code was released. If
 there are multiple hold codes, the system displays the AP
 Payment Control Detail form. Use that form to release multiple hold
 codes.

1. Click Close. The system clears the
 On
 Hold checkboxes at the header and line level, and the Release Hold
 Code checkbox remains unselected. When you refresh the screen, the system clears
 both checkboxes.Note: If you are releasing the hold code for the line item, the
 system clears the On Hold and the Release Hold
 Code checkboxes automatically

1. Repeat steps 1-2 for each transaction that requires hold code removal.
