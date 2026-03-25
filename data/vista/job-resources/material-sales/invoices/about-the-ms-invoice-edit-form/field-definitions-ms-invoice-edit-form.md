---
title: "Field Definitions: MS Invoice Edit Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/invoices/about-the-ms-invoice-edit-form/field-definitions-ms-invoice-edit-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/invoices/about-the-ms-invoice-edit-form/field-definitions-ms-invoice-edit-form"
---

# Field Definitions: MS Invoice Edit Form

The following is a list of field descriptions for the MS
 Invoice Edit form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq#

 Enter NEW, +, or N to create a new entry, or enter the batch sequence number of an existing entry to display.

##  Customer

 Specify the customer (from AR Customers) for this invoice. This field is inaccessible if a transaction has already been assigned to the invoice either manually or through initialization.

##  Customer Job

 Specify the customer job number for this invoice, or leave blank if this invoice applies to multiple jobs. If a job is specified here, you can only add transactions that match this job. Once you have assigned transactions to the invoice, the customer job cannot be deleted or changed.
Note: If you initialized the invoice, and the ‘Invoice Level’ for this customer is set to 0 (One Invoice Per Customer) in AR Customers, this field is inaccessible.
 If this is an intercompany invoice, and the 'Invoice Level' for the 'sell to' company is set to 1 (One Invoice per Customer and Job) in AR Customers, this field will default the JC job number. (Intercompany invoices must be initialized, so field will be disabled.)

##  Customer PO#

 Specify the customer’s PO number for this invoice, or leave blank if this invoice applies to multiple PO’s within the customer job. If you specify a PO number here, only those transactions matching this customer job and PO number can be added to the invoice. Once you have assigned transactions to the invoice, the PO# cannot be deleted or changed.
Note: If you initialized the invoice, and the ‘Invoice Level’ for this customer is set to 1 (One Invoice Per Customer and Job) in AR Customers, this field is disabled.

##  Description

 Enter a description of this invoice, up to 30 characters. If a quote exists for the customer/customer job/PO#, will default the description defined on the quote. If a quote does not exist, this field defaults to “Material Sale”. This field allows overrides.

