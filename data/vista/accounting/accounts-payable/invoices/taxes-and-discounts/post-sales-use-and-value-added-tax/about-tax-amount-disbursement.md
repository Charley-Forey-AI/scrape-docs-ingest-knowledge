---
title: "About Tax Amount Disbursement | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/post-sales-use-and-value-added-tax/about-tax-amount-disbursement"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/post-sales-use-and-value-added-tax/about-tax-amount-disbursement"
---

# About Tax Amount Disbursement

Vista disburses tax amounts differently based on tax type and upon any overrides you may have set up.

- Sales tax amounts disburse to the GL debit account specified for the transaction, and are credited to the GL payable account for the transaction's pay type (GL Account field, AP Payable Types form).

- Use tax amounts disburse to the GL debit account specified for the transaction, and are credited to the tax payables account specified for the tax code (Credit GL Account field, HQ Tax Codes form).

- Value Added Tax amounts disburse to the GL expense account associated with the tax code specified for the transaction (Debit GL Account field, HQ Tax Codes form), and are credited to the GL payable account associated with the transaction's pay type.

Note: In the AP Transaction Entry form, if you leave the tax code blank for a job cost line (JC, PO, or SL type), and you post the line with tax, the system relieves committed costs from the phase/cost type in the JC Cost Detail database table for the tax amount as follows:

- If phase and cost type overrides exist for the tax code, the system uses the
 tax code phase and cost type.

- If phase or cost type overrides do not exist for the tax code, the system
 uses the phase and cost type specified for the PO item.

- If a phase override exists for the tax code, but a cost type override does
 not exist, the system uses the tax code phase and the cost type from the PO
 line.

- If a cost type override exists for the tax code, but a phase override does
 not exist, the system uses the phase from the PO line and the tax code cost
 type.

Related concepts

- [About the HQ Tax Codes Form](/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form)

- [AP Vendors Form](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form)

- [JC Jobs Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)

- [AP Transaction Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form)

- [AP Unapproved Invoice Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)

- [AP Recurring Invoices Form](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form)
