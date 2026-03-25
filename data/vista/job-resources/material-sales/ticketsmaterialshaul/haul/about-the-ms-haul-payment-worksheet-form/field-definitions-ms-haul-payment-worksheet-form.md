---
title: "Field Definitions: MS Haul Payment Worksheet Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-payment-worksheet-form/field-definitions-ms-haul-payment-worksheet-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-payment-worksheet-form/field-definitions-ms-haul-payment-worksheet-form"
---

# Field Definitions: MS Haul Payment Worksheet Form

The following is a list of field descriptions for the MS Haul
 Payment Worksheet form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq#

Enter N, NEW, or + to create a new entry, or enter the
 batch sequence number of an existing entry to display.

## AP Co

Specify the AP company for this haul payment worksheet. Must be a valid AP company with the same vendor group as the AP company specified in MS Company Parameters.
The system uses the company specified here to validate the haul vendor for this worksheet, and will be the company to which the haul payment will be posted.

## Haul Vendor

Required.
If you initialized payments, this field is inaccessible, but defaults a vendor based on information on the initialized ticket or hauler time sheet transaction.
If entering payment manually, specify the
 vendor (from AP Vendors) for this haul payment. Only ticket or hauler time sheet
 transactions posted to this vendor and meeting the invoice restriction criteria can be
 added to this payment sequence in the grid below.
Note: If tracking vendor compliance for non-PO/SL invoices (flag in AP Company Parameters) and this vendor is out of compliance, an ***Out of Compliance*** warning is displayed in red above the header; however entry will be allowed.

## Invoice Restriction

Specify the sales type by which to restrict transactions (tickets and/or hauler timesheets) that can be applied to this haul vendor's invoice.

- N-None – Select this option if no restrictions apply. Any transaction posted to the specified haul vendor can be applied to this invoice, regardless of sale type.

- C-Customer/CustJob – Select this option to restrict by customer or customer/customer job. Only transactions for this haul vendor that reference the customer or customer and customer job (specified to the right) can be applied to this invoice.

- J-JC Job – Select this option to restrict by JC job. Only transactions for this haul vendor that reference the JC job (specified to the right) can be applied to this invoice.

- I-Inventory – Select this option to restrict by inventory location. Only transactions for this haul vendor that reference the inventory location (specified to the right) can be applied to this invoice.

Note: Transactions can only be applied to an invoice if they have not already been applied to another invoice in the current batch, are not in another batch, or have not been updated to AP.

## Customer

This field only displays when the Invoice
 Restriction is set to C-Customer/CustJob.
Required.
Specify the customer by which to restrict transactions applied to this haul vendor's invoice. Only transactions that reference this customer (and the customer job specified to the right) can be applied to this invoice.

## Customer Job

This field only displays when the Invoice
 Restriction is set to C-Customer/CustJob.
Specify the customer job by which to restrict transactions applied to this haul vendor's invoice. Only transactions referencing the specified customer and this customer job can be applied to this invoice.
If this field is left blank, only transactions referencing the specified customer that have no customer job designated can be applied to this invoice.

## JC Co

This field only displays when the Invoice
 Restriction is set to J-JC Job.
Required.
Specify the JC company by which to restrict transactions applied to this haul vendor's invoice. Only transactions referencing this Job Cost company (and the job specified to the right) can be applied to this invoice.
Note: You must enter both the JC company and Job; you cannot enter one without the other.

## JC Job

This field only displays when the Invoice
 Restriction is set to J-JC Job.
Required.
Specify the JC job by which to restrict transactions applied to this haul vendor's invoice. Only transactions referencing the specified job can be applied to this invoice.
Note: You must enter both the JC company and Job; you cannot enter one without the other.

## IN Co

This field only displays when the Invoice
 Restriction is set to I-Inventory.
Required.
Specify the IN company by which to restrict transactions applied to this haul vendor's invoice. Only transactions referencing this Inventory company (and the 'sell to' location specified to the right) can be applied to this invoice.
Note: If you do not specify an IN company in this field, you cannot specify a location in the next field. You must either leave both fields blank or enter a value in both fields; you cannot enter one without other.

## Sell To Location

This field only displays when the Invoice
 Restriction is set to I-Inventory.
Required.
Specify the 'sell to' location by which to restrict transactions applied to this haul vendor's invoice. Only transactions referencing this 'sell to' location can be applied to this invoice.
Note: If you did not specify an IN company in the previous field, you cannot specify a location in this field. You must either leave both fields blank or enter a value in both fields; you cannot enter one without other.

## AP Reference