##  Invoice #

 This field defaults a system-assigned number that uniquely identifies this billing. The invoice number is automatically assigned based on the ‘last invoice’ number in either AR or MS Company (depending on the “Use Invoice #s From” option in MS Company Parameters). You can override this number, up to 10 characters allowed. Changes to this number do not update the ‘last invoice’ number in AR or MS.

##  Receivable Type

 Required field.
 Initially defaults a receivable type based on the following:

- If invoices were initialized, this field defaults
 the receivable type defined at the location/category level (IN Location Category
 Override) for the ‘from location’ on the ticket transaction. If no override exists at
 the location/category level, then this field defaults the receivable type at the
 location level (IN Locations). If no receivable type exists for the location, then
 defaults the receivable type specified for the customer (AR Customers).

Note: As invoices are initialized, the system groups sales activity by Customer, Customer Job, Customer PO#, and Receivable Type. A separate invoice will be created for each unique Receivable Type.

- If entering invoice manually, this field defaults the receivable type specified for the customer in AR Customers. Only transactions having the same receivable type indicated in the invoice header can be added to the invoice (in the grid).

 The receivable type specified here identifies which AR GL Account to debit when this invoice posts.

##  Payment Terms

 This field defaults the payment terms for the customer as defined in AR Customers. You can override this field; use valid payment terms set up in HQ Payment Terms.
 The system uses payment terms to generate the default discount and due dates. Discounts offered are entered with ticket and haul detail; changing the payment terms here will have no affect on those values.

## Invoice Report

Invoice Report field on the Info tab of the MS Invoice Edit form.
Enter an MS invoice report to override the default MS invoice report for invoice delivery (which is set in MS Company Parameters or AR Customers). Press F4 to select from a list of standard and custom reports.

##  Invoice Date

 If you initialized the invoice, this field defaults the invoice date specified during initialization. If you entered the invoice manually, this field defaults the current date. You can override this field; the date must be equal to or earlier than the discount and due dates.
 The system uses this date as the transaction date when the invoice is posted to AR.

##  Discount Date

 This field is required if discount is offered; otherwise, leave the field blank.
 This field initially defaults a discount date based on the payment terms and the invoice date. You can override the default, but the entry must be equal to or greater than the invoice date, but equal to or earlier than the due date.

##  Due Date

 Required field.
 This field initially defaults a due date based on the customer’s payment terms and the invoice date. You can override the default, but it must be equal to or greater than invoice date.

##  Apply to Invoice

 Specify the invoice to which this invoice should be applied. This must be an AR invoice posted from MS to the same customer. Typically, you will only use this option when making corrections to previously posted invoices.
 When entry is updated to AR, an ‘adjustment’ transaction will be created and applied to the original invoice.

##  Payment Type

 If invoice was initialized, will default the payment type specified for the assigned transaction, and field is disabled.
 If entering invoice manually, specify the payment type for this invoice. Only transactions with this same payment type can be added to the invoice.

- A-On Account

- C-Cash (Check # input is enabled for optional entry)

- X-Credit Card

##  Check No

 For 'Cash' payment types only, when using 'auto apply payments' feature (in MS Company Parameters).
 If you initialized this 'cash sale' invoice, this field defaults the check number specified during ticket entry, and the field is inaccessible.
 If entering this 'cash sale' invoice manually, specify the check number for this invoice, up to 10 characters.
Note: All transactions added to this invoice must have the same check number assigned. If you did not assign a check number during ticket entry, you cannot add the transaction to the invoice.

## Ship To: Address, City, State, Zip, Country

Enter the shipping address for this invoice. This address will print on the invoice if the invoice format allows it.
If you initialized the invoice, the system pulls the shipping address from the ticket. If the invoice includes transactions for multiple customer jobs or POs, shipping address defaults as blank. Default will also be null if invoice is entered manually. You may override the default.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## Ship To: Add'l Address

Use this field to enter additional shipping address information for this invoice (up to 60 characters). For example, if the shipping address is in an office building, you might use this field to enter the building number and/or suite/room number.

##  Location Group

 Optional field.
 This field indicates whether transactions included on this invoice are limited to a specific Inventory location group.
 If you initialized the invoice with a location group restriction, this field will default a location group based on the transactions initialized to the invoice. You cannot change the location group; however, it can be set to blank (deleted). This will allow for adding tickets with differing locations to this invoice.
 If entering invoice manually, specify the location group (from IN Location Groups) by which to restrict transactions that can be included on this invoice, or leave blank if no restrictions apply. If you specify a location group, only transactions posted to locations within this location group may be included on this invoice. Once you add transactions, this value cannot be changed; however, it can be set to blank (deleted).

##  Location

 Optional field.
 This field indicates whether transactions included on this invoice are limited to a specific Inventory location.
 If you initialized the invoice with a location restriction, and/or you specified to print separate invoices per location, this field will default a location based on the transactions initialized to the invoice. Default cannot be changed or deleted. If you did not specify to print separate locations, this field will default as null, since there may be multiple transactions on the invoice with differing locations.
 If entering invoice manually, specify the
 location (from IN Locations) by which to restrict transactions that can be included on this
 invoice, or leave blank if no restriction. (If you specified a location group in the
 Location Group field, the location specified here must be assigned to that location group.)
 If you specify a location here, only transactions posted to this location may be included
 on this invoice. Once you add transactions, this value cannot be changed or deleted.

##  Print Level

 This field indicates the lowest level of detail that prints on this invoice.
 This field initially defaults the print level specified at the quote level if quote exists (for customer, customer job, or customer job/PO) and quote is set to ‘Print Separate Invoice’. If no override by quote exists, then defaults the print level specified for the customer in AR Customers. You can override the default.

- 1-Unit Price – Summarize and print detail at the material, unit of measure, and unit price level. All transactions with the same material number, unit of measure, and unit price will be summarized and printed as one line on the invoice.

- 2-Trans# – Print one line on the invoice for each transaction.

Note: If you select this option, the ticket number for each transaction will print on the invoice.

##  Subtotal Level

 This field indicates the lowest subtotal level that will print on this invoice.
 This field initially defaults the subtotal level specified at the quote level if quote exists (for customer, customer job, or customer job/PO) and quote is set to ‘Print Separate Invoice’. If no override by quote exists, then defaults the subtotal level specified for the customer in AR Customers. You can override the default.

- 1-CustJob

- 2-CustJob/CustPO

- 3-CustJob/CustPO/Date

- 4-CustJob/CustPO/Date/Loc

- 5-CustJob/CustPO/Date/Loc/Matl.

- 6-CustJob/CustPO/Date/Loc/Matl/UM. (Quantity subtotals only available at this level.)

Note: The Level specified here may be affected by other setup options in AR and in Material Sales:

- MS Company Parameters — There are two sort options that will affect what subtotal levels can be used: Sort by Sales Date and Sort by Location. If both are checked, all subtotal levels are available. If the Sort by Sales Date option is unchecked, the date will not print on invoices; therefore, Level 3 cannot be used. If Sort by Location is unchecked, the location will not print on invoices, and Level 4 cannot be used.

- AR Customers — You have the option to specify that separate invoices will print for each Customer, Customer/Job, or Customer/Job/PO#. If you are printing separate invoices per Customer, then all subtotal levels are available. If printing separate invoices per Customer/Job, Level 1 cannot be used. If printing separate invoices per Customer/Job/PO#, then Levels 1 and 2 cannot be used.

Note: In addition to subtotals being printed at the selected level, subtotals will also be printed for each level above the selected level.

##  Separate Haul Information on Invoice

 This field initially defaults setting specified at the quote level if quote exists (for customer, customer job, or customer job/PO) and quote is set to ‘Print Separate Invoice’. If no quote exists, then defaults the setting specified for the customer in AR Customers. You may override the setting.
 Check this box if material amounts and haul charges (Haul Rate and Haul Amount) will print in separate columns on the invoice.
 Do not check this box if haul information is to be combined with material information when printing invoices for this customer. Haul charges will be included with material amounts, rather than printed in separate columns on the invoice.The unit price will be calculated as Total / Material Units.

##  CM Co

 This field is accessible only when using the 'auto-apply payments' feature
 (in MS Company Parameters) and payment type is 'Cash'.
 Specify the CM company to which this 'cash'
 payment will be posted. Initially defaults the CM company assigned in AR Company Parameters
 or in IN Locations (if creating separate invoices per location). You may override the
 setting.

##  CM Account

 This field is enabled only when using the 'auto-apply payments' feature (in MS Company Parameters) and payment type is 'Cash'.
 Specify the bank account to which this 'cash'
 payment will be posted. Initially defaults the CM account assigned in AR Company Parameters
 or in IN Locations (if creating separate invoices per location). You may override the
 setting.

##  MS Trans

 This is the transaction number assigned to the ticket/haul transaction. If you initialized invoices, the system automatically defaults the appropriate transaction based on the initialization criteria.
 If adding invoices manually, press F4 for a list of available transactions. The selected transaction will be added if it is not already assigned to this or any other batch (invoice or ticket), has not been previously invoiced, matches the invoice’s header restrictions (i.e. Customer #, Customer Job and/or PO#, Payment Type, Location Group, Location, etc.), is not on hold, or has not been voided.
 To remove a line, simply highlight the row and press Delete. This will remove the transaction from the invoice, leaving it available for future billing.
Note: If you are using the 'auto-apply payments' feature (MS Company Parameters), and a check number is assigned to the invoice (header), the transaction you are adding must be assigned the same check number. If the check number is different, or no check number was assigned during ticket entry, you cannot add the transaction.
ADDITIONAL NOTE:You cannot edit transactions in this program. If a transaction needs to be edited, remove it from the invoice, pull it into a ticket batch (MS Ticket Entry), and make necessary corrections. It can then be re-added to the invoice here for billing.
 If the invoice has already been interfaced, you cannot add or delete transactions.

## Seq

Seq field on the Recipients tab in the MS Invoice Edit form.

 Enter N or + to create a new entry. The system will automatically generate a sequence number for you.

## Delivery Method

Delivery Method drop-down list on the Recipients tab of the MS Invoice Edit form.
Indicate the delivery method for the selected recipient.

- P-Print — Select this option to print invoices for delivery via postal mail.

- E-Email — Select this option to deliver invoices via email.

## Name

Name field on the Recipients tab of the MS Invoice Edit form.
Enter the name of the individual or company to whom you will be mailing or emailing this invoice.
Entry in this field is required regardless of Delivery Method.

## Email

Email field on the Recipients tab of the MS Invoice Edit form.
Enter the email address to use for this recipient.
Entry in this field is required if Delivery Method is E-Email.

## Address

Address field on the Recipients tab of the MS Invoice Edit form.
Enter the address to use for this recipient.
Entry in this field is reequired if the Delivery Method field is set to P-Print.

## Add'l Address

Add'l Address field on the Recipients tab of the MS Invoice Edit form.
If applicable, enter additional address details.

## City

City field on the Recipients tab of the MS Invoice Edit form.
Enter the city to use for this recipient.

Entry in this field is required if the Delivery Method field is set to P-Print.

## State

State field on the Recipients tab of the MS Invoice Edit form.
Enter the state to use for this recipient.
Entry in this field is required if the Delivery Method field is set to P-Print.

## Zip Code

Zip Code field on the Recipients tab of the MS Invoice Edit form.
Enter the zip code to use for this recipient.
Entry in this field is required if the Delivery Method field is set to P-Print.

## Country

Country field on the Recipients tab of the MS Invoice Edit form.
Enter the country to use for this recipient.

## Select

The Select checkbox on the attachments tab of the MS Invoice Edit form.
Select this checkbox next to any attachment you want to include on the invoice.
