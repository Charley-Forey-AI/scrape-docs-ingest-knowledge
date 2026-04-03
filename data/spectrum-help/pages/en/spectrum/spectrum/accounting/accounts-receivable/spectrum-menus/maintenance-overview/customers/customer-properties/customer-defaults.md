---
title: "Customer Defaults | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/customers/customer-properties/customer-defaults"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/customers/customer-properties/customer-defaults"
---

# Customer Defaults

Use the Customer Defaults screen to
 view additional properties fields pertaining to the customer.
Field
Description

Invoice defaults

Salesperson
Add the code for the default salesperson for this customer. The person's full name displays next to the code.

Related-Party G/L AccountsIf the selected customer is a related party, click this button
 to open the [Related-Party G/L Accounts](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-defaults/related-party-gl-accounts) window to manage override G/L accounts
 for related-party customers. Note: This button will be
 disabled if the Allow G/L account overrides by cost center option is
 selected.

Terms code
Enter the default terms code for this customer. The full terms description will display next to the terms code.
The default terms code may be overwritten during invoice entry.

Retention
Enter the typical retention percentage for this customer. During initial entry
 of a customer, this number defaults from the Accounts Receivable
 Installation screen. This is the default retention for this
 customer and may be changed in Customer Invoice
 Entry.
The retention amount entered in this field will default on the contract.

Taxable
Select Yes if this is a taxable customer, No if this is not a taxable customer, or No Default if the customer's invoices are conditionally taxable and the decision needs to be made on an invoice-by-invoice basis.

Sales tax code
Enter the default sales tax code (up to 15 alpha-numeric digits) for this
 customer, or press Enter to accept the software
 default. The full sales tax code description will display next to the tax
 code.
This code should have already have been set up in Sales Tax Code
 Maintenance. This is only the default tax code for this
 customer and may be changed during Invoice Entry.

Credit and collections

Date established
The date this customer was first entered into the software will display. A different date may be entered, if desired.

Credit limit
Enter the credit limit for this customer, if applicable.

Finance charge code
Enter the finance charge transaction code, or press F4 to select from a list of available finance charge codes. Up to 10 characters are permitted.
If a code is specified in this field, the Finance charge field must also be completed with a non-zero value. If no finance charge is to be assessed for this customer, do not enter a code.
This code is useful for companies that have departmentalized operations.
 Customers' interest income charged on transaction codes may then be posted
 to the correct department through the G/L code specified in
 Transaction Code File Maintenance.

Finance charge
If a Finance charge code has been specified, entry of a non-zero value in this field is required. Enter the monthly finance charge percentage for this customer. The percentage entered here will be used when Finance Charge Calculation is performed.

Send statements?
Select this checkbox if monthly statements are an option for this customer. Clear this checkbox if the customer should not receive statements.
Customers who fulfill the selection criteria in Print Statements will receive statements only if the checkbox is selected; statements will never print for customers for whom this checkbox is cleared.

Process transactions in local currency?
If Multi-Currency processing is being used, Administrators should select this
 checkbox if they need to specify an alternative currency when printing the
 Invoice Form and Customer Statement. If this checkbox is selected, a
 corresponding Currency Code field displays.

Currency code
Use this field to specify an alternative currency when printing the Invoice Form and Customer Statement. This setup will also control the A/R G/L account default in [Customer Invoice Entry](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-entry/customer-invoice-entry).
Note: The system will not allow you to make changes to the assigned currency
 code if the customer's balance is non-zero.

Pricing codes

Material
Add or edit the customer price level (1-5) for material pricing in the Work Order, Time + Material, Order Processing, and Materials Management modules, or use the drop-down menu to select the customer price level.
Fields in this section will be hidden if the Work Order, Time + Material,
 Materials Management, and Order Processing modules are not present.

Labor
Enter the customer price level (1-5) for labor pricing in the Work Order and Time + Material modules, or use the drop-down menu to select the customer price level.

WO material markup
Enter a material markup code in this field, or press F4 to select one.
This field will be hidden if the Work Order module is not present.
