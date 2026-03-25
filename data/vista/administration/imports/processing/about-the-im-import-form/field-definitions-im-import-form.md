---
title: "Field Definitions: IM Import Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/processing/about-the-im-import-form/field-definitions-im-import-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/processing/about-the-im-import-form/field-definitions-im-import-form"
---

# Field Definitions: IM Import Form

The following is a list of field descriptions for the IM
 Import form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Import File

 Enter the folder location of the data file.

## ImportID

 Enter the Import ID, up to 20 characters. This identification number (or code) is used to separate different import files from each other. This field defaults to the last active import ID.

## Template

 Specify the template that will be used to import the data file. Make sure to select a template that is appropriate for the data file being imported. This field defaults to the last active template.

## Starting Line Number

The Starting Line Number field in the IM Import form.
If this field is left blank, the import will start at the first line in the import file.
To start this import at a particular line number in the import file, specify that number here (must be greater than 0). For example, you might use this feature if you want the import to skip header rows or bad data in the import file.
If you specified a Starting Line Number for the template in IM Template, that number defaults here. You can override the default as needed; the system uses the value in this field to determine the starting line number during the import process. If this field is blank, the import starts at Line 1.

Related information

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)

- [About the IM Import Form](/en/vista/vista/administration/imports/processing/about-the-im-import-form)

- [About the IM Template Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form)
