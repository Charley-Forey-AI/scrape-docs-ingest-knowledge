---
title: "Field Definitions: HQ Materials Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form/field-definitions-hq-materials-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form/field-definitions-hq-materials-form"
---

# Field Definitions: HQ Materials Form

The following is a list of field descriptions for the HQ
 Materials form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Material

 Enter a material code, up to 20 characters.
Note: Using single quotes in the material code may cause
 errors in other programs.

## Description

Enter the description of this material, up to 60 characters.

## Category

Enter a category code or press F4 to select
 one from a list. Material categories are used to group materials together on reports (e.g.
 concrete, plumbing, general, etc.).
Categories are created and maintained using the [ HQ Material Categories ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-material-categories-form) form .

## Material Type

Specify the type for this material. The type allows you to categorize materials for F4 lookups in programs. For example, when using the F4 lookup at Material in Equipment Management, the lookup list will display only those materials assigned an Equipment type.

- Standard – Select this type if this is a standard material (i.e. used for jobs, purchase orders, subcontracts, expenses, etc.).

- Equipment – Select this type if this material is equipment related (i.e. parts, repair, etc.).

Note:If this is a surcharge material, the material type must be Standard.

## Active - Valid for Material Posting

Check this box if this material is active and may be used when posting transactions. Material will be included in F4 material lookups.
Note:If this is a surcharge material, you must check this box.

Leave this box unchecked if this material is not active and you do not want it used when posting transactions. Material will be excluded from standard F4 material lookups (except where ‘all materials’ lookup option is provided).
Note:Making a material inactive only removes it from F4 lookups; it does not restrict its use when posting transactions.

## Taxable for Purchases or Sales

Specify the tax status for this material. This option is used as a default when purchasing or selling this material.
Check this box if this material is taxable. This option is used in conjunction with the various tax options specified throughout the software to determine a tax code default.
Leave this box unchecked if this material is not taxable.
Note:If this is a surcharge material, the system will ignore this flag, so it is not necessary to change the default. Taxing of surcharges is handled at the surcharge code level (in MS Surcharge Codes).

## Stocked in Inventory

For use with the Inventory module.
Check this box if this is a stocked material. You must check this option for every material that will be set up at one or more inventory locations (in IN Location Materials).
Leave this box unchecked if this is a non-stocked material.
Note:If this is a surcharge material, this box must be checked.

## Standard: UM

Specify the unit of measure (from HQ Units of Measure) that will be the standard unit of measure for this material.

- The LS (lump sum) unit of measure is not valid for materials. Since materials carry units and unit cost, they are not compatible with the LS unit of measure.

- If this is a surcharge material, and you will be assigning this material to surcharge codes with a basis of 2-Material Units, you will need to set up all possible UMs on the Additional Units of Measure tab. The system will use the UM specified for the material on the parent ticket when assessing surcharges. During batch validation, the system will validate this UM against the UMs defined for the surcharge material, and if the UM is not set up for the surcharge material, an error is generated.

All other basis options use the surcharge material UM when assessing surcharges, so if you will not be assigning the surcharge material to surcharge codes with a basis of 2-Material Units, no additional UMs setup is required.

## Standard: Unit Cost

Specify the standard cost per unit of this material. This amount will be the default cost for the material when applying the material code - for example in PO Entry, AP Entry, or PM PO Change Orders.
Note:If this is a surcharge material, enter 0.00; surcharge values will be defined in MS Surcharge Codes or overridden in MS Quotes.

##  Per ECM

 Indicate which quantity this unit cost/unit price represents:
 E = Per each
 C = Per Hundred
 M = Per Thousand

## Standard: Unit Price

Specify the standard price per unit that will be used as the default when selling this material to jobs, equipment, or customers.
Note:If this is a surcharge material, enter 0.00; surcharge values will be defined in MS Surcharge Codes or overridden in MS Quotes.

##  Standard: Weight Conv

 Specify the number of pounds required to equal one unit of this material’s standard unit of measure. For example, if the standard unit of measure is TON, enter 2,000. This conversion factor (used by Material Sales and Inventory) allows conversion from pounds (lbs.) to this material’s standard unit of measure.
Note:If this field is left blank, the system cannot convert pounds to the specified unit of measure (where necessary) for this material, which may cause calculations to be inaccurate.

## Payment Discount Type

For use with Material Sales only.
Indicate the discount type that will be used when calculating material-based discounts in Material Sales.

