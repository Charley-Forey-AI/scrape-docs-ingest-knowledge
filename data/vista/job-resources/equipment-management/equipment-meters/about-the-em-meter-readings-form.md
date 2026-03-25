---
title: "About the EM Meter Readings Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-meter-readings-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-meter-readings-form"
---

# About the EM Meter Readings Form

Use this form to enter meter readings on equipment.


You can open this form from using the EM module
 Program folder or by clicking the Meters button in [EM Work Order Update ](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-update-form).
 The system can track both mileage (odometer)
 readings and hour meter readings on each piece of equipment; however, you will typically
 choose one or the other as appropriate to the type of equipment. Current meter readings are
 stored in the Equipment (EMEM) table and are used by the maintenance scheduling function to
 determine if equipment is due for service. A history of meter readings is also stored in the
 Meter Reading History (EMMR) table.
In addition to the current meter readings, the system can accumulate miles and hours, just as it accumulates costs. This information is useful for reporting statistics such as cost per hour and miles per gallon. The system accumulates miles automatically as you update odometer readings. Hours are accumulated from usage time cards, so they are not typically updated from meter readings; if you do not want to update hour meters (using this form), you can have the system automatically update the hour meter as you enter usage. See Automatic Hour Meter Updates section below.

- Equipment Meter Readings Info - The
 Equipment Meter Readings section (upper portion of screen) provides an informational
 display of each equipment's odometer and hour meter readings. The Meter Reading History section shows the previous date and reading
 for the equipment, as well as the next date and reading. The next date and reading
 fields display the values from a reading posted after the current transaction's reading
 date. You will only see values in these fields when posting retro meter readings for a
 piece of equipment (i.e. readings posted between two existing reading dates). The
 Equipment Master section displays the last date and reading for the equipment stored in
 EM Equipment.
Note: The Meter Reading History
 sections (hour meter and odometer) represent actual meter reading values; that is,
 readings entered directly in EM Meter Readings (having a source of "EMMeter"). When
 entering meter readings, the system defaults new reading values based on the previous
 readings shown in the Meter Reading History sections. However, if the previous readings
 are null, the system defaults the new readings from the Last Reading values (Equipment
 Master section).
 The Last Usage
 Reading section displays the last reading date and reading (updated when posting usage
 in EM, MS, and PR), as well as the usage posting source. These dates are informational
 only; they have no effect on the reading date entered for a meter reading.

- Retro Meter Readings - Meter readings are generally entered
 in equipment/reading date order. However, there can
 often be delays in receiving the data needed to enter
 readings, causing the need to enter readings for dates
 prior to the last reading date for a piece of equipment
 (retro readings). For information on how to enter retro
 meter readings, see [Retro Meter Readings](/en/vista/vista/job-resources/equipment-management/equipment-meters/retro-meter-readings#concept-3682--en__concept-3682).

- Updating the Equipment Master - The
 reading date and readings entered in this form for both the Hour Meter and
 the Odometer will update corresponding fields in EM Equipment. The
 Hour New Reading and
 Odo New Reading fields
 will automatically default the Last Reading for each meter (unless you are
 posting a retro meter reading, in which case the fields default as 0.00.
 See Retro Meter Reading section below for more information). If the mileage
 or hours have not changed since the last reading, the system will update EM
 Equipment as long as you enter a new reading date. If adding a previously
 posted transaction into the batch, updates to equipment readings will only
 occur if:

- The Reading Date is greater than the hour
 and/or odometer Date (in EM Equipment) and the hour meter and/or
 odometer Reading is not 0.00 (i.e. is an increase or decrease
 value—decrease values allow for corrections).

- The Reading Date is equal to the hour and/or
 odometer Date (in EM Equipment) and the hour meter and/or
 odometer Reading is greater than the hour meter and/or odometer
 Reading.

- Automatic Hour Meter Updates - Instead
 of regularly using this program to post hours, the system can update an
 equipment’s hour meter automatically for you based on the usage hours
 posted in EM Usage Posting or PR Timecard Entry (if usage posting allowed).
 To enable automatic updating of the hour meter, check the Update
 Hour Meter flag for the equipment in EM Revenue Rates by
 Equipment for each applicable revenue code. For example, you would want to
 update an hour meter for usage posted to daily or weekly revenue codes, but
 would probably not want the meter updated for hours posted to a standby
 revenue code.

- Manual Meter Updates - It is possible to update the odometer
 and hour meter fields directly in EM Equipment rather
 than using this form. The system will update the
 changes posted in EM Equipment to the EMMR with a
 reading date equal to the current system date.

- Posting Mileage by State - If you track
 mileage by state for IFTA (International Fuel Tax Agreement) reporting, you
 can use the EM Miles by State form, accessed by selecting File > Miles by State. Using EM Miles by State, you can enter 'on road' and 'off
 road' mileage for equipment by state. See EM Miles by State in Related
 Topics below for more information.

- Deleting Meter Readings - If you need to delete previously
 posted meter readings, you can do so; however, you will
 need to delete them in LIFO (Last In, First Out) order.
 Deleting readings out of order will result in
 inaccurate history. An alternative to deleting a meter
 reading (suggested method) is to post a correcting
 meter reading entry for the same day.Note: Regardless of which method
 you use, be aware that no updates to EM Equipment
 will occur.

Related information

- [About the EM Equipment Form](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form)

- [About the EM Miles By State/ EM Kilometers by State/EM Kilometers by Province Form](/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-miles-by-state-em-kilometers-by-stateem-kilometers-by-province-form)
