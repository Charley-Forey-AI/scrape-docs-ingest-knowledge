---
title: "About the EM Work Order Parts Posting Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-parts-posting-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-parts-posting-form"
---

# About the EM Work Order Parts Posting Form

Use this form (accessed from the EM Programs menu or by clicking the Post Parts button in EM Work Order Update) to post parts to work orders.
You will typically initialize the parts set up for a work order; however, you can manually enter parts.
If using the initialize feature (File > Initialize Parts From Work Order), each part initialized (based on entered criteria) will be set up as a separate sequence here.
When entering quantities for parts, if a part's status is ‘on order' or 'out of stock', change the units to 0.00 so that GL is not updated. When the part comes in, you can then enter the units and update GL. The unit of measure and unit price for each part default from HQ Materials or IN Location (if pulling parts from on-hand inventory); however, you can change the defaults as necessary. If you enter the equipment's current odometer and hour meter readings, the system will update the Hour and Odometer Reading and Date fields for the equipment in EM Equipment.
Note: If you are not validating parts (that is, the Validate Parts option is unselected in EM Company Parameters), you can enter any part here, regardless of whether it is set up in HQ Materials, as long as no IN location is specified. If you enter an inventory location, the part must exist for the specified location, regardless of how the Validate Parts option is set.

## Updates to Odometers, Hour Meters, and Reading Dates

When posting parts, updates to equipment odometers, hour meters, and meter reading dates (in EM Equipment) will depend on the update option selected for cost adjustments and parts posting in EM Company Parameters (Updates tab).
For more information about update options, click the links below.
[Meter Updates: Equipment Usage](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form/field-definitions-em-company-parameters-form#ID-0000b8af--en)
[Meter Updates: Costs Adj and Parts Posting](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form/field-definitions-em-company-parameters-form#ID-0000b8c0--en)
[Meter Updates: Fuel Posting](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form/field-definitions-em-company-parameters-form#ID-0000b8ce--en)
