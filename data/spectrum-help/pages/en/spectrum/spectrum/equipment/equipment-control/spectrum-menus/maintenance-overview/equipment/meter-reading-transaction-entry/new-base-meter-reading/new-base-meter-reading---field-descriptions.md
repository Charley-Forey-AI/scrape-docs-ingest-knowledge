---
title: "New Base Meter Reading - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry/new-base-meter-reading/new-base-meter-reading---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry/new-base-meter-reading/new-base-meter-reading---field-descriptions"
---

# New Base Meter Reading - Field Descriptions

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
When setting up a new meter for the specified equipment, you may enter a meter number that does not currently have a meter type designated in [Equipment Meters](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-meters).

Meter type
The meter type displays from the current setting in the [Equipment Meters](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-meters) screen, if one already exists, and no changes are allowed. If setting up a new meter, select a meter type from the available drop-down list.

Meter description
The meter description displays the current description from the [Equipment Meters](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-meters) screen, if one exists, and no changes are allowed. If setting up a new meter, enter a description.

Date
The date of the base reading defaults to the current Equipment Control processing date if no meter readings are present. If meter readings are present, then the date defaults to one day earlier than the earliest meter record date.
In order to allow equipment managers to enter initialization readings even after regular meter reading transactions have been recorded and the processing date has been adjusted, the software does not validate the minimum/maximum processing date in this window.
Example:
You acquire a new truck with an odometer reading of 20 KM. You want to track
 the life-to-date usage. To do this, you need to go to the [New Base Meter Reading](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry/new-base-meter-reading) window and
 enter the acquisition date and the base meter reading (20 KM). If you have
 regular maintenance scheduled for 30 KM, the life-to-date number will show
 10 KM when this maintenance comes due.

Base reading
Enter the reading that will serve as the starting point for the new meter. Enter the number that displays on the meter; only positive, whole numbers and zero are allowed. When installing a brand new meter this number should be zero. If any number other than zero displays on the meter, enter this number (this allows used equipment to be entered with a value other than zero).

Reading remarks
Enter an optional note related to the reading transaction. By default, the following text displays: "Initial base meter reading."
