---
title: "About the MS Invoice Print Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/invoices/about-the-ms-invoice-print-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/invoices/about-the-ms-invoice-print-form"
---

# About the MS Invoice Print Form

Use this form to print Material Sales invoices.
You can access this form by selecting File > Print Invoices from MS Invoice Edit.
 Options are provided that allow you to specify which invoice format to use, the order in which to sort and print invoices (customer number, sort name, or invoice number), and the range of invoices to print (based on the sort order). You also have the option to include invoices that are flagged as Cash or Credit Card payment types.
Vista™ comes with a standard invoice format for printing invoices. This standard format, MS Invoice, controls the overall look off your invoice (i.e. company logo, header and column positioning, etc.), and defaults when you first open the form. However, if you have created your own invoice format using Crystal Reports, you can specify that format here.
 Regardless of the invoice format you select here, how the detail appears on the invoice is determined by the print level and subtotal level options you selected for the customer in AR Customers, or overrode by quote or invoice. Additionally, the options to Sort by Sales Date or Location (in MS Company Parameters) affect the look of your invoices and determine the availability of some subtotal levels. See Invoice Format in Related Topics below.
 It is not required that you print your invoices before you interface them to AR. However, all invoices must be printed from a batch, so if you need to print a previously interfaced invoice, you must pull it back into an invoice batch before you can print it. See Reprinting Invoices in Related Topics below.
Note: Once an invoice is printed, it is flagged as 'printed' in the Invoice Batch Header table (MSIB). If you are tracking invoice detail (audit option in MS Company Parameters), and you remove or add tickets from an invoice after it has been printed, entries are automatically generated in the HQ Master Audit table (HQMA).These entries will be recorded for the MSID table and identify the MS Co#, Month, Transaction #, Invoice #, User, Date and time of change.
