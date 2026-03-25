---
title: "MS Material Payment Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/ms-material-payment-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/ms-material-payment-initialize-form"
---

# MS Material Payment Initialize Form

Use the MS Material Payment Initialize form to initialize entries into a material payment batch.
You can access this form by selecting File >  Initialize Payments from MS Material Payment Worksheet.
The form consists of three tabs, each with important default values to control the initialization of your worksheet:
Ticket RestrictionsThis tab identifies which transactions should be added to the material payment batch. Various selection criteria allow you to control which transactions are eligible for payment based on location group, from location, material vendor, material category, material range, and/or sale type. You must also specify to include tickets entered for a specific month (can be the current month or any month prior to the batch month), with the option to restrict by sale date range.Cost & Sales TaxThe Cost & Sales tab controls the unit cost and sales tax defaults by sales type. For each sales type, you must specify whether to default material unit cost values based on the MS Ticket Sales Price, PO Vendor Materials, Inventory Last Cost, or MS Quote Matl Vendor Cost. If you select None as the material cost default, unit costs will be set to 0.00.The Tax option determines the tax code default for taxable materials. You can specify to default from the "Sold to Customer" or the "Sold From Location". If you select the 0-Tax Exempt option, it only controls whether taxable materials are exempt from tax; it does not control non-taxable materials. Non-taxable materials are always be exempt from tax, regardless of the selected tax option you select. If you select the MS Ticket Sales Price or Inventory Last Cost material cost options, you will also have the option to specify whether unit costs are adjusted for sales tax. If you select the Adjust for Tax checkbox, material unit costs will be reduced by a tax rate (determined by the specified tax code).
AP Invoice DefaultsThis last tab sets important AP invoice default values. You will be required to enter the AP Co, Invoice Date, and AP Reference, but remaining fields are optional (e.g. due date, pay control, pay category and pay type, etc.). You also have options for creating separate invoices per material vendor and purchaser.Options are:

- Material Vendor, Customer, and Customer Job

- Material Vendor and JC Job

- Material Vendor and Sell To Location

If an option is selected, initialization generates a separate invoice per material vendor for each transaction meeting the purchaser criteria. If no options are selected, a single invoice generates per material vendor for all transactions with that sale type.
It is important to note that the Sale Type restriction (first tab) affects how these options work. For example, if restricting by C-Customer/CustJob, then only the Material Vendor, Customer, and Customer Job option is applicable. If you are not restricting by sale type (that is, the Sale Type option is None), all options are applicable and, if selected, will group invoices accordingly. If you select only one option, be aware that the system will create separate invoices for all transactions matching the selected option's criteria, and a single invoice created for all other transactions.

Once you have set your criteria, select the Update button to initialize the payment batch. Only those tickets matching the specified criteria that are not currently in another batch or have not been previously updated to AP, are initialized into the invoice batch.
During initialization, the system generates a unique AP Reference number for each payment sequence added to the batch. The first sequence generated is assigned the specified AP Reference number, while the remaining sequences are assigned a number based on the specified AP Reference number plus a sequential number (1-99). For example, if you specified an AP Reference number of 2008-01 and initialization generated five payment sequences, the AP Reference numbers would be as follows:
SeqAP Reference
12008-01
22008-011
32008-012
42008-013
52008-014

Note: You can make multiple passes by changing the selection criteria and then re-initializing the batch. Each pass adds new invoices to the existing entries in the batch. When making multiple passes, if initialization will combine tickets on existing invoices because all the information matches, but you want them to be on separate invoices, specify either a different invoice date or a different invoice description for each pass. The system will then generate new invoices for the tickets instead of adding them to existing invoices.

Once you have finished initializing payments, you can edit entries as necessary in MS Material Payment Worksheet.
