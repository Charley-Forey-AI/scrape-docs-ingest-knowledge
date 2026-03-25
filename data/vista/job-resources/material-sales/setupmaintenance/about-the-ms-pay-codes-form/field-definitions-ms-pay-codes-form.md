---
title: "Field Definitions: MS Pay Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-pay-codes-form/field-definitions-ms-pay-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-pay-codes-form/field-definitions-ms-pay-codes-form"
---

# Field Definitions: MS Pay Codes Form

The following is a list of field descriptions for the MS Pay
 Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Pay Code

Enter a pay code, up to 10 characters.
Note: If you are using the surcharges functionality in Material Sales, pay codes that will be assigned to surcharge codes (in MS Surcharge Codes) must have a basis of 7-Percent of Surcharge Total. Therefore, you will need to set up one or more pay codes that will be used for surcharges only.

##  Description

 Enter a description of this pay code, up to 30 characters.

## Pay Rate is Based On

Indicate how the system calculates pay charges for this pay code.

- 1-Per Unit

- 2-Per Hour

- 3-Per Load

- 4-Units Per Mile

- 5-Units Per Hour

- 6-Percent of Haul

- 7-Percent of Surcharge Total

Note: Option 7-Percent of Surcharge Total is only for use with the surcharges functionality. If you will be assigning this pay code to any surcharge codes (in MS Surcharge Codes), you must select this option.

##  Location Group

 Required field.
 Specify the location group (from IN Location Groups) for this pay rate.

##  Location

 Optional field.
 Specify the location for this pay rate. This
 must be a valid location (from IN Locations) for the specified location group. If this
 field is blank, the pay rate applies to all locations within the specified location group.

##  Category

 Optional field.
 Specify the category (from HQ Material Categories) for this pay rate. If this field is blank, the pay rate applies to all categories and materials, and you cannot enter a value in the Material field.

## Material

This field is optional and is accessible only when you enter a value in the Category field.
Enter the material for this pay rate. This must be a valid material (from HQ Materials) assigned to the specified category. If the field is blank, the pay rate applies to all materials in the specified category.
Note: Entry here overrides pay rates entered at the category level.

##  Truck Type

 Optional field.
 Specify the truck type (from MS Truck Types) for this pay rate. If this field is blank, the pay rate applies to all truck types.

##  Vendor

 Optional field.
 Specify the vendor (from AP Vendors) for this
 pay rate. If this field is blank, the pay rate applies to all vendors.

##  Truck

 This field is optional and is accessible only when you enter a value in the Vendor field.
 Enter the truck (MS Vendor Trucks) to which this pay rate applies. If left blank, and no vendor is specified, pay rate applies to all trucks. If left blank and a vendor and truck type are entered, this rate will apply to all trucks that match the vendor/truck type.

## UM

This field is required for pay codes with a pay rate basis of 1-Per Unit, 4-Units Per Mile, 5-Units Per Hour, and 7-Percent of Surcharge Total.
Specify the sales unit of measure for this pay rate. This must be a valid unit of measure set up in HQ Units of Measure.
If you enter a material for this line, this field defaults the sales unit of measure for the material (from HQ Materials). You can override this value, but it must be either the standard unit of measure for the material or a unit of measure specified for the material HQ Materials (Additional Units of Measure tab).

##  Zone

 Optional field.
 Specify the delivery zone for this pay rate, up to 10 characters. If this field is blank, the pay rate applies to all haul zones. The system does not validate this field.

## Pay Rate

Enter the default rate the system uses when calculating pay charges posted to this pay code.
For pay rates based on percent of haul or percent of surcharge total, a rate of 1.00 represents 100%.
Note: If this pay code is associated with surcharges (has a basis of 7-Percent of Surcharge Totaland is assigned to one or more surcharge codes in MS Surcharge Codes), the rate specified here will be used to determine the amount of the assessed surcharge that will be passed to the haul vendor.

## Min Amt

Specify the minimum payment amount for this pay code. You will generally only enter an amount here if hired haulers are guaranteed a minimum payment, regardless of quantity delivered.
Note: If this pay code is associated with surcharges (i.e.,
 has a basis of 7-Percent of Surcharge Totaland is assigned to one or more surcharge codes
 in MS Surcharge Codes), the minimum amount specified here will apply to the amount of the
 assessed surcharge that will be passed to the haul vendor.
Important: If you will be assigning this pay code to a
 surcharge code with negative rates, set this amount to 0.00.
The amount specified here defaults automatically on tickets, hauler timesheets, haul ticket add-ons, and haul payment worksheets where the pay basis amount is greater than 0.00 and the calculated payment amount is less than the amount specified here.
Note: You may override the minimum amount in MS Quotes (Pay Codes tab for standard pay codes and Surcharge Overrides tab for surcharge pay codes).
