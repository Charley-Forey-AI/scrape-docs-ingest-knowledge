---
title: "About the MS Invoice Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/invoices/about-the-ms-invoice-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/invoices/about-the-ms-invoice-initialize-form"
---

# About the MS Invoice Initialize Form

 Use this form to initialize invoices for customer sales based on entries in MS
 Ticket Entry or MS Hauler Time Sheet Entry.
You can open this form by selecting
 File > Initialize Invoices in [MS Invoice
 Edit](/en/vista/vista/job-resources/material-sales/invoices/about-the-ms-invoice-edit-form).
 Various selection criteria allow you to
 control what transactions are eligible for invoice initialization. You can restrict
 initialization based on location group, location, customer, customer job, and
 customer PO, bill frequency, and/or payment type.
 You also have the option to print
 separate invoices per location group or location. Typically, you will use one option
 or the other, since using both options may produce an effect opposite of what you
 want. For example, if you elect to print separate invoices per location group, each
 invoice for a customer will include transactions posted to all locations within the
 location group. Selecting the option to print separate invoices per location will
 override the 'separate invoices per location group', and you will get separate
 invoices for each location instead of for each location group.
 Once the criteria is defined, only
 those tickets or hauler time sheets that match the specified criteria will be
 initialized into the invoice batch. You can make multiple passes by changing the
 selection criteria and then reinitializing the batch. Each pass will add new
 invoices to the existing entries in the batch.
 During initialization, the system
 automatically:

- assigns an invoice number to each invoice based on either
 the 'Last Invoice Number' in AR Company Parameters (if using invoice numbers
 from AR ) or the 'Last Used MS Invoice #' in MS Company Parameters (if using
 invoice numbers from MS).

- assigns the invoice date specified in the initialization
 criteria to each invoice.

- assigns a discount date and due date to each invoice based
 on the specified invoice date and payment terms. If you are printing a separate
 invoice for each customer/customer job or customer/customer job/PO#, the system
 uses the payment terms specified on the quote (if quote exists). Otherwise, uses
 payment terms specified for each customer in AR Customers.

 When the initialization process is
 over, the system alerts you to the number of initialized tickets, as well as the
 number of skipped tickets due to incomplete receivable types. You can then edit
 invoices as necessary (though editing is limited) in MS Invoice Edit. You can then
 use the “Print Invoices” option in MS Invoice Edit (File menu) to print and post the
 invoice batch.

## Discounts

Discounts offered for early payment of invoices are calculated during ticket and/or
 hauler time sheet entry, and will appear at the bottom of the invoice. Discounts are
 calculated as follows:

1.  If the payment terms specified on the invoice are rate
 based, discounts are calculated on the material total using the discount
 rate specified in HQ Payment Terms. If haul charges exist, they will be
 included in the discount calculation.

1.  If the payment terms are material based, and the
 discount type is ‘rate’, calculation will be the rate times the material
 total. If discount type is ‘unit’, it will be the rate times the number of
 material units sold. Haul charges are not included in material-based
 discounts.

## Cutoff Date

If a cutoff date is specified for the customer’s payment terms (in HQ Payment Terms),
 the system will use that date when determining the invoice’s due dates and discount
 dates.
The following is a brief explanation of
 how the cutoff date affects the calculation of due dates and discount dates.
 If the invoice date falls prior to both
 the ‘Due Date’ and the ‘Cutoff Day’, then the calculated due date will be in the
 same month as the invoice date. The same is true for discounts, except that the
 ‘Discount Day’ is used instead of the ‘Due Day’.
 For example, you generate invoices on
 the 5th of July. The payment terms specify a ‘Cutoff Day’ of the 25th, and a ‘Due
 Day’ of the 30th. Therefore, the default due date for the invoice will be the 30th
 of July.
 If the ‘Due Day’ or ‘Cutoff Day’ falls
 on or before the invoice date, then the due date will fall in the next month.As with
 the previous scenario, the ‘Discount Day’ is used instead of the ‘Due Day’.
 For example, you are invoicing on the 5
 of July. The payment terms specify a ‘Cutoff Day’ of the 1st and a ‘Due Day’ of the
 5th. The default due date will be the 5th of August.

## Intercompany Invoices

If you are using the intercompany invoicing feature (flag in MS Company Parameters),
 you can only create intercompany invoices through initialization.
Because the ticket (or time sheet)
 transaction is posted to a job or inventory location instead of a customer, there is
 no way for the system to locate the transaction when you are trying to add it in the
 transaction grid. However, during initialization, when the system encounters the
 intercompany sale, it pulls the “purchasing” company’s customer number (as defined
 in HQ Company Setup) and creates the invoice.
 When initializing invoices for
 intercompany sales to 'Jobs', if you have set the "Invoice Level" (in AR Customers)
 to 1 (One invoice per Customer Job) for the 'sell to' company, the invoice
 initialization process will create a separate intercompany invoice for each job by
 substituting the JC Job for the Customer Job. The JC Job will be interfaced to AR in
 the same manner as Customer Jobs are for true customer sales.
 When the invoice batch is processed and
 interfaced to Accounts Receivable, the job cost and inventory detail for
 intercompany invoices is stored in the MSII (Material Sales Intercompany Invoices)
 file so that it can be used later to create the Accounts Payable invoices. Once you
 have created the AP Intercompany invoices, Job Cost and Inventory detail is updated,
 and invoices can then be processed in the normal manner.
