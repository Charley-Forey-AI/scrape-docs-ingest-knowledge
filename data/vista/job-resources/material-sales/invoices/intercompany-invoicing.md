---
title: "Intercompany Invoicing | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/invoices/intercompany-invoicing"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/invoices/intercompany-invoicing"
---

#  Intercompany Invoicing

Intercompany invoicing is a feature provided by Material Sales that allows you to bill another company within your corporation (sister-company) for materials they purchased from your company.
In order to implement intercompany invoices, you must check the Create Intercompany Invoices option in MS Company Parameters for the “selling” company. If unchecked, journal entries are made to the intercompany AR and AP accounts, but no invoices are created.
 In addition to checking the Create Intercompany Invoices option, you will need to assign a Vendor number to the ‘selling’ company and a Customer number to the ‘purchasing’ company. This is done in HQ Company Setup, in the Intercompany Assignments section of the Addtl Info tab. If both companies will be selling to each other, you will need to assign Customer and Vendor numbers to each company.
Note: It is suggested that you use the same Vendor # and Customer # as the company you are setting up.
Company
Customer #
Vendor #

 1
 1
 1

 2
 2
 2

 If both companies share the same customer and vendor groups, no special setup is required for customer/vendor assignment. However, if each company has their own customer and vendor master files, then you must make sure that the customer and vendor numbers assigned to each company (in HQ Company Setup) exist in both companies as shown in the diagram below.

## Posting Tickets/Hauler Time Sheets and Creating Invoices

 When using intercompany invoicing,
 sales to jobs or locations in another company are treated like customer sales. When
 the batch is processed, the detail for these sales is stored inMaterial Sales Ticket
 Detail (MSTD) so that it can be pulled later when processing the invoices. Job Cost
 and Inventory updates do not occur at this time.
 Material Sales intercompany invoices
 can only be created through initialization (in MS Invoice Initialize). Because the
 ticket (or time sheet) transaction is not posted to a customer, there is no way for
 the system to locate the transaction when you are trying to add it in the
 transaction grid. However, during initialization, when the system encounters the
 intercompany sale, it pulls the “purchasing” company’s customer number (as defined
 in HQ Company Setup) and creates the invoice.
 As with regular invoices, transactions
 assigned to an intercompany invoice cannot be edited. Necessary changes must be made
 by deleting the transaction and invoice, editing the transaction (in MS Ticket Entry
 or MS Hauler Time Sheet Entry), then re-initializing the invoice in MS Invoice
 Initialize.
 When the invoice batch is processed and
 interfaced to Accounts Receivable, the job cost and inventory detail for
 intercompany invoices is stored in the MSII (Material Sales Intercompany Invoices)
 file so that it can be used later to create the Accounts Payable invoices. Once you
 have created the AP Intercompany invoices, Job Cost and Inventory detail is updated,
 and invoices can then be processed in the normal manner.
