---
title: "Field Definitions: MS Material Payment Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/ms-material-payment-initialize-form/field-definitions-ms-material-payment-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/ms-material-payment-initialize-form/field-definitions-ms-material-payment-initialize-form"
---

# Field Definitions: MS Material Payment Initialize Form

The following is a list of field descriptions for the MS
 Material Payment Initialize form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Location Group

 Check this box to restrict transactions for payment to a specified location group or range of location groups (indicated to the right of this field).
 Do not check this box if you do not want to restrict initialization by location group. Initialization will include all transactions, regardless of location group.

##  Location Group: Begin/End

 Specify the beginning and ending in a range of location groups (from IN Location Groups) by which to restrict payment initialization. Only ticket and time sheet transactions posted to locations within this range of location groups will initialize for payment.

##  From Location

 Check this box to restrict transactions for payment to a specified 'from' location or range of locations (indicated to the right of this field).
 Do not check this box if you do not want to restrict initialization by 'from' location. Initialization will include all transactions, regardless of location.

##  From Location: Begin/End

 Specify the beginning and ending in a range of locations (from IN
 Locations) by which to restrict payment initialization. Transactions with a ‘from location’
 within this range of locations will initialize for payment. If you are also restricting by
 location group, locations within the specified range must be assigned to a location group
 within the specified range of location groups.

##  Material Vendor

 Check this box to restrict transactions for payment to a single material vendor (indicated to the right of this field).
 Do not check this box if you do not want to restrict initialization by material vendor. Initialization will include all transactions, regardless of material vendor.

##  Material Vendor

 Specify the vendor (from AP Vendors) for restricting payment initialization. Transactions
 posted to this material vendor will initialize for payment.

##  Material Category

 Check this box to restrict transactions for payment to a single material category (indicated to the right of this field).
 Do not check this box if you do not want to restrict initialization by material category. Initialization will include all transactions, regardless of material category.

##  Material Category

 Specify the material category (from HQ Material Categories) for restricting payment initialization. Transactions posted to materials within this material category will initialize for payment.

##  Material Code

 Check this box to restrict transactions for payment to a single material or range of materials (indicated to the right of this field).
 Do not check this box if you do not want to restrict initialization by material code. Initialization will include all transactions, regardless of material.

##  Material Code: Begin/End

 Specify the beginning and ending in a range of materials (from HQ Materials) by which to restrict payment initialization. Transactions posted for materials within this range of materials will initialize for payment. If you are also restricting by material category, initialization will only include materials with the material range that are assigned to the specified material category.

##  Sale Type

 Specify the sale type by which to restrict transactions for payment.

- N-None – All transactions meeting all other selection criteria will initialized for payment, regardless of sale type.

- C-Customer/CustJob – Only 'customer' transactions referencing the Customer and Customer Job (specified below) that meet all other selection criteria will be initialized for payment.

- J-JC Job – Only 'job' transactions referencing the JCCo and Job (specified below) that meet all other selection criteria will be initialized for payment.

- I-Inventory – Only 'inventory' transactions referencing the INCo and To Location (specified below) that meet all other selection criteria will be initialized for payment.

Note: The system uses the sale type to restrict the transactions pulled into the batch; it is not used to group transactions together on an invoice. You must use the 'create a separate invoice by' options to group transactions by sale type.

##  Customer

 This field is accessible only if restricting by 'C-Customer/Cust Job' sale type.
 Specify the customer by which to restrict transactions for payment. Only transactions referencing this customer and meeting all other selection criteria will initialize.
 If this field is blank, initialization will include all 'customer' transactions meeting the selection criteria.
Note: You must specify a customer here if you will also be restricting by Customer Job.

##  Customer Job

 This field is accessible if restricting by 'C-Customer/Cust Job' sale type and a Customer is specified.
 Specify the customer job by which to restrict transactions for payment. Only transactions referencing this customer/customer job and meeting all other selection criteria will initialize.
 If this field is blank, initialization will include all transactions for the specified customer that meet the selection criteria.
Note: If you leave both Customer and Customer Job blank, initialization will include all 'customer' transactions meeting the selection criteria.

##  JCCo

 This field is accessible only if restricting by 'J-JC Job' sale type.
 Specify the JC company by which to restrict transactions for payment. Only transactions referencing this JC company and meeting all other selection criteria will be initialized.
 If left blank, initialization will include all 'job' transactions meeting the selection criteria.
Note: You must specify a company here if you will also be restricting by Job.

