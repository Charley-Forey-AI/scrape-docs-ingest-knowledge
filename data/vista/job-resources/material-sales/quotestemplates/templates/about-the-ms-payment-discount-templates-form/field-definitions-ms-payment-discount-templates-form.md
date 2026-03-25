---
title: "Field Definitions: MS Payment Discount Templates Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/quotestemplates/templates/about-the-ms-payment-discount-templates-form/field-definitions-ms-payment-discount-templates-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/quotestemplates/templates/about-the-ms-payment-discount-templates-form/field-definitions-ms-payment-discount-templates-form"
---

# Field Definitions: MS Payment Discount Templates Form

The following is a list of field descriptions for the MS
 Payment Discount Templates form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Discount Template

 Enter a number for this discount template, up to four digits.

##  Description

 Enter a description of this discount template, up to 30 characters.

##  Location Group

 Required field.
 Specify the location group (from IN Location Groups) for this discount.

##  Location

 Optional field.
 Specify the location for this discount. This
 must be a valid location (from IN Locations) for the specified location group. If this
 field is blank, the discount applies to all locations within the specified location group.

##  Category

 Required field.
 Specify the category (from HQ Material Categories) for this discount.

##  Material

 Optional field.
 Enter the material for this discount. This must be a valid material (from HQ Materials) assigned to the specified category. If this field is blank, the discount applies to all materials in the specified category.
Note: Entry here overrides discounts entered at the category level.

##  UM

 Required field.
 Specify the sales unit of measure for this material or category of materials. This must be a valid unit of measure set up in HQ Units of Measure.
 If you enter a material for this line, this field defaults the sales unit of measure for the material (from HQ Materials). You can override this value, but it must be either the standard unit of measure for the material or a unit of measure specified for the material in HQ Materials (Additional Units of Measure tab).

##  Pay Disc Rate

 Enter the rate or amount that the system uses to calculate the discount for this material or material category. If the posted material’s Payment Discount field (in HQ Materials) is set to Rate, this amount will be the rate at which the discount is calculated. If the material’s Payment Discount option is set to Per Unit, this will be the amount per unit used in calculation of the discount amount.
 Enter all amounts as decimals (e.g. .10). If a Rate, the system interprets this value as 10%. If Per Unit, the system interprets this value as $.10 per unit.
