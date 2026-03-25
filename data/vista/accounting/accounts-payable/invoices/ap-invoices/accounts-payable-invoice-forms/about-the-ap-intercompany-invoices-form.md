---
title: "About the AP Intercompany Invoices Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/about-the-ap-intercompany-invoices-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/about-the-ap-intercompany-invoices-form"
---

# About the AP Intercompany Invoices Form

Use the AP Intercompany Invoices form when your organization has Material Sales companies that sell materials to jobs and/or inventory locations in other companies, and both companies should be treated as two, separate entities.
This form is only used when the Material Sales module is installed.
To implement intercompany invoicing, select the “Create Intercompany Invoices” checkbox in the MS Company Parameters form for each MS company that sells materials across companies.
The Material Sales module treats intercompany sales similar to customer sales, generating an AR invoice for the Customer representing the purchasing JC and/or IN Company. The job cost and inventory detail for these sales (materials sold, haul charges, tax, JC Co#, Job, Phase, IN Co#, Location, etc.) is stored in the MS Intercompany Invoice tables (MSII and MSIX), and used to initialize AP transactions here.
To initialize intercompany invoices, specify the MS company and the invoice date(s). Optionally, you can restrict initialization by “sold to” location. When doing so, indicate the company that bought the materials. When the Update button is clicked, all of the unprocessed intercompany invoices meeting the restriction criteria will be displayed in the grid. The criteria can be changed and the grid refreshed until only those invoices you are ready to process are displayed.
Warning: Invoice amounts can be edited or even deleted
 while in an AP Entry batch, but an update is not made to MS or AR reflecting your changes.
 If changes are needed, post correcting entries in MS and process them as you would any
 other intercompany sale.
When you are ready to process the invoices, click the Post button. This will bring up the AP Batch Process form, allowing you to process the invoices as normal. Once processed, they can be paid like any other AP invoice (in AP Payment Posting).

[](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-company-parameters-form)MS Company Parameters
[](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-posting-form)AP Payment Posting
[](/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/ap-maintenance-forms/ap-batch-process-form)AP Batch Process
