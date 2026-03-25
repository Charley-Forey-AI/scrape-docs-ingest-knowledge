---
title: "Field Definitions: EM Work Order Mass Update Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-mass-update-form/field-definitions-em-work-order-mass-update-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-mass-update-form/field-definitions-em-work-order-mass-update-form"
---

# Field Definitions: EM Work Order Mass Update Form

The following is a list of field descriptions for the EM Work
 Order Mass Update form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Beginning/Ending WO

 Enter the beginning and ending work order in the range of work orders that you wish to update or close. Leave blank if not restricting selection by work order range.

##  JC Co

 Enter the Job Cost company by which to restrict selection of work orders to close/update, or leave blank to include work orders for all equipment, regardless of JC company assignment.
Note: Entry must be made here if you will be restricting
 selection by job.

##  Job

 This
 field is only enabled when an entry is made in the JC Co field.
 Enter the job (from JC Jobs) by which to
 restrict selection of work orders to close/update, or leave blank to include work orders
 for all equipment, regardless of job assignment.

##  Location

 Enter the location (from EM Locations) by which to restrict selection of work orders to close/update, or leave blank to include work orders for all equipment, regardless of location assignment.

##  Category

 Enter the equipment category (from EM Categories) by which to restrict selection of work orders to close/update, or leave blank to include work orders for all equipment, regardless of category assignment.

##  Dept

 Enter the department (from EM Departments) by which to restrict selection of work orders to close/update, or leave blank to include work orders for all equipment, regardless of department assignment.

##  Assigned Shop

 Enter the shop (from EM Shops) by which to restrict selection of work orders to close/update, or leave blank to include work orders for all equipment, regardless of shop assignment.

##  PR Co

 Enter the PR company by which to restrict selection of work orders to close/update, or leave blank to include work orders for all equipment, regardless of PR company assignment.
Note: Entry must be made here if you will be restricting selection based on mechanic.

##  Mechanic

 Enter the mechanic by which to restrict selection of work orders to close/update, or leave blank to include work orders for all equipment, regardless of mechanic assignment. Mechanic must be a valid employee (from PR Employees) for the PR company specified in the previous field.

##  Search by Date

- None – Select this option if not restricting work order selection based on date.

- Created – Select this option to restrict selection of work orders based on creation date.

- Due – Select this option to restrict selection of work orders based on due date.

- Scheduled – Select this option to restrict selection of work orders based on schedule date.

##  Beginning/Ending Date

 Enter the beginning and ending date in a range of created, due, or scheduled dates (depending on Search by Date option) by which to restrict selection of work orders to close/update.

##  Work Order: Update

 Check this box to include this work order when updating work orders. When the Apply button is clicked, this work order will be updated with specified changes.
Note: Checking this box will automatically check the Update
 box for all items on the work order. You can override the Update setting for each item on
 the WO Items tab.
 Leave this box unchecked if you do not want to update this work order.

## Work Order: Hours

Enter the hour reading for this equipment at the time this work order was completed/closed. This value should be based on the current reading for the equipment, not the total reading (current + replaced).

-  You should not need to enter a value here if you are only updating the PR Co, mechanic, or repair type.

- The hours entered here cannot exceed the Total Hours reading for the equipment. If the reading is incorrect, you can update it using EM Meter Readings.

- If you enter Hours here, you will be unable to edit the hours at the work order item level.

## Work Order: Odometer

Enter the odometer reading for this equipment at the time this work order was completed/closed. This value should be based on the current reading for the equipment, not the total reading (current + replaced).

-  You should not need to enter a value here if you are only updating the PR Co, mechanic, or repair type.

- The odometer reading entered here cannot exceed the Total Odo reading for the equipment. If the reading is incorrect, you can update it using EM Meter Readings.

- If you enter an odometer reading here, you will be unable to edit the odometer reading at the work order item level.

##  WO Items: Update

 Check this box to include this work order item when updating work orders. When the Apply button is clicked, this work order item will be updated with specified changes.
Note: If you check at least one item on a work order for
 update, the Update box will be checked for the work order header as well, regardless of
 whether it was previously unchecked.
 Leave this box unchecked if you do not want to update this work order item.

##  WO Items: PR Co

 Enter the new PR Co for this work order item. Work order item will be updated once you click Apply and Save Changes buttons.
Note: Entry must be made here if you will be assigning a
 mechanic to this work order.