- N – No Discount - No payment discount allowed.

- U – Discount Amt Per Unit - Discounts will be calculated based on an amount per unit, using the amount specified to the right of this option.

- R – Discount Rate per Dollar - Discounts will be calculated on a rate (percentage) of the material total, using the rate specified to the right of this option.

- Payment discounts are used only when the material is specified on a ticket (in MS Ticket Entry) where the payment terms for the customer or contract are flagged for ‘Discount Based on Material’ (option in HQ Payment Terms).

- If this is a surcharge material, the system ignores discount information in this form and bases discounts on the surcharge code and the parent ticket in MS Ticket Entry (the ticket to which the surcharge will be applied).

##  Amount/Rate

 For use with Material Sales only. Disabled if Payment Discount is ‘No Discount’.
If using the ‘Discount Amt per Unit’ discount option, specify the Amount per unit that will be used to calculate payment discounts for this material in Material Sales.
 If using the ‘Discount Rate per Dollar’ discount option, specify the Rate per dollar that will be used to calculate payment discounts for this material in Material Sales. This rate applies to the material total.
Note: Payment discounts specified here will only be used
 when the material is specified on a ticket (in MS Ticket Entry) where the payment terms for
 the customer or contract are flagged for ‘Discount Based on Material’ (option in HQ Payment
 Terms).

##  Purchase UM

Enter the unit of measure that will be used as
 the default when purchasing this material - for example when creating a PO in PO Purchase
 Order Entry. This is a required field, but it can be the same as the standard unit of
 measure.
 If this unit of measure differs from the
 standard unit of measure set up using the UM field in the Standard section on this
 tab, you need to define how the two different units of measure relate using the Additional
 Units of Measure tab. [More](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form)
Units of measure are created and maintained
 using the [ HQ Units of Measure ](/en/vista/vista/administration/headquarters/company-setup/hq-units-of-measure-form) form. You can open this form by
 pressing F5 in this field.
Note: The LS (lump sum) unit of measure is not valid for
 materials. Since materials carry units and unit cost, they are not compatible with the LS
 unit of measure.

## Sales UM

Enter the unit of measure that should be used
 when the material is sold to a job, equipment, or customer.This is a required field, but it
 can be the same as the standard unit of measure selected in the UM field in the
 Standard section on this tab.
If this unit of measure differs from the standard unit of measure, it must be set up for this material on the Additional Units of Measure tab. [More](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form)
Units of measure are created and maintained using the [ HQ Units of Measure ](/en/vista/vista/administration/headquarters/company-setup/hq-units-of-measure-form)form.
Note: The LS (lump sum) unit of measure is not valid for
 materials. Since materials carry units and unit cost, they are not compatible with the LS
 unit of measure.

##  Metric UM

 Entry in this field is optional.
 Specify the metric unit of measure (from HQ Units of Measure) by which this material may be bought or sold. The metric unit of measure must be set up for this material on the Additional Units of Measure tab.
Note: The LS (lump sum) unit of measure is not valid for
 materials. Since materials carry units and unit cost, they are not compatible with the LS
 unit of measure.

## Matl Phase

Specify the phase (from JC Phases) that will be
 used as the default when costing this material to a job, or leave blank if there is no
 standard phase for this material.
Note:If this is a surcharge material, surcharges will
 only be posted to this phase if the Phase and Cost Type Based On drop-down
 field is set to 2-Material for the surcharge code used to track this material. If this
 field is left blank, surcharges will be posted to the same material phase specified on
 the parent ticket (i.e. the original ticket for which the surcharge was assessed).

## Matl CT

Specify the cost type (from JC Cost Types) that will be used as the default when costing this material to a job, or leave blank if there is no standard cost type for this material.
Note:If this is a surcharge material, surcharges will
 only be posted to this cost type if the Phase and Cost Type Based On drop-down
 field is set to 2-Material for the surcharge code used to track this material. If this
 field is left blank, surcharges will be posted to the same material cost type specified
 on the parent ticket (i.e. the original ticket for which the surcharge was
 assessed).

## Haul Phase

Specify the default phase (from JC Phases) to
 be used when posting haul charges to a job from Material Sales. If this field is left
 blank, haul charges will be posted to the same phase as the material.
Note:If this is a surcharge material, surcharges will
 only be posted to this phase if the Phase and Cost Type Based On drop-down
 field is set to 1-Haul for the surcharge code used to track this material. If this field
 is left blank, surcharges will be posted to the same haul phase specified on the parent
 ticket (i.e. the original ticket for which the surcharge was assessed).

