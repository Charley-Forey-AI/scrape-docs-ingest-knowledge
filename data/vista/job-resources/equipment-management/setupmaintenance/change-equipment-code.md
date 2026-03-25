---
title: "Change Equipment Code | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/change-equipment-code"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/change-equipment-code"
---

# Change Equipment Code

Change the code for a piece of equipment.

1. In the Old
 Equipment field, specify the existing code. Press Tab
 or Enter to move off the field.

- The system runs a check to see if the
 code you are trying to change is already in the process of being changed by
 another user. If it is, a message displays telling you it is being changed
 and you cannot go any further. The message will also indicate the new
 equipment number and the user changing it.

- If the code is not in the process of
 being changed, the system then runs a check to determine if the equipment
 code exists in any open batches and displays a warning if it does. The Open
 Batch List displays the open batches in which the equipment exists. You must
 post all the batches before you can change the equipment’s code.

- If the equipment does not exist in any
 open batches, the Table List tab defaults and lists all tables in which the
 code exists, as well as the number of records in each table.

1. In the New
 Equipment field, enter the new equipment code. The Change button
 is enabled.

1. Click the Change button to implement the equipment code change.  The
 program will cycle through all listed tables, changing the equipment code on all
 records referencing the old equipment code. When the update is complete, a
 message displays indicating the code change is complete and giving you the
 option to change another code. Note: Although the Equipment Master table
 (EMEM) is not displayed in the Table List, it is automatically updated with
 the new equipment code.