The AP Reference field on the MS Haul Payment Worksheet form, header Info tab.
Required.
For initialized payments, this field defaults the AP reference number specified during initialization. You can override the default.
If entering payment manually, enter the AP reference number, up to 30 characters, for this payment sequence.
The reference number specified here will update to the AP invoice created when you post this batch.
Note: If the Prevent Duplicate AP Reference box is checked in AP Company Parameters and the reference number specified here already exists for the haul vendor on another transaction, a message displays in red (above) indicating that the reference number is already in use and identifying the transaction number and expense month. You must change the reference number before posting the batch.If the Prevent Duplicate AP Reference box is not checked, a warning displays, but entry is allowed.

##  Invoice Date

 Required.
 If you initialized payments, this field defaults the invoice date specified during initialization. You can override the default. If overridden, the invoice due date will recalculate based on the payment terms specified for the payment sequence, regardless of whether a due date was specified during initialization.
 If entering payment manually, enter the invoice date. The field initially defaults the current date.
 The invoice date specified here will update to the AP invoice created when you post this batch.

##  Description

 If you initialized payments, this field defaults the description specified during initialization. You can override the default.
 If entering payment manually, enter the description for this payment sequence, up to 30 characters. Initially defaults a description of “Material Haul”.
 The description specified here will update to the AP invoice created when you post this batch.

##  Pay Terms

 If you initialized payments, this field defaults the payment terms of the specified haul
 vendor. You can override the default.
 If entering payment manually, specify the
 payment terms for this payment sequence. Initially defaults the payment terms specified for
 the vendor in AP Vendors, if one exists.
 The system uses the payment terms specified here when creating the AP Invoice to determine any vendor discounts and discount date.

##  Due Date

 Required.
 If you initialized payments, this field defaults the due date specified during initialization. You can override the default.
 If entering payment manually, specify the due date for this invoice. Initially defaults a due date based on the payment terms assigned to the specified haul vendor. If you do not specify payment terms for the vendor, this field defaults blank.

## Hold Code

If you initialized payments, this field defaults the hold code specified during initialization. You can override the default with a valid hold code set up in HQ Hold Codes.
If entering payment manually, enter a hold code (from HQ Hold Codes) for this payment sequence, if applicable.
Note: The system automatically applies all hold codes assigned to the vendor in AP Vendor Hold Codes when creating the invoice. This field provides an opportunity for you to specify an additional hold you may want on the invoice.

##  Pay Control

 If you initialized payments, this field defaults the pay control code specified during initialization. You can override the default.
 If entering payment manually, enter a pay control code, up to 10 characters, for this payment sequence, if applicable.
 If you enter a pay control code, it will update to the AP invoice, and can be used to selectively group transactions together for payment within AP.

##  CM Co#

 If you initialized payments, this field defaults the CM company specified during initialization. You can override the default.
 If entering payment manually, enter the CM company for this payment sequence. Initially defaults the CM company specified for this MS company’s AP company (in AP Company Parameters, Subledgers tab).

## CM Account

Enter the CM Account for making payments, or accept the default. The
 entry must be a valid account set up in CM Accounts. You can override this field,
 regardless of the default.
This field defaults differently depending on how you enter the payment:
Manual Entry
This field initially defaults the CM Account #
 specified in AP Company Parameters. When you enter the haul vendor for this invoice, the
 system updates this field with the CM Account from AP Vendors. If no CM
 account is specified for the vendor, the system uses the CM Account #
 from AP Company Parameters.
MS Haul Payment Initialize
This field initially defaults the CM account
 specified in MS Haul Payment Initialize. If no CM account was specified during
 initialization, the system updates this field with the CM Account from AP Vendors. If no CM
 account is specified for the vendor, the system uses the CM Account#from
 AP Company Parameters.

## Pay Category

The Pay Category field on the MS Haul Payment Worksheet form, header Info tab.

This field only displays if the Using Payable Category checkbox is selected in AP Company Parameters and is only enabled if the Allow Payable Type Override checkbox is also selected.
If payable type overrides are allowed, specify the pay category for this payment sequence. The pay category specified here determines the default pay type.
This field defaults a pay category as follows:

- If an override pay category is specified for the current user in VA User Profile, that pay category defaults here.

- If no override pay category is specified for the user in VA User Profile, defaults the pay category defined in AP Company Parameters.

- If no pay category is defined for the company, this field defaults as blank. (In this case, the pay type default will be the Expense pay type from AP Company Parameters.)

Note: If you do not specify a pay category in this field, you cannot specify a pay type in the Pay Type field. You must either leave both fields blank or enter a value in both. If you elect to leave both fields null, the update will automatically assign the expense pay type from AP Company Parameters.

