---
title: "About the MS Haul Payment Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-payment-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-payment-initialize-form"
---

# About the MS Haul Payment Initialize Form

Use this form (accessed by selecting File >  Initialize
 Payments from MS Haul Payment Worksheet) to initialize entries into a hauler payment
 batch.
Various selection criteria allow you to control the
 transactions eligible for payment initialization. You can restrict initialization to a
 range of location groups, 'from' locations, and/or tickets, a selected haul vendor,
 truck, or by sale type. If restricting by sale type, additional options allow for
 restricting by customer/cust job, JCCo/Job, or INCo/To Location (depending on sale type
 selected).
Note: Restricting by sale type only controls the transactions
 eligible for initialization to the payment batch; it does not control which transactions
 are grouped together on invoices. If you want to group transactions by sale type, use
 the 'create separate invoice' options (see below).
The Include Tickets and Time Sheets
 Entered for Month field allows for specifying the posting month from
 which to pull transactions for payment initialization. This month can be the current
 batch month (default) or any month prior to the current batch month. You also have the
 option to specify a range of sale dates by which to restrict tickets and timesheets
 included during initialization.

## Payment Information

After defining selection criteria, you
 must define the payment information. This includes the invoice and due dates, the
 invoice description, AP Company (must be a valid AP company with the same vendor
 group as the MS AP company), AP reference number, pay control and hold codes, and CM
 account information. If you are using pay categories (flag in AP Company
 Parameters), you also have the option to specify a pay category and pay type. If the
 pay category is left blank, the pay type must also be blank. You cannot enter one
 without the other.
Note: The Invoice Date,
 AP Company, AP Reference,
 CM Co# and CM Account fields are
 required.
After entering all required information,
 select Update to initialize. Only those tickets
 and/or hauler time sheets that match the specified criteria, that are not currently
 in another batch or have not been previously updated to AP, and that are flagged as
 hauler type ‘H’ (haul vendor), will initialize into the invoice batch.
During initialization, the system
 generates a unique AP Reference number for each payment sequence added to the batch.
 The first sequence generated will be assigned the specified AP Reference number,
 while the remaining sequences will be assigned a number based on the specified AP
 Reference number plus a sequential number (1-99). For example, if you specified an
 AP Reference number of 2005-0001 and initialization generated five payment
 sequences, the AP Reference numbers would be assigned as follows:
Seq
AP Reference

1
2005-0001

2
2005-00011

3
2005-00012

4
2005-00013

5
2005-00014

Note: You can make multiple passes by changing the
 selection criteria and then reinitializing the batch. Each pass will add new
 invoices to the existing entries in the batch. When making multiple passes, if
 initialization will combine tickets on existing invoices because all the information
 matches, but you want them to be on separate invoices, specify either a different
 invoice date or a different invoice description for each pass. The system will then
 generate new invoices for the tickets instead of adding them to existing invoices.
Once you have finished initializing
 payments, you can edit entries as necessary in [MS Haul
 Payment Worksheet ](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-payment-worksheet-form).
