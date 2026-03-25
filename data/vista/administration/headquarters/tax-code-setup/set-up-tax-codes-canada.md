---
title: "Set Up Tax Codes: Canada | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/tax-code-setup/set-up-tax-codes-canada"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/tax-code-setup/set-up-tax-codes-canada"
---

# Set Up Tax Codes: Canada

You can set up Canadian tax codes using the HQ Tax Codes form.
Create a single-level code if only one tax rate is
 applicable. For instance, if you are paying a Harmonized Sales Tax (HST), you can create
 a single-level tax code with the combined rate of GST and PST percentages. You can then
 pay the Canada Revenue Agency the entire amount, who will in turn distribute the correct
 amount to the participating province.

1. In HQ Tax Codes, define the rate at which the system calculates the tax using the New field in the Single Level Rates section of the form. If you specify both an old and new rate, the Effective Date field determines when the old rate expires and the new rate goes into effect.

1. Specify a tax liability account in the Credit GL Account field.

1. Enter the JC tax phase and cost type in the JC Tax Phase and JC Cost Type fields if you need to post taxes to a specific phase code and/or cost type.

1. Select the Add'l Options tab and check the Value Added Tax (VAT) box.

1. Check the Federal Goods and Services Tax (GST) box for codes tracking GST. Do not select this checkbox for a code tracking Provincial Sales Tax (PST).

1.  For PST codes, if you are including the GST in
 the PST basis, check the Include GST in PST Basis
 box.Note: When you check this box, the system calculates the
 GST portion first, adds it to the tax basis, and then calculates the PST
 portion. Example 1 displays how this works when creating AP, AR, and JB
 invoices. For AR and JB invoices, if you include holdback in tax
 calculations and have specified to track holdback separately (that is, you
 selected the Distribute Tax on
 Holdback checkbox in AR Company Parameters), the system
 calculates holdback tax using the same method; the only difference is that
 the tax basis is the holdback amount (see Example 2).Example 1Example 2
Tax Basis: 1000.00GST Tax Rate: 5%
PST Tax Rate: 10%
1,000.00 x 5%= 50.00 (GST)
1,000.00 + 50.00 = 1,050.00 (new
 tax basis)
1,050 x 10% =
 105.00 (PST)
50.00 (GST) +
 105.00 (PST) = 155.00 (total tax)
1,000.00 = 155.00 = 1,155.00
 (total invoice amount)
Amount: 1,000.00Holdback: 100.00
Tax Basis: 900.00
GST Tax Rate: 5%
PST Tax Rate: 10%
TAX:
900.00 x 5% = 45.00 (GST)
900.00 + 45.00 = 945.00 (new tax basis)
945.00 x 10% = 94.50 (PST)
94.50 (PST) + 45.00 (GST) =
 139.50 (total tax)
HOLDBACK
 TAX:
100.00 x 5% = 5.00
 (GST)
5.00 + 100.00 =
 105.00
105.00 x 10% = 10.50
 (PST)
5.00 (GST) + 10.50
 (PST) = 15.50 (total holdback tax)
139.50 + 15.50 = 155.00 (total of
 tax and holdback tax)
1,000
 + 155.00 = 1155.00 (total invoice
 amount)

1. If you want to track holdback tax liabilities
 separate from standard tax liabilities, enter a GL account in the Credit GL Hdbk
 Account field.

1. Enter a GL account to track holdback ITC payables
 in the Credit GL Holdback Tax Acct field.

1. For GST codes, check the Expense Tax
 Paid box. The system enables the Debit GL
 Account and Debit GL Hdbk Account
 fields.

1. Enter a GL account to track standard ITC amounts
 in the Debit GL Account field.

1. Enter a GL account in the Debit GL Hdbk
 Account field. This account is the holdback ITC contra
 account.

1. If you need to create a multi-level code, do not enter a tax liability account in the Credit GL Account field. The system automatically uses the GL accounts from the single level codes.

1. Save the record as normal.

For more information on how the system tracks standard
 and holdback ITCs, see [Tracking Holdback Input Tax Credits: Canada](/en/vista/vista/accounting/accounts-payable/payments/retainage/holdback-input-tax-credits-canada).

Related information

- [Tax Code](/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form/field-definitions-hq-tax-codes-form#ID-0000fb9f--en)
