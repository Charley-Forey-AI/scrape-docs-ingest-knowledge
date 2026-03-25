---
title: "About Updating Hauler Payments to AP | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-updating-hauler-payments-to-ap"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-updating-hauler-payments-to-ap"
---

# About Updating Hauler Payments to AP

When you post a hauler payment batch (using MS Batch Process), the system creates AP invoices based on the information provided in the MS Haul Payment Worksheet form.
The information from the hauler payment
 worksheet is used to create expense invoice transactions in Accounts Payable and post
 corresponding GL distributions in General Ledger. When you post the batch, any changes
 to hauler payment information entered in the worksheet, along with the assigned AP
 Reference, update back to the Transaction Detail table (MSTD).
The system creates a single AP invoice for
 each sequence in the batch. Separate expense lines are created for each Haul Expense GL
 Account to be debited. Haul Expense accounts can be based on the selling location, sale
 type, sold to company (if intercompany sale), and material category. If offering
 discounts and expensing net amounts (i.e. Post Discounts Offered to GL and Net Amounts
 to Subledgers option is checked in AP Company Parameters), separate expense lines will
 also be created for each discount offered.
Updates to GL are controlled by the GL
 Expense Posting level selected for expense transactions in AP Company Parameters.

- Summary - If interfaced at this
 level, entries will be summarized and one entry will be posted to GL per each
 batch sequence, GL company, and GL account. The Summary GL Description specified
 for expense transactions will be used as the GL transaction description.

- Transaction - If interfaced at this
 level, one entry will be posted to GL for each batch sequence, GL company, GL
 account, and transaction number. Vendor #, Sort Name, AP Reference, and/or other
 fields selected for that level of update in AP Company will be used to create
 the GL transaction description.

- Line - If interfaced at this level,
 one entry will be posted to GL for each batch sequence, GL company, GL account,
 transaction number, and line. Vendor #, Sort Name, AP Reference, and/or other
 fields selected for that level of update in AP Company will be used to create
 the GL transaction description.

## GL Distributions - AP GL Company

DebitCredit
 Intercompany AR GL
 Account
(Based on the MS
 and AP GL Companies. Offsets the material expense payable. Only
 used if the MS & AP GL Companies are not equal.)
 Accounts Payable GL
 Account
(Based on the
 Expense Pay Type assigned in AP Company Parameters. Use total
 invoice amount.)

## GL Distributions - MS/IN GL Company

DebitCredit
 Material Expense GL
 Account
 (Based on the
 location and sale type, with overrides by ‘sell to’ company,
 material category, or both.)
InterCo AP GL
 Account
 (Based on the MS
 and AP GL Companies. Offsets the material expense. Only used if
 the MS & AP GL companies are not equal.

Related information

- [About the MS Haul Payment Worksheet Form](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-payment-worksheet-form)
