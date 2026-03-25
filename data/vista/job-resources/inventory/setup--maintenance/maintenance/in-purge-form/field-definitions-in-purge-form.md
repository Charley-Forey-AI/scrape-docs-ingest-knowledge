---
title: "Field Definitions: IN Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/setup--maintenance/maintenance/in-purge-form/field-definitions-in-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/setup--maintenance/maintenance/in-purge-form/field-definitions-in-purge-form"
---

# Field Definitions: IN Purge Form

The following is a list of field descriptions for the IN
 Purge form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Location

 Specify the Inventory location (IN Locations) to delete.

##  Delete Options

 Indicate the purge option to use:

- Delete Location and all of its Materials - Select this option to delete the location specified above, and all of its assigned materials.

- Delete all Materials, but leave Location on file - Select this option to delete all of the materials from the location specified above, but leave the location itself on file.

- Delete a select Material from Location - Select this option to delete a specific material from the specified location.

 Eligible materials will be deleted from the Inventory Detail (INDT), Monthly Activity (INMA), Material UM (INMU), and Materials (INMT) tables. If you selected the Delete Location and all of its Materials option, entries will also be purged from the Location Company Category (INLC), Location Company Override (INLS), Location Category Override (INLO), and Location Master (INLM) tables.
Note: If not purging selected materials, the purge process will skip materials not meeting the criteria and only purge those that do. When the purge process is complete, you will receive a message indicating the number of materials purged and not purged. If purging a selected material and material does not meet criteria, a message displays indicating the reason.

##  Material

 If using the option to purge a selected material from the location specified above, enter that material here. This must be a valid material that currently exists at the specified location.

##  Notes

 Use this tab to enter any miscellaneous notes about this item. The space allowance is virtually unlimited.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.
