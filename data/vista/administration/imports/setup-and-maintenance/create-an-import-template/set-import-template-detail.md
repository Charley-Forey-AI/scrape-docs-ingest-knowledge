---
title: "Set Import Template Detail | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail"
---

# Set Import Template Detail

Use the Template Detail tab on [IM Template](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form) to format import details by record type. This tab displays all columns for the record type(s) specified on the Record Types tab. When you specify more than one record type on the Record Types tab, the Record Type column appears in the grid, which sorts by this column. Use the columns on this grid to specify how information uploads to Vista™. You can set default information, indicate each record’s location in the imported file, and set data reformatting options.
Note: The Nullable column cells are read only and indicate whether the column of your source file can be left blank or not. When the checkbox is selected, the import value can be blank and the file will still pass the validation phase. If not checked, the system requires a value (which could include a zero, for example).
See [Template Detail Samples](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/template-detail-samples) for basic information on how you might set up templates.
The following instructions detail how to set import template details.

1. Set data default options using the User Default Value , Overwrite Import Value , and/or the Use Viewpoint Default fields. For more information, see[Determining Import Defaults](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/determining-import-defaults).

1. In the Cross Reference field, enter the name of the cross reference, if necessary. For more information, see [IM Cross Reference](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-cross-reference-form). Note: If you are importing data that is incompatible with Vista™, you must add an additional identifier record to the Template Detail tab, in addition to specifying a cross-reference. For more information on adding additional identifiers, see [Adding Additional Import Identifiers](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/add-additional-import-identifiers).

1. Specify the location of the record in the imported file. If you specified the:

-  Delimited file format on the Info tab, use the Record Column field.

- Fixed Width file format, use the Beginning Position and Ending Position fields.

-  XML file format, use the XML Tag field.

- For more information, see [Setting Import File Formats](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/about-import-file-formats) or see the F1 help for each field.

1. In the Format Info field, specify the method for reformatting the data, if applicable. For more information, see the [F1 help](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form/field-definitions-im-template-form#ID-000130ee--en).

1. If this is a direct import template, check the Update Column if you want the system to update the field/column in the system with the data in the import file. Note: If you are using the “Insert and Update” or “Update Only” import options (from the Direct Import Type field), and the text file is determined to already exist in the destination table (based on fields with the Update Key box checked), the system will update the field/column with data from the text file. If you are using the Insert only import option, and the record already exists in the destination table, the system will not import the record from the text file. The system displays the Update Column and Update Key fields only for direct imports. The Update Key field is display only and indicates if the record is a key field.

1. Check the Prompt on Import box to have the system prompt the user to enter a value for this record during the import process. Note: This option is useful when you require user defaults, but the default changes for each import (e.g., Company, CM Account, PR Group, Vendor Group, etc.). If you check this box, the system displays the IM User Input Detail form during the import process (which is run using IM Import). What you enter in the Value field in IM User Input Detail overrides the text file’s value and becomes the imported value. However, this new value can be overridden by the data default options for the template. For more information, see [Determining Import Defaults](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/determining-import-defaults).

1. Save the template once you configure each record appropriately.

Related information

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)

- [Import Types](/en/vista/vista/administration/imports/setup-and-maintenance/import-types)