##  Job

 This field is accessible if restricting by 'J-JC Job' sale type and a JC company is specified.
 Specify the JC job by which to restrict transactions for payment. Only transactions referencing this JC company/job and meeting all other selection criteria will initialize.
 If left blank, initialization will include all transactions referencing the specified JC company that meet the selection criteria.
Note: If you leave both JCCo and Job blank, initialization will include all 'Job' transactions meeting the selection criteria.

##  INCo

 This field is accessible only if restricting by 'I-Inventory' sale type.
 Specify the IN company by which to restrict transactions for payment. Transactions referencing this IN company and meeting all other selection criteria will initialize.
 If this field is blank, initialization will include all 'inventory' transactions meeting the selection criteria.
Note: You must specify a company here if you will also be restricting by To Location.

##  To Location

 This field is accessible if restricting by 'I-Inventory' sale type and an IN company is specified.
 Specify the 'to location' by which to restrict transactions for payment. Only transactions referencing this INCo/To Location and meeting all other selection criteria will initialize.
 If left blank, initialization will include all transactions referencing the specified IN company that meet the selection criteria, regardless of location.
Note: If you leave both INCo and To Location blank, initialization will include all 'inventory' transactions meeting the selection criteria.

##  Include Tickets Entered for Month

 Required.
 Specify the month to pull transactions from for payment initialization. This field initially defaults the current batch month, but you can override this default with any month that is prior to the current batch month.Transactions posted in this month that meet all other selection criteria will initialize to the payment worksheet.

##  Include Tickets With Sale Dates: From/Through

 Specify the date from and through which to restrict payment initialization. Tickets posted to a material vendor with a sale date within this range will initialize for payment.

##  Customer Sales: Material Cost

 Select the cost option to use for determining the default unit cost to be paid to the material vendor for tickets posted to customers:

- 0-None – Unit cost will default as 0.00.

- 1-MS Ticket Sales Price – Defaults the unit price specified for this material on the MS ticket.

- 2-PO Vendor Materials – Defaults a unit cost based on the cost option specified for the vendor/material/UM in PO Vendor Materials.

- 3-Inventory Last Cost – Defaults the Last Unit Cost specified for this material (based on the 'sold from' location and UM) in IN Location Materials.

- 4-MS Quote Matl Vendor Cost – Defaults the Unit Cost specified on the customer quote for the location/material vendor/material/UM.

Note: If you check the Adjust for Sales Tax option (only available for options 1 and 3), the unit cost for taxable materials will be reduced by a tax rate, and the sales tax will be posted as a separate part of the invoice line (in AP).

##  Customer Sales: Sales Tax

 Select how the default tax code will be determined for materials sold to
 customers.

- 0-Tax Exempt – Materials are exempt from sales tax. Tax code will default as null. May be overridden (in MS Material Payment Worksheet) if the material is flagged as taxable in HQ Materials.

- 1-Sold To Customer – Tax code will default from AR
 Customers. If material is not taxable (flag in HQ Materials), the tax code will
 default as null and cannot be overridden.

- 2-Sold From Location – Tax code will default from IN
 Locations for the 'sold from' location. If material is not taxable (flag in HQ
 Materials), the tax code will default as null and cannot be overridden.

##  Customer Sales: Adjust for Sales Tax

 Enabled only when Material Cost option is 1 (MS Ticket Sales Price) or 3 (Inventory Last Cost).
 Check this box to reduce the default unit cost for materials sold to customers by a tax rate. If a material is taxable (flag in HQ Materials), the default unit price will be reduced by the appropriate tax rate (based on tax code), and the sales tax will be posted as a separate part of the invoice line (in AP).
Note: This feature is most useful when your ticket price or inventory cost includes sales tax that needs to be separated on the AP invoice.
 Do not check this box if the default unit cost for materials sold to customers will not be adjusted for sales tax.

##  Job Sales: Material Cost

 Select the cost option to use for determining the default unit cost to be paid to the material vendor for tickets posted to jobs:

- 0-None – Unit cost will default as 0.00.

- 1-MS Ticket Sales Price – Defaults the unit price specified for this material on the MS ticket.

- 2-PO Vendor Materials – Defaults a unit cost based on the cost option specified for the vendor/material/UM in PO Vendor Materials. If material cost overrides have been set up for the job, the default unit cost will be based on the override.

- 3-Inventory Last Cost – Defaults the Last Unit Cost specified for this material (based on the 'sold from' location and UM) in IN Location Materials.

- 4-MS Quote Matl Vendor Cost – Defaults the Unit Cost specified on the job quote for the location/material vendor/material/UM.

