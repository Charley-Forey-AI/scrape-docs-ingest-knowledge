---
title: "Field Definitions: SM Rate Override Base Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-override-base-form/field-definitions-sm-rate-override-base-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-override-base-form/field-definitions-sm-rate-override-base-form"
---

# Field Definitions: SM Rate Override Base Form

The following is a list of field descriptions for the SM Rate
 Override Base form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Equipment Rates: Markup

The Equipment Rates: Markup field on the SM Rate Override Base form, Info tab.
Enter the override markup percent to apply when capturing equipment used on a work order for the customer, service site, or quote (depending on whether you accessed this form via SM Customers, SM Service Site, or SM Work Order Quotes). For example, enter 5% as 5.00000.
Leave this field blank if no override markup applies.
When entering work completed equipment lines
 in SM Work Orders (Work Completed tab), the system uses this percentage in conjunction with
 the equipment usage rate (defined for the revenue code in EM Revenue Rates by Category or
 EM Revenue Rates by Equipment) to derive the Billable Rate.
Note: The system will only use the rate specified here if an advanced rate is not found for the equipment and revenue code specified on work completed equipment line. However, since equipment rate overrides can be defined at the rate template, effective date, customer, and service site levels, the system will use a specific hierarchy to determine which equipment rates to use. For more information, see [Equipment Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides/equipment-rate-hierarchy).

## Labor Rates: Rate

The Labor Rates: Rate field on the SM Rate Override Base form, Info tab.
Enter the override labor rate to use when entering work completed labor lines on a work order for the customer, service site, or quote (depending on whether you accessed this form via SM Customers, SM Service Site, or SM Work Order Quotes).
Leave this field blank if no override markup applies.
When entering work completed labor lines in SM
 Work Orders (Work Completed tab), the system uses this rate to derive the Billable
 Rate.
Note: You can override the labor rate specified here by technician, craft/class, call type, and/or pay type in SM Advanced Labor Overrides (accessed by selecting the Advanced button to the right). The system will only use the rate defined here if no advanced rate is found matching the criteria specified on the work completed labor line. However, since labor rate overrides can be defined at the rate template, effective date, customer, and service site levels, the system will use a specific hierarchy to determine which labor rates to use. For more information, see [Labor Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides/labor-rate-hierarchy).

## Material Rates: Type

The Material Rates: Type drop-down on the SM Rate Override Base form, Info tab.
Specify the material rate type.

- N - No Override - Select this option if you are not overriding the base markup or discount rate defined on the rate template assigned to this service site or customer (depending on whether you accessed this form via SM Customers or SM Service Site).

- M - Markup - Select this option if the Percent specified below represents a markup rate.

- D - Discount - Select this option if the Percent specified below represents a discount rate.

The system uses the type specified here in conjunction with the Basis and Percent defined for the rate template to determine billable amounts for material-related work completed Misc, Inventory, and Purchase lines on a work order. However, this setting is only used if there are no overrides defined for a specific category or material in SM Override Category Material (accessed by selecting the Advanced button below). For more information, see [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy).

## Material Rates: Basis

The Material Rates: Basis drop-down on the SM Rate Override Base form, Info tab.
This field is enabled only when the Type is M-Markup or D-Discount.
Select the rate basis to use in determining the billable rate for work completed materials on a work order for the customer, service site, or quote (depending on whether you accessed this form via SM Customers, SM Service Site, or SM Work Order Quotes).
Note: Material rate overrides defined by category and/or material in SM Override Category Material (accessed by clicking the Advanced button to the right and then double-clicking in the Category & Material Overrides grid in SM Rate Override Material) will override those defined here. The rates defined here will only be used if no overrides exist at the category/material level for the service site or customer

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

For more information about how the system determines which material rate to use, see [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy).

## Material Rates: Break Points By

The Material Rates: Break Points By drop-down on the SM Rate Override Base form, Info tab.
Select how to apply rate break points when calculating discounts or markups for stocked or purchased materials specified on a work order using this template.

- T-Total Cost - Select this option to apply rate break points based on the total cost of the material. For example if you have a break point value of $500, the system will apply a markup or discount when the material total is equal to or greater than $500.

- U-Unit Cost - Select this option to apply rate break points based on the unit cost of the material. For example if you have a break point value of $10, the system will apply a markup or discount when the material's unit cost is equal to or greater than $10.

## Material Rates: Percent

The Material Rates: Percent field on the SM Rate Override Base form, Info tab.

This field is enabled only when the Type is M-Markup or D-Discount.
Required.
Enter the override markup or discount percent to apply to materials specified on work completed inventory or work completed purchase lines on a work order for the customer, service site, or quote (depending on whether you accessed this form via SM Customers, SM Service Site, or SM Work Order Quotes). For example, enter 5% as 5.00000.
The system uses this rate for work completed inventory, work completed purchase lines, and work completed miscellaneous lines as follows:

- Miscellaneous lines - The system uses this rate when a material SM Cost Type is entered (that is, the cost type category is M-Material), regardless of whether you specify a material.

-  Inventory lines - The system always uses this rate, even if no SM Cost Type is specified.

-  Purchase lines - The system uses this rate if:

- You enter a material SM Cost Type for the PO item, regardless of whether you specify a material.

- You enter material for the PO item, but you enter a non-material SM Cost Type or leave the SM Cost Type blank.

Note: If you enter a value of 0.00 here, the system assumes that you intended this value and no markup or discount rate is applied to the work completed line; no further rate search will occur. If you override the markup/discount rate defined here by rate break point in SM Rate Override Material (accessed by selecting the Advanced button to the right), you must specify a rate here. If this rate is 0.00, the break points are ignored.

### Break Points

When using break points, the system first calculates the billable rate for the work completed line using the rate specified here. It then multiplies the billable rate x quantity to derive the material total. The material total is then compared to the rate break points defined in SM Rate Override and, if a match is found, the system recalculates the billable rate using the rate break point rate. If no match is found, the previously calculated billable rate is used.

Note: You can override the markup/discount rate defined here by category or material in SM Override Category Material (accessed by selecting the Advanced button to the right and selecting the Category & Material Overrides tab). The system will only use the rate defined here if no advanced rates are found for the material/category specified on the work completed labor line or in the rate break points table. However, since material rate overrides can be defined at the rate template, effective date, customer, and service site levels, the system will use a specific hierarchy to determine which material rates to use. For more information, see [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy).

## Non-Material Purchases: Markup Percent

The Non-Material Purchases: Markup Percent field on the SM Rate Override Base form, Info tab.
Enter the override markup percent to apply to non-material Misc and Purchase work completed lines on a work order for the customer, service site, or quote (depending on whether you accessed this form via SM Customers, SM Service Site, or SM Work Order Quotes). Enter 5% as 5.00000.
Leave this field blank if no override markup applies. The system will use the rate at the next level of the rate hierarchy to determine the rate to use.
 Non-material work completed lines are defined as follows:

- Miscellaneous lines specifying a non-material SM Cost Type (one with a cost type category other than M-Material) with no material specified or lines were where no SM Cost Type is specified and no material is specified.

- Purchase lines with a non-material SM Cost Type or null SM Cost Type and no material specified

 The system applies this rate to the Cost Rate of the work completed purchase line to determine the Billable Rate.
 Enter 0.00 if no markup will be applied to non-material purchases.
