---
title: "Tax Code Setup: United States | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/tax-code-setup/tax-code-setup-united-states"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/tax-code-setup/tax-code-setup-united-states"
---

# Tax Code Setup: United States

You can setup tax codes using the HQ Tax Codes form.

## Single-Level Codes

Apply single level tax codes only if one tax rate is applicable. For instance, if you only pay a state sales tax, you only need to set up single level tax codes.
When setting up a single-level tax code, define the rate at which the system should calculate the tax using the New field in the Single Level Rates section of the form. If you specify both an old and new rate, the Effective Date field determines when the old rate expires and the new rate goes into effect. You must also specify a tax liability account in the Credit GL Account field. Additionally, enter the JC tax phase and cost type in the JC Tax Phase and JC Cost Type fields, if you need to post taxes to a specific phase code and/or cost type.

## Multi-Level Codes

Apply multi-level tax codes when there are multiple levels of taxes required (e.g., a code that includes city and county taxes). In order to apply multi-level codes, you must link them with single level tax codes since the only rates associated with a multi-level code are the cumulative rate of all specified single level codes.
When creating a multi-level code, you must first create the associated single-level codes. When creating the multi-level code, specify the GL account in the Credit GL Account field. If you need to post taxes to a specific phase and/or cost type, enter the tax phase and cost type in the JC Tax Phase and JC Cost Type fields. Use the Single Level Members tab to assign the single-level codes.
For example, if you owe taxes that are payable to a city, county, and state, you must first set up each entity as a single level code. Each single level code is then associated with the same multi-level code, as seen below:Multi-Level Code
Single-Level CodesRate
State5%
City1%
County2%

The system adds the rate of all single level codes together when performing a tax calculation. Using the example from Table 1 above, the system calculates an 8% tax. The old and new rate totals for all single-level codes display in the Multi-Level Rates section of the Info tab for the associated multi-level code.

Related information

- [Tax Code](/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form/field-definitions-hq-tax-codes-form#ID-0000fb9f--en)
