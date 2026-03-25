---
title: "About the JB Progress Item SM and Tax Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-progress-item-sm-and-tax-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-progress-item-sm-and-tax-form"
---

# About the JB Progress Item SM and Tax Form

Use this form to enter stored materials information or
 override retainage and tax information.
Access this form by double-clicking on any record on the Item SM/Tax tab in JB Progress
 Billing.

## Stored Materials

Use this section to enter materials that have purchased and stored, as well as
 materials (stored and/or new) that been installed since the last billing.
All materials that were stored after the
 last billing display in the Previous SM field.
The difference between the purchased
 amount and the installed amount displays in the Net Invoice SM field. If an amount
 exists in the Previous SM field, that value is added to the amount in the Net
 Invoice SM field and displays in the To Date SM field.

## Overriding Retainage Information

Retainage amounts automatically calculate based on the rates set
 up for the contract or items in JC Contracts and JC Contract Items,
 respectively.
 Normally, retainage amounts do not need
 to be changed. If the retainage needs to be overridden, you can enter retainage
 information for each item using the SM Retainage % and SM Retg This Invoice fields
 on this form.
Alternately, enter retainage information
 by selecting File > Retainage Totals from the JB Progress Billing form to enter
 retainage at the contract level using the JB Progress Bill Retg Totals form.
 Entering retainage at the contract level overrides the rate/amount specified for
 each item, even when an item’s standard retainage was originally overridden at the
 item level. For more information, refer to JB Progress Bill Retg Totals in Related
 Topics below.

## Overriding Sales Tax

The system calculates sales tax automatically based on standard rates. You will
 typically not need to alter this information; however, you can use this form to
 override tax information, if necessary.
If tax is overridden and items are
 subsequently changed in JB Progress Billing, the system recalculates the tax using
 the standard rate. In this case, you will need to reenter the override.
Note: If you post intercompany invoices (i.e. the
 JC/AR company differs from the JC/JB company) and tax is applied to a billing, the
 tax liability remains with the AR company. For example, let’s assume a JB company of
 #1 and an AR company of #2. If you post a billing in JB Co #1 for $1050 (includes
 $50 tax), the following updates occur:
AR Co #2

- Receivables account is debited
 $1050

- Sales Tax Payable account is
 credited $50

- Intercompany Payables account is
 credited $1000

JB Co #1

- Intercompany Receivables account
 is debited $1000

- Contract Revenue account is
 credited $1000

## Retainage Tax

If you specified to include retainage in tax calculations (i.e. you have checked the
 Calculate Tax on Retainage box in AR Company Parameters), both work complete and
 stored materials retainage amounts will be included in the tax basis for the invoice
 item.
However, if you also specified to
 ‘Distribute Tax to Retainage’ (option in AR Company Parameters), retainage tax will
 be excluded from the tax basis and calculated separately. In this case, two
 additional fields are displayed in the Tax section:

- Total
 Retainage – This display-only field shows the total
 retainage (work complete and stored materials) for the billing item. Since
 you are calculating/tracking retainage tax separately, this amount is
 excluded from the item’s tax basis.

- Retainage
 Tax – This field defaults the calculated retainage tax for
 the billing item ([work complete retainage + stored materials retainage] x
 tax rate).

Note: For countries tracking Provincial Sales Tax
 (PST) and/or Goods & Services Tax (GST), such as Canada and Australia, retainage
 tax amounts will be broken out and updated to the appropriate GST/PST retainage tax
 payable accounts (as defined in HQ Tax Codes). The PST and GST amounts (included in
 tax basis) will be updated to the appropriate tax payable accounts.
DebitCredit
AR Receivables 
 1039.50
Job Revenue  1000.00


Retg Receivables 
 115.50
GST Tax Payables 
 45.00

PST Tax Payables 
 94.50

GST Retg Tax
 Payables  5.00

PST Retg Tax
 Payables  10.50

The following are related topics:

- [JB Progress Billing Form](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-progress-billing-form)

- [JC Contracts Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)

- [JC Contract Items Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)

- [About the JB Progress Bill Retg Totals Form](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-progress-bill-retg-totals-form)
