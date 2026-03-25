---
title: "Set Record Types for Import Templates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-record-types-for-import-templates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-record-types-for-import-templates"
---

# Set Record Types for Import
 Templates

Use the Record Types tab on [IM Template](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form) to define record types for import templates. Record types identify each type of record in the imported data file and act as an organizational tool; each record type is associated with a specific database table. For example, when importing AP invoices, the data file will likely contain header and line detail records. In this case, both header and line record types should be set up on the Record Types tab, one for each database table (APHB, APLB). For standard import templates, the record type is the database table name where the system is uploading data. However, if you add additional record types, you may use any value (e.g., “header”, “line”, etc.).
Important: Upon import, the system treats the record type that is alphabetically first as the header. If you name your header items "Header" and your line items "Lines," you will not have a problem; however, if your line items were named "Detail," your import will assume the "Detail" records are the header records because D precedes H.
When creating a new template, the system defaults record types on the Record Types tab, based on the import form you specified in the Import Form field on the Info tab. If you created this template using IM Template Copy, the template retains the record types from the original template. In both cases, you may not need to use this tab. However, if you are creating a new template or modifying a template, you may need to add additional record types on this tab.
The following instructions detail how to add a record type to the Record Types tab.

1. Enter a name for the record type in the
 RecordType
 field.

1. In the
 Form
 field, enter the name of the form that you are importing data into. The system defaults the form's associated table name in the
 TableName
 field.

1. Enter a description for the record type in the
 Description
 field.

1. Check the Skip box
 to have the system ignore records associated with this record type during the import
 process. Note: You will typically use this option when extra
 records or extraneous lines of data are in the import file. For example, if you
 were importing a file that contained header, detail, and total records, and you
 did not want to include the header and total records, you would check this box for
 the header and total records.

Related information

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)

- [Create an Import Template](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template)

- [Set Import Template Detail](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail)

- [About the IM Template Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form)
