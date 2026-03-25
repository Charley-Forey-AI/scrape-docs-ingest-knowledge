---
title: "About Subledger Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-accounts/about-subledger-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-accounts/about-subledger-codes"
---

# About Subledger Codes

Subledger codes can prevent you from posting to an incorrect account when posting in the subsidiary ledgers (other modules).
For example, if an account has sub ledger code of 'J', you must be posting to a job. If the account has a code of 'E', you must post to a piece of equipment, and so forth. Available subledger codes are:

- J-Job

- E-Equipment

- I-Inventory

- C-Cash

- P-Payables

- R-Receivables

- S-Service

- Blank (None, use in any)

Because all forms that update Cash, Payables, and Receivables accounts do this automatically without the account being input, all modules (other than General Ledger) will prevent entry of these accounts.
Entry of transactions in the General Ledger will not prevent input of any of these accounts because it is assumed that these are adjusting or correcting entries and that use of the GL forms is restricted to users who understand the implications of their entries.
