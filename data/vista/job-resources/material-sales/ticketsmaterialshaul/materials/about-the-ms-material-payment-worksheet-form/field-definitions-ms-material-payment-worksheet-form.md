---
title: "Field Definitions: MS Material Payment Worksheet Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/about-the-ms-material-payment-worksheet-form/field-definitions-ms-material-payment-worksheet-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/about-the-ms-material-payment-worksheet-form/field-definitions-ms-material-payment-worksheet-form"
---

# Field Definitions: MS Material Payment Worksheet Form

The following is a list of field descriptions for the MS
 Material Payment Worksheet form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  AP Reference

The AP Reference field on the MS Material Payment Worksheet form, header Info tab.
 Enter the AP reference number for this invoice, up to 30 characters. Typically, this is the invoice number supplied by the material vendor.
If the Prevent Duplicate AP Reference checkbox is selected in AP Company Parameters and the AP reference already exists for the material vendor on another transaction, a message displays in red above this field, indicating that the reference number is already in use and identifying the transaction number and expense month. If you initialized the transaction, you will need to change the reference number before posting the batch. If you are manually entering transactions, you will need to change the reference number before you can save the record. Press F4 for a list of existing reference numbers for the material vendor.
 If the Prevent Duplicate AP Reference checkbox is not selected, a warning displays, but entry is allowed.

## AP Co

Enter the AP company to update with this material vendor invoice. Defaults the MS AP company, but may be overridden with any valid AP company, as long as the following applies:

- Both the posting AP company and the MS AP company share the same vendor and tax groups.

- Both AP companies have the same GL interface levels specified (i.e. Summary, Transaction, Line, or None).

##  CM Acct

 Enter the CM Account for making payments, or accept the default. The entry must be a valid
 account set up in CM Accounts. You can override this field, regardless of the default.
 This field defaults differently depending on how you enter the payment.
 Manual Entry
 If you are entering the payment manually,
 this field initially defaults from the CM Account# field in AP Company Parameters. When you
 enter a vendor in the Material Vendor field, the system updates this field with the number
 from the CM Account field in AP Vendors. If the CM Account field in AP Vendors is blank,
 the system uses the number from the CM Account# field in AP Company Parameters.
 MS Material Payment Initialize
 If you are initializing the payment from MS
 Material Payment Initialize, this field initially defaults from the CM Account field on
 that form. If you leave the field blank, the system updates this field with the number from
 the CM Account field in AP Vendors. If the CM Account field in AP Vendors is blank, the
 system uses the number from the CM Account# field in AP Company Parameters.

##  CMCo

 If you initialized payments, this field defaults the CM company specified during initialization. You can override the default.
 If entering payment manually, enter the CM company for this payment sequence. Initially defaults the CM company specified for this MS company’s AP company (in AP Company Parameters, Subledgers tab).

##  Customer

 This field is accessible only if Invoice Restriction is 'Customer/CustJob'.
 Specify the customer for restricting tickets added to this invoice. Only tickets posted to this customer (for the specified vendor) can be added to this invoice.
 If left blank, tickets posted to any customer (for the specified vendor) where the customer job is blank may be added to this invoice.
Note: Once you add tickets to the invoice, this field is inaccessible and cannot be changed.

##  Customer Job

 This field is accessible only if Invoice Restriction is 'Customer/CustJob'.
 Specify the customer job by which to restrict tickets added to this invoice. Only tickets posted to this customer and customer job (for the specified vendor) can be added to this invoice.
 If this field is blank, only tickets posted to the specified customer where the customer job is blank may be added to this invoice.
 If both customer and customer job are blank, tickets posted to any customer (for the specified vendor) where the customer job is blank can be added to this invoice.
Note: Once tickets are added to the invoice, this field is disabled and cannot be changed.

##  Description

 If you initialized payments, this field defaults the description specified during initialization. You can override the default.
 If entering payment manually, enter the description for this payment sequence, up to 30 characters. Initially defaults a description of “Material Purchase”.

##  Due Date

 Required.
 If you initialized payments , this field defaults the due date specified during initialization. You can override the default.
 If entering payment manually, specify the due date for this invoice. Initially defaults a due date based on the payment terms assigned to the specified material vendor. If no payment terms are specified for the vendor, defaults as blank. You can override the default.

## ECM

Specify the quantity this unit cost represents. Initially defaults based on the selected Cost Defaults option (Options menu, Cost Defaults), but may be overridden.

- E-Per Each

- C-Per Hundred

- M-Per Thousand

