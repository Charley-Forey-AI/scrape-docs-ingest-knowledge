---
title: "Field Definitions: JB T M Template Material Rates Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-material-rates-form/field-definitions-jb-t-m-template-material-rates-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-material-rates-form/field-definitions-jb-t-m-template-material-rates-form"
---

# Field Definitions: JB T M Template Material Rates Form

The following is a list of field descriptions for the JB T M
 Template Material Rates form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Template

 Specify the T&M template that the material rate overrides apply to. If you accessed this form from JB T&M Template Setup, this field defaults the currently active template and is disabled.

##  Material Group

 Specify the material group.

##  Material

 Specify the material the override rate applies to.

##  Override Option

 Specify the type of rate override to use for this material.

- C-Cost Plus Markup - Select this option if the rate override is based on cost plus markup. The system uses the average, last, or standard unit cost, depending on the selected Cost Option (last column in grid), plus the markup rate specified in the Markup/Discount Rate field. If the material is a non-stocked material, the standard unit cost from HQ Materials will always be used, regardless of how this option is set. If the material is stocked, the average, last, or standard unit cost will be pulled from IN Location Materials.

- P-Price Less Discount - Select this option if the rate override is based on the unit price less a discount. If the material is non-stocked, the standard unit price from HQ Materials is used. If the material is stocked, the standard unit price from IN Location Materials is used. The discount rate used is either the Markup/Discount Rate specified, or as specified for the location (IN Location Materials) or the customer in AR Customers.

##  Markup/Discount Rate

 Enter the markup or discount rate to use when billing this material.
 If the Override Option is “C-Cost Plus
 Markup,” the material is billed as Units x Unit Cost x Rate. Units are the number of units
 posted to JC. Unit Cost is the average, last, or standard unit cost defined for the
 material in IN Locations. However, if the material is non-stocked, the standard unit cost
 in HQ Materials is always used. The Rate is the Markup Rate specified here.
 If the Override Option is “P-Price Less Discount,” the material is billed as Units x Unit Price x Rate. Units are the number of units posted to JC. Unit Price is the specific price entered in one of the Specific Price fields (depending on the effective date). If a Specific Price is not entered, the unit price is the standard unit price from HQ Materials or IN Location Materials, depending on whether the material is non-stocked or stocked (respectively). The Rate is the Discount Rate specified here.

##  Old Specific Price

 Enter the unit price to use when billing this material. This price is used for transactions posted prior to the effective date specified above.

- If the Override Option drop-down is set to “P-Price Less Discount”,” material is billed using this price, less the discount specified in the "Markup/Discount Rate" field.

- If the Override Option drop-down is set to “C-Cost Plus Markup,” material is billed using this price, plus the markup specified in the "Markup/Discount Rate" field.

 The value entered here (along with the specified markup/discount rate), overrides any other unit price or unit cost specified for the material in HQ or IN. If left blank, the unit price comes from HQ Materials or IN Location Materials, depending on whether the material is non-stocked or stocked (respectively).

##  New Specific Price

 Enter the unit price to use when billing this material. This price will only be used for transactions posted on or after the effective date specified above.

- If the Override Option drop-down is set to “P-Price Less Discount”,” material is billed using this price, less the discount specified in the "Markup/Discount Rate" field.

- If the Override Option drop-down is set to “C-Cost Plus Markup,” material is billed using this price, plus the markup specified in the "Markup/Discount Rate" field.

 The value entered here (along with the specified markup/discount rate), overrides any other unit price or unit cost specified for the material in HQ or IN. If left blank, the unit price comes from HQ Materials or IN Location Materials, depending on whether the material is non-stocked or stocked (respectively).

##  Cost options

 For Override Option C (Cost plus Markup) only, indicate which cost method to use when billing this material.
Note: If the material is non-stocked, the standard unit price (from HQ Materials) is used.
