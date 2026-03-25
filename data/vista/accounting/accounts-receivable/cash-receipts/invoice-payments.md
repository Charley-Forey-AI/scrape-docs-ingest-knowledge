---
title: "Invoice Payments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/invoice-payments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/invoice-payments"
---

# Invoice Payments

If you initialized payments (using AR Initialize Receipt),
 the system applies payments based on the information entered during initialization.
If the payment amount fully covers the
 invoice, the appropriate amount is applied to each line on the invoice. If the payment
 amount does not fully cover the invoice, the system will apply the payment to each item
 on the invoice (sequentially) until the payment amount is fully distributed. You can
 change the applied amounts as necessary and/or the items to which the payment is
 applied. If taking a discount, do not subtract that amount from the amount you are
 applying. The system will automatically adjust the Total payment (shown above the grid).
 For more information about taking discounts, see the Discount Taken subtopic below.
Note: If the selected invoice was created in Job Billing
 and still contains open retainage, a warning is displayed (in red) as a reminder that
 when applying cash to Unpaid Retainage in AR, the Open Retainage value in JB becomes
 inaccurate.
If you did not initialize payments, you must
 apply payment to invoice lines manually. You can enter the Apply Amount, Apply Tax,
 Apply Retg, and Apply FC charge values manually or have the system apply them
 automatically by placing focus in the Apply Amount column and pressing Ctrl + A. Payment
 amount must be sufficient to cover the indicated amounts.
