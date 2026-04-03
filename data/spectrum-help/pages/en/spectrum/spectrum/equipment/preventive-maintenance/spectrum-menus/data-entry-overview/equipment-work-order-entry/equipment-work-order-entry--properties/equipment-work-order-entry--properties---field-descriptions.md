---
title: "Equipment Work Order Entry- Properties - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/preventive-maintenance/spectrum-menus/data-entry-overview/equipment-work-order-entry/equipment-work-order-entry--properties/equipment-work-order-entry--properties---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/equipment/preventive-maintenance/spectrum-menus/data-entry-overview/equipment-work-order-entry/equipment-work-order-entry--properties/equipment-work-order-entry--properties---field-descriptions"
---

# Equipment Work Order Entry- Properties - Field Descriptions

Use the table below when completing the fields on this
 screen.
Fields
Descriptions

Summary

Description
Enter a brief description for this
 equipment work order (for example, "Replace fan belt").
Mechanic
Enter the name of the person who is
 assigned to perform this service.
Meter number
Enter the equipment meter number for
 which the equipment meter reading will occur. Some pieces of equipment have
 multiple meters; entering a meter number in this field specifies which meters
 are associated with the equipment work order. To record multiple meter
 readings, click the Meter
 button.
Priority
Use the drop-down menu to select the
 equipment's repair priority. Once a priority code is selected, the status's
 color-coded icon and description display next to this field.Priority codes are set up and maintained using the
 Priority File Maintenance screen.

Eq. repair status
Use the drop-down menu to select the
 equipment's repair status. Once a status code is selected, the status's
 color-coded icon and description display next to this field.Status codes are set up and maintained using the Repair
 Status File Maintenance screen.

Work order status
Use the drop-down menu to select the
 work order's applicable status: Open, Finished, or Closed.
Dates/times

Order date
Enter the date that the work for the
 selected piece of equipment was requested, press F4 to select a date from the
 Date Change window, or press Enter to accept the system default of the current Preventive
 Maintenance processing date.The date in this field is
 used in the calculations for the Mean Time Before Failure Report and Mean
 Time to Repair Report.

Required date
Enter the date that the selected piece
 of equipment must be back in service. To select a date from the Date Change
 window, press F4.

Work start date
Enter the work order service date on
 which the maintenance began. To select a date from the Date Change window,
 press F4.If you use the 'set-to-now' button, the associated
 Time field will
 be set to the current system time.

Set-to-now checkboxes
The four key date fields on this screen
 offer 'set-to-now' buttons that allow you to quickly set the fields to the
 current system date when a work order is open. In addition, when you use the
 'set-to-now' feature in the Work
 start date or Work
 finish date fields, the associated Time fields will be set to
 the current system time.
Work finish date
Enter the date on which the equipment
 maintenance was completed. To select a date from the Date Change window, press
 F4.

- When a date is entered in this field, the status of
 the Work order
 status field is automatically set to Finished.

- If you use the 'set-to-now' button, the associated
 Time field
 will be set to the current system time.

Return to service
Enter the date that the selected piece
 of equipment returned to active service. To select a date from the Date Change
 window, press F4.The return to service date stops the clock on the
 equipment work order. This calculated difference between the Ordered date and the
 Return to
 service date is considered the repair time.This date is used
 in the calculations for the Historical format of the Backlog Report, the
 Mean Time Before Failure Report and the Mean Time to Repair
 Report.

Closed date
Enter the date that the work order was
 closed or press F4 to
 select a date from the Date Change window. Remember that the work order needs
 to remain open until all costs are updated.When a date is
 entered in this field, the software performs a validation to confirm that
 the operator is permitted to close the work order. A confirmation window
 opens if the work order status has not yet been changed to Closed. The window
 includes warning text if any work order details have not been set to
 Closed. When
 the operator clicks OK, the Status
 field will be set to Closed. If the operator
 clicks Cancel,
 then the date in the Closed
 date field will be removed. When a work order is closed, the
 Work finished date
 is set equal to the Closed date if not already
 set.

Classification

Problem type
Enter a problem type code for the
 selected equipment work order or press F4 or use the drop-down menu
 to select from a list of available problem type codes. When a code is
 specified, the associated description will display next to this field. If the Require problem type code in equipment work order checkbox
 on the Preventive Maintenance Installation screen is selected, then entry in
 the Problem type
 field is required. Otherwise, entry is optional.
Problem types are established and maintained on the Problem Type Code
 Maintenance screen. Typical problem types may include Engine burning oil,
 Squeaky brakes,
 Bald tires, and
 so forth.

Problem cause
Enter a problem cause code, or press
 F4 or use the
 drop-down menu to select from a list of available problem cause codes. When a
 code is specified, the associated description displays next to this field. If the Require problem cause code in equipment work order checkbox
 on the Preventive Maintenance Installation screen is selected, then entry in
 this field is required. Otherwise, entry in this field is optional
 optional.
Problem cause codes are established and
 maintained on the Problem Cause File Maintenance screen. Typical problem
 causes may include Wear and
 Tear, Equipmentmalfunction,
 Human error,
 and so forth.

From printed?
If Yes displays, the current
 work order has been printed at least once. If No displays in this field,
 the current work order has not been printed. No entry is allowed.
Entered by
The current operator code and name
 default.
Reported by
Enter the name of the person (up to 30
 alpha characters) who reported the selected equipment's problem and need for
 maintenance. Entry in this field is optional.
Contact name
Enter the name of the person (up to 30
 alpha characters) who should be contacted in case of questions regarding the
 selected equipment's maintenance. Entry in this field is optional.
