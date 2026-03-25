---
title: "Invoice Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/invoices/invoice-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/invoices/invoice-options"
---

#  Invoice Options

The format of Material Sales invoices, from which invoice form is used, to how the information is sorted and printed on the invoice, is determined by several options that are defined at the company and customer levels, with some overrides provided at the quote level or when printing the invoices.
The following is a run-down of these options:

## MS Company Parameters

- Invoice Format – Identifies the
 Crystal Report used to print Material Sales invoices. The default is MS
 Invoices, but you do have the option to specify a format other than the
 standard one provided with Vista software. May be overridden when printing
 invoices (in MS Invoice Print).

- Sort by Sales Date – Identifies
 whether transactions included on the invoice will be sorted by the sales
 date. If checked, the sales date will print on invoices and will be
 available for subtotals.

- Sort by Location – Identifies
 whether transactions included on the invoice will be sorted by the “from”
 location. The “from” location will print on invoices and will be available
 for subtotals. This option should not be used if you will be using the
 “Separate Invoice by Location” option when initializing invoices.

## AR Customers

- Invoice Level – Identifies
 whether a separate invoice will be created for each customer, for each
 customer and job, or for each customer, job, and PO#. May be overridden at
 the quote level.

- Print Level – Indicates the
 lowest level of detail that will be printed on an invoice. If you elect to
 print detail at the “unit price” level, all transactions with the same
 material number, unit of measure, and unit price will be summarized and
 printed as one line on the invoice. If you print at the “transaction #”
 level, one line will be printed on the invoice for each transaction. May be
 overridden at the quote level or invoice level.

Note: If printing at the transaction level (Level 2),
 the ticket number for each transaction will print on the invoice.

- Subtotal Level – Indicates
 the lowest subtotal level that will print on an invoice. There are 6
 levels to select from, each level including subtotals for prior levels.
 Some levels are affected by setup options at the company and/or customer
 level. May be overridden at the quote or invoice level.

- Customer Job(Cannot be used
 if printing at the customer job or customer job/customer PO levels)

- Customer Job/Customer PO
 (Cannot be used if printing at the customer job/customer PO level.)

- Customer Job/Customer
 PO/Date  (Cannot be used if Sort by Sales Date option is not in
 use.)

- Customer Job/Customer
 PO/Date/Location  (Cannot be used if Sort by Location option is not
 in use.)

- Customer Job/Customer
 PO/Date/Location/Material.

- Customer Job/Customer
 PO/Date/Location/Material/UM.

- Separate Haul Info on
 Invoice – Indicates whether haul charges will print in a separate column
 from material amounts on the invoice. May be overridden at the quote or
 invoice level.

## MS Quotes

- Create a Separate Invoice – Overrides the invoice level
 for the customer, indicating that a separate invoice will be generated for
 tickets matching the quote. Typically, you will only check this option for
 customer job or customer job/customer PO# quotes, where you want to override
 the invoice level for a specific job or purchase order for that customer.
 For example, if you normally print separate invoices for each unique
 customer/customer job combination, but have a specific PO for that customer
 that you want printed separately, you would set up a quote for that
 customer/customer job/customer PO#, and set this option to Y (checked). When
 invoices are initialize all transactions referencing the specified
 customer/customer job/customer PO# will be grouped together and printed on
 an invoice separate from the invoice for the customer/customer job.

## MS Invoice Initialize

- Separate Invoice per Location – Indicates that a separate
 invoice will be printed for each unique location. Using this option does not
 nullify the other “separate invoice per” options, it is just an additional
 way to separate groups of invoices. For example, if you are grouping
 invoices together by customer/customer job, normally, all transactions
 pointing to the same customer/customer job will print on the same invoice.
 However, if that same customer/customer job bought materials from two
 separate locations, and you are using this option, two separate invoices
 will print, each containing all transactions posted to the sales
 location/customer/customer job.
