---
title: "Field Definitions: EM Cost Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-cost-codes-form/field-definitions-em-cost-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-cost-codes-form/field-definitions-em-cost-codes-form"
---

# Field Definitions: EM Cost Codes Form

The following is a list of field descriptions for the EM Cost
 Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Cost Code

Use this field to identify a type of equipment maintenance that you want to track costs on - for example BRAKES, TIRES, or FUEL.
The cost code must be unique and it can be up to 10 characters long.

## Description

Enter a description of the cost code. The description can be up to 30 characters long.

## Revenue Breakdown Code

Enter the revenue breakdown code for this cost
 code or press F4
 to select one from a list.
This field allows you to summarize and compare cost codes to revenue breakdown codes. For example if you have a cost code for Fuel and a revenue breakdown code for Fuel, you can run a report that compares the portion of revenue for fuel to the actual fuel cost.
Revenue codes are created and maintained using
 the [EM Revenue Breakdown Codes ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-breakdown-codes-form) form. You can open this form by
 pressing F5
 in this field.

## EM Cost Type

Specify each of the valid cost types that apply to this cost code. Costs can only be posted to this cost code for the cost types specified here.

## UM

Enter the unit of measure by which to track units for this cost code/cost type. All units posted in this unit of measure for this cost code/cost type will be updated to both the Cost Detail (EMCD) and Annual Costs (EMAC) tables. Units posted to this cost code/cost type in another unit of measure will be updated to the Cost Detail table only.
Note: If you change the unit of measure for a cost type and records exist in the Cost Header table (EMCH) for the cost code/cost type combination, a warning is displayed. The warning notifies you that changing the unit of measure will cause EMCH to be updated with the same U/M value, and that EMMC (Monthly Costs) will also be recalculated based on the UM. You have the option to continue with the change or to cancel it.
