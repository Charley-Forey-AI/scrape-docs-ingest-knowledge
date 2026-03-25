---
title: "Invoicing | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/invoices/invoicing"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/invoices/invoicing"
---

# Invoicing

 The Material Sales invoice programs are used to bill customers for materials they have purchased from your company. Invoices are based on tickets or time sheets posted to customers in MS Ticket Entry or MS Hauler Time Sheet Entry, respectively, and are created using either of the following methods:

- Automatic Invoicing – Invoices are generated automatically from tickets and hauler time sheets using the MS Invoice Initialize program (accessed by selecting the Initialize Invoices option from the File menu of MS Invoice Edit). Using the specified selection criteria (i.e. location group, location, customer, customer job, customer PO#, billing frequency, payment type, and/or date range), the system automatically creates invoices for the eligible tickets and time sheets based on each customer’s invoice level (as specified in AR Customers). If a quote exists for a customer, and the “Create a Separate Invoice” option is checked, separate invoices will be generated for tickets and time sheets posted to that quote, based on the customer’s invoice level. For example, if a customer’s invoice level is set to summarize sales onto a single invoice, but a quote for one of the customer’s jobs is flagged to create a separate invoice, sales to that customer job will be put on one invoice, and other sales to that Customer will be put on another.

- Manual Invoicing – Invoices can be entered directly in the MS Invoice Edit program. The invoice header contains information such as receivable type, pay terms, invoice, discount, and due dates. You can also override the print and subtotal levels for the invoice, and indicate that haul information will be printed in a separate column on the invoice. The lower section of the form contains the transaction grid, which allows the addition (or deletion) of transactions to the invoice by transaction number.

 Regardless of how transactions are added to invoice, they cannot be edited in this program. The transaction information is display only; therefore, any corrections that you need to make must be made in the source program (i.e. MS Ticket Entry or MS Hauler Time Sheet Entry). To do this, highlight the transaction in the grid, and delete it. It can then be pulled into a batch in the source program, corrected as needed, reprocessed, and then added back to the invoice in MS Invoice Edit.
Note: This process can only be accomplished if you HAVE NOT already interfaced the invoice to AR and GL.
 You can initialize and process invoices as soon as you have processed a batch of tickets. However, because ticket detail is available until it is purged (in MS Purge), you can schedule your invoicing based on your company’s needs, whether on a daily, weekly, or monthly basis.
 Once the invoices have been generated and you
 are satisfied with them, select the Print Invoices option from the File menu, which will
 bring up the MS Invoice Print program. Invoices can be sorted and printed by customer
 number, sort name, or invoice number. The format of the invoice is determined by the
 Invoice Format option specified in MS Company Parameters (may be overridden at the time of
 printing) and the print and subtotal levels specified for the customer (or overridden by
 quote). For more information, see Invoice Options in Related Topics below.
 When invoices are initialized, cash sales are
 grouped together by customer and check number. These invoices are not generally printed,
 but will update AR and GL when the batch is posted. If you are using the Auto Apply
 Payments on Cash Sales option (MS Company Parameters), payments will be automatically
 created during the interface and cash receipts will be applied to their corresponding
 invoice. CM detail will reflect a deposit for each CM company and CM account in the batch
 using a deposit reference comprised of the date posted and a sequence number.
