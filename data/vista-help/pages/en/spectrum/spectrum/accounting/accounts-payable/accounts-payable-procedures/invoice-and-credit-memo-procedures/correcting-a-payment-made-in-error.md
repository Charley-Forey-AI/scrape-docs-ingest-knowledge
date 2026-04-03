---
title: "Correcting a Payment Made in Error | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/invoice-and-credit-memo-procedures/correcting-a-payment-made-in-error"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/invoice-and-credit-memo-procedures/correcting-a-payment-made-in-error"
---

# Correcting a Payment Made in Error

The invoice arrives from the vendor.

- the invoice is entered

- the invoice is updated to the vendor's account and to the G/L
At this point, there is an Open invoice on the vendor account, and a credit balance in the G/L accounts payable account.
Credit: AP Debit: the G/L account(s) entered on the lower half of A/P Vendor Invoice Entry

1. A check is issued to pay the invoice.

- the invoice is selected for payment

- the pre-check register is printed and reviewed for accuracy

- the check is printed

- the payment is updated to the vendor's account

- the check run is updated to the G/L
At this point, there is no longer an Open item on the vendor account; there is one record in the vendor history for the above payment. There is no balance in the G/L Accounts Payable account.
Debit: AP Credit: Cash

1. Discover that the invoice should not have been paid. Void the check.

- void the check

- update the void entry to the vendor's account

- update the void entry to the G/L
At this point, there is again an Open item on the vendor's account and a credit balance in the G/L Accounts Payable account. The vendor's history contains two records: the original payment record, plus a new record for the void transaction.
Debit: Cash
Credit: AP
Important: The invoice is now ready to be paid. If it will be paid at a later date, proceed as usual. If the invoice will never be paid and should be removed entirely, proceed with steps four and five.

1. Create a credit memo to offset the invoice.

- create a credit memo for the invoice

- update the credit memo
At this point, there are two Open items on the vendor's account: one for the invoice and one for the credit memo. There are still two records in the vendor history. There is no balance in the G/L Accounts Payable account.
Debit: A/P
Credit: the G/L account(s) originally entered for the invoice on the lower half of Invoice Entry.

1. Clear the A/P accounts

- select BOTH the invoice and the credit memo

- the pre-check register is printed and reviewed for accuracy

- a void check is printed

- both payments are updated to the vendor's account

- the check run is updated to the G/L
At this point, there are no Open items on the vendor's account and there are four entries in the vendor's history, leaving a proper paper trail for accounting purposes. The two previous records are retained, and one entry each is added for the invoice and credit memo from the latest check run. There is no affect on the G/L since the check was for net-zero.
