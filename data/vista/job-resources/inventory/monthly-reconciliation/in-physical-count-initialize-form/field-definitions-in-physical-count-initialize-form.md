---
title: "Field Definitions: IN Physical Count Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/monthly-reconciliation/in-physical-count-initialize-form/field-definitions-in-physical-count-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/monthly-reconciliation/in-physical-count-initialize-form/field-definitions-in-physical-count-initialize-form"
---

# Field Definitions: IN Physical Count Initialize Form

The following is a list of field descriptions for the IN
 Physical Count Initialize form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Beginning/Ending Category

 Enter the beginning and ending in a range of material categories to initialize to the worksheet, or leave blank to initialize all categories.

##  Beginning/Ending Material

 Enter the beginning and ending in a range of materials to initialize to the worksheet, or leave blank to initialize all materials.
 If a range of material categories was specified, only those materials within the category range will be included.

## Select All Locations

Select this checkbox to have all locations in the Available Locations grid initialized to the worksheet.

##  Include Physical Locations

 Select this checkbox to display the physical location for each item in the Available Inventory Locations grid.

## Count Date

Specify the date to be recorded as the default count date for all entries on the worksheet. If left blank, all worksheet entries will default as null.

## Initialize System Count

Check this box to have a system count determined for each material as it is added to the worksheet. Materials already on the worksheet will not be affected.
If this box is unchecked, the System Count column will be left null (blank) for all materials added to the worksheet. Materials already on the worksheet will not be affected.
Note: If a system count is not implemented at this time, it can be updated later using the System Count option in the File menu of the worksheet.

## Include Count Date Activity

Check this box to include activity from all sources (i.e., all transactions in INDT) posted on the specified count date (specified above) in the system count.
Leave this box unchecked if activity posted on the specified count date should be excluded from the system count.
