---
title: "Build Finance Charge Transactions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/finance-charge-entry/build-finance-charge-transactions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/finance-charge-entry/build-finance-charge-transactions"
---

# Build Finance Charge Transactions

This window is used to automatically calculate finance charges for all customers who have overdue balances, and who have a finance charges percentage greater than zero entered in the customer file.
 For example, let's assume that an invoice dated 3/1 has terms of net 15 days. Then the due date would be 3/16. When this function is run after the 16th and the invoice is unpaid, it becomes eligible for a finance charge (depending on the finance charge percentage indicated in the customer's file). Note that a grace period can be indicated; if a 10-day grace period were allowed, the invoice in this example would not be considered overdue until after the 26th of the month. In calculating the overdue balance, subject-to finance charge and open balances on adjustment transactions specified in Transaction Code File Maintenance as excluded will not be included in the total. These finance charges are calculated, but are not posted to the customer accounts until both the Finance Charge Update and Cash Receipts Journal update are done. No report prints when this update is executed. Instead, print a Finance Charge Edit List. If the Finance Charge Entry/Change is run again before updating, all existing finance charge transactions are deleted then recomputed.
Finance charge examples:
Assume customer ABC has the following overdue amounts:
Cost center 1: $40
Cost center 2: $10
Cost center 3: $50
Cost center 4: -$5
Minimum charge applied: The finance charge is 5% and the minimum charge is $10. The $10 minimum applies, and is distributed as follows:
Cost center 1: $4.21
Cost center 2: $1.05
Cost center 3: $5.26
Cost center 4: $ .52–
Percentage applied: The finance charge is 5% and the minimum charge is $2. The 5% charge applies, and is distributed as follows:
Cost center 1: $2.00
Cost center 2: $0.50
Cost center 3: $2.50
Cost center 4: $ .25–
