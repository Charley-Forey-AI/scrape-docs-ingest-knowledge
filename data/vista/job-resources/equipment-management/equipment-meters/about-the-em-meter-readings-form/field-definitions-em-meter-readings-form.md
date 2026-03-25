---
title: "Field Definitions: EM Meter Readings Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-meter-readings-form/field-definitions-em-meter-readings-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-meter-readings-form/field-definitions-em-meter-readings-form"
---

# Field Definitions: EM Meter Readings Form

The following is a list of field descriptions for the EM
 Meter Readings form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq #

 Enter the sequence number of an existing entry or enter N, New, or + to add a new sequence. The system will automatically assign the next available sequential number.

## Action

The Action drop-down on multiple forms throughout Vista.
When entering new records, this field defaults to A (Add) and cannot be accessed.
For existing records, select the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all related module files. (The delete functions in the toolbar and Records menu only delete the entry from the batch.

## Reading Date

Enter the reading date for the hour meter and/or odometer readings for this equipment. Defaults the current date (first sequence in new batch) or the date entered for the previous transaction.
 You may enter a date less than or greater than the Last Read Date; however, if date falls prior to Last Read Date, the system will only allow the entry if the reading date is greater than the meter's Previous Date and less than the Next Date.

- If the new reading date falls prior to Last Read Date, but both dates are in the same month, the system will automatically set the Next Date equal to the Last Read Date and allow the entry.

- If you enter two meter readings for a piece of equipment with the same reading date, the system will only allow the entry if one transaction has a 0.00 hour reading and an odometer reading greater than 0.00, and the other transaction has an hour reading greater than 0.00, but a 0.00 odometer reading.

- Reading dates must be less than or equal to the last day of the batch month; future reading dates are not allowed.

## Equipment

Enter an equipment code or press F4 to select
 the equipment from a list.
 The Equipment Meter Readings section at the top of the form will display the equipment meter reading information. You can also see this information using the Meters tab on the [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form) form.

## Odometer: New Reading

Enter the equipment’s new odometer
 reading. Initially defaults the last actual odometer reading for the equipment (i.e., the
 previous reading shown in the Odometer section above, under Meter Reading History). If the
 reading is null, defaults the Last Reading value from the Equipment Master section. If the
 Last Reading value is 0.00, the new reading will default as 0.00.
 If the mileage has not changed since the last meter reading, accept the default. This allows update of the new reading date to EM Equipment. If this equipment does not use an odometer, leave the default at 0.00.

- If the mileage entered here is less than the
 previous reading, you will receive a warning; however, the system will allow the
 entry. The reading will be updated to EMMR (Meter Readings), but will not update EMEM
 (Equipment).

- If you are entering a retro meter reading, the reading date and the value entered in this field must fall between the Previous Date/Reading and the Next Date/Reading.

- The Difference field (to the right)
 shows the difference between the previous reading and the new reading entered here.
 If this reading is the first reading after a replaced meter entry, the difference
 will be the new amount— this will indicate that the previous reading was done prior
 to the meter replacement.

## Hour New Reading

Enter the equipment’s new hour meter
 reading. Initially defaults the last actual hour meter reading for the equipment (i.e., the
 previous reading shown in the Hour Meter section above, under Meter Reading History). If
 the reading is null, defaults the Last Reading value from the Equipment Master section. If
 the Last Reading value is 0.00, the new reading will default as 0.00.
 If the hours have not changed since the last meter reading, accept the default. This allows update of the new reading date to EM Equipment. If this equipment does not use an hour meter, leave the default at 0.00.

- If the hours entered here are less than the previous
 reading, you will receive a warning; however, the system will allow the entry. The
 reading will be updated to EMMR (Meter Readings), but will not update EMEM
 (Equipment).

- If you are entering a retro meter reading, the reading date and the value entered in this field must fall between the Previous Date/Reading and the Next Date/Reading.

- The Difference field (to the right)
 shows the difference between the previous reading and the new reading entered here.
 If this reading is the first reading after a replaced meter entry, the difference
 will be the new amount— this will indicate that the previous reading was done prior
 to the meter replacement.
