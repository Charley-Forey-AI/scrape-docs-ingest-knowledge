---
title: "Retro Meter Readings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/equipment-meters/retro-meter-readings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/equipment-meters/retro-meter-readings"
---

# Retro Meter Readings

Meter readings are generally entered in equipment/reading
 date order. However, there can often be delays in receiving the data needed to enter
 readings, causing the need to enter readings for dates prior to the last reading date for a
 piece of equipment (retro readings).
When entering these readings, you must enter
 a reading date greater than the meter's previous reading date and less than the meter's
 next reading date (both shown in the informational display above the tab pages). For
 example, if the previous reading date was 02/15/2010 and the next reading date is
 03/10/2010, the new reading date must be at least 02/16/2010 and no greater than
 03/09/2010.
Note: This functionality applies only to meter readings
 entered in this form.
In some cases, hours are reported more
 quickly than mileage and posted via other sources (e.g. payroll timecards). The system
 tracks odometer and hour meter readings separately, allowing you to enter end-of-month
 odometer readings after hours have already been posted in PR (i.e. the odometer's
 reading date is greater than its last reading date, but less than the hour meter's last
 reading date). This also applies to hour readings that are posted after odometer
 readings.

- If the new reading date falls prior
 to Last Read Date, but both dates are in the same month, the system will
 automatically set the Next Date equal to the Last Read Date and allow the entry.


- The transaction's reading date must
 be equal to or less than the last day of the batch month; the system does not
 allow 'future' reading dates.

- If two meter readings exist for a
 piece of equipment with the same reading date, the system will only allow the
 entry if one transaction has a 0.00 hour reading and an odometer reading greater
 than 0.00, and the other transaction has an hour reading greater than 0.00, but
 a 0.00 odometer reading (see example below).

Hour New Reading
Odo New Reading

Transaction #1
0.00
5,500.00

Transaction #2
100.00
0.00
