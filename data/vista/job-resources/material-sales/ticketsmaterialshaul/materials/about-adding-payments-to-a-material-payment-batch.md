---
title: "About Adding Payments to a Material Payment Batch | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/about-adding-payments-to-a-material-payment-batch"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/about-adding-payments-to-a-material-payment-batch"
---

# About Adding Payments to a Material Payment Batch

You can add payments to a material payment batch using the MS Material Payment Worksheet form.

- Select File > Initialize Payments. This opens the [MS Material Payment Initialize ](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/ms-material-payment-initialize-form) form, where various criteria enable you to restrict which transactions will be initialized to the worksheet.

- Add payments to the batch manually by using by using the header to enter the AP invoice defaults and the grid to add ticket transactions for payment.

## Using the Header to Enter AP Invoice Defaults

For each payment sequence, in the AP Co field, specify the AP company to which the material payment will be posted. This can be any valid AP company, as long as the following applies:

- Both the posting AP company and the MS AP company share the same vendor and tax groups.

- Both AP companies have the same GL interface levels specified (i.e. Summary, Transaction, Line, or None).

You can use the Invoice Restriction field to restrict by sale type the transactions that can be added to the worksheet for the specific material vendor. Available options are:

- N-None – Select this option if no restrictions apply. Any transaction posted to the specified material vendor can be applied to the invoice, regardless of sale type.

- C-Customer/CustJob – Only transactions posted to the specified material vendor that reference a designated customer and customer job can be applied to the invoice. If the customer job is blank, only transactions for the customer that have no customer job specified can be applied to the invoice. If both customer and customer job are left blank, tickets posted to any customer where the customer job is blank may be applied to the invoice.

- J-JC Job – Only transactions posted to the specified material vendor that reference a designated JC company and job can be applied to the invoice. If the JCCo and Job are left blank, tickets posted to any JCCo/job may be applied to the invoice.

- I-Inventory – Only transactions posted to the specified material vendor that reference a designated IN company and 'sell to' location can be applied to the invoice.

You can also specify other information in the invoice header. This includes the AP reference number, invoice date and description, pay terms (used to determine due and discount dates), hold code and pay control number (as applicable), and the CM account from which the payment will be made. If you are using pay categories (flag in AP Company Parameters), you will also have the option to specify the pay category and pay type. If you leave the pay category null, the pay type must also be null. You cannot enter one without the other.
Note: If you do not allow duplicate AP reference numbers (flag in AP Company Parameters) and the AP reference number already exists for the material vendor, a message displays in red above this field, indicating that the reference number is already in use and identifying the transaction number and expense month. If you initialized invoices, change the reference number before posting the batch. If manually entering invoices, you cannot save the record until the reference number is changed. If the ‘Prevent Duplicate AP Reference’ option is not checked, you will receive a warning, but entry is allowed.

## About Using the Grid to Add Ticket Transactions for Payment

After entering header information, use the detail section to add eligible ticket transactions to the invoice. Eligible ticket transactions are those that:

- match the invoice restriction specified in the header (e.g. if restricting by customer/customer job, transactions must be posted to that customer/customer job);

- were posted in a month equal to or prior to the current batch month;

- are not applied to another invoice in the current batch or do not exist in another batch; and

- have not already been updated to AP

After you add a transaction, the system displays ticket information, along with the cost information (unit cost, total cost, tax code, tax basis, tax amount). The cost information will default based on how you have set the cost and sales tax default options (Options menu). The following list discusses each default option.

- Cost Defaults – This option determines the unit cost defaults for materials. The unit cost is the dollar amount paid to the vendor per unit, per hundred units, or per thousand units of the material. Options are:

- None – Unit cost will default as 0.00.

- Ticket Sales Price – Defaults the unit price/ECM specified for the material on the MS ticket.

- PO Vendor Material – Defaults the unit cost/ECM based on the cost option specified for the vendor/material/UM in PO Vendor Materials. If materials were sold to a job and overrides exist for the job (in PO Vendor Materials), the overrides will be used.

- IN Last Cost – Defaults the Last Unit Cost/ECM specified for the material (based on the 'sold from' location and UM) in IN Location Materials.

- Adjust Cost for Sales Tax – This option determines whether the unit cost adjusts for sales tax. If you select this option, the unit cost for the material will be reduced by a tax rate (determined by tax code), and the sales tax will post as a separate part of the invoice line (in AP). You should only need to use this feature if your ticket price or inventory cost includes sales tax that needs to be separate on the AP invoice.

Note: This option is disabled if you select the ‘None’ or ‘PO Vendor Material’ cost default options or the ‘Tax Exempt’ sales tax default option.

- Sales Tax Defaults – This option determines the tax code default for taxable materials (i.e. Materials with the ‘Taxable for Purchases or Sales’ flag checked in HQ Materials). Options are:

- Tax Exempt – Materials are exempt from sales tax. Tax codes will default as blank. You may override this default for taxable materials only.

- Sold To – Tax codes will default based on the purchaser (i.e. if customer, defaults from AR Customers, if job, defaults from JC Jobs, if IN location, defaults from IN Locations.) If the material is not taxable, the tax code defaults as blank and cannot be overridden.

- Sold From Location – Tax codes will default from the 'sold from' location (as defined in IN Locations). If the material is not taxable, the ax code defaults as blank and cannot be overridden.

You can edit unit cost and tax defaults as necessary. You can also delete any ticket transactions that you will not pay with the current invoice.
As you add transactions to the batch, information displays in the header in three display-only fields:

- Invoice Amt equals the sum of the Total Cost amounts for all tickets currently in the batch.

- Invoice Tax equals the sum of the Tax Amount amounts for all tickets currently in the batch.

- Invoice Total equals Invoice Amt plus Invoice Tax.

The amounts in these display fields change as transactions are added, edited, and deleted.
After transactions have been added to the batch, to update the material payment information to AP, select File  > Batch Process and process the batch as normal. For more information, refer to [MS Batch Process ](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-batch-process-form).
Note: Once you have invoiced material payments, it is recommended that you do not edit the related tickets. However, if you must edit the tickets, limited edits are allowed. For more information, see [About Editing and Deleting Tickets](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-editing-and-deleting-tickets).

Related information

- [About the MS Material Payment Worksheet Form](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/about-the-ms-material-payment-worksheet-form)
