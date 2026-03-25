---
title: "Creating an Import Cross Reference to Convert Data Values | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/creating-an-import-cross-reference-to-convert-data-values"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/creating-an-import-cross-reference-to-convert-data-values"
---

# Creating an Import Cross Reference to Convert Data Values

The following instructions detail how to create an import cross reference to convert data values.
The most common reason for creating import cross-references is to convert data values during the import process. For example, if you are importing MS ticket details and the third-party system’s Hauler Type field has 3 import options (O, 1, and 2) you would need to correlate those options with the Vista™ hauler types (E, H, or N). To create cross-reference for converting data values, use IM Cross Reference.

1. In the Template field, enter the name of the template that will utilize this cross-reference. Press F4 to see a list of available templates.

1. Enter the record type that the cross-reference applies to in the Record Typefield. Press F4 to see a list of record types associated with the template.

1. Enter a name for the cross-reference in the XRefName field.

1. Enter the identifier for the importing field in the Target Identifier field. Press F4 for a list of field identifiers associated with the template (on the Template Detail tab of IM Template).

1. If you are using cross-references that were set up in the PM module, check the Use PM Import Cross Reference Values box and enter the PM template in the PM Template field.

1. On the Source Identifiers tab, enter the identifier associated with the importing field. This is the same number as the one you entered in the Target Identifier field.

1. On the Cross References tab, enter the value that you are importing in the Import Value field. For blank (null) import values, enter [null].

1. In the Viewpoint Value field, enter the value as it should display in Vista™. If value should display as blank (null), enter [null]. Note: If the field has multiple values associated with it, repeat steps 7 and 8 for each value. For example, you might use this option for a drop-down list field with multiple values (e.g., an ECM field).

1. Save the cross-reference record.

1. In IM Template, on the Template Detail tab, enter the cross-reference name from step 2 in the Cross Reference field for the importing field. Now, each time you import data with the template, the import process notes the cross-reference and uses it to locate the appropriate set of cross-reference values.

Related information

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)

- [About the IM Cross Reference Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-cross-reference-form)

- [Creating a Cross Reference to Import Incompatible Data Formats](/en/vista/vista/administration/imports/setup-and-maintenance/creating-a-cross-reference-to-import-incompatible-data-formats)

- [Creating an Import Cross Reference for Multiple Data Records](/en/vista/vista/administration/imports/setup-and-maintenance/creating-an-import-cross-reference-for-multiple-data-records)
