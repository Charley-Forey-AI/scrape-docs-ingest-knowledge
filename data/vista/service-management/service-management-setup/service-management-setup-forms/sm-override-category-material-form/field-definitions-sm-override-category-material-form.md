---
title: "Field Definitions: SM Override Category Material Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-override-category-material-form/field-definitions-sm-override-category-material-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-override-category-material-form/field-definitions-sm-override-category-material-form"
---

# Field Definitions: SM Override Category Material Form

The following is a list of field descriptions for the SM
 Override Category Material form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq

The Seq field on the SM Override Category Material form and on the Category & Material Overrides tab in SM Rate Override Material.
Enter N, New, or + to add a new material or category
 override sequence. The system automatically assigns the next available sequence
 number.

##
Category

The Category field on the SM Override Category Material form, Info tab and on the Category & Material Overrides tab in SM Rate Override Material.
Enter the category for which you are setting up the override markup or discount rate or leave blank if this override sequence applies to a specific material; you cannot specify both a category and a material for an override sequence.
Note: Material and category overrides set up in this form at the service site or customer levels, will override those set up at the rate template level, respectively.

## Material

The Material field on the SM Override Category Material form, Info tab and on the Category & Material Overrides tab in SM Rate Override Material.
Enter the material for which you are setting up the override markup or discount rate or leave blank if you specified a category (above) for this override sequence; you cannot specify both a category and a material for an override sequence.
Note: Material and category overrides set up in this form at the service site or customer levels, will override those set up at the rate template level, respectively.

## SM Cost Type

The SM Cost Type field on the SM Override Category Material form, Info tab and on the Category & Material Overrides tab in SM Rate Override Material..
Enter the SM cost type to apply override rates towards. Press F4 to select from a list of valid SM cost types.

## Override Rate: Type

The Override Rate: Type drop-down on the SM Override Category Material form, Info tab and on the Category & Material Overrides tab in SM Rate Override Material..
Specify the rate type for this material or category override sequence.

- Markup - Select this option if the Percent
 specified below represents a markup rate.

- Discount - Select this option if the Percent
 specified below represents a discount rate.

Note: Material and category overrides set up in this form at the service site or customer levels, will override those set up at the rate template level, respectively.

## Override Rate: Basis

The Override Rate: Basis drop-down on the SM Override Category Material form, Info tab and on the Category & Material Overrides tab in SM Rate Override Material.

Select the rate basis for this category or material override sequence. The basis selected here will be used in billable rate calculations when entering materials on a work order that reference the specified material or category.
Note: Material and category overrides set up in this form at the service site or customer levels, will override those set up at the rate template level, respectively.

For each of the applicable default descriptions below, IN Location Materials and HQ Materials apply as follows:

- HQ Materials — Inventory lines that reference an HQ material (that is, IN Co and Location are not specified), Purchase lines that specify a material, and Misc lines generated from AP where a material is specified.

- IN Location Materials — Work completed Inventory lines with an IN Co and Location specified.

A-Actual CostTypically used with Markups.Select this option to use the Total Actual Cost specified on the work completed line.
This option does not apply to work completed Purchase lines; therefore if you select this option, the system will use the Total Project Cost in markup/discount calculations for Purchase lines.
S - Standard CostTypically used with Markups.Select this option to use the standard unit cost defined for the material in HQ Materials or IN Location Materials.
This option does not apply to material-related work completed lines that do not specify a material; therefore if you select this option, the system handles the markup/discount calculations as follows:

- For work completed Misc lines that reference a material-related SM Cost Type, but do not reference a material, the system uses the Total Actual Cost.

- For work completed Purchase lines that reference a material-related SM Cost Type, but do not reference a material, the system uses the Total Projected Cost.

V - Average CostTypically used with Markups.Select this option to use the Avg Unit Cost defined for the material in IN Location Materials.
This option does not apply for work completed lines that specify an HQ Material or do not specify a material; therefore if you select this option, the system handles the markup/discount calculations as follows:

- For lines that specify an HQ Material, the system uses the Standard Unit Cost in HQ Materials.

- For work completed Misc lines that reference a material-related SM Cost Type, but do not reference a material, the system uses the Total Actual Cost.

- For work completed Purchase lines that reference a material-related SM Cost Type, but do not reference a material, the system uses the Total Projected Cost.

