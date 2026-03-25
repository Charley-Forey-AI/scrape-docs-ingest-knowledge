---
title: "Field Definitions: EM Meter Reading Adjustment Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-meter-reading-adjustment-form/field-definitions-em-meter-reading-adjustment-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-meter-reading-adjustment-form/field-definitions-em-meter-reading-adjustment-form"
---

# Field Definitions: EM Meter Reading Adjustment Form

The following is a list of field descriptions for the EM
 Meter Reading Adjustment form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Equipment

Required.
Enter the equipment (from EM Equipment) for which you are making meter reading adjustments. Initially defaults the equipment selected in EM Equipment.
Note: Equipment cannot exist in an open meter reading batch.

## Select Meter Reading Type

Required.
Select the type of meter reading to adjust.

- Odometer

- Hours

- The meter reading type will always default as "Odometer" unless the equipment's current odometer reading is 0.00 and the hour meter reading is greater than 0.00.

- The grid will automatically refresh when switching between Odometer and Hours and start/end date values have been entered.

## Start/End Date

Required.
Enter the beginning and ending date in a range of dates containing the posted meter readings you wish to adjust. The grid will automatically populate with meter readings for the selected equipment/reading type that fall within the specified date range.

## Mth - Month

Enter the month (within the specified date range) by which to restrict the transactions shown in the grid. The grid will refresh to display only those transactions posted in the specified month.

## Trans

Optional.
Enter the transaction number of the meter reading you wish to change. You will only need to enter a value in this field if you are changing a single transaction.
The grid will refresh to display only the meter reading with this transaction number.
Note: The transaction number is displayed for each meter reading in the Trans column (last column in grid).

## New Meter

Used for manual entry only.
Enter the new meter reading for this transaction. New reading must be greater than the previous meter reading. You may leave this field blank if you are adjusting the new replaced meter reading only.
Note: Once you move off this field, the New Total Meter and New Difference amounts are recalculated to include the new value.

## New Replaced Meter

Used for manual entry only.
Enter the new replaced meter reading for this transaction. New reading must be greater than the previous replaced meter reading. You may leave this field blank if you are adjusting the new meter reading only.
Note: Once you move off this field, the New Total Meter and New Difference amounts are recalculated to include the new value.

## Meter Grid Update

Select whether to Delete or Recalculate meter readings.

- Delete - Select this option to delete all meter reading records shown in the grid.

Note: When you select this option, if both odometer and hour meter readings exist for the equipment, you will receive the following warning:
Warning: XX readings may not be permanently deleted because XXXX readings exist!
If the meter reading type is Odometer, XX will be Odometer and XXXX will be Hour Meter. For a meter reading type of Hours, this is reversed.

- Recalculate - Select this option to recalculate the meter readings for all records in the grid. When selected, the Meter Adjustment Type drop-down to the right is enabled, allowing you to specify the type of meter reading adjustment to apply.

## Meter Adjustment Type

This drop-down is enabled only when Meter Grid Update is set to Recalculate.
Select the type of meter reading adjustment to apply.

- 1-New Meter Reading

- 2-Adjust Meter Reading

- 3-New Replaced Meter Reading

- 4-Adjust Replaced Meter Reading

Options 1 and 3 allow you to enter the new
 meter reading in the Meter field. The new reading will be
 applied to the first entry in the grid; all subsequent entries will be adjusted
 accordingly.
Options 2 and 4 allow you to specify an
 'adjustment' amount (negative or positive) in the Meter field. The amount entered will be
 added to or subtracted from all readings in the grid.

## Meter

If you selected adjustment type 1 - New Meter Reading or 3- New Replaced Meter Reading, use this field to enter the new meter reading value. Then click the Preview button. The new reading will be applied to the first entry in the grid; all subsequent entries will be adjusted accordingly.
If you selected adjustment type 2 - Adjust Meter Reading or 4- Adjust Replaced Meter Reading, use this field to enter the adjustment amount (may be a positive or negative value). Then click the Preview button. The system will apply the adjustment amount to each reading in the grid (either adding to or subtracting from the current reading value).
Note: This field is not intended to be used with manual updates. Be aware that if you manually entered adjustments to readings in the grid and then enter a value in this field, clicking the Preview button will wipe out the existing grid values and replace them with the new recalculated values.
