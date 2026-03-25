---
title: "MS Invoice Formats | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/invoices/ms-invoice-formats"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/invoices/ms-invoice-formats"
---

# MS Invoice Formats

When an invoice is created, how the detail appears on the invoice is determined by several options.
These include:

- Sort by Sales Date, Sort by Sales Location - These two options are available in MS Company Parameters, and determine whether transactions will be sorted on the invoice by the sales date and/or inventory location. If both options are checked, the sales date and sales location will print on the invoice, and all subtotal levels will be available. If not checked, they will not appear on the invoice, and will affect which subtotal levels are available. (See Subtotal Level option below.)

- Invoice Level - The invoice level is specified for each customer in AR Customers. It determines whether a separate invoice will be created for each customer, for each customer and job, or for each customer, job, and PO#.

- Print Level - The print level is defined by customer (AR Customers), but can be overridden on a quote or by invoice. The print level indicates the lowest level of detail that will be printed on an invoice. You have the option to print detail at the 'unit price' level, which means that all transactions with the same material number, unit of measure, and unit price will be summarized and printed as one line on an invoice. You can also opt to print at the 'transaction' level, which will print one line on an invoice for each transaction.

Note: If printing at the transaction level (Level 2), the ticket number for each transaction will print on the invoice.

- Subtotal Level - The subtotal level is defined by customer using the AR Customers form, but can be overridden on a quote or by invoice. It indicates the lowest subtotal level that will print on an invoice.

Note: The subtotal level specified may be affected by the sort options (Sort by Sales Date, Sort by Location) specified in MS Company Parameters, and by the invoice level specified for the customer in AR Customers.
 For example, if both sort level options are selected, all subtotal levels are available. However, if the ‘Sort by Sales Date’ option is unchecked, the date will not print on invoices; therefore, Level 3 cannot be used. If ‘Sort by Location’ is unchecked, the location will not print on invoices, and Level 4 cannot be used.
 If the invoice level for the customer is set to print separate invoices per customer, then all subtotal levels are available. If printing separate invoices per Customer/Job, Level 1 cannot be used. If printing separate invoices per Customer/Job/PO#, then Levels 1 and 2 cannot be used.

- Separate Haul Info on Invoice - This option is specified at the customer level (AR Customers), but may be overridden on a quote or by invoice. If in use, material information and haul information will print in separate columns on the invoice. Otherwise, haul information will be combined with the material information when invoices are printed. The haul rate will not print, and haul charges will be combined with the material amount. The unit price will then be a calculation of the total amount divided by the number of material units.
