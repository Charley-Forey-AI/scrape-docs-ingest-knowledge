---
title: "Equipment Tires - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-tires/equipment-tires---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-tires/equipment-tires---field-descriptions"
---

# Equipment Tires - Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Tire
Enter the tire code you want to associate with this equipment code or select
 from a list of available tire codes. You can also use the New button in the
 Search Tires window to create a new tire code.

Description
The previously entered tire description will display in this field.

Mounting info

Mount date
Enter the date the tires were mounted on the equipment, or select a date.

Meter #
Enter the meter number for this equipment tire code or select from a list of available meter numbers.

Meter reading
The meter reading is calculated for the tires and displays here. The meter reading is based on the Mount date and will display a reading for that date if it exists, and if no meter reading exists for the Mount date this field will be blank. No entry is allowed.
If a meter reading was entered in the [Meter Readings](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry/meter-readings)
 window, the software determines the change in meter between the most recent
 reading for the current month and the last meter reading dated prior to the
 beginning of the month for each of the four meters. The current month
 beginning and end dates are based on the current Equipment Control
 processing date and the fiscal calendar. The elapsed meter calculation uses
 the Meter History table, and unposted entries are disregarded.
Meter Readings with Different Meter Types or a Base
 Entry:
If the starting and ending meter readings have
 different meter types, or there is a base entry within the range of
 these two readings, then the software will look at the first record
 with a matching meter to the latest current-month reading and use this
 as the beginning value.
If any record
 between the beginning and ending date range is marked as a base
 reading, then the software computes the change in meter before and
 after the meter replacement as follows:
[
 <End meter> minus <Base>] + [End meter before base>
 minus <Begin meter>]

Properties

Current position
Enter the current position of the equipment tire (for example, left front).

Comments
Enter any additional details regarding this equipment tire.

Last rotation date
Enter the date that this equipment tire was last rotated.

Removal date
Enter the date the tire was removed from the equipment. After entering a removal date, the Status field automatically defaults to Inactive.

Status
If a new tire is being added, the status defaults to Active. If a date has been entered in the Removal date field, then the Status field automatically defaults to Inactive.

Buttons

New Warranty button
Click this button to open the [New / Edit Warranty for Equipment Tire or Component](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-components/new--edit-warranty-for-equipment-tire-or-component) window.

Meter button
Click this button to open the [Meter Readings](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry/meter-readings) window where you can enter meter readings (such as odometers) while recording tire info.
