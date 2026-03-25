---
title: "Field Definitions: EM Standard Maintenance Groups Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-standard-maintenance-groups-form/field-definitions-em-standard-maintenance-groups-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-standard-maintenance-groups-form/field-definitions-em-standard-maintenance-groups-form"
---

# Field Definitions: EM Standard Maintenance Groups Form

The following is a list of field descriptions for the EM
 Standard Maintenance Groups form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Equipment

 Enter the equipment for which you are setting up this standard maintenance group.

##  Maintenance Group

 Enter a code, up to 10 characters that uniquely identifies the group of tasks this maintenance group represents.

##  Description

 Enter a description of the maintenance group, up to 60 characters.

## Basis

Specify the unit basis for this maintenance group.

- H-Hours — Select this option to schedule maintenance based on the number of hours logged.

- M-Miles/Kilometres — Select this option to schedule maintenance based on the number of miles or kilometres driven.

- G-Gallons/Litres — Select this option to schedule maintenance based on the gallons or litres of fuel used.

- F-Annual Fixed Date — Select this option to schedule maintenance on the same date every year (specified in the [Month / Day ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-standard-maintenance-groups-form/field-definitions-em-standard-maintenance-groups-form#ID-0000cd5a--en)fields to the right).

## Month / Day

These fields are accessible only if the basis is ‘F-Annual Fixed Date'. Entry is required.
Specify the month and day on which the annually scheduled maintenance will occur.
 Initialization will include only equipment not serviced within 45 days of the month and day specified here. For example:
Month / Day: 4/1
Current Date: 3/25/13
Last Done
Due, WO Created?

2/4/13
Yes

3/4/13
No

## Service Scheduling

Use the fields in this section to specify the interval at which to schedule maintenance for the designated maintenance group and when service-due warnings should begin. The interval type (Hours, Miles/Kilometres, or Gallons/Litres) displayed will correspond to the Basis specified for the maintenance group.
The following two options are only enabled
 when the Basis is H-Hours, M-Miles/Kilometres, or G-Gallons/Litres:

- Perform Service Every _____ (Hours, Miles/Kilometres, or Gallons/Litres) or every _____ days

Specify the interval in hours, miles/Kilometres, or gallons/Litres between services. If applicable, also indicate the number of days between services. You can enter a maximum of 3650 days (equivalent to 10 years.) If number of days is indicated, service will be due at whichever interval comes first.

- Warn When Service Within _____ (Hours, Miles/Kilometres, or Gallons/Litres) of being due

Indicate the number of hours, miles/Kilometres, or gallons/Litres before service is due that you want these items to start appearing on the EM Scheduled Maintenance Report. For example, if oil is to be changed every 3,000 miles/Kilometres, you may want to start seeing this on the schedule when the odometer is within 500 miles/Kilometres of the time maintenance is due.
This option is enabled only when the
 Basis is F-Annual Fixed Date

- Create Work Order _____ days prior to Annual Fixed Date

Indicate the number of days prior to the
 specified annual fixed date that work orders may be created for this maintenance group. For
 example, if the annual fixed date is 12/15 and you specify 30 days in this field, the
 maintenance group will only be included in initialization if the WO Date (specified in EM
 Work Order Init) falls within 30 days or less of the annual due date (e.g. the WO Date is
 11/16 or later).
Note: When determining maintenance groups/items due for maintenance, initialization will exclude any item where the Last Done date falls within the variance specified here. For example:
Note: Annual Fixed Date: 6/15  Create Work Order ___ days
 prior to Annual Fixed Date: 30 WO Date: 5/25/2019
Note: If the Last Done date is 5/20/2019, item falls within
 the 30-day variance and is not due for maintenance. Item will display on the Items Not Due
 list.
Note: If the Last Done date is 4/20/2019, item falls outside
 the 30-day variance and is due for maintenance. Item will be added to the Items Due
 list.

##  Delete Items On Completion

 Check this box to delete items in this maintenance group as they are completed. Items that are not completed will remain in the group until the next scheduled service. Typically used when all items in the group are one-time only repairs.
 Leave this box unchecked if not deleting maintenance items as they are completed.
Note: You cannot combine items that you want deleted upon completion with items that you do not want deleted. Therefore, if you have both types of items, you will need to set them up on separate maintenance groups.

##  Linked Maint Group

 Specify the standard maintenance group to link to the ‘master’ maintenance group specified above. Items in this maintenance group will be included when performing maintenance on items in the master maintenance group.

##  Item

 Enter a number (0-32,767) or enter ‘N’, ‘New’, or ‘+’ to have the system the next sequential number available.

##  Description

 Enter a description of this maintenance item, up to 60 characters.

## Cost Code

Specify the cost code to post labor and/or material costs to for this item once it becomes a work order.
Note: If you have specified to allow changes to cost codes on work orders (in EM Company Parameters), you may override this cost code when editing the work order (in EM Work Order Edit).

##  Repair Type

 Specify the repair type for this item. Some examples of repair types might be PM, Scheduled Maintenance, Warranty, Inspection Problem, and so forth.

##  Work Performed

- In-House – Select this option if performing the work on this item in-house.

- Outside – Select this option if having work performed on this item at an outside shop.

##  Estimated Hours

 Specify the number of hours you estimate it will take to complete the work on this item.

## Estimated Cost

Specify the estimated cost to complete this item.

## Last Done: Hours

Specify the hour meter reading from the last performed maintenance on this item.
You will only need to make an entry in this field when first going online. Once you have begun using work orders, this field is updated automatically each time this item is completed and given a meter reading and completion date.
Note: This value represents the current meter reading, not the total meter reading (i.e. current + replaced).
If setting up a new maintenance group/item and the item has been completed within the last maintenance cycle, make sure you enter the last done hours and last done date to prevent the system from considering the new item as ‘due for maintenance’.

- If you manually update the Last Done information for a maintenance item and the hour meter has been replaced for the equipment, the system will assume the updated values are for the current meter unless the last done date is earlier than the replaced meter date OR the last done date is the same as the replaced meter date, but the last done hours are greater than the current hours. In which case, it will assume the reading is for the replaced meter.

For information about how the system
 determines whether an item is due for maintenance when replaced meters exist, see [Meter Replacements](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-standard-maintenance-groups-form) topic in the form help for EM Standard
 Maintenance Groups.

- Hovering over the Last Done Hours
 field will display a tool tip showing the total hours (last done hours + replaced
 meter hours). This value is used when determining items due for maintenance in EM
 Work Order Initialization (see Meter Replacements link above).

## Last Done: Miles

Specify the odometer reading from the last performed maintenance on this item.
You will only need to make an entry in this field when first going online. Once you have begun using work orders, this field is updated automatically each time this item is completed and given an odometer reading and completion date.
Note: This value represents the current meter reading, not the total meter reading (i.e. current + replaced).
If setting up a new maintenance group/item and the item has been completed within the last maintenance cycle, make sure you enter the last done miles and last done date to prevent the system from considering the new item as ‘due for maintenance’.

- If you manually update the Last Done information for a maintenance item and the odometer has been replaced for the equipment, the system will assume the updated values are for the current meter unless the last done date is earlier than the replaced meter date OR the last done date is the same as the replaced meter date, but the last done miles are greater than the current miles. In which case, it will assume the reading is for the replaced meter.

Note: For information about how the system determines
 whether an item is due for maintenance when replaced meters exist, see [Meter Replacements](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-standard-maintenance-groups-form) topic in the form help for EM Standard
 Maintenance Groups.

- Hovering over the Last Done
 Miles field will display a tool tip showing the total miles (last
 done miles + replaced meter miles). This value is used when determining items due
 for maintenance in EM Work Order Initialization (see Meter Replacements link
 above).

##  Last Done: Gallons

 Specify the fuel usage reading from the last performed maintenance on this item.
 You will only need to make an entry in this field when first going online. Once you have begun using work orders, this field is updated automatically each time this item is completed and given a fuel usage reading and completion date.
 If setting up a new maintenance group/item and the item has been completed within the last maintenance cycle, make sure you enter the last done gallons and last done date to prevent the system from considering the new item as ‘due for maintenance’.

## Last Done: Date

Specify the last maintenance date for this item.
You will only need to make an entry in this field when first going online. Once you have begun using work orders, this field is updated automatically each time this item is completed and given a completion date.

- The selection process in EM Work Order Initialize looks at this date when determining if an item is due for maintenance, and will include items with a null ‘last done’ date. Therefore, when setting up new maintenance groups/items, it is suggested that you enter a date here to prevent the system from considering new items as ‘due for maintenance’.

- If you manually update the Last Done information for a maintenance item and the odometer and/or hour meter has been replaced for the equipment, the system will assume the updated values are for the current meter unless the last done date is earlier than the replaced meter date OR the last done date is the same as the replaced meter date, but the last done hours or miles are greater than the current hours or miles. In which case, it will assume the reading is for the replaced meter.

For information about how the system determines whether an item is due for maintenance when replaced meters exist, see [Meter Replacements](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-standard-maintenance-groups-form) topic in the form help for EM Standard Maintenance Groups.

## Part Code

Use this field to select the part needed to complete the maintenance item. Enter a part code or press F4 to select a part from a list. Once the part is selected, the fields on the Parts tab will populate with the part information.
 If the Validate Parts/Materials box is checked
 on the Parts tab of the EM Company Parameters form, the selected part must be a valid HQ
 material, vendor material, or equipment part cross-referenced to a valid HQ material.

## Part Description

This field will populate with the description
 of the part selected in the Part Code field.

## UM - Unit of Measure

This field populates with the standard unit of
 measure of the part selected in the Part Code field, but you can change this
 field if the default does not apply.
Enter the unit of measure for this part or
 press F4
 to select one from a list. Only units of measure set up on the equipment will
 display in the list ([HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form)Additional Units of Measure tab).

## Quantity

Based on the unit of measure selected in the
 UM
 field, enter the quantity of this part needed to complete the maintenance item.

## Purchased/Stocked

Use this field to select if the part it purchased or stocked.

- Purchased - Select this option if purchasing this part from a vendor.

- Stocked - Select this item if acquiring this item from on-hand stock.

## Required

Check this box if this part is required for the completion of this maintenance item.
