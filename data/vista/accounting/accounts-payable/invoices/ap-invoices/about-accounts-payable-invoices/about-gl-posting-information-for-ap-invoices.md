---
title: "About GL Posting Information for AP Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-gl-posting-information-for-ap-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-gl-posting-information-for-ap-invoices"
---

# About GL Posting Information for AP Invoices

Every invoice posted in Accounts Payable (via the AP
 Transaction Entry form) updates the General Ledger based on the GL accounts defined for
 other modules throughout the system.
Updates to General Ledger occur automatically when you post an
 invoice via the AP Batch Process. The GL accounts defined in other modules determine
 both the debits and credits associated with an invoices. Depending on the initial setup
 and the type of transaction you enter, the system may default a GL account without
 allowing an override, default a GL account with override allowed, or may require
 entry.
The following table describes the defaults on a transaction
 without retainage, use tax, or discounts.
Table 1. GL Account Defaults for AP Transaction EntryTrans Type
Default GL Account (Debit)
Default GL Account (Credit)

1-Job
The JC Department account
 assigned to the job/phase/cost type.
The Job pay type designated for
 the pay category (in AP Pay Category. If you did not specify a
 pay category, or you are not using one, the default is the Job pay
 type designated in AP Company Parameters.

2-Inventory
The IN location account for the
 material.
The Expense pay type designated
 for the specified pay category (in AP Pay Category). If you did
 not specify a pay category, or you are not using one, the default is
 the Expense pay type designated in AP Company Parameters.

3-Expense
The AP Vendors account
 for the vendor, or if a material, the HQ Materials account.

4-Equip
The EM department account for
 the equip/cost code/cost type.

5-Work Order
The EM Departments account for
 the equip/cost code/cost type.

6-Purch Order
Default for all PO types (Job, Inv, Exp,
 Equip, WO), is the same as like-named transaction types.
The Expense pay type designated
 for the specific pay category (in AP Pay Category) except for Job
 POs, in which case the default is the pay category's Job pay type.
 If you do not specify a pay category, or you are not using one, the
 default is the Expense or Job (for Job POs) pay type designated in
 AP Company Parameters.

7-Subcontract
The JC Departments account
 assigned to the job/phase/cost type of SL.
The Subcontract pay type
 designated for the specified pay category (in AP Pay Category). If
 you did not specify a pay category, or you are not using one, the
 default is the Subcontract pay type designated in AP Company
 Parameters.

8- SM Work Order
Defaults from SM Departments for Misc Work
 Completed lines or the override account by call type and/or cost
 type. See [SM Departments](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-departments-form) for more information.
The GL account for the line's pay
 type.

Note: The Pay Type specified for an invoice line determines the GL credit
 account. GL accounts for Pay Types are assigned in AP Payable Types.The GL debit
 account is specified on the invoice line and defaults based on the line type. If you
 selected the Allow GL Account
 Override checkbox in the Company Parameters form of the related
 module (JC, EM, or IN), you may override the defaulted account. For SM Work Order
 lines, no override is allowed.

The following table displays information on how the system
 posts to accounts on transactions with retainage, use tax, and/or discounts.
Table 2. GL Account Defaults for Transactions with Retainage,
 Tax, and DiscountsTransaction
GL Account (Debit)
GL Account (Credit)

Transaction with Retainage
Gross + retainage amount follows the Trans
 Type (i.e. Job, Inventory, Expense, Equipment, Work Order, Purchase
 Order, Subcontract).
Retainage amount posted to Pay Type for
 ‘Retainage’ for the specified pay category (in AP Category). If no
 pay category is specified or pay categories are not used, uses pay
 type for 'Retainage' specified in AP Company Parameters. Gross less
 retainage follows Pay Type for specified Trans Type (see Table 1
 above).

Transaction with Discount
If Post Discounts Offered to GL and Net
 Amounts to Subledgers option in AP Company Parameters is not
 checked, gross amount follows Trans Type (discount posted later at
 payment time).
If Post Discounts Offered to GL and Net
 Amounts to Subledgers option in AP Company Parameters is checked,
 gross less discount amount follows Trans Type. Discount amount is
 posted to the Discount Offered GL Account (from AP Company
 Parameters).
Gross amount follows Pay Type for specified
 Trans Type (see Table 1 above).

Transaction with Use Tax
Gross + tax follows the Trans Type.
 However, if the transaction is posted to a job, and the tax code has
 a phase and cost type assigned to it in HQ Tax Codes, the tax amount
 is posted to the GL account for that cost type.
Tax amount to HQ Tax Codes Sales Tax
 Payable account, gross amount follows Pay Type for specified Trans
 Type (see Table 1 above).

Related information

- [AP Pay Category Form](/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/ap-pay-typescategories-forms/ap-pay-category-form)

- [AP Company Parameters Form](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form)

- [AP Payable Types Form](/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/ap-pay-typescategories-forms/ap-payable-types-form)
