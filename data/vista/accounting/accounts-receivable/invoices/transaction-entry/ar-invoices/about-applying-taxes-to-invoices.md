---
title: "About Applying Taxes to Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-invoices/about-applying-taxes-to-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-invoices/about-applying-taxes-to-invoices"
---

# About Applying Taxes to Invoices

You can apply taxes in AR Invoice Entry if you selected the
 Post Taxes on Invoices check
 box in AR Company Parameters.
If you do not select the checkbox all tax-related fields in AR Invoice Entry are disabled and taxes cannot be posted to invoices. This holds true for contract-related invoices as well, regardless of whether a tax code has been assigned to the contract.
 If you select the Post Taxes on Invoices checkbox in AR Company Parameters, the following applies:

- If you are applying taxes to a contract invoice, the tax code defaults as assigned to the invoice line's contract item and is used calculate the tax amount. The tax amount is then applied to the line's total.
If no tax code is assigned to the contract item, you can still post taxes to the invoice line by manually entering the tax code as applicable.

- If you apply taxes to a non-contract invoice, the tax code specified for the customer (AR Customers) is used to calculate the tax amount.

## About Retainage Tax

If you have checked the Post Taxes on Invoices option, two additional options are available (in AR Company Parameters) that determine how the system handles retainage tax.

- Calculate Tax on
 Retainage - If you select this option, retainage is included
 in tax calculations. The Tax Basis used to calculate the tax amount for each
 invoice line (red arrow) includes the line's retainage amount. When the
 invoice is posted, the full amount of tax (blue arrow) is updated to the tax
 payables account (Credit GL Account in HQ Tax Codes) and is due for payment.
  If you do not select the Calculate Tax on
 Retainage option, tax calculations exclude retainage.
 However, tax is calculated for the retainage when it is released (in AR
 Release Retainage).

- Distribute Tax to
 Retainage - If you select this option (only available if
 calculating tax on retainage), the tax calculation for retainage is handled
 differently. In this case, retainage tax is tracked separately and
 therefore, not included in the tax basis (red arrow). The system calculates
 the invoice tax amount (tax basis x tax rate) and displays the amount in the
 Tax field (blue arrow). It then calculates the retainage tax (retainage x
 tax rate) and displays the amount in the Retainage Tax field (green arrow).
 When the invoice is processed, the Tax amount is updated to the tax payables
 account and the Retainage Tax is updated to the Credit GL Retg Account
 (specified in HQ Tax Codes). The retainage tax will be due for payment when
 the retainage is released. You will typically not use this feature for US companies, as retainage
 tax is not generally withheld as part of the retention amount. Its
 intended use is for those countries using Value Added Tax (VAT), where
 retainage tax is withheld for later release (e.g., Canada, Australia,
 etc.). When processing VAT-related transactions, the update will credit
 the GST/PST tax expense accounts, as well as the GST/PST retainage tax
 payable accounts.

## About Posting Taxes on Intercompany Invoices

If you post an intercompany invoice to which tax has been applied, the tax liability will remain with the Accounts Receivable company.
For example, if Co #1 posts an invoice of $1050 (includes $50 tax) to a contract in JC Co #2, Co #1 will receive a debit of $1050 to their Receivables account, a credit of $50 to their Sales Tax Payable account, and a credit of $1000 to their Intercompany Payables account. Co #2 will receive a debit of $1000 to their Intercompany Receivables account and a credit of $1000 to their Contract Revenue account.

## Taxes on Adjustments, Credit Memos, and Write-Offs

When entering adjustments for a transaction line, the tax code field is disabled. If the adjustment is being entered to correct the tax code, follow these steps:

1. Apply equal negative values to the existing line. This will, in effect, zero out the line to cancel it.

1. Add a new line with the appropriate amounts. You can now enter the correct tax code in the Tax Code field. The system will now distribute tax amounts to the correct tax code.

If you are entering a credit memo or write-off, the tax code field will always be disabled, as credits or write-offs must always 'credit' the same tax code as specified on the original invoice. You will however, be able to enter a credit amount and credit tax basis, which will then calculate the correct amount of tax to credit or write off.
Additionally, for contract-related invoices, if the Interface
 Taxes option in JC Contracts is checked, taxes calculated for each invoice line will
 update the JCCM (Contracts form) and the JCCI (Contract Items) files. In both cases,
 taxes will be added to the revenue or billing-to-date on the contract.