Note: If you check the Adjust for Sales Tax option (only available for options 1 and 3), the unit cost for taxable materials will be reduced by a tax rate, and the sales tax will be posted as a separate part of the invoice line (in AP).

##  Job Sales: Sales Tax

 Select how the default tax code will be determined for materials sold to
 jobs.

- 0-Tax Exempt – Materials are exempt from sales tax. Tax code will default as null. May be overridden (in MS Material Payment Worksheet) if the material is flagged as taxable in HQ Materials.

- 1-Sold To Customer – Tax code will default from JC
 Jobs. If material is not taxable (flag in HQ Materials), the tax code will default as
 null and cannot be overridden.

- 2-Sold From Location – Tax code will default from IN
 Locations for the 'sold from' location. If material is not taxable (flag in HQ
 Materials), the tax code will default as null and cannot be overridden.

##  Job Sales: Adjust for Sales Tax

 Enabled only when Material Cost option is 1 (MS Ticket Sales Price) or 3 (Inventory Last Cost).
 Check this box to reduce the default unit cost for materials sold to jobs by a tax rate. If a material is taxable (flag in HQ Materials), the default unit price will be reduced by the appropriate tax rate (based on tax code), and the sales tax will be posted as a separate part of the invoice line (in AP).
Note: This feature is most useful when your ticket price or inventory cost includes sales tax that needs to be separated on the AP invoice.
 Do not check this box if the default unit cost for materials sold to jobs will not be adjusted for sales tax.

##  Inventory Sales: Material Cost

 Select the cost option to use for determining the default unit cost to be paid to the material vendor for tickets posted to Inventory locations:

- 0-None – Unit cost will default as 0.00.

- 1-MS Ticket Sales Price – Defaults the unit price specified for this material on the MS ticket.

- 2-PO Vendor Materials – Defaults a unit cost based on the cost option specified for the vendor/material/UM in PO Vendor Materials.

- 3-Inventory Last Cost – Defaults the Last Unit Cost specified for this material (based on the 'sold from' location and UM) in IN Location Materials.

- 4-MS Quote Matl Vendor Cost – Defaults the Unit Cost specified on the inventory quote for the location/material vendor/material/UM.

Note: If you check the Adjust for Sales Tax option (only available for options 1 and 3), the unit cost for taxable materials will be reduced by a tax rate, and the sales tax will be posted as a separate part of the invoice line (in AP).

##  Inventory Sales: Sales Tax

 Select how the default tax code will be determined for materials sold to
 inventory.

- 0-Tax Exempt – Materials are exempt from sales tax. Tax code will default as null. May be overridden (in MS Material Payment Worksheet) if the material is flagged as taxable in HQ Materials.

- 1-Sold To Location – Tax code will default from IN
 Locations for the ‘sold to’ location. If material is not taxable (flag in HQ
 Materials), the tax code will default as null and cannot be overridden.

- 2-Sold From Location – Tax code will default from IN
 Locations for the 'sold from' location. If material is not taxable (flag in HQ
 Materials), the tax code will default as null and cannot be overridden.

##  Inventory Sales: Adjust for Sales Tax

 Enabled only when Material Cost option is 1 (MS Ticket Sales Price) or 3 (Inventory Last Cost).
 Check this box to reduce the default unit cost for materials sold to Inventory locations by a tax rate. If a material is taxable (flag in HQ Materials), the default unit price will be reduced by the appropriate tax rate (based on tax code), and the sales tax will be posted as a separate part of the invoice line (in AP).
Note: This feature is most useful when your ticket price or inventory cost includes sales tax that needs to be separated on the AP invoice.
 Do not check this box if the default unit cost for materials sold to Inventory locations will not be adjusted for sales tax.

##  AP Co#

 Required.
 Specify the AP company for this material payment batch. Initially defaults the AP company assigned to the current MS company (in MS Company Parameters). May be overridden with any valid AP company, as long as the following applies:

- Both the posting AP company and the MS AP company share the same vendor and tax groups.

- Both AP companies have the same GL interface levels specified (i.e. Summary, Transaction, Line, or None).

Note: The AP company may be overridden by sequence in the payment worksheet.

##  Invoice Date

 Required.
 Specify the date that will become the default invoice date for all initialized payments. You may override the default by sequence on the payment worksheet.
Note: When making multiple passes of criteria to generate invoices, if initialization will combine tickets on existing invoices because all the information matches, but you want them to be on separate invoices, you can use a different invoice date for each pass. The system will then generate new invoices for the tickets instead of adding them to existing invoices.

##  Due Date

 Required.
 Specify the date that will become the default due date for all initialized payments. You may override the default by sequence on the payment worksheet.
