---
title: "Unposted Transactions in Spectrum | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/general-ledger-inquiries-overview/unposted-transactions-inquiry/unposted-transactions-in-spectrum"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/general-ledger-inquiries-overview/unposted-transactions-inquiry/unposted-transactions-in-spectrum"
---

# Unposted Transactions in Spectrum

Each transaction has a source file which shows where it originated from. The table below shows the transactions and why they are unposted.
Transaction source
What is counted?
Which date is used to determine unposted items?
Tip to resolve

Accounts Payable invoices / credit memos
Count unposted records from Vendor Invoice Entry
G/L date of invoice
Highlight the source and click Update.
With the cursor on the Batch field, click the drop-down arrow. Select a batch code and click Details to view the unposted transactions.

Accounts Payable manual checks
Count unposted checks from Manual Check Entry
Check date
There are two possible solutions here:

- Highlight the source and click Update. With the cursor on the Batch code field, click the drop-down arrow to view the unposted transaction count by batch.

- Navigate to Accounts Payable  >  Data Entry  >  Credit Card Payments. Click Update. With the cursor on the Batch code field, click the drop-down arrow to view the unposted transaction count by batch.

Accounts Payable void checks
Count unposted, non-zero checks from Void Check Entry
Void transaction date
Highlight the source and click Update.

Accounts Payable regular checks
Count checks that have been printed in Payment Processing / Print Checks
Check date
Highlight the source and click Update.
Preview the A/P Payment Register and update.

Accounts Payable payment G/L transactions
Count unposted transactions on the Payments G/L Report
G/L date
Highlight the source and click Update.
Preview the Payments G/L Register and update.

Accounts Receivable invoices / credit memos
Count unposted records from Customer Invoice Entry
G/L date of invoice
Highlight the source and click Update.
With the cursor on the Batch field, click the drop-down arrow to view the unposted transaction count by batch.

Accounts Receivable draw requests
Count draws with non-zero 'this period' billing from Draw Request Entry.
Period-to date (but ignore draws with blank date)
Highlight the source and click Update.
Press Enter to accept the batch code.
Click the Select button to open the Select Applications to Update window.
Unposted draws are those with an amount in the 'This period billing' column. In other words, only those with current billing (not zero) are counted.

Accounts Receivable cash receipts / adjustments
Count unposted checks from Cash Receipts Entry and Misc. Cash Receipts screens.
Transaction date
Highlight the source and click Update.
With the cursor on the Batch field, click the drop-down arrow to view the unposted transaction count and amounts by batch.

Accounts Receivable finance charges
Count unposted transactions in Finance Charge Entry / Change
Transaction date
Highlight the source and click Update.
View the unposted finance charges in detail on Finance Charge Entry.

Cash Management reconciliation transactions
Count addition and deduction transactions from Reconciliation Adjustments Entry
Transaction date
Highlight the source and click Update.
By account, preview the Other Reconciliation Adjustment Register.
Cancel the update.

Cash Management direct checks
Count unposted direct checks
Check date
Highlight the source and click Update.
By account, preview the Direct Checks Register.
Cancel the update.

Cash Management void direct checks
Count unposted void direct checks
Void transaction date
Highlight the source and click Update.
By account, preview the Void Direct Checks Register.
Cancel the update.

Cash Management wire transfers
Count unposted records from the Wire Entry screen
Transaction date
Highlight the source and click Update.
By account, preview the Wire Transfers Register.
Cancel the update.

Cash Management void wire transfers
Count unposted void records from Void Wire Transfer Entry
Void transaction date
Highlight the source and click Update.
By account, preview the Void Wire Transfers Register.
Cancel the update.

Equipment Control transactions
Count unposted transactions from the detail portion of Equipment Transaction Entry
Transaction date
Highlight the source and click Update.
Preview the Ownership Cost G/L Register.
Cancel the update.

Equipment Control G/L transactions
Count unposted transactions on the Equipment Control G/L Report
Transaction date
Highlight the source and click Update.
With the cursor on the Batch field, click the drop-down arrow to view the unposted transaction counts.

Equipment Control depreciation / license / insurance
Count unposted transactions from the detail portion of Depreciation/License/Insurance Entry
Last day of period assigned to transaction
Highlight the source and click Update.
Preview the Ownership Cost Journal.
Cancel the update.

Equipment Control DLI G/L transactions
Count unposted transactions on the Depreciation/License/Insurance G/L Report
Transaction date
Highlight the source and click Update.
Preview the Ownership Cost G/L Register.
Cancel the update.

Fixed Assets depreciation
If the cycle is fully updated, set record count to zero. Otherwise, count assets with non-zero current depreciation from Depreciation Entry / Edit
Depreciation date
Highlight the source and click Update.
Preview the Fixed Assets G/L Summary Report.
Cancel the update.

General Ledger journal entries
Count unposted journal entries with detail records
Journal entry date
Navigate to General Ledger  >  Data Entry  >  Journal Entry to view unposted entries.

Inventory Control shipped job requisitions
Count requisitions with status of Shipped from Job Requisition Entry
Ship date (but ignore requisitions with blank date)
Highlight the source and click Update.
Preview the Inventory Transaction Report.
Cancel the update.

Inventory Control physical inventory transactions
If a physical inventory is not in progress, set record count to zero. Otherwise, count transactions from Physical Count Data Entry
Current Inventory Control processing date
Highlight the source and click Update.
Preview the Count Transaction Listing to view the unposted records.

Inventory Control other transactions
Count unposted transactions on the Inventory Transaction Report
Transaction date
Highlight the source and click Update.
Preview the Inventory Transaction Report.
Cancel the update.

Inventory Control G/L transactions
Count unposted transactions on the Inventory G/L Report
G/L date
Highlight the source and click Update.
Preview the Inventory Transaction Report.
Cancel the update.

Job Cost Transactions
Count unposted transactions from detail records in Job Cost Transaction Entry
Transaction date
Highlight the source and click Update.
With the cursor on the Batch field, click the drop-down arrow to view the unposted transactions.

Job Cost G/L transactions
Count unposted transactions on the Job Cost G/L Report
Transaction date
Highlight the source and click Update.
Preview the Job Cost G/L Detail Report.
Cancel the update.

Materials Management
Count tickets from Scale Ticket Entry
Scale ticket date
Highlight the source and click Update.
With the cursor on the Ticket # field, click the drop-down arrow to view the unposted transactions.

Order Processing invoices
Count unposted invoices from Invoice Entry
Invoice date
Highlight the source and click Update.
Preview the Invoice Register Report.
Cancel the update.

Order Processing G/L transactions
Count unposted transactions on the Invoice G/L Report
G/L date
Highlight the source and click Update.
Preview the Invoice G/L Detail Report.
Cancel the update.

Order Processing unprinted invoices
Count invoices that have not been printed.
Invoice date
Highlight the source and click Update.
Preview the OP Invoice Print, set for first print only.

Payroll time cards
If the cycle is fully updated, set record count to zero. Otherwise, count time cards from Time Card Entry
Check date assigned to pay cycle
Highlight the source and click Update.
Select Time Card Listings.
Preview the report to view unposted time cards.

Purchase order 2-step receiving with packing list update
Count purchase orders from Packing List Quantity Entry that have not yet been updated to Inventory
Receipt date
Highlight the source and click Update.
Preview Summary Packing List Quantity Edit List.
Cancel the update.

Service Contract Earned Revenue Transactions
Count number of scheduled records from Service Contract Billings
Scheduled date
Highlight the source and click Update.
Preview Earned Revenue Register.
Cancel the update.
