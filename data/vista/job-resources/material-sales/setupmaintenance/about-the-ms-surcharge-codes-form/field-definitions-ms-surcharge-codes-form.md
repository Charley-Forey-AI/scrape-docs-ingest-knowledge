---
title: "Field Definitions: MS Surcharge Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-codes-form/field-definitions-ms-surcharge-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-codes-form/field-definitions-ms-surcharge-codes-form"
---

# Field Definitions: MS Surcharge Codes Form

The following is a list of field descriptions for the MS
 Surcharge Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Surcharge Code

Enter a number (0-255) to represent this surcharge.

## Description

Enter a description that easily identifies this surcharge, up to 30 characters.

## Effective Date

Enter the effective date for this surcharge code or click the calendar button and select the correct date from the displayed calendar.
This date will be used to determine whether to use the Surcharge Rate or Old Surcharge Rate when assessing surcharges based on this surcharge code. May be left blank if rates are always applicable, regardless of date.

## Rate is Based On

From the drop-down menu, select the option that applies to this surcharge code. The option selected here determines which value the Surcharge Rate (defined on the Rates tab) will be applied against.

- 1-Material Total – Calculate surcharges based on the material total (surcharge rate x material total).

- 2-Material Units – Calculate surcharges based on the material units (surcharge rate x material total).

Note: If you select this option, the system uses the UM specified for the material on the parent ticket when assessing surcharges. During batch validation, the system validates this UM against the UMs defined for the surcharge material and generates an error if a match is not found. To ensure no errors are encountered during batch validation, make sure you set up all possible UMs (in HQ Materials and IN Location Materials) for the related surcharge material.

- 3-Haul Total – Calculate surcharges based on the haul total (surcharge rate x haul total).

- 4-Haul Units – Calculate surcharges based on the haul units (surcharge rate x haul basis).

- 5-Distance – Calculate surcharges based on the distance (surcharge rate x miles).

- 6-Loads – Calculate surcharges based on the number of loads (surcharge rate x loads).

- 7-Fixed Amount – Calculate surcharges using a fixed amount (surcharge rate x 1).

## Phase and Cost Type Based On

From the drop-down menu, select the option that applies to this surcharge.

- 1-Haul - Select this option to post
 surcharges to the haul phase and cost type specified for the surcharge material (in
 HQ Materials). If you select this option and no haul phase/cost type is specified for
 the surcharge material, surcharges will be posted to the haul phase/cost type
 specified on the parent ticket (i.e. the ticket to which the surcharge applies).

- 2-Material - Select this option to
 post surcharges to the material phase and cost type specified for the surcharge
 material (in HQ Materials). If you select this option and no material phase/cost type
 is specified for the surcharge material, surcharges will be posted to the material
 phase/cost type specified on the parent ticket.

## Surcharge Material

Enter the surcharge material (set up in HQ Materials) associated with this surcharge code. Press F4 for a list of valid materials.
Note: The F4 lookup has no way to distinguish between regular materials and surcharge materials; however, if you set up surcharge materials using a specific number range or naming scheme, you can use the filter function to restrict the list to surcharge materials.

## Active

Check this box to activate this surcharge code. Surcharge code must be active in order to be available for assessing fees/surcharges.
Uncheck this box to deactivate this surcharge code. Surcharge code will be unavailable for assessing fees/surcharges.
Note: Surcharge codes can still be assigned to surcharge groups, even if they are inactive. If a surcharge group has inactive surcharge codes, the system will skip those codes during surcharge calculation in MS Ticket Entry. However, you can manually add an inactive surcharge code to a ticket and a surcharge amount will be calculated.

## Allow Discounts with Material Discounts

Check this box to apply discounts to surcharges assessed for any ticket referencing this surcharge code. The discount rate/amount will default from the parent ticket (i.e. the ticket to which the surcharge applies) and will be applied to all related surcharge record(s).
Note: Discounts will only be applied to surcharges if the parent ticket offers a discount and the discount type is R-Discount Rate per dollar.
Uncheck this box if you do not extend discounts to surcharges.

## Subject to Sales Tax When Material is Taxable

Check this box to apply sales tax to surcharges. The tax rate will default from the parent ticket (i.e. the ticket to which the surcharge applies) and will be applied to all related surcharge record(s).
Note: Taxes will only be applied to surcharges if the material specified on the parent ticket is taxable.

## Calculate Surcharge on Cash Sales

Select this checkbox to calculate surcharges on cash sales. When entering tickets (in MS Ticket Entry), the system will automatically calculate surcharges on tickets with a C-Cash or X-Credit Card payment type that reference this surcharge code.
Do not select this checkbox if you do not apply surcharges to cash sales.

## Pay Code

Enter the pay code (from MS Pay Codes)
 associated with this surcharge code. Pay code must have the Pay Rate is Based
 On field set to 7-Percent of Surcharge Total.
 This pay code will be used to determine how much of the surcharge will be passed to the hauler. Leave blank if you do not pass surcharges to the haul vendor or if pay rates are set up to include surcharges.

