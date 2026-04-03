---
title: "Work Order Billing Setup | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/work-order-billing-setup"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/work-order-billing-setup"
---

# Work Order Billing Setup

Use the Work Order Billing Setup
 screen to enter information about the work order that includes terms, lead source, print
 status, and rates.
Note: The Alternate bill-to address and Over/under billing sections of this screen will be hidden when a 'Job' work
 order is displayed on this screen.
Field
Description

Classification

Lead source
Enter a valid lead source code. Entry
 in this field will be required if the Work Order
 Installation option for 'Require lead source in work order
 entry?' is selected.
Salesperson
Enter a valid code identifying the
 person responsible for this sale. When a work order is
 created from the Service Contract module and a salesperson is associated
 with the service contract, the salesperson code from the Service Contract
 module defaults into this field.

Taken by
The operator ID defaults as the person
 entering the order. The default can be overridden if desired.
Print status
The current print status of the work
 order displays.
Terms and conditions

Terms code
Enter the payment terms code for this
 work order. The terms code must have been previously defined in A/R
 Terms Code File Maintenance.
Sales tax code
Enter a valid sales tax code for this
 billing customer; up to 15 characters are allowed. The sales tax code must have
 been previously defined in Accounts Receivable > Sales Tax Code Maintenance. For job work orders, the sales tax code
 defaults from the job setup. If the Use tax
 classification checkbox is not selected in Job
 Cost Installation, the tax code specified in the Job File Maintenance > Properties window defaults. Otherwise, if tax classification is used,
 the A/R sales tax code specified in Tax Classification File
 Maintenance for the code assigned to the job will default.

Spectrum computes the tax rate based on the
 current Accounts Receivable processing date.

Taxable?
Select this checkbox if the work for
 this customer is taxable; otherwise, leave this checkbox clear.
G/L department
This must-enter field will only be
 enabled for 'Site' work orders. This field will default from Work
 Order Type File Maintenance into each new work order. If the
 field is blank in Work Order Type File Maintenance, then
 this field will be blank by default and the operator must enter a valid code
 before close is permitted. The code entered here will be
 used whenever a new transaction is added for Labor, Material and Other
 Charges.
Note: This field will be
 hidden when a 'Job' work order is displayed on this screen.

Cost center
If the cost center feature is enabled
 in the Enterprise Installation screen for this
 company,enter a cost center code for this billing.
Alternate bill-to address

Print alternate address on work order form and invoice?
Select this checkbox to print an
 alternate address on the work order form and invoice. When this checkbox is
 selected, the Bill-to code will be must-enter.  If no
 alternate address is specified, the customer's address will display below.


Bill-to code
Select an alternate address to include
 on work order form and invoice.
Over/under billing

Override company-wide earned revenue markup %?
When this checkbox is selected, the
 Over/Under Billing format of the Profitability Report will be calculated using
 the markup percentage specified below rather than the one stored in the
 Work Order Installation screen.
Override markup %
Enter a positive value in this field
 for the override markup percentage to apply to the work order. This field will
 only be available for entry if the Override company-wide earned revenue markup
 % checkbox is selected.
Billing rates

Material level
If a contract is specified, the pricing
 level defaults from Service Contract File Maintenance.
 If a contract is not specified, the pricing level defaults from
 Customer File Maintenance. The default may be
 overridden if desired.
Labor level
If a contract is specified, the pricing
 level defaults from Service Contract File Maintenance.
 If a contract is not specified, the pricing level defaults from
 Customer File Maintenance. The default may be
 overridden if desired.
Material markup
This field will default from
 Service Contract Maintenance if a contract # has been
 specified. If the markup field is blank in Service Contract
 Maintenance, then the field will default from Site
 Standard Charges. If the markup field is blank in
 Site Standard Charges, then the field will default
 next from Customer File Maintenance. If the markup field
 is blank in Customer File Maintenance, then the field
 will default from Work Order Installation as a last
 resort. The Material markup code entered here will be
 used when the software tries to compute the unit price from the cost of a
 material item when added into Material Entry or the detail windows of
 Purchase Order Entry or Accounts Payable > Invoice/Credit Memo Entry. This optional entry field will only be enabled for 'Site'
 work orders. When calculating the markup price, the software marks up the
 cost, including any sales and use tax.
Note: This field will be hidden when a 'Job' work order is
 displayed on this screen.
