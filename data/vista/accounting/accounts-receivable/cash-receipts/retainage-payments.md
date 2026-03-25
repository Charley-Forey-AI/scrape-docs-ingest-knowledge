---
title: "Retainage Payments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/retainage-payments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/retainage-payments"
---

# Retainage Payments

If you have posted retainage to AR invoices, you can have the system automatically apply payment to the unpaid portion of the retainage.
If you selected the Include Retainage checkbox in AR Initialize Receipt, the
 system automatically applies the payment to both the amount due and unpaid retainage for each item until
 payment is satisfied. If the amount of the check is not sufficient
 to cover both the amount due and the unpaid retainage for an item, the payment is applied to the amount due only. You can adjust applied amounts manually for any item.
Note: If you do not select the Include Retainage checkbox in the
 Apply Payment window, you can still apply payment to retainage by entering the amount
 manually.
It is important to note that when you are
 applying a payment to retainage, the amount displayed in the Amount Due column does not
 reflect the unpaid retainage amount. Therefore, you must adjust the Applied Amount to
 include both the Amount Due and the Unpaid Retg. For example, if the Amount Due is
 $1000 and the unpaid retainage is $100, the Applied Amount must be $1100.

## Retainage Tax

If you selected the Distribute Tax to Retainage checkbox in AR Company Parameters, the system calculates retainage tax separately during invoice entry. It is generally considered payable when retainage is released. However, you can apply payment to retainage before it is
 released (typically used if you do not release retainage in AR Release
 Retainage). When you apply payment to retainage (manually or via initialization), it is
 automatically applied to the retainage tax as well. If you selected the Include Apply
 RetgTax in Grid checkbox (Options menu), the amount applied to retainage tax displays in
 the Apply RetgTax column. You can override the amount if necessary, as long as the
 amount does not exceed the amount of retainage tax due.
