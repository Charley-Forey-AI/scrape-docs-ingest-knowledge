---
title: "About the EM Work Order Item Update Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-item-update-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-item-update-form"
---

# About the EM Work Order Item Update Form

Use this form to update all items on a specified work order with the same detail.
Access this form by clicking the Update
 All button in EM Work Order Update.

## Update All WO Items

Use this section to specify what information to
 update to all items on the work order. You can
 update the mechanic, repair type, and status code.
 If you update the status and select a 'final'
 status code (one with Status Type of
 Final in PM Status Codes), you can also
 update the completion date, current odometer, and
 current hours. For work order items associated
 with scheduled maintenance, the completion date
 and meter readings at completion time will update
 the Last Done Hours and/or Miles
 fields in EM Standard Maintenance Groups. The
 system compares this completion data against the
 equipment’s actual meter to create the scheduled
 maintenance reports.
Note: If a work order contains a mix of items with
 and without components, the screen displays the
 following message below the Curr Hours
 field:

Mixed WO Items. Cannot update Equipment and
 Component Meters
Although the system will allow entering a final
 status and completion date, both the Curr Odo and
 Curr Hours fields will be disabled.

## Odometer and Hour Meter
 Readings

When changing the current odometer and/or hour
 meter readings for an item flagged with a ‘final’
 status, you will generally enter values equal to
 or less than the equipment's current readings.
 However, if you enter a value that exceeds the
 current readings on file for the Equipment, you
 will receive a warning. The system will allow the
 entry; however, to prevent discrepancies, you
 should run EM Meter Readings to update the
 equipment's hour meter accordingly.Note: Updates
 to the hour meter and/or odometer in this form
 will only update the last done hours and/or miles
 (respectively) in EM Standard Maintenance Groups
 for each equipment/maintenance group/item; they do
 not update the Hour Meter or Odometer readings in
 EM Equipment.
Note: To update the current
 readings on file for the equipment, use the EM
 Meter Readings form (which you can access by
 clicking the Meters button above). For information
 about updating meter readings, see Meters in
 Related Topics below.

Once you have entered the necessary data, click
 the Update All button to update all items
 with the new information. Close the form to return
 to the EM Work Order Update form.Note: To clear
 data and start over, click the Clear All
 button.
