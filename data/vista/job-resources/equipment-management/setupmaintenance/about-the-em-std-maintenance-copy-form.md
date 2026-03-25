---
title: "About the EM Std Maintenance Copy Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-std-maintenance-copy-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-std-maintenance-copy-form"
---

# About the EM Std Maintenance Copy Form

Use this form to copy maintenance groups from one piece of equipment to another.
Click the Copy button on the EM Standard
 Main Groups form to open this form.
If several pieces of equipment have identical or similar tasks, you can set up a standard maintenance group for one piece of equipment, and then copy it to another piece of equipment or an entire category of equipment.
Maintenance groups are set up at the equipment level so that you can accurately track the Last Done dates and meter readings. If you want maintenance handled at the category level, you can only do so by copying the equipment’s maintenance group(s) to a category of equipment.
When copying maintenance groups, you can specify whether to add new items/part or replace existing ones. If you select the Add New Items/Parts Onlyoption, the copy process will skip the existing maintenance items and/or parts and add only those items and/or parts that do not already exist for the destination category/equipment. If you select the Replace Existing Items/Parts option, the system will update all existing maintenance items and/or parts for the destination category/equipment with new information, and add items and/or parts that do not already exist.
The Save Last Done Meter Data box,
 when checked, will save the last done hours, gallons, miles, and date when copying
 maintenance groups/items to the destination equipment/category. However, the system
 saves ‘last done’ data for replaced maintenance items only. For all new items, the
 meter data defaults as null.
Note: The copy process will skip equipment flagged as ‘inactive’.
If notes (header and/or item) exist for the source equipment/maintenance group, the system will copy them to the destination equipment/category as follows:

- If the maintenance group does not already exist for the destination equipment/category, the system will copy both the header and item notes.

- If the maintenance group already exists for the destination equipment/category and you select the Add New Items/Parts Only option, the system will skip changes/additions to header and/or item notes and copy only those notes entered for new items.

- If the maintenance group already exists for the destination equipment/category and you select the Replace Existing Items/Partsoption, the system will skip changes/additions to header notes; however it will copy changes/additions to existing item notes, as well as notes entered for new items.

Once you have completed copying a maintenance groups, you can modify the information as necessary in EM Standard Maintenance Groups.
