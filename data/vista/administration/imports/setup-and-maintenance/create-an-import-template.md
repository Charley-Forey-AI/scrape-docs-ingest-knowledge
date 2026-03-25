---
title: "Create an Import Template | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template"
---

# Create an Import Template

If the standard Vista import templates do not meet
 the necessary criteria for importing data, use IM Template to create custom templates.
 You can create custom templates from scratch or you can copy and modify an existing
 template.
Note: It is strongly recommended that you copy a standard template
 and then modify the copy. For more information, see [Copying Import Templates](/en/vista/vista/administration/imports/setup-and-maintenance/copy-import-templates).

The following instructions explain how to create a custom
 template from scratch. You can also use these instructions to modify existing templates.
 For more information on specific fields, refer to F1 (field level) help.

1. In the
 Template field, enter a name or number for the custom
 template.

1. In the
 Description field, enter a description of the template.


1. In the Import
 Form field, enter the form to use for importing data or press
 F4 to select from a list of available forms.

1. Accept the default for the
 Import
 Routine, Upload Routine, and Viewpoint
 Routine fields.Note: If you require a different routine for any of
 the options, you must create the routine in the database and reference it in the
 appropriate field. For more information on creating database routines, speak to
 your database administrator.

1. For direct imports only
 (such as vendor imports), use the Direct Import Type drop-down to
 specify the direct import type (Insert and Update, Insert Only, or Update Only). For
 a list of direct import templates, see [Standard Import Templates](/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates).

1. If you require additional
 import functions that do not exist in the import, upload, or Viewpoint routines,
 enter a routine in the User Routine field.Note: To enter a routine in this field, you must
 first create the routine in the database.

1. In the Choose the
 format that best describes your data section, select the file format
 applicable to this template.

- Delimited

- Fixed Width

- XML

Important: If you plan to include attachments when importing data, you
 must use the Delimited file format.

1. If you selected the Delimited file format for this template, use the
 Choose the delimiter that separates your data section to
 select the appropriate delimiter. If you select Other, use the
 Other text box to specify the delimiter to use.

1. If you selected the XML file format for this template, use the XML Row
 Tag field to enter the XML tag (without the '<>' brackets) that
 determines each row (record) in the data file.

1. If the template updates more
 than one table, select the Multiple Table Upload box.

1. If you selected the
 Multiple
 Table Upload box, specify the location of the Record Type column in
 the import file.

- For delimited file formats, enter
 the column number in the Record Type Column field.


- For fixed width file formats,
 enter the beginning and ending position numbers in the  Beginning
 Position and Ending Position fields.

1. If you want the import to skip header rows or bad data in the import file, use the
 Starting Line Number field to enter the starting number.

1. Optional. If you require
 record types for this import other than the record types defaulted for the selected
 import form, use the Record Types tab to add additional record types. For more
 information, see [Setting Record Types for Import Templates](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-record-types-for-import-templates).

1. Optional. If you require
 additional template detail other than what defaults for the selected import form, use
 the Template Detail tab to set up additional identifiers. For more information, see
 [Setting Import Template Detail](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail).

1. Optional. Set up import
 notifications on the Notifications tab. For more information, see [Setting Import Notifications](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/set-import-notifications).

1. Save the template.

Related information

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)

- [Set Record Types for Import Templates](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-record-types-for-import-templates)

- [Set Import Template Detail](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail)

- [About Import File Formats](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/about-import-file-formats)

- [Set Import Notifications](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/set-import-notifications)

- [About the IM Template Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form)

- [About the IM Template Copy Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-copy-form)

- [Import Forms](/en/vista/vista/administration/imports/setup-and-maintenance/import-forms)

- [About the IM Work Edit Form](/en/vista/vista/administration/imports/processing/about-the-im-work-edit-form)
