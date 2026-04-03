---
title: "Equipment Meters - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-meters/equipment-meters---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-meters/equipment-meters---field-descriptions"
---

# Equipment Meters - Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields
Descriptions

Meter type
Select the meter type for this equipment from the drop-down menu: Miles, Hours, Kilometers, or Usage. The Usage method adds the number of hours entered in Transaction Entry, Payroll Time Card Entry and Accounts Receivable Invoice Entry to the meter figure. This is particularly handy for those pieces of equipment that do not currently have a functional meter in use.
If meter type is set to Usage, the meter readings will then be updated through the ER, EO, and ED hours entered through Payroll. The meter reading can trigger maintenance tasks in Preventive Maintenance if the task is set-up that way, so it is possible to have hours entered through Payroll trigger when maintenance tasks are due.
To view information about meter replacement, click [Meter Replacement](/en/spectrum/spectrum/equipment/equipment-control/troubleshooting/meter-replacement).

Meter description
Enter a description for this meter. This label displays in the entry screen when recording meter readings.

Last reading
The latest meter reading for this meter displays, including future-dated entries (for example, if the processing dates have been temporarily adjusted). When multiple readings exist on the same day, the log entry date is used and readings display in log time order.

Last read date
The date associated with the most recent meter reading for each of the four meters displays.

Month-to-date
This row displays the change in the meter readings between the most recent reading for the current month and the last meter reading dated prior to the beginning of the month for each of the four meters. The current month beginning and end dates are based on the current Equipment Control processing date and the fiscal calendar.
Note Regarding Meter Readings with Different Meter Types or a Base Entry:
If the starting and ending meter readings have different meter types, or there is a base entry within the range of these two readings, then the software will look at the first meter history record with a matching meter to the latest current-month reading and use this as the beginning value.
If any record between the beginning and ending date range is marked as a base reading, then the software computes the change in meter before and after the meter replacement as follows:
[ <End meter> minus <Base>] + [End meter before base> minus <Begin meter>]

Year-to-date
This row displays the change in the meter readings between the most recent reading for the current fiscal year and the last meter reading dated in the prior fiscal year for each of the four meters.

Life-to-date
The life-to-date value is equal to the meter reading of the current period unless any base readings are present for the meter or more than one meter type was used. If meter readings are present, then the date of the base reading defaults to one day earlier than the earliest meter record date. See the note below for these calculations.
Example:
You acquire a new truck with an odometer reading of 20 KM. You want to track the life-to-date usage. To do this, you need to go to the [New Base Meter Reading](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry/new-base-meter-reading) window and enter the acquisition date and the base meter reading (20 KM). If you have regular maintenance scheduled for 30 KM, the life-to-date number will show 10 KM when this maintenance comes due.
Note Regarding Meter Readings with Different Meter Types or a Base Entry:
If the starting and ending meter readings have different meter types, or there is a base entry within the range of these two readings, then the software will look at the first record with a matching meter to the latest current-month reading and use this as the beginning value.
If any record between the beginning and ending date range is marked as a base reading, then the software computes the change in meter before and after the meter replacement as follows:
[ <End meter> minus <Base>] + [End meter before base> minus <Begin meter>]

Meter base
This displays the latest meter reading marked as a base reading for each of the four meters, including future date entries (for example, if the processing dates have been temporarily adjusted).

In service date
This field displays the date associated with the latest base reading that was entered for the current meter. This is NOT the Equipment in service date (although the Equipment in-service and the meter could often match).
