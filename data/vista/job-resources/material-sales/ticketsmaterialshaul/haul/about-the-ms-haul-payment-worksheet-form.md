---
title: "About the MS Haul Payment Worksheet Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-payment-worksheet-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-payment-worksheet-form"
---

# About the MS Haul Payment Worksheet Form

Use this form to prepare ticket and time sheet data prior to
 generating AP invoices for your independent haul vendors.
You can initialize payments to the batch
 using [MS Haul Payment Initialize ](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-payment-initialize-form) (accessed by selecting
 File > Initialize
 Payments) or enter them manually in this form.

## Invoice Restriction

The Invoice
 Restriction field allows you to restrict worksheet transactions
 based on sale type. By restricting the transactions for an invoice, you can
 effectively create separate invoices for each haul vendor based on customer/customer
 job, JC job, and/or 'sell to' location. Available options are:

- N-None – Select this option if no restrictions apply. Any
 transaction posted to the specified haul vendor can be applied to the invoice,
 regardless of sale type.

- C-Customer/Cust Job – Only transactions that reference a
 designated customer and customer job can be applied to the invoice. (Note: If
 the customer job is blank, only transactions for the customer that have no
 customer job specified can be applied to the invoice.)

- J-JC Job – Only transactions that reference a designated JC
 company and job can be applied to the invoice.

- I-Inventory – Only transactions that reference a designated
 IN company and 'sell to' location can be applied to the invoice.

## Pay Category and Pay Type

If you are using pay categories (i.e. you checked the Using Payable
 Category box in AP Company Parameters), you will also have the
 option to specify the pay category and pay type. These fields will default as
 defined for the company, but may be overridden.Note: If you leave the pay category blank, the pay type must
 also be blank. You cannot enter one without the other.

## Ticket and Timesheet Transactions

After entering header information, you can manually add ticket or hauler time sheet
 transactions using the detail section of the form.
You can add only transactions that:

- match the invoice restriction specified in the header;

- have a hauler type of H-Haul Vendor and were posted to the
 same haul vendor specified in the header;

- were posted in a month equal to or prior to the current
 batch month;

- are not applied to another invoice in the current batch or
 do not exist in another batch; and

- have not already been updated to AP.

You can add, delete, or make minor edits
 to transactions in the grid as necessary. Although you cannot edit any of the hauler
 information (i.e. material, truck, truck type, etc.), you can edit the pay code,
 basis amount, pay rate, or amount.
Note: For Australia or Canada (where the Default
 Country in HQ Company Setup is AU or CA), you also have the option
 to edit haul payment tax info. For more information about these fields, see Haul
 Payment Taxes section below.

## Haul Payment Taxes (Australia and Canada)

You can calculate taxes on haul payments to a vendor when entering tickets (in MS
 Ticket Entry) or hauler time sheets (in MS Hauler Time Sheets); the calculated tax
 amounts will then be included when processing haul payments in this form.
If you did not include haul payment
 taxes on the original ticket or timesheet transactions, you may add that information
 here. Once you enter the haul pay tax type and tax code, the system calculates the
 haul payment tax amount (tax rate x pay amount).
Haul payment tax amounts will be updated
 to Accounts Payable when processing haul payments in MS Batch Process.

## Invoice Totals

As you add transactions, they will update the Basis, Haul,
 Surcharge, and Invoice totals above the
 header.
The basis total will be the total of units, hours, loads, etc.
 (depending on the transaction pay codes), which can be useful in reconciling haul
 vendor invoices with tickets. However, if transactions included for payment have
 differing pay codes--that is, the pay rate basis differs between pay codes--the
 basis total may not be meaningful (e.g. if pay rate basis for one transaction is
 units and pay rate basis for another transaction is hours, the basis total would be
 a sum of units and hours).
Although haul charges and surcharges are
 calculated during ticket entry, they will appear as separate transactions when
 pulled in for payment. The haul total represents the total invoice net of
 surcharges; it will be the sum of all transactions in the grid with the Surcharge box unchecked. The surcharge total will be the sum of all
 transactions with the Surcharge box checked. The
 invoice total will be the sum of the haul and surcharge totals.

## Surcharges

If you are using the surcharges functionality in Material Sales, surcharges assessed
 for a ticket that are associated with a pay code (in MS Surcharge Codes) will be
 pulled in with the parent ticket during initialization.
Note: If you manually add transactions to the grid,
 you must add surcharge tickets separately; adding a parent ticket to the grid does
 not automatically pull in the related surcharge ticket(s).
Pay rates for surcharges are based on a
 percent of the surcharge total; therefore, the pay basis for each surcharge ticket
 will automatically default the surcharge amount. As with normal haul payment
 transactions, the system will use the standard pay rate hierarchy to determine the
 rate to use for surcharge transactions. See [Pay Rate Hierarchy - Table 1](/en/vista/vista/job-resources/material-sales/setupmaintenance/pay-rate-hierarchy---table-1) for more
 information.

## Discounts

Although discount dates and amounts are not included on the worksheet, they will
 calculate during the batch update based on the payment terms for the haul vendor.
 Discount taken amounts display for each applicable invoice on the MS Hauler Payment
 AP Audit list. The update determines the GL distributions based on the Post
 Discounts Offered to GL and Net Amounts to Subledgers option in AP Company
 Parameters. For more information, see [About Using Discounts ](/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/about-discounts).

## Vendor Compliance

If you are tracking vendor compliance for non-PO/SL invoices (flag in AP Company
 Parameters), and you specify a non-compliant haul vendor, a warning indicating the
 vendor is ***Out of Compliance*** displays in red above the invoice header; however
 entry will be allowed.

## Updating to Accounts Payable

To update haul payment information to AP, select File > Batch
 Process and process the batch as normal. For more information, see [MS Batch Process ](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-batch-process-form).
When a hauler payment batch posts, the
 system creates AP expense invoices based on the information provided here. The
 update to AP allows you to only add invoices; you cannot use it to correct or delete
 previously interfaced information. If you need to change hauler payment information
 that has been previously updated to AP, you should post additional tickets or time
 sheets with reversing entries, then create and post a new hauler payment batch.
Note: You may edit or delete AP invoices created from
 a hauler payment batch using the AP Transaction Entry form; however, the system will
 not automatically update MS. You can manually update the information in MS by first
 deleting the transactions in AP Transaction Entry, and then editing the related
 ticket in MS Ticket Entry.
 For more information about the AP
 update, see [Update to
 AP](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-updating-hauler-payments-to-ap).

Related information

- [About Updating Hauler Payments to AP](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-updating-hauler-payments-to-ap)