Note: Due date specified here overrides the standard payment terms due date calculation.

##  Description

 Enter the description to use for all initialized payment sequences, up to 30 characters. Initially defaults a description of “Material Purchase”.You may override the description by sequence on the payment worksheet.
Note: When making multiple passes of criteria to generate invoices, if initialization will combine tickets on existing invoices because all the information matches, but you want them to be on separate invoices, you can enter a different description for each pass. The system will then generate new invoices for the tickets instead of adding them to existing invoices.

##  AP Reference

The AP Reference field on the MS Material Payment Initialize form.
 Required.
 Enter the AP reference number to use for all initialized payment sequences, up to 30 characters.You may override the reference number by sequence on the payment worksheet.

##  Pay Control

 Optional.
 Enter the pay control code to use for all initialized payment sequences, up to 10 characters.You may override the pay control code by sequence on the payment worksheet.

##  Hold Code

 Optional.
 Enter the hold code (from HQ Hold Codes) to use for all initialized payment sequences.You may override the hold code by sequence on the payment worksheet.

##  Pay Category

The Pay Category field on the MS Material Payment Initialize form, AP Invoice Defaults tab.
 Displays only if using pay categories (flag in AP Company Parameters).
 Specify the pay category for this material payment batch. The pay category determines the default pay type. Initially defaults a pay category as follows:

- If you have set up a standard or user pay category override in F3 Properties (not recommended), defaults the F3 pay category.

- If no F3 override exists, defaults the pay category specified for the current user in VA User Profile.

- If no override pay category is specified for the user, defaults the pay category defined in AP Company Parameters.

- If no pay category is defined for the company, default will be null. (In this case, pay type default will be the expense pay type from AP Company Parameters.)

 Default may be overridden if you allow overrides to pay type (flag in AP Company Parameters); otherwise, input is disabled.
Note: If you leave the pay category null, the pay type must also be null. You cannot enter one without the other.

##  Pay Type

The Pay Type field on the MS Material Payment Initialize form, AP Invoice Defaults tab.
 Displays only if using pay categories (flag in AP Company Parameters).
 Specify the pay type for this material payment batch. Initially defaults the expense pay type for the specified pay category. If no pay category is specified, defaults the expense pay type from AP Company Parameters.
 Default may be overridden if you allow overrides to pay type (flag in AP Company Parameters); however, pay type must be either assigned to the specified pay category (in AP Payable Types) or an 'unassigned' pay type. Unassigned pay types have no pay category restriction.
Note: If the pay category is null, the pay type must also be null. You cannot enter one without the other.

##  CM Co#

 Optional.
 Enter the CM company to use for all initialized payment sequences. Initially defaults the CM company specified (in AP Company Parameters, Subledgers tab) for the AP company indicated above.
 May be overridden by sequence on the payment worksheet.

##  CM Account

 Optional.
 Enter the CM account from which all initialized payments will be made. Initially defaults the CM account specified (in AP Company Parameters, Subledgers tab) for the AP company indicated above.If null, CM Account will be specified when payment is made from AP.
 May be overridden by sequence on the payment worksheet.

## Create a Separate Invoice By

- Matl Vendor, Customer, and Customer Job – Check this box to generate a separate invoice per material vendor, customer, and customer job. Leave unchecked to generate a single invoice per material vendor.

- Matl Vendor and JC Job – Check this box to generate a separate invoice per material vendor, JC company, and JC job. Leave unchecked to generate a single invoice per material vendor.

- Matl Vendor and Sell To Location – Check this box to generate a separate invoice per material vendor, IN company, and 'sell to' location. Leave unchecked to generate a single invoice per material vendor.

Note: If you are restricting by Sale Type, make sure you select the option that is applicable to the selected sale type. For example, if restricting by 'Customer' sale type, then only the 'separate invoice per material vendor, customer, customer job' option would be applicable.
If the Sales Type restriction is 'None', any of these options are applicable. However, if you check one option but not the others, separate invoices will be generated for transactions falling under the selected option's criteria, and a single invoice generated per haul vendor for the remaining transactions.
For example, if:
Matl Vendor, Customer, Customer Job:  Y
Matl Vendor and JC Job:  N
Matl Vendor and Sell To Location:  N
Invoices would be generated as follows:
Material Vendor
Invoice
Customer/Cust Job
JC Job
Sell To Loc

1
1001
250 / 0001

1002
300 / 0010

1003

13000-001

1003

300

2
1004
600 / 0001

1005
625 / 0025

1006

25310-100

1006

225
