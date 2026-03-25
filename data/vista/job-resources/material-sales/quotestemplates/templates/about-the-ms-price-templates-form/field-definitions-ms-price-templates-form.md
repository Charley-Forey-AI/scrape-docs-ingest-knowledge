---
title: "Field Definitions: MS Price Templates Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/quotestemplates/templates/about-the-ms-price-templates-form/field-definitions-ms-price-templates-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/quotestemplates/templates/about-the-ms-price-templates-form/field-definitions-ms-price-templates-form"
---

# Field Definitions: MS Price Templates Form

The following is a list of field descriptions for the MS
 Price Templates form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Sequence

Use this field to identify each unique record on this tab.
Enter a '+' and the system will create a new record and automatically assign it the next available sequence number.

##  Price Template

 Enter a number for this pricing template, up to four digits.

##  Description

 Enter a description of this pricing template, up to 30 characters.

## Effective Date

 You can use this field to set up material pricing for future use, without affecting current pricing.
Enter the date that the new rates, prices, and/or minimum amounts should take effect.
 Tickets with a sale date posted on or after this date will use the 'new' rates, prices, and minimum amounts. Tickets posted before this date use the 'old' rates, prices, and minimum amounts.

## Location Group

Enter a location group or press F4 to select one from a list. Location groups are created and maintained using the [ IN Location Groups ](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-location-groups-form) form.
 Required field.

## Location

Use this field to set up a rate for a specific location that is associated
 with the location group. If you leave this field blank, the rate will apply to all
 locations associated with the group.
Enter a location or press F4 to select a
 location from a list. Only locations associated with the group selected in the Location Group
 field will display in the list.
Locations are associated with location groups
 using the Location
 Group field on the Info tab of the [IN Locations ](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form) form.

## Category

Enter a category or press F4 to select
 one from a list.
Categories are created and maintained using the [HQ Material Categories](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-material-categories-form) form.

## Material

Use this field if the rate should only apply
 to a specific material. If you leave this field blank, the rate will apply to all materials
 that are associated with the category selected in the Category field.
Note: Entry here overrides pricing entered at the category level.
 Enter the material for this pricing or press
 F4
 to select one from a list. Only materials associated with the category selected in the
 Category field will display in the list.
Materials are created and maintained using the [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form) form. Materials are associated with a category using the

##  UM

 Required field.
 Specify the sales unit of measure for this material or category of materials. This must be a valid unit of measure set up in HQ Units of Measure.
 If you enter a material for this line, this field defaults the sales unit of measure for the material (from HQ Materials). You can override this value, but it must be either the standard unit of measure for the material or a unit of measure specified for the material in HQ Materials (Additional Units of Measure tab).

##  Old Rate

 The system only uses this field if the Old Unit Price field is 0.00.
 Enter the rate used to calculate a default unit price. The system applies this rate to the standard cost or price found in IN Location Materials (stocked materials) or HQ Materials (non-stocked materials) based on the pricing option selected in IN Company Parameters.
Note: The system only uses this rate for tickets posted prior to the Effective Date specified above.

##  Old Unit Price

 The system only uses this field for tickets posted prior to the Effective Date.
 Enter the unit price to use as a default for this material or category of materials when entering tickets. This may be a positive or negative value.
 If you enter a material for this line, this field defaults the unit price based on the unit of measure specified.
 If this field is set to 0.00, the system uses the markup/discount rate entered in the Old Rate field.

##  Old ECM

 The system only uses this field for tickets posted prior to the Effective Date.
 Specify what quantity the unit price (previous field) represents.

- E-Each

- C-Per Hundred

- M-Per Thousand

##  Old Min Amt

 The system only uses this field for tickets posted prior to the Effective Date.
 Specify the minimum amount that the system can charge per ticket for this material or category of materials. The system uses this amount if the calculated total for the material is less than this amount and the material units are greater than 0.00.

##  New Rate

 The system only uses this field if the New Unit Price field is 0.00.
 Enter the rate used to calculate a default unit price. The system applies this rate to the standard cost or price found in IN Location Materials (stocked materials) or HQ Materials (non-stocked materials) based on the pricing option selected in IN Company Parameters.
Note: The system uses this rate only for tickets posted on or after the Effective Date.

##  New Unit Price

 The system only uses this field for tickets posted prior to the Effective Date.
 Enter the unit price to use as a default for this material or category of materials when entering tickets. This may be a positive or negative value.
 If you enter a material for this line, this field defaults the unit price based on the unit of measure specified.
 If this field is set to 0.00, the system uses the markup/discount rate entered in the New Rate field.

##  New ECM

 The system only uses this field for tickets posted prior to the Effective Date.
 Specify what quantity the unit price (previous field) represents.

- E-Each

- C-Per Hundred

- M-Per Thousand

##  New Minimum Amt

 The system only uses this field for tickets posted prior to the Effective Date.
 Specify the minimum amount that the system can charge per ticket for this material or category of materials. The system uses this amount if the calculated total for the material is less than this amount and the material units are greater than 0.00.
