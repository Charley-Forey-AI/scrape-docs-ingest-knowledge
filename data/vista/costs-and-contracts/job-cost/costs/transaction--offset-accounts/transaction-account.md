---
title: "Transaction Account | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/transaction--offset-accounts/transaction-account"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/transaction--offset-accounts/transaction-account"
---

# Transaction Account

When posting Cost or Revenue Adjustments, each transaction line
 must be assigned a Transaction Account. This account number initially defaults to the GL
 account specified in the Department file (JC Departments) for the cost type indicated on
 the transaction line.
Note: Transaction accounts must be defined in General Ledger with a Sub Ledger code of ‘J’ or null.
If there is no GL account specified for the cost type in the Department file, you must specify one on the transaction line. Once the line has been assigned a Transaction Account, that account can only be changed (overridden) if the Allow GL Account Override* option is selected.
* For Cost Adjustments, this option is located on the GL Cost tab in JC Company Parameters.
* For Revenue Adjustments, this option is located on the GL Revenue tab in JC Company Parameters.
Note: When posting cost adjustments, if the transaction
 account is assigned a Cross Reference Memo Acct (in GL Chart of
 Accounts), any hours posted for the cost adjustment will be updated to the memo account.
