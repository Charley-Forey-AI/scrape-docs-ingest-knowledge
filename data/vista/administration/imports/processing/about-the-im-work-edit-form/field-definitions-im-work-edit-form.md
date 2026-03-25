---
title: "Field Definitions: IM Work Edit Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/processing/about-the-im-work-edit-form/field-definitions-im-work-edit-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/processing/about-the-im-work-edit-form/field-definitions-im-work-edit-form"
---

# Field Definitions: IM Work Edit Form

The following is a list of field descriptions for the IM Work
 Edit form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Column Name

 This field defaults the column name assigned to this field in the destination file; it cannot be changed.

##  Identifier

 This field defaults the number assigned to identify this field in the destination file; it cannot be changed.

## Import ID

Import ID field in the IM Work Edit form.
Specify the ID number of the import work file
 to edit. This field defaults the last-used import ID. Press F4 for a list
 of valid Import IDs.

##  Imported Value

 Defaults the value for this field as defined in the import text file.

##  Record Seq

 This number identifies each record in the work file.
 Specify the sequence number of the record to edit. Use the arrow buttons to scroll through the records.

## Record Type

Record Type field in the IM Work Edit form.
For single-file imports, this field defaults the record type for the template.
For multiple file imports, specify the record type to edit.

## Upload Value

Defaults to the value that will be uploaded to the destination file; the value may be overridden.
Note: If the "Update all Record Sequences" option is checked (IM Work Edit, Records menu), any changes to this value automatically updates all existing record sequences for this Import ID/Record Type/Import Template/Identifier. If record sequences should not be updated automatically, uncheck the option before making any changes to an upload value.
Note: If the value in this field represents the customer sort name, and the text file contains more than one record where the first 15 characters of the customer name is the same, the sort name will default as follows:

- the first record will retain the 15-character adaptation of the customer name (in all caps)

- subsequent records will default a 15-character sort name with the customer number appended to the end

For example:
Customer Name
Customer Number
Upload Value

Bragg Construction East
3525
BRAGG CONSTRUCT

Bragg Construction West
3526
BRAGG CONSTRUCT3526