## Revenue Code

Enter the revenue code associated with this
 surcharge code. Revenue code must have the Based on MS Haul Charge/Surcharge box
 checked (in EM Revenue Codes).
 This revenue code will determine how much of the surcharge will be passed to the equipment revenue account. Leave blank if you do not pass surcharge revenue to the equipment revenue account or if revenue rates are set up to include surcharges.

## Sequence

Enter the sequence number for this surcharge rate.

## Location Group

Required.
Enter the location group (from IN Location Groups) to which this rate applies.
Note: When surcharges are assessed, this rate will only be used if data entered on parent ticket (ticket for which surcharges are being assessed) matches all other criteria defined for this surcharge code/rate and no quote overrides exist.

## Location

Enter the location (from IN Locations) to
 which this rate applies. If left blank, this rate will apply to all locations within the
 specified location group.
Note: When surcharges are assessed, this rate will only be used if data entered on parent ticket (ticket for which surcharges are being assessed) matches all other criteria defined for this surcharge code/rate and no quote overrides exist.

## Category

Enter the material category (from HQ Material
 Categories) to which this rate applies. If left blank, the Material field
 (right) is disabled and this rate will apply to all categories and materials.
Note: When surcharges are assessed, this rate will only be used if data entered on parent ticket (ticket for which surcharges are being assessed) matches all other criteria defined for this surcharge code/rate and no quote overrides exist.

## Material

Enter the material (from HQ Materials) to which this rate applies. Must be a valid material for the specified material category. If left blank, this rate will apply to all materials for the specified category. If you did not specify a category (left), no material can be entered here and rate will apply to all categories and materials.
Note: When surcharges are assessed, this rate will only be used if data entered on parent ticket (ticket for which surcharges are being assessed) matches all other criteria defined for this surcharge code/rate and no quote overrides exist.

## Truck Type

Enter the truck type (from MS Truck Types) to which this rate applies. If left blank, this rate will apply to all truck types.
Note: When surcharges are assessed, this rate will only be used if data entered on parent ticket (ticket for which surcharges are being assessed) matches all other criteria defined for this surcharge code/rate and no quote overrides exist.

## UM

Enter the unit of measure (from HQ Units of Measure) to which this rate applies. If left blank, this rate will apply to all units of measure.
Note: When surcharges are assessed, this rate will only be used if data entered on parent ticket (ticket for which surcharges are being assessed) matches all other criteria defined for this surcharge code/rate and no quote overrides exist.

## Zone

Enter the haul zone to which this rate applies. If left blank, this rate will apply to all haul zones.
Note: When surcharges are assessed, this rate will only be used if data entered on parent ticket (ticket for which surcharges are being assessed) matches all other criteria defined for this surcharge code/rate and no quote overrides exist.

## Surcharge Rate

Enter the surcharge rate for this sequence. The system will used this rate in conjunction with the surcharge basis to calculate a surcharge amount. When surcharges are assessed, this amount will only be used if:

- the Sale Date specified on the parent ticket (ticket for which surcharges are being assessed) is greater than or equal to the Effective Date specified for this surcharge code (Info tab) and,

- the data on the parent ticket matches all other criteria defined for this surcharge code/rate, and no quote overrides exist.

Note: If you enter a negative rate in this field, you must
 set the Min
 Amt to 0.00.

## Min Amt

Enter the minimum amount for this surcharge rate. You will generally enter an amount here if you require a guaranteed surcharge amount. When surcharges are assessed, this amount will only be used if:

-  the calculated surcharge amount is less than this amount and,

- the Sale Date specified on the parent ticket (ticket for which surcharges are being assessed) is greater than or equal to the Effective Date specified for this surcharge code (Info tab) and,

- the data on the parent ticket matches all other criteria defined for this surcharge code/rate, and no quote overrides exist.

Note: If you entered a negative Surcharge Rate
 for this sequence, you must set this amount to 0.00.

## Old Surcharge Rate

Enter the old surcharge rate for this sequence. The system will used this rate in conjunction with the surcharge basis to calculate a surcharge amount. When surcharges are assessed, this amount will only be used if:

- the Sale Date specified on the parent ticket (ticket for which surcharges are being assessed) is less than the Effective Date specified for this surcharge code (Info tab) and,

- the data on the parent ticket matches all other criteria defined for this surcharge code/rate, and no quote overrides exist.

Note: If you enter a negative rate in this field, you must
 set the Old Min
 Amt to 0.00.

## Old Min Amt

Enter the old minimum amount for this surcharge rate. You will generally enter an amount here if you require a guaranteed surcharge amount. When surcharges are assessed, this amount will only be used if:

-  the calculated surcharge amount is less than this amount and,

- the Sale Date specified on the parent ticket (ticket for which surcharges are being assessed) is less than the Effective Date specified for this surcharge code (Info tab) and,

- the data on the parent ticket matches all other criteria defined for this surcharge code/rate, and no quote overrides exist.

Note: If you entered negative Old Surcharge
 Rate for this sequence, you must set this amount to 0.00.
