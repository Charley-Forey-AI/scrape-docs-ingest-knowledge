---
title: "Using Payable Categories | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/using-payable-categories"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/using-payable-categories"
---

# Using Payable Categories

If you require separate GL accounting for the different divisions, branches, or regions within your company, you can set up pay categories to represent each division, with each pay category defining its own set of pay types for transaction posting.
Pay categories determine pay type defaults. If a pay category is specified during invoice entry (AP Transaction Entry, AP Recurring Invoices, AP Unapproved Invoice Entry), the pay type defaults from the pay category based on the invoice line type. If you change a pay category, the pay type also changes. If you leave the pay category blank, or you are not using pay categories, pay types default from AP Company Parameters (Pay Types/Discounts/ICR tab).Note: When posting transactions in other modules that allow pay category/pay type entry (for example, MS Haul Payment Worksheets, MS Material Payment Worksheets, and PO Purchase Order Entry), default behaviors are the same as they are in AP.

To set up the system to use payable categories:

1. Set up payable categories in [AP Pay Category](/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/ap-pay-typescategories-forms/ap-pay-category-form).

1. In AP Company Parameters, check the Using Payable Category box (Pay Types/Discounts/ICR tab) to activate the use of payable categories. When you check this box, posting programs that require a pay type will also include a Pay Category field (i.e., AP Transaction Entry, AP Recurring Invoices, AP Unapproved Invoice Entry, and PO Purchase Order Entry). Although entry in this field is optional, you are always required to specify a pay type for the transaction line. The system enables the Payable Category Default field.

1. In the Payable Category Default field, enter the default pay category the system will use for transactions entered in AP Transaction Entry, AP Recurring Invoices, AP Unapproved Invoice Entry, and PO Purchase Order Entry. The system also uses this pay category as the default when updating subcontracts to AP via the SL Update to AP form.Once you specify a pay category on one of the transaction entry forms, the Pay Type field will default from AP Pay Category based on the associated line type.If you leave the Payable Category Default field blank on one of the transaction entry forms, the Pay Category field defaults as blank and the pay type defaults from AP Company Parameters (Pay Types/Discounts/ICR tab).
Note: You can set up overrides to the company default pay category by user in [VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form). If you choose to define pay category defaults by user, the system uses the user override each time the user enters a transaction. It is important to note that pay category defaults are not company specific; therefore, if you override by user, it is recommended that the specified pay category is set up for every company to which the user has access.

If you have defined a pay category default in F3 Properties (not recommended), it will override both the VA User Profile and AP Company Parameters defaults.

1. If you want to allow overrides to pay categories and pay types during posting, select the Allow Payable Type Override checkbox.

Related information

- [AP Payable Types Form](/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/ap-pay-typescategories-forms/ap-payable-types-form)

- [AP Transaction Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form)

- [AP Recurring Invoices Form](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form)

- [AP Unapproved Invoice Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)

- [PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)
