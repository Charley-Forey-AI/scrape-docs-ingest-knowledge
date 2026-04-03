---
title: "Replace Meter - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry/replace-meter/replace-meter---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry/replace-meter/replace-meter---field-descriptions"
---

# Replace Meter - Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields
Descriptions

Batch
The operator's logon id defaults. Press Enter to accept the default, or type a batch code to identify the readings recorded at this time.

Equipment
Enter the equipment code for the equipment you want to record the initial meter reading for, or use the available drop-down list to select an equipment code.

New meter

Meter #
Select the meter number (numbers 1-4) that you want to record the initial meter reading for. Once entered, the meter description will display adjacent to this field.
Note: If using the Preventive Maintenance module, only meter #1
 transactions will flow to the Preventive Maintenance Schedule.

Meter type
The meter type displays from the current setting in the [Equipment Meters](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-meters) screen, or you can select a different meter type from the available drop-down list.

Meter description
The meter description displays the current description from the [Equipment Meters](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-meters) screen, or you can enter a different description.

Date
The date of the base reading defaults to whichever is later: the current Equipment Control processing date or one day later than the latest meter record date. You may enter a different date, but it must be later than the latest date already present in the meter tables, and you cannot change the date to the same date as that in the Old meter section of this window.

Base reading
Enter a base reading number; only positive whole numbers and zero are allowed. Enter zero to establish the replacement date with a brand new meter.

Reading remarks
Enter an optional note related to the reading transaction.

Old meter

Meter
This field displays the same meter number as specified in the New meter section of this window. No changes are allowed.

Last reading
This field displays the last meter reading and date (even if it is a future date).

Enter final reading for old meter?
This checkbox defaults to selected, and then allows you to complete the Date and Reading fields for the old meter. When this checkbox is clear, the corresponding Date and Reading fields are disabled. The number displayed in this box should be the same as the final value displayed on the old meter.
Note: This checkbox is unavailable if the last reading date from
 the meter transaction table is exactly one day earlier than the date in the
 New meter section of this window.
