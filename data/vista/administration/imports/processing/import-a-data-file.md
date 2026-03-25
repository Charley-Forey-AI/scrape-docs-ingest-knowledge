---
title: "Import a Data File | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/processing/import-a-data-file"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/processing/import-a-data-file"
---

# Import a Data File

You can import a data file so that you can upload the data into a related Vista™ form.
When you import data, the system creates a temporary work file for transferring data from third-party software packages into a limited set of Vista software data files. You can edit the work file as needed before you upload your data into Vista. For more information, see [IM Work Edit](/en/vista/vista/administration/imports/processing/about-the-im-work-edit-form).
Pre-requisites: You must have an import template set up for the type of data you are importing. For more information, see [IM Template](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form).
The following instructions explain how to import a data file. For more information on specific fields, refer to F1 (field) help.

1. In the ImportID field, enter a unique ID number to identify this import.

1. In the Template field, enter the import template or press F4 to select from a list of valid import templates.Note: It is important that the specified template is appropriate for the type of data being imported. For more information, see [IM Template](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form).

1. In the Import File field, enter the location of the data file.

1. (Optional) In the Starting Line Number field, enter the starting line number or accept the default value. For more information, see [Starting Line Number](/en/vista/vista/administration/imports/processing/about-the-im-import-form/field-definitions-im-import-form#ID-000133cb--en).

1. Click Execute to begin the import process. As data is loaded into the work file, the Import Results box displays progress information. If the import process encounters any errors, a message displays describing the error and the import process is aborted. You must correct any errors before resuming and completing the import.
Note:About Validation LevelsThe import process doesn't apply the same level of validation as when you enter data manually. As an example, when you enter records in the MS Ticket Entry form, a warning appears if the amount entered is greater than the customer's credit limit. During the import process, such warnings do not appear.
