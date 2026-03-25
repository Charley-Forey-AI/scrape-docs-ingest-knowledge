---
title: "About General Ledger and Subledger Posting Levels | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/ap-company-setup/about-general-ledger-and-subledger-posting-levels"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/ap-company-setup/about-general-ledger-and-subledger-posting-levels"
---

# About General Ledger and Subledger Posting Levels

Vista™ allows you to define the level of detail that you want posted from Accounts Payable to the General Ledger accounts and to the subledgers of Job Cost, Equipment Management, Inventory, and Cash Management.
As part of the implementation process, interfaces can be suppressed to allow the set up of open transactions in AP without updates to modules that will have directly entered balance forwards.
Interfaces to General Ledger may be done in summary or detail for both invoice entry (GL Expense Posting tab) and payments (GL Payment Posting tab). If summary is chosen, a single transaction is posted to each account affected within a batch. You can determine the transaction description that is posted. If detail is chosen, a single transaction is posted for each account affected within an invoice transaction, or for each invoice line and for each check payment. The description of the GL transaction may consist of various elements of the AP transaction. You can determine which elements are used and in what order. If summary is chosen here, GL accounts that have the Interface Detail box checked in the GL Chart of Accounts form are still interfaced in detail.

## Subledgers

Interfaces to Job Cost and Equipment Management allow an option for detail at the transaction or line level. A separate entry is made for each Job/Phase/Cost Type or Equipment/Cost Code/Cost Type regardless of the option selected. If there are multiple lines each within different materials or parts going to the same cost record, the transaction/line level option is used to determine if one or more records go to the detail files (JCCD or EMCD).
Interfaces to Inventory allow for detail at the line level. A separate entry detail entry is created per Batch, IN Co#, Location, Material, AP Trans#, and AP Line#. All units are converted to the Material’s standard unit of measure.
Interfaces to Cash Management allow for detail at the payment level. One CM detail entry is created per Batch, CM Co#, and CM Reference. If the entry corresponds to a check number, vendor is included in the detail. If the payment is an EFT, only the total amount is recorded.
