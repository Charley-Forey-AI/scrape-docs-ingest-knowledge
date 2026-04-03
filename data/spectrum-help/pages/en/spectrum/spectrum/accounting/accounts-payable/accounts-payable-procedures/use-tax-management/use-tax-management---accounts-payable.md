---
title: "Use Tax Management - Accounts Payable | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/use-tax-management/use-tax-management---accounts-payable"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/use-tax-management/use-tax-management---accounts-payable"
---

# Use Tax Management - Accounts Payable

Use Tax Code Maintenance – set rates, type of tax (sales or use). If the type is left blank, the software will assume Use Tax. G/L accrual account is defined here as well.
Vendors – can
 set a default tax code here. It will accrue this tax on each invoice entered in
 A/P Vendor Invoice Entry, unless the invoice is distributed to a
 job and the tax classification file specifies tax code override.
A/P Vendor Invoice Entry – In invoice entry, you can search on the amount field to see/modify use tax rates, codes, amount, and more. If the type is "Use", only an accrual will be made. The expense side of the entry will combine both the invoice amount and the use tax amount into one amount. If the tax type is "Sales", it will increase the amount owing to the vendor. You can set Use/Sales/Taxable status by line item in A/P Vendor Invoice Entry. When you exit from the invoice entry detail, you will see only the amount to be paid to the vendor in the pop-up window (for example, invoice + sales tax amounts, no use tax will display). Taxable amounts are only amounts subject to sales tax, not to use tax.
If the vendor and job do not have any tax class codes assigned, once you enter a Sales or Use tax code on an invoice line item in A/P Vendor Invoice Entry, the tax rate will default to additional lines in A/P Vendor Invoice Entry from the previous line.
Sales and Use tax codes and amounts show on the A/P Transaction Register.
