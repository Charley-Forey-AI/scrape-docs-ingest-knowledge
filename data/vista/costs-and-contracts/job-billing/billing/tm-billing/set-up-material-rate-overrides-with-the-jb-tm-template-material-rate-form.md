---
title: "Set up Material Rate Overrides with the JB T&M Template Material Rate form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/set-up-material-rate-overrides-with-the-jb-tm-template-material-rate-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/set-up-material-rate-overrides-with-the-jb-tm-template-material-rate-form"
---

# Set up Material Rate Overrides with the
 JB T&M Template Material Rate form

You can set up material rate overrides from the JB T&M Template Material Rate
 form.
Access this form from either the JB Programs folder
 or by double-clicking a record on the Matl Rate Overrides tab in JB T&M Template
 Setup.
Material categories must be set up in HQ
 Materials and/or IN Location Materials before setting up material rate overrides.
To set a material rate override:

1. Select an override option from the Override Option drop-down: C-Cost Pl us Markup or P-Price Less Discount. Note: If “C-Cost Pl us Markup” is selected, specify a cost option in the Cost Options drop-down. If “P-Price Less Discount” is selected, the rate is based on the unit price (from either HQ or IN) less the discount specified in the Markup/Discount Rate field.

1. Enter the markup or discount rate in the Markup/Discount Rate field. Note: If “C-Cost Pl us Markup” was selected from the Override Option drop-down, the value entered here is the markup rate. If “P-Price Less Discount” was selected from the Override Option drop-down, the value entered here is the discount rate.

1. Enter the new rate in the New Specific Price field. Note: This value, along with the markup or discount, is used as the unit price for the material. If you do not specify a value, the standard unit price from HQ Materials is used for stocked materials. For non-stocked materials, the standard unit price from IN Location Materials is used.
Note: Update old prices for all entries in the grid by selecting File > Move Specific Price to Old. This option will automatically update the Old Specific Price fields with the values in the New Specific Price fields.

1. Select a cost option from the Cost Options drop-down: S-Std Unit Cost, A-Avg Unit Cost, or L-Last Unit Cost. Note: This drop-down is used when “C-Cost Pl us Markup” is selected in the Override Option drop-down. If a material is not stocked, the standard unit cost from HQ Materials is used. Otherwise, the stocked material’s average, last, or standard unit price from IN Location Materials is used.
Note: If you enter a specific price, it overrides any unit cost or unit price specified for the material in HQ or IN, regardless of the cost option.
Materials without override rates are billed based on the pricing option set for the template sequence in JB T&M Template Setup (Price Opt. field). For more information, see Pricing Option in Related Topics below.

[](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form)HQ Materials
[](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form)IN Location Materials
[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup
