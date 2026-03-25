---
title: "Add Additional Import Identifiers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/add-additional-import-identifiers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/add-additional-import-identifiers"
---

# Add Additional Import Identifiers

Each field on the Template Detail tab (IM Template) is associated with an identifier. This is a unique number that identifies each field.
You may need to add additional identifiers to an import template if you are importing data that is incompatible with Vista™ or you need to associate multiple fields in the data file with a single field in the system. Additional identifiers facilitate cross-referencing data records, and the system uses them to represent the incompatible record from the data file, and then cross-references it with the identifier associated with the importing field in the system. Prior to adding a cross-reference, you must create any applicable additional identifiers. For more information on creating cross-references, see [IM Cross Reference](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-cross-reference-form).
To add additional identifiers to an import template to facilitate cross references

1. On the Template Detail tab of IM Template, enter the record type for the field in the Record Type field. Press F4 to see a list of record types specified for the template.

1. Enter an identifier number in the Identifier  field. Enter N , New , or + to have the system select the next available number. Note: When adding an additional identifier, the number must be 1000 or greater to differentiate additional identifiers from standard system fields.

1. Configure the rest of the fields in the grid, as appropriate. For more information, see [Setting Import Template Detail](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail). Note: You will not enter anything in the Cross Reference field until step 5.

1. Create the cross reference in [IM Cross Reference](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-cross-reference-form).

1. Enter the cross reference name in the Cross Reference column for the importing field, as well as the Cross Reference field for the additional identifier(s).

When you run the import process, the system will use the additional identifier as a placeholder to help convert the incompatible data format to the Viewpoint format, or associate multiple data records in the imported file with a single Viewpoint field.
You may need to add a Record Key identifier to enable the template to import documents that will become attached to their related data records during the import process.
If you want to import documents along with the data records in your data file, the template you are using must have a RecordKey identifier. If the template does not have one, you must add it. For more information about importing documents along with their data records, see the [Delimited File Format](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/about-import-file-formats) section of [Setting Import File Formats](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/about-import-file-formats).
To add a RecordKey identifier to an import template to facilitate importing attached documents

1. On the Template Detail tab of IM Template, enter an identifier number in the Identifier  field. Enter N , New , or  +  to have the system select the next available number. Note: When adding an additional identifier, the number must be 1000 or greater to differentiate additional identifiers from standard system fields.

1. In the Description field, enter 'RecordKey'.

1. Configure the rest of the fields in the grid, as appropriate. For more information, see [Setting Import Template Detail](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail).

Related information

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)

- [Create an Import Template](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template)

- [Set Import Template Detail](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail)

- [Creating a Cross Reference to Import Incompatible Data Formats](/en/vista/vista/administration/imports/setup-and-maintenance/creating-a-cross-reference-to-import-incompatible-data-formats)

- [Creating an Import Cross Reference for Multiple Data Records](/en/vista/vista/administration/imports/setup-and-maintenance/creating-an-import-cross-reference-for-multiple-data-records)

- [About the IM Template Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form)

- [About the IM Cross Reference Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-cross-reference-form)
