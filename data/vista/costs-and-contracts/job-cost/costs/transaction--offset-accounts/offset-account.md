---
title: "Offset Account | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/transaction--offset-accounts/offset-account"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/transaction--offset-accounts/offset-account"
---

# Offset Account

Offset accounts are used to define the offsetting GL account to the Transaction account. These are needed only on transactions that are posting additional costs or making accrual or reversal entries. They are not required on transactions that are merely to correct a phase code, cost type, or job, or when another transaction is the offset and the two Transaction accounts offset each other or are the same account.
When you specify an offset account, this account will be used any time the detail record is modified in another batch. If you do not use an offset account, then you must create another transaction to which the current transaction will balance. (The amount of each batch that has not yet been distributed to offsetting GL accounts is always displayed on the screen.)
Note: If you are using the Auto Reversal option for any transaction line, you must enter an Offset Account for that line. Additionally, offset accounts cannot have any sub ledger codes assigned to them.
