---
title: "About Meter Grid Updates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-meter-grid-updates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-meter-grid-updates"
---

# About Meter Grid Updates

If you choose the Meter Grid Update method (below grid), you
 must specify whether to Delete or Recalculate the transactions in the grid.

- Delete - Permanently deletes all meter readings in the grid. If using
 this option, make sure only the transactions you want deleted are showing in the
 grid.

Note: When using this option, you need to restrict the
 transactions shown in the grid to only those readings you really want deleted. Once you
 click the Delete Meter Readings button, the delete cannot be undone, nor can you
 retrieve the deleted readings in any other manner. If you unintentionally delete a
 reading, you will need to recreate it in EM Meter Readings.
Note: If the equipment has both Odometer and Hour meter
 readings, a message displays informing you that the reading you are trying to delete may
 not be permanently deleted because readings of the other type exist. If the Difference
 is 0.00 for the opposite reading, it will delete both readings. However, if the
 Difference is not 0.00, you will need to delete Odometer and Hour Meter
 readings separately for each transaction (using the Select Meter Reading Type
 option).

- Recalculate - If you select this option, you must then
 specify one of the following adjustment types:

- 1-New Meter Reading

- 2-Adjust Meter Reading

- 3-New Replaced Meter Reading

- 4-Adjust Replaced Meter Reading

Options 1 and 3 allow you to enter the new meter
 reading in the Meter field. The new reading will be applied to the first entry in the
 grid; all subsequent entries will be adjusted accordingly.
Options 2 and 4 allow you to specify an
 'adjustment' amount (negative or positive) in the Meter field. The amount entered will
 be added to or subtracted from all readings in the grid.
Once you have entered the new reading or
 adjustment amount, click the Preview button to review the changes—this step is highly
 recommended, since you cannot undo changes once they are implemented. While in preview
 mode, you have the option to manually make changes where necessary or to undo the
 changes and start over. Once you are sure all changes are accurate, click the Update
 Meter Readings button to update the meters as indicated.
