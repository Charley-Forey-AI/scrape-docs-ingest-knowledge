---
title: "Field Definitions: MS Haul Payment Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-payment-initialize-form/field-definitions-ms-haul-payment-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-payment-initialize-form/field-definitions-ms-haul-payment-initialize-form"
---

# Field Definitions: MS Haul Payment Initialize Form

The following is a list of field descriptions for the MS Haul
 Payment Initialize form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Location Group

 Check this box to restrict transactions for payment to a specified location group or range of location groups (indicated to the right).
 Leave this box unchecked if not restricting initialization by location group. Initialization will include all transactions, regardless of location group, that meet all other criteria.

##  Location Group: Begin/End

 Specify the beginning and ending in a range of location groups (from IN Location Groups) by which to restrict payment initialization. Only ticket and time sheet transactions posted to locations within this range of location groups, that meet all other selection criteria, will be initialized for payment.
Note: If both fields are left blank, initialization will include all transactions, regardless of location group, that meet all other criteria.

##  From Location

 Check this box to restrict transactions for payment to a specified location or range of locations (indicated to the right of this field).
 Leave this box unchecked if not restricting initialization by 'from' location. Initialization will include all transactions, regardless of location, that meet all other criteria.

##  From Location: Begin/End

 Specify the beginning and ending in a range of locations (from IN
 Locations) by which to restrict payment initialization. Only transactions with a ‘from
 location’ within this range of locations, that meet all other selection criteria, will be
 initialized for payment. If you are also restricting by location group, locations within
 the specified range must be assigned to a location group within the specified range of
 location groups.
Note: If both fields are left blank, initialization will include all transactions, regardless of location, that meet all other criteria.

##  Ticket

 Check this box to restrict transactions for payment to a specific ticket number or range of ticket numbers (indicated to the right).
 Leave this box unchecked if you are not restricting initialization by ticket number. Initialization will include all transactions, regardless of ticket number, that meet all other criteria.

##  Ticket: Begin/End

 Specify the beginning and ending in a range of ticket numbers by which to restrict payment initialization. Only transactions with a ticket number within the specified range that meet all other criteria will be initialized for payment.
Note: If both fields are left blank, initialization will include all transactions, regardless of ticket number, that meet all other criteria.

##  Haul Vendor

 Check this box to restrict transactions for payment to a single haul vendor (indicated to the right).
 Leave this box unchecked if not restricting initialization by haul vendor. Initialization will include all transactions, regardless of haul vendor, that meet all other criteria.

##  Haul Vendor: Vendor

 Specify the vendor (from AP Vendors) by which to restrict payment initialization. Only
 transactions posted to this haul vendor that meet all other selection criteria will be
 initialized for payment.

##  Vendor Truck

 The system enables this field after you select the Haul Vendor checkbox and specify a vendor.
 Check this box to restrict transactions for payment to a single haul vendor’s truck (indicated to the right of this field).
 Leave this box unchecked if not restricting initialization by a specific vendor truck. Initialization includes all transactions, regardless of haul vendor, that meet all other criteria.

##  Sale Type

 Specify the sale type by which to restrict transactions for payment.

- N-None – All transactions meeting all other selection criteria will initialized for payment, regardless of sale type.

- C-Customer/Cust Job – Only 'customer' transactions referencing the Customer and Customer Job (specified below) that meet all other selection criteria will initialize for payment.

- J-JC Job – Only 'job' transactions referencing the JCCo and Job (specified below) that meet all other selection criteria will initialize for payment.

- I-Inventory – Only 'inventory' transactions referencing the INCo and To Location (specified below) that meet all other selection criteria will initialize for payment.

Note: The sale type is only used to restrict the transactions pulled into the batch; it is not used to group transactions together on an invoice. You must use the 'create a separate invoice by' options to group transactions by sale type.

##  Customer

 This field is accessible only if restricting by 'C-Customer/Cust Job' sale type.
 Specify the customer by which to restrict transactions for payment. Only transactions referencing this customer that meet all other criteria will be initialized.
 If this field is blank, initialization includes all 'customer' transactions that meet all other criteria.
Note: You must specify a customer here if restricting by Customer Job.

##  Customer Job

 This field is accessible if you are restricting by 'C-Customer/Cust Job' sale type and a Customer is specified.
 Specify the customer job by which to restrict transactions for payment. Only transactions referencing this customer/customer job that meet all other criteria will be initialized.
 If this field is blank, initialization includes all transactions for the specified customer that meet all other criteria.
