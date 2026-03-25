---
title: "About the HQ Tax Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form"
---

# About the HQ Tax Codes Form

Use this form to set up and maintain tax codes (single and multi-level) for application throughout the system.
Set up single-level codes when only one tax rate is applicable. If multiple tax rates are required, you can create a multi-level code and associate it with all applicable single-level codes.
Note:This file is NOT a master file. Tax codes entered here are automatically set up in the Tax Codes and Rates group assigned to the currently active Company ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form), Add’l Info tab). All information set up here applies only to the currently active company and any companies that may be sharing the specified Tax Codes and Rates group.

## Setting up Multi-Level Codes

When creating a multi-level VAT code, do not specify a tax liability account in the Credit GL Account field. The system automatically uses the specified GL accounts from the single-level codes.
For example, if you are creating a multi-level code to track both Goods and Services Tax (GST) and Provincial Sales Tax (PST), you must first set up each one as a single-level code. You would then associate both single-level codes with the same multi-level code, as seen the table below.
Multi-Level Code

Single-Level CodesRate
GST5%
PST10%

The system calculates tax amounts based on how you have set up your GL accounts for the single-level codes.

The process for setting up your tax codes differs depending on your country. Select a link below to get detailed instructions for your specific location.
[Tax Code Setup: United States](/en/vista/vista/administration/headquarters/tax-code-setup/tax-code-setup-united-states)
[Set Up Tax Codes: Australia](/en/vista/vista/administration/headquarters/tax-code-setup/set-up-tax-codes-australia)
[Set Up Tax Codes: Canada](/en/vista/vista/administration/headquarters/tax-code-setup/set-up-tax-codes-canada)