L - Last CostTypically used with Markups.Select this option to use the Last Unit Cost defined for the material in IN Location Materials.
This option does not apply for work completed lines that specify an HQ Material or do not specify a material; therefore if you select this option, the system handles the markup/discount calculations as follows:

- For lines that specify an HQ Material, the system uses the Standard Unit Cost in HQ Materials.

- For work completed Misc lines that reference a material-related SM Cost Type, but do not reference a material, the system uses the Total Actual Cost.

- For work completed Purchase lines that reference a material-related SM Cost Type, but do not reference a material, the system uses the Total Projected Cost.

P - Standard PriceTypically used with Discounts.Select this option to use the standard unit price defined for the material in HQ Materials or IN Location Materials.
This option does not apply to material-related work completed lines that do not specify a material; therefore if you select this option, the system handles the markup/discount calculations as follows:

- For work completed Misc lines that reference a material-related SM Cost Type, but do not reference a material, the system uses the Total Actual Cost.

- For work completed Purchase lines that reference a material-related SM Cost Type, but do not reference a material, the system uses the Total Projected Cost

Note: If the unit of measure specified for the work completed material line does not match the Standard UM defined for the material (in HQ Materials), the system will use the unit cost or unit price (if using Standard Price) defined for the posted unit of measure in the Add'l UMs table (Inventory lines) or Additional Units of Measure table (Purchase lines).

## Override Rate: Break Points By

The Override Rate: Break Points By drop-down on the SM Override Category Material form, Info tab and on the Category & Material Overrides tab in SM Rate Override Material.

Select how to apply rate break points when calculating discounts or markups for stocked or purchased materials specified on a work order using this template.

- T-Total Cost - Select this option to apply rate break points based on the total cost of the material. For example if you have a break point value of $500, the system will apply a markup or discount when the material total is equal to or greater than $500.

- U-Unit Cost - Select this option to apply rate break points based on the unit cost of the material. For example if you have a break point value of $10, the system will apply a markup or discount when the material's unit cost is equal to or greater than $10.

## Override Rate: Percent

The Override Rate: Percent field on the SM Override Category Material form, Info tab and on the Category & Material Overrides tab in SM Rate Override Material.
Enter the standard markup or discount percent to apply when work completed inventory or work completed purchase lines on a work order reference this material or category (e.g. enter 5% as 5.00000)
The system will use this rate when determining the billable rate for the work completed line.

- This field initially defaults as 0.00. If you leave the value at 0.00, the system assumes that you intended this value and no markup or discount rate will be applied to the work completed line for the specified material or category; no further rate search will occur.

- Material and category overrides can be set up at the rate template, effective date, customer, and service site levels; therefore, the system will use a specific hierarchy to determine which rates to use. For more information, see [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy).

## Break Point Value

The Break Point Value field on the SM Override Category Material form, Rate Break Points tab.
Enter the amount to use as a break point when applying discounts or markups to stocked or purchased materials specified on a work order. The system will apply a markup or discount rate (depending on the rate type selected for the material or category) using the percentage specified to the right.
 The option you selected in the Break Point By
 field for the category or material determines what the break point value represents. If you
 selected Total Cost, the system will apply the specified percentage when the total cost of
 the material reaches this amount. If you selected Unit Cost, the system will apply the
 specified percentage when the unit cost of the material reaches this amount. For more
 information about rate break points, see [Rate Break
 Points](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/about-material-rate-break-points).
Note: Rate break points set up by material or category in this form at the service site or customer levels, will override those set up at the rate template level, respectively.

## Percent

The Percent field on the SM Override Category Material form, Rate Break Points tab.
Enter the percent to use for applying discounts or markups (depending on the rate type for the material or category) to stocked or purchased materials on a work order (e.g. enter 5% as 5.00000).
 The system will apply this percentage when
 the total cost or unit cost of the material (depending on the Break Points By
 option selected for the rate template) reaches the amount specified in the Break Point
 Value field for this entry.
For information about how the system uses rate break points when calculating the discount or markup rate for materials on a work completed line, see [Rate Break Points](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/about-material-rate-break-points).
Note: Because material rates/overrides can be defined at the rate template, effective date, customer, service site, and work order quote levels, the system will use a specific hierarchy to determine which material rates to use. For more information, see [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy).
