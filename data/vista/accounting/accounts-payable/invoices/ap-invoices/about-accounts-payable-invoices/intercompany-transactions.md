---
title: "Intercompany Transactions | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/intercompany-transactions"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/intercompany-transactions"
---

# Intercompany Transactions

You can use a single AP company to process payables for more than one subledger company.
You must set up an AP company for each HQ company that posts invoices and payments. Typically, this means setting up a separate AP company for each GL company that expenses are posted to (that is, job, equipment, and inventory).

 However, sometimes a single AP company is used to process payables for more than one subledger company. For example, you may post job expenses to JC Co #1 and JC Co #2, but have them invoiced in AP Co#1. How the system updates journal entries in this situation depends on which GL company the expense company is pointing to.
For example, you assign GL Co #1 to AP Co #1. You post expenses to JC Co#1 and JC Co #2, both of which point to GL Co #1. When a batch of transactions is posted, debit and credit entries are made to one GL company (#1).
Example:
If however, the JC companies point to different GL companies, intercompany journal entries will automatically be made based on the accounts specified in GL Intercompany Accounts. When the batch of transactions is posted, debit and credit entries are made to both GL Co #1 & 2.
Example:
Note: For users in Australia and Canada, intercompany Value Added Tax (VAT) transactions will work only when you are not including retention/holdback. If you are processing an intercompany VAT transaction that contains retention/holdback, you must create the bill in the receiving company and the payable in the paying company and then pay and receive.
