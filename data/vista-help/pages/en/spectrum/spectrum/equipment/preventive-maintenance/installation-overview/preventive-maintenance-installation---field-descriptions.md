---
title: "Preventive Maintenance Installation - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/preventive-maintenance/installation-overview/preventive-maintenance-installation---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/equipment/preventive-maintenance/installation-overview/preventive-maintenance-installation---field-descriptions"
---

# Preventive Maintenance Installation - Field Descriptions

When the installation screen is selected for the first time, the system will beep and "CONTROL RECORD HAS NOT BEEN CREATED OK TO PROCEED" will display in the lower left corner of the screen. Once this installation screen has been completed and the information saved, the message will not appear again.
Fields
Descriptions

Scheduled P.M.

Default permanent task notes to print?
The system is prompting for a default
 setting to use during Equipment Work Order Form. If you select this checkbox,
 any task notes that have been entered will print on the equipment work order.
 If you do not select this checkbox, then no task notes will be printed. This
 is only a default setting and may be overridden each time equipment work orders
 are printed.
Equipment work orders

Require problem type code in equipment work order?
Select this checkbox to require users
 to complete the Problem
 type field on the Equipment Work Order Entry >  New/Edit Equipment Work Order - Other Info tab when recording equipment work orders; otherwise, leave this
 checkbox clear. If this field is left clear, completing the Problem type field is
 optional.
Require problem cause code in equipment work order entry?
Select this checkbox to require users
 to complete the Problem
 cause field on the Equipment Work Order Entry >  New/Edit Equipment Work Order - Other Info tab when recording equipment work orders; otherwise, leave this
 checkbox clear.
Include labor on form?
Select this checkbox to list the
 standard hours and rates for each task.
Include parts on form?
Select this checkbox to list the parts
 required for each task, if any.
Disallow work order to be closed if P.O. with outstanding quantity due is present?
Select this checkbox to prevent
 operators from setting a work order's status to Closed in Equipment Work
 Order Entry if any open purchase orders reference the work order number and the
 Qty. due field on
 that detail line is non-zero on the New/Edit Equipment Work Order - Purchases
 tab; otherwise, leave this checkbox clear.
Reset priority code when P.O. item-on-order for the work order is received?
Select this checkbox to have the
 software automatically reset the maintenance priority during P.O. Receiving if
 any open purchase order detail lines with quantity received reference the work
 order number; otherwise, leave this checkbox clear.
New priority code
Enter the maintenance priority code to
 be assigned during Purchase Order Receiving, press F4 or double click on this
 field to select from a list of available priority codes. When a valid code is
 entered, the associated icon and description display next to this field. All
 priority codes must be entered in the Priority File Maintenance screen prior to
 being used in this field.This field is only available if
 the Reset priority code when
 P.O. item-on-order for the work order is received checkbox
 is selected.
If the Reset priority code when P.O.
 item-on-order for the work order is received checkbox is
 later cleared, this field is cleared and made unavailable.

Next work order #
Enter the next maintenance work order
 number, or press Enter to leave blank and advance to the next prompt.This is the next number that will be assigned to new
 maintenance work orders. This number will be auto sequenced by the system
 when creating new maintenance work orders, either from Maintenance Work
 Order Entry screen or when selected on the Maintenance Schedule
 Report.

Inventory parts

Update Inventory Control?
Select this checkbox if you want parts
 used for service posted to Inventory Control. If you
 select this checkbox:

- The P.M. Service Performed Update will create an E
 transaction type in the Inventory Transaction file for items entered in
 the parts list.

- Entry in the Warehouse and Cost category fields in
 the [P.M. Tasks Performed Information - Field Descriptions](/en/spectrum/spectrum/equipment/preventive-maintenance/spectrum-menus/data-entry-overview/p.m.-schedule/p.m.-tasks-performed-information---field-descriptions) window will be required.

If this checkbox is left clear, then the inventory
 file will be unaffected by service performed entries.
