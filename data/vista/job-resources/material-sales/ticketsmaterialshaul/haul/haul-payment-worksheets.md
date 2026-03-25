---
title: "Haul Payment Worksheets | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/haul-payment-worksheets"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/haul-payment-worksheets"
---

# Haul Payment Worksheets

The MS Haul Payment Worksheet program allows you to generate AP invoices from vendor payment information entered on tickets or time sheets, then update the invoices to AP for payment.
Note: If you are handling vendor payments directly in
 Accounts Payable and do not enter payment information on tickets or time sheets, you
 will not need to use the Haul Payment Worksheets program.
You can either initialize invoices using the
 Initialize Payments option (File menu) or add the entries manually. Initialization
 allows you to automatically generate invoices from ticket or time sheet entries using a
 series of criteria. Transactions can be restricted by location group, location, and/or
 haul vendor. You can also restrict transactions based on sales dates. Once you have
 defined the criteria, the initialization process will generate invoices for all
 transactions meeting the specified criteria. Only one invoice is generated per haul
 vendor, so if multiple transactions exist for a vendor, they will be added to the same
 invoice.
If you are manually entering payments,
 header information is entered manually, and transactions are added in the grid based on
 data in the header. Only ticket and hauler time sheet transactions not already updated
 to AP that were posted in the same month as the current worksheet batch may be added.
 Additionally, transactions must be posted to the same haul vendor specified in the
 header.

## Editing Haul Payment Transactions

Once transactions have been added to the grid (whether through initialization or
 manually), you can delete them or make limited changes to them.
This includes changing the Pay Code,
 Basis, Pay Rate, and/or Amount. However, any other changes must be made in the
 originating program (i.e. Ticket Entry or Hauler Time Sheet Entry).
For Australian and Canadian companies:
 You can also enter/edit haul payment tax information (tax type, code, basis, and
 amount) for eligible transactions. See [MS Haul Payment Worksheet](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-payment-worksheet-form) for more information.
If you enter haul charges and payment
 information on time sheets, then reconcile (verify) them with existing tickets, both
 transactions will be pulled into the worksheet during initialization. Since haul and
 payment information was not entered with the ticket, the ticket transaction will not
 be assigned a pay code. In addition, the Basis, Pay Rate, and Amount values will be
 set to 0.00 (as shown in Trans# 21 below). Be careful that you do not duplicate
 payment information (as shown in second illustration).
Correct
Incorrect

## Deleting Haul Payment Transactions

If you delete transactions from the worksheet, they will not be included with the
 current invoice, but will be available for future invoicing. If you not want to pay
 a transaction, but do not want it to keep appearing each time you initialize a new
 batch, you can change the payment Amount to 0.00. This allows you to process the
 transaction without paying it, and in addition, will link the transaction to the AP
 reference number.

## Updating Haul Payment Transactions to AP

When you are ready to update haul payment information to AP, select the Batch Process
 option from the File menu and process the batch as normal. When interfaced to AP,
 the AP reference is recorded in Ticket Detail (MSTD), providing a link to AP
 transaction tables.