##  Hold Code

 If you initialized payments, this field defaults the hold code specified during initialization. You can override the default, but the hold code must be valid (set up in HQ Hold Codes).
 If entering payment manually, enter a hold code (from HQ Hold Codes) for this payment sequence, if applicable.
Note: All hold codes assigned to the vendor in AP Vendor Hold Codes will automatically be applied when the invoice is created.This field provides an opportunity for you to specify an additional hold you may want on the invoice.

##  INCo

 This field is accessible only if Invoice Restriction is 'Inventory'.
 Required.
 Specify the IN company by which to restrict tickets added to this invoice. Only tickets posted to a 'sold to' location within this IN company may be added to this invoice.
Note: Once tickets are added to the invoice, this field is disabled and cannot be changed.

##  Invoice Date

 Required.
 If you initialized payments, this field defaults the invoice date specified during initialization. You can override the default. If overridden, the invoice due date will be recalculated based on the payment terms specified for the payment sequence.
 If entering payment manually, enter the invoice date. Initially defaults the current date.

##  Invoice Restriction

 Specify the sales type by which to restrict transactions (tickets) that can be applied to this material vendor's invoice.

- N-None – Select this option if no restrictions apply. Any ticket posted to the specified material vendor can be applied to this invoice, regardless of sale type.

- C-Customer/CustJob – Select this option to restrict by customer and customer job. Only transactions for this material vendor that reference the specified customer and customer job can be applied to this invoice.

- J-JC Job – Select this option to restrict by JC job. Only transactions for this material vendor that reference the specified JCCo/Job can be applied to this invoice.

- I-Inventory – Select this option to restrict by inventory location. Only transactions for this material vendor that reference the specified INCo/Location can be applied to this invoice.

 Additional fields display for all options except 'None', and will be based on the option selected.
Note: Once you add tickets to the invoice, this field is inaccessible and cannot be changed.

##  JCCo

 This field is accessible only if Invoice Restriction is 'JC Job'.
 Specify the JC company by which to restrict tickets added to this invoice. Only tickets posted to a job in this JC company (for the specified vendor) may be added to this invoice.
 If left blank, tickets posted to any JCCo/job (for the specified vendor) may be added to this invoice.
Note: Once tickets are added to the invoice, this field is disabled and cannot be changed.

##  Job

 This field is accessible only if Invoice Restriction is 'JC Job'.
 Required if JC company specified.Specify the job by which to restrict tickets added to this invoice. Only tickets posted to this JCCo/job (for the specified vendor) may be added to this invoice.
 If the JCCo/job is left blank, tickets posted to any JCCo/job (for the specified vendor) may be added to this invoice.
Note: Once tickets are added to the invoice, this field is disabled and cannot be changed.

##  Material Vendor

 Specify the material vendor (from AP Vendors) for this invoice. This field represents
 vendor who invoiced you for materials you sold.
