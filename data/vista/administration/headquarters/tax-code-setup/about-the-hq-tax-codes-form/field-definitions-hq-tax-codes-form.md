---
title: "Field Definitions: HQ Tax Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form/field-definitions-hq-tax-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form/field-definitions-hq-tax-codes-form"
---

# Field Definitions: HQ Tax Codes Form

The following is a list of field descriptions for the HQ Tax
 Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Tax Code

The Tax Code field on the HQ Tax Codes form, Info tab.
Enter a tax code, up to 10 characters.

Related information

- [Set Up Tax Codes: Australia](/en/vista/vista/administration/headquarters/tax-code-setup/set-up-tax-codes-australia)

- [Set Up Tax Codes: Canada](/en/vista/vista/administration/headquarters/tax-code-setup/set-up-tax-codes-canada)

- [Tax Code Setup: United States](/en/vista/vista/administration/headquarters/tax-code-setup/tax-code-setup-united-states)

## Description

The Description field on the HQ Tax Codes form, Info tab.
Enter a description of the tax code, up to 30 characters.

## Multi-Level Tax Code

The Multi-Level Tax Code checkbox on the HQ Tax Codes form, Info tab.
Select this checkbox if you will be using this code to combine and post multiple taxes (for example, state, city, and county tax). You will not specify a rate for this tax code. Instead, the system calculates the tax rate based on the combined total of this code's assigned single level tax codes.
Leave this box unselected if this is a single level tax code. You will need to specify old and new rates for this tax code for calculating taxes.
Note: Use the Single Level Members tab to link single level tax codes to multi-level tax codes.

## Single Level Rates: Old

The Single Level Rates: Old field on the HQ Tax Codes form, Info tab.
Enabled for Single Level tax codes only.
Indicate the rate to use for calculating taxes if the posting date is earlier than the Effective date specified below. For example, enter 5% as .050000, 10% as .100000, and so on.

## Single Level Rates: New

The Single Level Rates: New field on the HQ Tax Codes form, Info tab.
Enabled for Single Level tax codes only.
Enter the new tax rate to use whenever posting date is equal to or later than the Effective date specified below. For example, enter 5% as .050000, 10% as .100000, and so on.

## Effective Date

The Description field on the HQ Tax Codes form, Info tab.
Enabled for Single Level tax codes only.
Specify the date on which the new rate specified above becomes effective.

## Credit GL Account

The Credit GL Account field on the HQ Tax Codes form, Info tab.
Enter the GL liability account for the following:

- Posting use tax in AP, JC, EM, and IN.

- Posting sales tax in JB and AR.

- Tracking tax on sales amounts for VAT codes.

Press F4 for a list of valid accounts.
Note: Check online help for each of the modules listed above for additional information on tax calculations.

## JC Tax Phase

The JC Tax Phase field on the HQ Tax Codes form, Info tab.

Specify the phase (from JC Phases) for this tax code. If you specify a phase here, tax expensed to a job will be posted to this phase. If left blank, tax will be posted to the phase designated in the transaction.
Note: For locked jobs (those with the Phases on this job are locked selected in JC Jobs), if you enter this tax code for a job-related transaction and the phase specified here does not exist for the job (in JC Job Phases), the system throws an error and will not allow you to save the transaction record. You must either enter a different tax code for the transaction or add this phase to the job in JC Job Phases.

## JC Cost Type

The JC Cost Type field on the HQ Tax Codes form, Info tab.

Enter the cost type (from JC Cost Types) for this tax code. If you specify a cost type here, tax expensed to a job will be posted to this cost type. If left blank, tax will be posted to the cost type designated in the transaction.
Note: For locked jobs (those with the Phases on this job are locked selected in JC Jobs), if you enter this tax code for a job-related transaction and the cost type specified here does not exist for the job phase (in JC Job Phases), the system throws an error and will not allow you to save the transaction record. You must either enter a different tax code or add this cost type to the job phase in JC Job Phases.

## Linked Tax Code

The Linked Tax Code field on the HQ Tax Codes form, Single Level Members tab.
For use with multi-level tax codes only.
Specify the single level tax code to link to this multi-level tax code. The old and new rates for the tax code are displayed to the right. The use of these rates for calculating taxes is determined by the Effective date specified for the tax code.
Note: Once you assign a single level tax code here, the multi-level tax code to which it is assigned will be updated to the Assigned to these Multi-Level Tax Codes grid (Info tab).

## Value Added Tax (VAT)

The Value Added Tax (VAT) checkbox on the HQ Tax Codes form, Add'l Options tab.
Select this checkbox to use this code for handling VAT requirements. If this is a multi-level tax code, you must select this checkbox for all associated single-level codes.
Leave this box unselected if not using this tax code to handle VAT requirements.
Select the links below for additional information.

## Federal Goods & Services Tax (GST)

The Federal Goods & Services Tax (GST) checkbox on the HQ Tax Codes form, Add'l Options tab.
This option is only enabled for single-level VAT codes.
Select this checkbox to have the system use this code for GST requirements.
Leave this box unselected if not using this tax code for GST requirements.

## Include GST in PST

The Include GST in PST checkbox on the HQ Tax Codes form, Add'l Options tab.
This field applies to certain provinces in Canada only; it is enabled only for single-level VAT codes.
Select this checkbox to have the system include Goods and Services Tax (GST) in the tax basis when calculating Provincial Sales Tax (PST).
Note: You cannot select this checkbox for GST codes.

Leave this checkbox unselected to exclude Goods and Services Tax (GST) from the tax basis when calculating Provincial Sales Tax (PST).

## Credit GL Ret/Hdbk Account

The Description field on the HQ Tax Codes form, Info tab.
For Australia, the title of this field is Credit GL Ret Account.
For Canada, the title of this field is Credit GL Hdbk Account.
Enter the GL liability account for tracking retainage tax on sales amounts for VAT codes. Press F4 for a list of valid accounts.

## Credit GL Hdbk/Ret Tax Acct

(AU/CA only)The Credit GL Hdbk/Ret Tax Acct field on the HQ Tax Codes form, Info tab.
For Australia, the title of this field is Credit GL Ret Tax Acct.
For Canada, the title of this field is Credit GL Hdbk Tax Acct.
Enter the GL account to track retainage ITC payables. Press F4 for a list of GL accounts.

## Expense Tax Paid (Used to Track Tax Credit)

The Expense Tax Paid (Used to Track Tax Credit) field on the HQ Tax Codes form, Add'l Options tab.
Applies to Australian and Canadian users only.
The system enables this checkbox for single-level VAT codes used for GST requirements.
Select this checkbox to track Input Tax Credits (ITCs) separately from tax on sales. Once you select this checkbox, the system enables the Debit GL Account field and,

- for Australia, the Debit GL Ret Account field.

- for Canada, the Debit GL Hdbk Account (CA) field.

## Debit GL Account

The Debit GL Account field on the HQ Tax Codes form, Add'l Options tab.
The system enables this field when you select the Expense Tax Paid checkbox.
Enter a GL account for tracking the Input Tax Credit (ITC) amount paid to vendors.

## Debit GL Hdbk/Retg Account

The Debit GL Hdbk/Retg Account field on the HQ Tax Codes form, Add'l Options tab.
For Australia, the title of this field is Debit GL Ret Account
For Canada, the title of this field is Debit GL Hdbk Account.
The system enables this field when you select the Expense Tax Paid checkbox.
Enter a GL account for tracking retainage Input Tax Credits (ITCs) separately from standard ITCs.
