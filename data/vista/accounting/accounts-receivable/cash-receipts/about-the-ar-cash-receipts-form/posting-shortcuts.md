---
title: "Posting Shortcuts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/posting-shortcuts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/posting-shortcuts"
---

# Posting Shortcuts

There are several shortcuts available for posting payment
 information in the AR Cash Receipts form.
Shortcuts are only available from the Total Applied field during Add mode. Available shortcuts include:
Ctrl + A
This shortcut sets the amount in the Total Applied field to the
 Current Due amount. If
 applicable, it also sets the Tax
 Applied column to the amount in the
 UnPaid Tax field, the
 FC Applied column to the
 amount in the UnPaid FC
 field, the Disc Taken to
 the available discount amount (Disc
 Offered field minus Prev
 Disc Taken), and the Tax
 Disc to the amount in the
 Avail TaxDisc field.
 Disc Taken and
 Tax Disc amounts are only
 applied if the transaction date is less than or
 equal to the selected invoice's discount date.

Ctrl + W
This shortcut sets the Disc Taken amount to the available discount amount
 (Disc Offered field minus
 Prev Disc Taken field).
 This shortcut is only applicable if a discount
 applies to an invoice (set during invoice entry).
 This function allows you to auto apply the
 discount even when the transaction date is greater
 than the invoice's discount date.

Ctrl + E
This shortcut sets the Tax Disc to the Avail
 TaxDisc amount. This shortcut is only
 applicable if a discount applies to an invoice
 (set during invoice entry). This function allows
 you to auto apply the discount even when the
 transaction date is greater than the invoice's
 discount date.

Ctrl + F
This shortcut changes the Total Applied amount to the Due Less
 FC amount and removes the
 UnPaid FC amount from the
 FC Applied column.

Ctrl + G
This shortcut sets the Retg Applied amount to the UnPaid
 Retg amount and updates the
 Total Applied column by the
 same amount. If you are using the
 Distribute Tax to Retainage
 feature (AR Company Parameters), unpaid retainage
 includes retainage tax.

Ctrl + Q
This shortcut reduces the Total Applied amount by the Tax
 Applied amount

Note: Reverse the above options by re-clicking the shortcut keys.

Ctrl + T
This shortcut processes a tax reversal for the selected invoice. This option allows you to
 reverse unpaid taxes that were included on the
 invoice. When entering this shortcut, a prompt
 displays. Click Yes to
 process the tax reversal. If there is unpaid tax
 for the invoice, the system creates an adjustment
 transaction in AR Invoice Entry and applies it to
 the original invoice. A message displays, stating
 that an invoice entry batch was created, along
 with the batch month and ID. The system updates
 the current transaction to reflect the tax
 adjustment (the UnPaid Tax
 field is set to 0.00 and the Current
 Due column adjusts accordingly). If
 tax has been paid on the invoice, a message
 displays that that the system will not reverse tax
 until the partial tax payment has been deleted or
 reversed. If tax was not originally applied, or
 was written off, a message displays stating that
 there is not any tax to write off.

Note: The system adds the Tax Reversal and Apply Retainage adjustment transactions to an AR batch. If a batch is already open, the system adds the transaction to the existing batch. If an open batch does not exist, the system opens a new batch. Post transactions in the usual manner.