Note: If 'all invoice' compliance has been set up for this
 vendor and the vendor is out of compliance, a red warning will display above (next to the
 Seq
 # field).

##  Month

 Specify the posting month of the ticket transaction to add to the worksheet. Entry must be a month that is the same as or prior to the current batch month.

##  Pay Category

The Pay Category field on the MS Material Payment Worksheet, header Info tab.
 This field displays if you are using pay categories (flag in AP Company Parameters).
 Specify the pay category for this payment sequence. The pay category specified here determines the default pay type. Initially defaults a pay category as follows:

- If you have set up a standard or user pay category override in F3 Properties (not recommended), defaults the F3 pay category.

- If no F3 override exists, defaults the pay category specified for the current user in VA User Profile.

- If no override pay category is specified for the user, defaults the pay category defined in AP Company Parameters.

- If no pay category is defined for the company, default will be null. (In this case, pay type default will be the expense pay type from AP Company Parameters.)

 You can override the default if you allow overrides to pay type (flag in AP Company Parameters); otherwise, this field is inaccessible.
Note: If this field is blank, the Pay Type field must also be blank. You cannot enter one without the other. If you elect to leave both blank, the update will automatically assign the expense pay type from AP Company Parameters.

##  Pay Control

 If you initialized payments, this field defaults the pay control code specified during initialization. You can override the default.
 If entering payment manually, enter a pay control code, up to 10 characters, for this payment sequence, if applicable.
 If you enter a pay control code here, it can be used to selectively group transactions together for payment within AP.

##  Pay Terms

 Specify the payment terms for this material vendor. Initially defaults the payment terms
 specified for the material vendor in AP Vendors. Pay terms specified here will be used when
 creating the AP invoice to determine due dates, discount dates, and vendor discounts.

##  Pay Type

The Pay Type field on the MS Material Payment Worksheet, header Info tab.
 This field displays if you are using pay categories (flag in AP Company Parameters).
 Specify the pay type for this payment sequence. Initially defaults the expense pay type for the specified pay category. If you do not specify a pay category, this field defaults the expense pay type from AP Company Parameters.
 Default may be overridden if you allow overrides to pay type (flag in AP Company Parameters); however, pay type must be either assigned to the specified pay category (in AP Payable Types) or an 'unassigned' pay type. Unassigned pay types have no pay category restriction.
Note: If the pay category is null, the pay type must also be null. You cannot enter one without the other. If you elect to leave both null, the update will automatically assign the expense pay type from AP Company Parameters.

##  Sell To Location

 This field is accessible only if Invoice Restriction is 'Inventory'.
 Required.
 Specify the IN location by which to restrict tickets added to this invoice. Only tickets posted to this 'sold to' INCo and Location may be added to this invoice.
Note: Once tickets are added to the invoice, this field is disabled and cannot be changed.

##  Seq#

 Enter ‘N’, ‘NEW’, or ‘+’ to create a new entry, or enter the batch sequence number of an existing entry to display.

##  Tax Amt

 Initially defaults an amount based on the tax rate x tax basis. You can override the default.

##  Tax Basis

 Specify the basis on which to calculate sales tax for this material. Initially defaults the total cost of the material. If material is not taxable or no tax code was entered, tax basis will default as 0.00.

##  Tax Code

 Specify the tax code to use for determining the sales tax for this
 material, if applicable. Must be a valid tax code defined in HQ Tax Codes for the AP
 company's tax group.
 Tax code initially defaults based on the selected tax default option (Options menu, Sales Tax Default).

- Tax Exempt – Materials are exempt from sales tax. Tax code will default as null, but may overridden if the material is flagged as Taxable in HQ Materials.

- Sold To – Tax code will default based on the
 purchaser (i.e. if customer, defaults from AR Customers, if job, defaults from JC
 Jobs, if IN location, defaults from IN Locations.) If material is not flagged as
 taxable (in HQ Materials), tax code will default as null and cannot be overridden.

- Sold From Location – Tax Code will default from IN
 Locations as defined for the 'sold from' location. If material is not flagged as
 taxable (in HQ Materials), tax code will default as null and cannot be overridden.

##  Tax Type

 Specify the tax type for this transaction.

- 1-Sales

- 3-VAT (Value Added Tax)

 Default is determined by the Default Country specified for the active company in HQ Company Setup:

- If Default Country is ‘US’, defaults as ‘1-Sales’.

- If Default Country is other than ‘US’ (e.g. AU, CA, etc.), defaults as ‘3-VAT’.

 You may override the default as necessary.

##  Total Cost

 Total amount paid to the vendor for this material. Initially defaults an amount based on units x unit cost/ECM. Overrides to this amount will cause the unit cost to recalculate.

##  Trans#

 If you initialized payments, this field displays the ticket transaction to include on the invoice. You cannot edit this field, but transactions may be added to or deleted from the batch.
 If entering payments manually, specify the ticket transaction to add to this payment sequence. Transaction must be posted to the material vendor specified in the header, and must be posted in a month equal or prior to the invoice batch month. Press F4 for a list of valid ticket transactions.
Note: Transactions can only be applied to an invoice if they have not already been applied to another invoice in the current batch, are not in another batch, or have not been updated to AP.

##  Unit Cost

 Specify the unit cost for this material. The cost must be equal to or greater than 0.00. This is the dollar amount that will be paid to the vendor per unit, per hundred units, or per thousand units of this material. Initially defaults a value based on the selected Cost Defaults option (Options menu, Cost Defaults). Options are:

- None – Unit cost will default as 0.00.

- Ticket Sales Price – Defaults the unit price specified for this material on the MS ticket.

- PO Vendor Material – Defaults a unit cost based on the cost option specified for the vendor/material/UM in PO Vendor Materials.

- IN Last Cost – Defaults the Last Unit Cost specified for this material (based on the 'sold from' location and UM) in IN Location Materials.

Note: If you selected the Adjust Cost for Sales Tax option (Options menu), the unit cost for this material will be reduced by a tax rate (determined by tax code), and the sales tax will be posted as a separate part of the invoice line (in AP). You should only need to use this feature if your ticket price or inventory cost includes sales tax that needs to be separated on the AP invoice.
Note: The Adjust Cost for Sales Tax option is only available for Ticket Sales Price and IN Last Cost default options and Sold To and Sold From Location sales tax default options.
