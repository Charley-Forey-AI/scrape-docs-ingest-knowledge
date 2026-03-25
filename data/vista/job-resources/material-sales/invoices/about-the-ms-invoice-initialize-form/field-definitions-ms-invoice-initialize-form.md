---
title: "Field Definitions: MS Invoice Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/invoices/about-the-ms-invoice-initialize-form/field-definitions-ms-invoice-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/invoices/about-the-ms-invoice-initialize-form/field-definitions-ms-invoice-initialize-form"
---

# Field Definitions: MS Invoice Initialize Form

The following is a list of field descriptions for the MS
 Invoice Initialize form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Separate Invoice Per Location Group

 Check this box to generate a separate invoice per customer/location group. Each invoice generated for a customer/location group will include all transactions posted to locations within the location group. If restricting by location group, the system generates separate invoices for each location group within the specified range.
 Do not check this box if you do not want separate invoices printed for each customer/location group. Each invoice generated for a customer will include all transactions, regardless of location group. If restricting by location group, only transactions posted to locations within the specified range of location groups will be included on the invoice.
Note: The 'Separate Invoice Per Location' option works independently of this option; therefore, if you want all locations groups included on a single invoice per customer, you should not check the 'Separate Invoice Per Location" option. That option, when checked, will print a separate invoice per customer/location, regardless of how you set this flag.

##  Restriction Options

 For each option, indicate whether to use as restriction for initialization.
Location Group – Check this box to restrict transactions for billing to a specified location group or range of location groups (indicated to the right of this field). If not checked, initialization will include all transactions, regardless of location group.
Location – Check this box to restrict transactions for billing to a specified location or range of locations (indicated to the right of this field). If not checked, initialization will include all transactions, regardless of location.
Customer – Check this box to restrict transactions for billing to a single customer (indicated to the right of this field). If not checked, initialization will include all transactions, regardless of customer.
Customer Job – Enabled only if the “Customer” option is checked, and a customer is specified.Check this box to restrict transactions for billing to a single customer job (indicated to the right of this field). If not checked, initialization will include all transactions, regardless of customer job.
Customer PO# – Enabled only if the “Customer” option is checked, and a customer is specified.Check this box to restrict transactions for billing to a single customer PO# (indicated to the right of this field). If not checked, initialization will include all transactions, regardless of PO#.
Billing Frequency – Check this box to restrict transactions for billing to a single bill frequency (indicated to the right of this field). If not checked, initialization will include all transactions, regardless of bill frequency.
Payment Type – Check this box to restrict transactions for billing to a single payment type (indicated to the right of this field). If not checked, initialization will include all transactions, regardless of payment type.

##  Location Group: From/To

 Specify the beginning and ending in a range of location groups (from IN Location Groups) to restrict by. Only transactions ‘sold from’ locations within this range of location groups will be initialized to an invoice.

##  Separate Invoice Per Location

 Check this box to create a separate invoice per location by customer. If restricting by location, a separate invoice will be generated for each location within the specified range by customer.
 Do not check the box if you do not want separate invoices printed for each location by customer. All tickets or hauler time sheets posted to the same customer will be printed on a single invoice, regardless of location. If restricting by location, only locations within the range will be included on the invoice.

##  Location: From/To

 Specify the beginning and ending in a range of locations (from IN
 Locations) to restrict by. Only transactions ‘sold from’ locations within this range will
 be initialized to an invoice. If you are also restricting by location group, locations
 within this range must be assigned to the specified location group. If using the “Separate
 Invoice Per Location” option, then a separate invoice will be generate for each location
 within this range by customer.

## Customer

Enter an AR customer number or press
 F4
 to select one from a list. Only transactions posted to this customer will be initialized to
 an invoice. AR customers are created and maintained using the [ AR Customers ](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form) form.

##  Customer Job

 Enabled only if the “Customer” option is checked, and a customer is specified.
 Specify the customer job to restrict by. Only transactions posted to this customer job will be initialized to an invoice.

##  Customer PO#

 Enabled only if the “Customer” option is checked, and a customer is specified.
 Specify the customer PO# to restrict by. Only transactions posted to this customer PO# will be initialized to an invoice.

## Billing Frequency

Use this field to initialize invoices using the
 billing frequency on the AR customers. Enter a billing frequency or press F4  to
 select one from a list. Only transactions associated with an AR customer with the
 selected billing frequency will be initialized to an invoice.
Billing frequencies are created and maintained using
 the [ HQ Frequency Codes ](/en/vista/vista/administration/headquarters/company-setup/hq-frequency-codes-form) form, and they are associated with
 AR customers using the Bill Frequency field on the Material
 Sales tab of the [ AR Customers ](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form) form.

##  Payment Type

 Specify the payment type (A-On Account, C-Cash, X-Credit Card) to restrict by. Only transactions with this payment type will be initialized to an invoice.

## Include Ticket & Time Sheets: From/Through

Specify the date from and through which to include transactions for billing.Transactions with a ‘sales’ date within this date range will be included on an invoice. The system excludes all transactions with dates prior to the ‘From’ date and later than the ‘Through’ date.

##  Invoice Date

 Required.
Specify the default date that the system will assign to each invoice generated during initialization. Discount and Due dates will calculate based on this date and the customer’s payment terms. You can override this date in MS Invoice Edit.
Note: Once you enter the invoice date, the Update button is enabled, allowing you to initialize invoices based on selection criteria.
