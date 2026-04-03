---
title: "Applying Cash Receipts Automatically | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receiptsadjustment-entry/applying-cash-receipts-automatically"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receiptsadjustment-entry/applying-cash-receipts-automatically"
---

# Applying Cash Receipts Automatically

Use this procedure to apply cash receipts automatically in
 Accounts Receivable.
This feature will automatically apply the remaining
 undistributed balance to open items currently selected. It will apply the payment in
 oldest-to-newest sequence. the update will affect only invoice and credit memo type items,
 not payments or adjustments.

1. In the Customer field, enter
 the code of the customer who sent the cash payment.

1. In the Transaction code field,
 enter the transaction code for the cash receipt.

1. In the Check # field, enter the
 check number for the cash receipt.

1. Complete the G/L Date, Amount and ABA routing # fields for the cash
 receipt and press Enter.

1. Enter the Applied amount and Discount taken for the receipt.

1. Click the Auto-Apply button.

1. Select the Take discounts past the discount due date checkbox to include discounts past due date. The software will only take discounts past the discount due date if this checkbox is selected.

1. Select the Clear reversing credit memos checkbox to clear reversing credit memos automatically. When you select this checkbox, the software will find invoice number matches only and leave all other credits unapplied. If you want to include any matching credit memos within the selection criteria, be sure to also select the Include adjustment credit memos checkbox.

1. Select the Include adjustment credit memos checkbox to automatically apply selected credit memos and specify a through due date. The software will only apply credits through the date specified.

1. Select the Apply receipt to retention balances checkbox if you want to apply retention balances automatically.

1. Click the OK button and proceed
 with the update. The update first applies all reversing credit memos and invoices,
 and then adjustment credit memos up to the due date specified.Then the update applies
 invoices in due date order. If the remaining unapplied balance is not exactly the
 same as the open invoice amount, the current portion will be applied first, then
 discount, then the retention balance.
