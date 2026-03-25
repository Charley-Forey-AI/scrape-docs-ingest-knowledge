---
title: "Field Definitions: EM Work Order Item Update Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-item-update-form/field-definitions-em-work-order-item-update-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-item-update-form/field-definitions-em-work-order-item-update-form"
---

# Field Definitions: EM Work Order Item Update Form

The following is a list of field descriptions for the EM Work
 Order Item Update form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## PR Co

Specify the PR Co of the mechanic for all items on this work order.

##  Mechanic

 Specify the mechanic (from PR Employees) to assign to all items on this work order.
 Click ‘Update All’ button to update all items with this mechanic.

##  Status Code

 Specify the status (from EM Work Order Status Codes) to assign to all items on this work order. If you enter a 'Final' status code (status code with a Status Type of Final), you must enter a completion date.
 Click ‘Update All’ button to update all items with this status code.

##  Repair Type

 Specify the repair code (EM WO Repair Types) to assign to all items on this work order.
 Click ‘Update All’ button to update all items with this repair type.

##  Date Completed

 This field is only accessible for items assigned a 'Final' status code.
 Enter the completion date to assign to all items on this work order. Initially defaults the current date. Entry here updates the ‘Last Done Date’ field in EM Standard Maintenance Groups for each equipment/maintenance group/item.
 Click ‘Update All’ button to update all items with this completion date.

## Current Odometer

This field is only accessible for items
 assigned a 'final' status code (i.e. status codes with a  Status Type of
 Final).
Note: If a work order contains a mix of items with and
 without components, this field is disabled. The following message will display below the
 Curr
 Hours field:
Mixed WO Items. Cannot update Equipment and
 Component Meters
Enter the equipment odometer reading to assign to all items on this work order. Initially defaults the equipment’s current odometer reading. If you override the default and the value entered exceeds the current reading on file for the equipment, the following message displays:
Warning: Odometer entered exceeds the Odo reading on file for Equipment. To update current reading, click the ‘Meters’ button.”
The system allows the entry; however, to
 prevent discrepancies, you will need to run EM Meter Readings to update the equipment's
 odometer accordingly. Although entry in this field updates the Last Done Miles
 field in EM Standard Maintenance Groups for each equipment/maintenance group/item, it does
 not update the Odometer reading in EM Equipment.
Click Update All to update all items with this
 odometer reading.

## Current Hours

This field is only accessible for items
 assigned a 'final' status code (i.e. status codes with a  Status Type of
 Final).
Note: If a work order contains a mix of items with and without components, this field is disabled. The following message will display below this field:
Mixed WO Items. Cannot update Equipment and
 Component Meters
Enter the equipment hour meter reading to assign to all items on this work order. Initially defaults the equipment’s current hour meter reading. If you override the default and the value entered exceeds the current reading on file for the equipment, the following message displays:
Warning: Hour meter entered exceeds the Hour meter reading on file for Equipment. To update current reading, click the ‘Meters’ button.”
The system allows the entry; however, to
 prevent discrepancies, you will need to run EM Meter Readings to update the equipment's
 hour meter accordingly. Although entry in this field updates the Last Done Hours
 field in EM Standard Maintenance Groups for each equipment/maintenance group/item, it does
 not update the Hour Meter reading in EM Equipment.
Click Update All to update all items with this
 hour reading.