## Pay Type

The Pay Type field on the MS Haul Payment Worksheet form, header Info tab.

This field is only enabled if the Allow Payable Type Override checkbox is selected.
If using pay categories, this field initially defaults the Expense pay type for the specified pay category. You may change the default as needed; however, the pay type must either be assigned to the pay category or be a pay type that has no pay category restriction (that is, the Restrict Pay Type to Pay Category checkbox in AP Payable Types is not selected).
 If not using pay categories, this field defaults the Expense pay type specified in AP Company Parameters and may be overridden as needed.
Note: If you are using pay categories but did not specify a pay category in the previous field, you cannot specify a pay type here. You must either leave both fields blank or enter a value in both. If you elect to leave both fields null, the update will automatically assign the expense pay type from AP Company Parameters.

##  Month

 Specify the posting month of the ticket or hauler time sheet transaction to add to the worksheet. Entry must be a month that is the same as or prior to the current batch month.

## Trans#

If you initialized payments, this field displays the ticket or time sheet transaction to include on the invoice. Cannot be edited, but transactions may be added to or deleted from the batch.
Note: If you are using the surcharges functionality, each
 surcharge generated during ticket entry will appear as a separate transaction in the grid
 (below the original ticket transaction). Surcharge transactions are identified by a
 checkmark in Surcharges box (last column in grid).
If entering payments manually, specify the ticket or time sheet transaction to add to this payment sequence. Transaction must be posted to the vendor specified in the header, and must be posted in the same month as the invoice batch. Press F4 for a list of valid ticket and time sheet transactions.
Note: When manually adding ticket transactions to the grid, any related surcharge transactions must also be added manually; unlike initialized payments, the system does not automatically pull in surcharge transactions when the related ticket transaction is added to the grid. Surcharge transactions will always be assigned the same ticket number as the original ticket transaction.

## Pay Code

This field initially defaults the pay code assigned to the ticket or time sheet transaction. Pay code is used to determine the haul vendor’s payment for this transaction. Changing this default will cause the basis, pay rate, and payment amount to recalculate based on the new pay code's setup and the transaction's detail.
Note: If this is a surcharge transaction (Surcharge box
 checked on Info or Grid tab), this field defaults the pay code assigned to the surcharge
 code (in MS Surcharge Codes). Changing this default will clear the basis amount and cause
 the pay rate and amount to default as 0.00.

## Pay Basis

This field initially defaults the ticket or time sheet’s basis amount. If you change the default (may be either positive or negative amount), the payment amount for this transaction will recalculate.
Note: If this is a surcharge transaction (Surcharge box
 checked on Info or Grid tab), this field defaults the surcharge total amount.

## Pay Rate

This field initially defaults the pay rate from the ticket or time sheet. Changing the default will cause the payment amount to be recalculated.
Note: If this is a surcharge transaction (Surcharge box
 checked), this field defaults the pay rate defined for the pay code assigned to the
 surcharge code (in MS Surcharge Codes).

## Amount

This field initially defaults the payment amount based on pay basis x pay rate; however, if the calculated payment is less than the minimum payment amount specified for the pay code (in MS Quotes or MS Pay Codes), this field will default the minimum payment amount. Overriding this amount will cause the system to recalculate the pay rate.
Note: The system ignores the minimum amount for surcharge transactions with a negative payment amount; negative payment amounts will remain intact unless manually changed.

## Haul Pay Tax Type

Enabled for Australia and Canada only (i.e.
 the Default
 Country in HQ Company Setup is AU or CA).
This field initially defaults the haul pay tax type assigned to the ticket or time sheet transaction. Accept the default or specify the haul payment tax type for this transaction.

- 1-Sales

- 2-Use

- 3-VAT (Value Added Tax)

## Haul Pay Tax Code

Enabled for Australia and Canada only (i.e.
 the Default
 Country in HQ Company Setup is AU or CA).
This field initially defaults the haul pay tax code assigned to the ticket or time sheet transaction. Accept the default or specify the tax code to use for calculating taxes on payments to the haul vendor for this transaction.

## Haul Pay Tax Amt

Enabled for Australia and Canada only (i.e.
 the Default
 Country in HQ Company Setup is AU or CA).
This field initially defaults the haul pay tax amount calculated for the ticket or hauler time sheet (tax rate x pay amount). Accept the default or specify the total amount of tax to apply to the haul vendor payment for this transaction.

## Surcharge

Display only, indicating whether transaction is a surcharge. This box will be checked for all surcharge transactions and unchecked for all non-surcharge transactions.
