---
title: "About the MS Invoice Edit Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/invoices/about-the-ms-invoice-edit-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/invoices/about-the-ms-invoice-edit-form"
---

# About the MS Invoice Edit Form

Use this form to perform all of the functions related to a batch of MS invoices.
This includes initializing, editing, and printing invoices, manually entering and printing new invoices, adding existing invoices into a batch for a reprint, voiding invoices, and posting invoices to AR.
Whether you are creating a new invoice or editing an existing one, this form only allows you to delete or add transactions to the invoice. You do not have access to the transaction line fields. If a transaction (ticket or time sheet) requires editing, delete it from the invoice, pull it up in MS Ticket Entry or MS Hauler Time Sheet Entry, make the necessary changes, and then add it back to the invoice.
Note: Once you have interfaced an invoice to AR/GL (in MS Batch
 Process), the transactions are no longer available for editing. If you need to make
 corrections to an invoice that has already been posted to AR/GL, see [Correcting Invoiced Transactions](/en/vista/vista/job-resources/material-sales/invoices/correcting-invoiced-transactions).

- Surcharges - Surcharges assessed for a ticket will show as a separate transaction line on the invoice. If you remove the parent transaction from the invoice, make sure you also remove the surcharge transaction. If you removed a ticket from the invoice for editing purposes, once you pull the ticket back into a ticket batch for editing, the system will flag the surcharge transaction for deletion and then reassess the surcharges once you save the edits to your ticket. When you add the ticket back to an invoice, the new surcharge line will be included.

- Intercompany Invoices - If you use the 'intercompany invoicing' feature, you cannot add intercompany invoices manually; use MS Invoice Initialize to initialize them. As with regular invoices, you cannot edit transactions for intercompany invoices. Necessary changes must be made by deleting the transaction and invoice, editing the transaction (in MS Ticket Entry or MS Hauler Time Sheet Entry), then re-initializing the invoice in MS Invoice Initialize.

- Cash Sale Invoices - Cash sale invoices are those
 invoices where the payment type is cash. If you are using the Auto Apply Payment
 on Cash Sales feature (in MS Company Parameters), the system will automatically
 apply payments to these invoices when they are interfaced to AR. The system uses
 the CM Account information set up in AR Company (with overrides by Location) to
 apply payments. A deposit transaction is created in CM, with the deposit number
 being a unique number based on the posting date and auto-generated sequence
 number. For example, if you posted the invoice on December 15, 2008, the deposit
 number would be 081215-1. If you specified a check number during ticket entry
 and invoices are initialized, a separate invoice is generated for each unique
 check number. Transactions with the same check number will be grouped together
 on the same invoice. If you did not specify a check number during ticket entry,
 transactions will be group together and a single invoice generated. When the
 invoice batch is processed, a payment is generated for each invoice. Note: When initializing invoices, the invoice
 level specified for each customer (in AR Customers) will affect how invoices
 are generated, regardless of check number assignment. This is also true if
 you selected the Separate Invoice per Location option during invoice
 initialization.

For example, if you specified to generate a
 'separate invoice per customer job', and you have two tickets with the same check
 number but differing customer jobs, two invoices will be generated, both with the
 same check number. However, if both tickets have the same customer job, only one
 invoice will be generated.

- Adding Transactions to Cash Sale Invoices - If you are using the 'auto apply payments' feature, regardless of whether you initialize invoices or enter them manually, you can only add transactions to an invoice that have the same check number as specified in the invoice header. Transactions that were not assigned an invoice number can only be added to an invoice that has no assigned check number.