Note: If you leave both Customer and Customer Job blank, initialization will include all 'customer' transactions meeting the selection criteria.

##  JCCo

 This field is accessible only if restricting by 'J-JC Job' sale type.
 Specify the JC company by which to restrict transactions for payment. Only transactions referencing this JC company that meet all other criteria will be initialized.
 If left blank, initialization will include all 'job' transactions that meet all other criteria.
Note: You must specify a company here if you will also be restricting by Job.

##  Job

 This field is accessible if restricting by 'J-JC Job' sale type and a JC company is specified.
 Specify the JC job by which to restrict transactions for payment. Only transactions referencing this JC company/job that meet all other criteria will be initialized.
 If left blank, initialization will include all transactions referencing the specified JC company that meet all other criteria.
Note: If you leave both JCCo and Job blank, initialization will include all 'Job' transactions meeting the selection criteria.

##  INCo

 This field is accessible only if restricting by 'I-Inventory' sale type.
 Specify the IN company by which to restrict transactions for payment. Only transactions referencing this IN company that meet all other criteria will be initialized.
 If left blank, initialization will include all 'inventory' transactions that meet all other criteria.
Note: You must specify a company here if you will also be restricting by To Location.

##  To Location

 This field is accessible if restricting by 'I-Inventory' sale type and an IN company is specified.
 Specify the 'to location' by which to restrict transactions for payment. Only transactions referencing this INCo/To Location that meet all other criteria will be initialized.
 If left blank, initialization will include all transactions referencing the specified IN company that meet the selection criteria.
Note: If you leave both INCo and To Location blank, initialization will include all 'inventory' transactions meeting the selection criteria.

## Include Tickets & Time Sheets Entered for Month

Required.
Specify the month from which to pull transactions for payment initialization. This field initially defaults the current batch month, but you can override it with any month that is prior to the current batch month. Transactions posted in this month that meet all other selection criteria will initialize to the payment worksheet.

## Include Tickets & Time Sheets : From/Through

Specify the date from and through which to restrict payment initialization. Tickets and time sheets having a sale date within this range that meet all other selection criteria will be initialized for payment.

##  Include Only Tickets and Time Sheets With a Pay Code Assigned

 Check this box to include only those tickets and time sheets assigned a pay code (that meet all other criteria) when initializing payments.
 Leave this box unchecked to include all tickets and time sheets meeting selection criteria, regardless of whether they are assigned a pay code.

##  Create a Separate AP Invoice by

You can create separate invoices by haul vendor and sale type by using the
 Create a Separate AP Invoice by section on the MS Haul Payment
 Initialize form.
The 'Create a Separate AP Invoice by' section
 allows you to create separate invoices by haul vendor and sale type. The available options
 are as follows:

- Haul Vendor, Customer, Customer Job –
 Check this box to generate a separate invoice per haul vendor, customer, and customer
 job. Leave unchecked to generate a single invoice per haul vendor.

- Haul Vendor and JC Job – Check this box
 to generate a separate invoice per haul vendor, JC company, and JC job. Leave
 unchecked to generate a single invoice per haul vendor.

- Haul Vendor and Sell To Location – Check
 this box to generate a separate invoice per haul vendor, IN company, and 'sell to'
 location. Leave unchecked to generate a single invoice per haul vendor.

Note: If you are restricting by Sale Type, make sure you
 select the option that is applicable to the selected sale type. For example, if restricting
 by 'Customer' sale type, then only the 'separate invoice per haul vendor, customer,
 customer job' option would be applicable. If the Sales Type restriction is 'None', any of
 these options are applicable. However, if you check one option but not the others, separate
 invoices will be generated for transactions falling under the selected option's criteria,
 and a single invoice generated per haul vendor for the remaining transactions.
If you select an option, initialization will
 create a separate invoice per haul vendor for each transaction meeting the option's
 criteria. For unselected options, the system creates a single invoice per haul vendor for
 all transactions with that sale type.
It is important to note that the Sale Type
 restriction will affect how these options work. For example, if you restrict by sale type
 'C' (Customer/Cust Job), then only the 'create a separate invoice per haul vendor,
 customer, and customer job' option would be applicable. If you are not restricting by sale
 type (i.e. Sale Type option is 'None'), all options would be applicable, and if checked,
 would group invoices accordingly. However, if you check only one option and not the others,
 be aware that separate invoices will be created for all transactions matching the selected
 option's criteria, and a single invoice created for all other transactions.
