---
title: "Reverse Vendor Invoice | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/reverse-vendor-invoice"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/reverse-vendor-invoice"
---

# Reverse Vendor Invoice

Use the option to reverse invoice entries that have already
 been updated using A/P Transaction Update (which follows the A/P Transaction
 Register).
To reverse an invoice, Spectrum creates a credit memo; to reverse a credit memo, Spectrum creates an invoice. This will leave the correct accounting paper trail. Additionally, Spectrum will automatically update the reversed items to history so that you don't have to create a $0.00 check in order to transfer these entries to the history file.
Important: After reversing entries have been created, the
 reversal will update automatically.The reversal will be added to the vendor open item list
 when the G/L period of the reversal differs from the original transaction. If the reversal
 is assigned a date within the same fiscal period as the original item, both the invoice and
 credit memo will automatically be transferred to vendor history.

- The invoice number of the reversed item will be the same as the original, but with a C instead of an I. If that number already exists as a credit memo, then use of this screen to create the credit memo will be disallowed. Instead, simply add the credit memo manually using [Vendor Invoice Entry](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry).

- When an invoice created using Subcontractor Billing is reversed, the associated quantities are reduced on the subcontract as well when it is a unit price subcontract.

- This screen may only be used to correct open items. If an invoice has already been paid, it will be necessary to void the check before use of this feature.

- You can use this screen to remove a 'Hold" from an invoice.

- If pay-when-paid processing is being used, this update will conditionally set the 'Pay-when-paid' flag in new transactions generated.

- If your A/P invoice was originally created using purchase order packing
 list(s), you will see a message stating "Purchase Order (PO#) receiving will be
 reversed." just below the Invoice Remarks. After the A/P invoice reversal (credit
 memo) has been updated, the Purchase Order > Data Entry > Packing List Quantity Entry should be modified to the correct quantity.

- Create an unposted copy of the original invoice. This allows you to correct entry errors discovered after posting the transaction, such as distributing costs to the wrong job or phase.

- When you are using the two-step receiving method and job accrual methods, a
 reversal will not affect the previous packing lists and updates. When reversed,
 Spectrum will create a credit for the AP invoice and you can proceed with PO
 Receiving again (that is, redo the second step of the two-step process).

- Once you complete this screen and click Continue, the software performs the update. Any images attached to the original transaction will stay with the transaction.
Note: To reverse an invoice or credit memo paid with a credit
 card, create an adjustment/invoice to offset. To void a check or reverse a credit
 card payment in Accounts Payable, use [Void Check Entry](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/void-check-entry).

Related information

- [Reverse Open Invoice Entry Update](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/reverse-vendor-invoice/reverse-open-invoice-entry-update)

- [Performing Invoice Reversals for Previous Months](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/performing-invoice-reversals-for-previous-months)

- [G/L Error Correction](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/gl-error-correction)