##  WO Items: Mechanic

 Enter the new mechanic for this work order item. Work order item will be updated once you click Apply and Save Changes buttons. Mechanic must be a valid employee (from PR Employees) for the PR company specified in the previous field.

##  WO Items: Status

 Enter the new status for this work order item. If you are closing this item, this should be a status with a status type of ‘Final’.Work order item will be updated once you click Apply and Save Changes buttons.
Note: If changing to a ‘Final’ status, you will need to
 enter the completion date in the Complete Date field (to the right).

##  WO Items: Repair Type

 Enter the new repair type for this work order item. Work order item will be updated once you click Apply and Save Changes buttons.

##  Complete Date

 This field is enabled only when you enter a status code with a ‘Final’ status type (in the Status field).
 Enter the completion date for this closed work order item. Work order item will be updated once you click Apply and Save Changes buttons.

## WO Items: Hours

This field is only enabled when the item's
 status is a 'Final' type and you have entered a date in the Complete Date
 field.
Enter the hour reading for this equipment or component at the time this work order item was completed/closed. This value should be based on the current reading for the equipment or component, not the total reading (current + replaced).

-  You should not need to enter a value here if you are only updating the PR Co, mechanic, or repair type. You will be unable to enter a value in this field if the status is something other than a ‘Final’ type.

- The hours entered here cannot exceed the Total Hours reading for the equipment (or Comp Total Hours reading if a component). If the reading is incorrect, you can update it using EM Meter Readings.

- If you entered Hours at the work order header level, you will be unable to edit the hours here.

- If you leave the hours null (blank) for a work order item and the hours are also null for the associated work order, the system will use the equipment's current hours reading. If the item is for a component, the system will use the component's current hours reading.

## WO Items: Odometer

This field is only enabled when the item's
 status is a 'Final' type and you have entered a date in the Complete Date
 field.
Enter the odometer reading for this equipment or component at the time this work order item was completed/closed. This value should be based on the current reading for the equipment or component, not the total reading (current + replaced).

-  You should not need to enter a value here if you are only updating the PR Co, mechanic, or repair type. You will be unable to enter a value in this field if the status is something other than a ‘Final’ type.

- The odometer reading entered here cannot exceed the Total Odo reading for the equipment (or Comp Total Odo reading if a component). If the reading is incorrect, you can update it using EM Meter Readings.

- If you entered mileage at the work order header level, you will be unable to edit the mileage here.

- If you leave the odometer reading null (blank) for a work order item and the odometer reading is also null for the associated work order, the system will use the equipment's current odometer reading. If the item is for a component, the system will use the component's current odometer reading.

##  WO Items: WO Item Notes

 Enter any notes pertaining to this work order item. Entry allowance is virtually unlimited.

##  WO Item Update Overrides: PR Co

 Enter the override PR Co for work order items. All selected work order items (those with the Update box checked) will be updated with this PR Co when the Apply button is clicked.
Note: Entry in this field enables the Mechanic field.

##  WO Item Update Overrides: Mechanic

 This field is only enabled once you enter an override PR company.
 Enter the override mechanic for work order items. Mechanic must be a valid employee (from PR Employees) for the PR company specified in the previous field. All selected work order items (those with the Update box checked) will be updated with this mechanic when the Apply button is clicked.

##  WO Item Update Overrides: Status

 Enter the new status for work order items. If you are closing work orders, this should be a status with a status type of ‘Final’.All selected work order items (those with the Update box checked) will be updated with this status when the Apply button is clicked.

##  WO Item Update Overrides: Repair Type

 Enter the override repair type for work order items. All selected work order items (those with the Update box checked) will be updated with this repair type when the Apply button is clicked.

##  WO Item Update Overrides: Complete Date

 This field is enabled only when you enter a status code with a ‘Final’ status type (in the Status field).
 Enter the completion date for closed work order items. All selected work order items (those with the Update box checked) will be updated with this completion date when the Apply button is clicked.

##  WO Item Update Overrides: Status

 Enter the new status for work order items. If you are closing work orders, this should be a status with a status type of ‘Final’.All selected work order items (those with the Update box checked) will be updated with this status when the Apply button is clicked.

##  Apply Overrides Option

- Work Order – Select this option to update only the work order item on which you currently have focus in the grid. Work order must have Update box checked in order for changes to be applied.

- All Selected WO's – Select this option to update all selected work orders (those with the Update box checked). Changes will be updated to work order items when the Apply button is clicked.

Note: Although changes will be applied when the Apply button
 is clicked, you must click the Save Changes button to save the changes and clear the grid.