For example, if you set the following check
 boxes like this:
 Haul Vendor, Customer, Customer Job
 Haul Vendor and JC Job
 Haul Vendor and Sell To Location
The system generates invoices as follows:
Haul Vendor
Trans #
APRef
Customer/ Cust Job
JC Job
Sell To Loc

1
25
1001
250 / 0001

1
26
1002
300 / 0010

1
27
1003

13000-001

1
28
1003

300

2
29
1004
600 / 0001

2
30
1005
625 / 0025

2
31
1006

25310-100

2
32
1006

225

##  Invoice Date

 Required.
 Specify the date that will become the default invoice date for all initialized payments. You may override the default by sequence on the payment worksheet.
Note: When making multiple passes of criteria to generate invoices, if initialization will combine tickets on existing invoices because all the information matches, but you want them to be on separate invoices, you can use a different invoice date for each pass. The system will then generate new invoices for the tickets instead of adding them to existing invoices.

##  Due Date

 Required.
 Specify the date that will become the default due date for all initialized payments. You may override the default by sequence on the payment worksheet.
Note: Due date specified here overrides the standard payment terms due date calculation.

##  Description

 Enter the description to use for all initialized payment sequences, up to 30 characters. Initially defaults a description of “Material Haul”. You may override the default by sequence on the payment worksheet.
Note: When making multiple passes of criteria to generate invoices, if initialization will combine tickets on existing invoices because all the information matches, but you want them to be on separate invoices, you can enter a different description for each pass. The system will then generate new invoices for the tickets instead of adding them to existing invoices.

##  AP Company

 Required.
 Specify the AP company for this haul payment batch. Initially defaults the AP company assigned to the current MS company (in MS Company Parameters). May be overridden with any valid AP company having the same vendor group as the MS Company.
Note: The AP company may be overridden by sequence in the payment worksheet.

##  AP Reference

The AP Reference field on the MS Haul Payment Initialize form.
 Required.
 Enter the AP reference number to use for all initialized payment sequences, up to 30 characters.You may override this reference number by sequence on the payment worksheet.

##  Pay Control

 Optional.
 Enter the pay control code to use for all initialized payment sequences, up to 10 characters.You may override by sequence on the payment worksheet.

##  Hold Code

 Optional.
 Enter the hold code (from HQ Hold Codes) to use for all initialized payment sequences. You may override by sequence on the payment worksheet.

##  Pay Category

The Pay Category field on the MS Haul Payment Initialize form.

This field only displays if the Using Payable Category checkbox is selected in AP Company Parameters and is only enabled if the Allow Payable Type Override checkbox is selected.
If payable type overrides are allowed, specify the pay category for this payment sequence. The pay category specified here determines the default pay type.
This field defaults a pay category as follows:

- If an override pay category is specified for the current user in VA User Profile, that pay category defaults here.

- If no override pay category is specified for the user in VA User Profile, defaults the pay category defined in AP Company Parameters.

- If no pay category is defined for the company, this field defaults as blank. (In this case, the pay type default will be the Expense pay type from AP Company Parameters.)

Note: If you do not specify a pay category in this field, you cannot specify a pay type in the Pay Type field. You must either leave both fields blank or enter a value in both. If you elect to leave both fields null, the update will automatically assign the expense pay type from AP Company Parameters.

##  Pay Type

The Pay Type field on the MS Haul Payment Initialize form.

This field is only enabled if the Allow Payable Type Override checkbox is selected.
If using pay categories, this field initially defaults the Expense pay type for the specified pay category. You may change the default as needed; however, the pay type must either be assigned to the pay category or be a pay type that has no pay category restriction (that is, the Restrict Pay Type to Pay Category checkbox in AP Payable Types is not selected).
 If not using pay categories, this field defaults the Expense pay type specified in AP Company Parameters and may be overridden as needed.
Note: If you did not specify a pay category in the previous field, you cannot specify a pay type here. You must either leave both fields blank or enter a value in both. If you elect to leave both fields null, the update will automatically assign the expense pay type from AP Company Parameters.

##  CM Co#

 Optional.
 Enter the CM company to use for all initialized payment sequences. Initially defaults the CM company specified (in AP Company Parameters, Subledgers tab) for the AP company indicated above.
 May be overridden by sequence on the payment worksheet.

##  CM Account

 Optional.
 Enter the CM account from which all initialized payments will be made. Initially defaults the CM account specified (in AP Company Parameters, Subledgers tab) for the AP company indicated above.If null, CM Account will be specified when payment is made from AP.
 May be overridden by sequence on the payment worksheet.