## Haul CT

Specify the default cost type (from JC Cost Types) to be used when posting haul charges to a job from Material Sales. If this field is left blank, haul charges will be posted to the same cost type as the material.
Note:If this is a surcharge material, surcharges will
 only be posted to this cost type if the Phase and Cost Type Based On drop-down
 field is set to 1-Haul for the surcharge code used to track this material. If this field
 is left blank, surcharges will be posted to the same haul cost type specified on the
 parent ticket (i.e. the original ticket for which the surcharge was assessed).

##  Haul Code

 Enter the default haul code (from MS Haul Codes) that will be used to calculate haul charges for this material in Material Sales.May be overridden.

##  Price Service ID

 If you subscribe to a pricing service, enter the pricing service identification number for this material, up to 30 characters. This number will be used for pricing updates.

##  UM

 Enter any additional unit of measure (from HQ Units of Measure), other than the standard unit of measure, by which this material may be bought or sold.
Note: The LS (lump sum) unit of measure is not valid for
 materials. Since materials carry units and unit cost, they are not compatible with the LS
 unit of measure.
TIP: Use the ‘Initialize Locations’ option (File menu) to auto-add this unit of measure to all Inventory locations stocking this material.

## Conversion Factor

Enter the number of units of the standard unit of measure it will take to equal one unit of this unit of measure. This field is used to convert this unit of measure to the standard unit of measure for this material.
For example, if this material is normally dealt with in square feet, but is sometimes bought or sold in 4’ x 8’ sheets, set the conversion factor to 32.
Note:Units inputs have a decimal precision of three (i.e. .000); therefore, if this a stocked material and you update additional UMs to Inventory, it is important to understand the effects that the conversion factor defined for these UMs may have when updating IN/GL with posted units. If the conversion factor has a non-zero value in the 4th (.0245) or 5th position (.00245), rounding may occur.

For example:
Posted Units:
10.00

Unit Cost:
128.25000

Conversion Factor:
.00245

Conversion to Std Units:
.025 (10.00 x .00245 = 0.0245, rounded to .025)

Total Cost:
3.21 (.025 x 128.25 = 3.20625, rounded to 3.21)

Calculation with decimal precision of 5 (.00000)

Posted Units:
10.00

Unit Cost:
128.25

Conversion Factor:
.00245

Conversion to Std Units:
.0245 (10.00 x .00245 = 0.0245

Total Cost:
3.14 (.0245 x 128.25 = 3.14212, rounded to 3.14

## Cost

Enter the cost that will default whenever this
 material is purchased in this unit of measure. Initially defaults the calculation of the
 Standard Unit
 Cost x Conversion Factor x Cost ECM.

## Price

Enter the default price at which this material
 in this unit of measure will be sold. Initially defaults the calculation of the Standard Unit
 Price x Conversion Factor x Price ECM.

##  ECM

 Indicate which quantity the cost/price represents.
 E = Per each
 C = Per Hundred
 M = Per Thousand

##  No Discount/Pmt Disc Per Unit/Pmt Disc Rate

 For use in Material Sales only.
 This field’s label differs depending on the Discount Type specified for this material (Info tab).

- No Discount – This label displays when the Discount Type is ‘None’. Defaults as 0.00000 and is disabled.

- Pmt Disc Per Unit – This label displays when the Discount Type is ‘Discount Amt per Unit’. Specify the payment discount amount per unit for this material/UM.

- Pmt Disc Rate – This label displays when Discount Type is ‘Discount Rate per Dollar’. Specify the payment discount rate to use for this material/UM.

##  Country

 Required.
 Enter the country to which the price index applies.
Note: The price index being assigned to this material must
 exist for this country (and the state specified in the next field) in HQ Escalation Index.

##  State

 Required.
 Enter the state to which the price index applies.
Note: The price index being assigned to this material must
 exist for this state (and the country specified in the previous field) in HQ Escalation
 Index.

##  Price Index

 Required.
 Enter a valid price index for this material. Price index must exist in HQ Escalation Index for the specified country/state.

##  Component Matl

 Required.
 Enter the component material to which price escalation adjustments will apply. This component material must be set up for the finished material in IN Bill of Materials or IN Bill of Materials Override.

##  Notes

 Enter any notes pertaining to this entry. Space is virtually unlimited.
