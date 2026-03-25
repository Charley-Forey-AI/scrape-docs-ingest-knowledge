---
title: "Field Definitions: EM Work Order Update Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-update-form/field-definitions-em-work-order-update-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-update-form/field-definitions-em-work-order-update-form"
---

# Field Definitions: EM Work Order Update Form

The following is a list of field descriptions for the EM Work
 Order Update form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Work Order

 Enter the work order to update. Press F4 for a list of valid work orders.
 Once you enter the work order, all items on the work order display in the grid. You can update each work order item manually or use the Update All feature to update all work order items at the same time with the same information.

##  PR Co

 Enter the PR Co of the mechanic for this work order item.

##  Mechanic

 Specify the mechanic (from PR Employees) for this work order item.
Note: If you change the mechanic for a work order item with
 a 'Final' status, a warning displays, but entry is allowed.

##  Status Code

 Specify the status of this work order item. Entering a 'Final' status code (status type of ‘Final’ in EM Work Order Status Codes) enables the Date Completed, Current Odometer, and Current Hours fields.

##  Repair Type

 Specify the repair code (EM WO Repair Types) that applies to this work order item.
Note: If you change the repair code for a work order item
 with a 'Final' status, a warning is displayed, but entry is allowed.

##  Date Completed

 This field is only accessible if you assign a ‘Final’ status to the work order item.
 Enter the date this work order item was completed. Initially defaults the current date. This field updates the ‘Last Done Date’ field in EM Standard Maintenance Groups for the equipment/maintenance group/item.
Note: If you change the completion date for a work order
 item with a 'Final' status, a warning is displayed, but entry is allowed.

## Curr Odo

This field is only accessible if you assign a
 'final' status code (i.e. status code with a  Status Type of Final) to the work order
 item.
Enter the equipment’s odometer reading at the time this work order item was completed. Initially defaults to 0.00. You will typically enter a value that is equal to or less than the current reading on file for the equipment. However, if you enter a value that exceeds the last reading for the equipment, the following message displays:
Warning: Odometer entered exceeds the last Odo reading on file for Equipment. To update current reading, click the ‘Meters’ button.
The system allows the entry; however, to
 prevent discrepancies, you will need to run EM Meter Readings to update the equipment's
 odometer accordingly. Although entry in this field updates the Last Done Miles
 field in EM Standard Maintenance Groups for this equipment/maintenance group/item, it does
 not update the Odometer reading in EM Equipment.

## Curr Hours

This field is only accessible if you assign a
 'final' status code (i.e. status code with a Status Type of Final) to the work order
 item.
Enter the equipment’s hour meter reading at the time this work order item was completed. Typically, this value is equal to or less than the current reading on file for the equipment. If you enter a value that exceeds the last reading for the equipment, the following message displays:
Warning: Hour meter entered exceeds the last Hour meter reading on file for Equipment. To update current reading, click the ‘Meters’ button.
The system allows the entry; however, to
 prevent discrepancies, you will need to run EM Meter Readings to update the equipment's
 hour meter accordingly. Although entry in this field updates the Last Done
 Hoursfield in EM Standard Maintenance Groups for this equipment/maintenance
 group/item, it does not update the Hour Meter reading in EM Equipment.
