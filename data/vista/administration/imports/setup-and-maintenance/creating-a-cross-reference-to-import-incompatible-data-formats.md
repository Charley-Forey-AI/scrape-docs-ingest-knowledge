---
title: "Creating a Cross Reference to Import Incompatible Data Formats | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/creating-a-cross-reference-to-import-incompatible-data-formats"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/creating-a-cross-reference-to-import-incompatible-data-formats"
---

# Creating a Cross Reference to Import Incompatible Data Formats

When importing data from a third-party system, you may find that some data formats are not compatible with Vista™ software. In this situation, you can create a cross-reference to associate the two formats during the import process.
Prior to creating a cross-reference for incompatible data formats, you will need to create an additional identifier in IM Template on the Template Detail tab. This additional identifier is associated with the identifier of the importing field and the system uses it as a temporary location/placeholder as data is imported and converted into an appropriate format for Vista software. For more information on creating an additional identifier, see [Adding Additional Import Identifiers](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/add-additional-import-identifiers).
The following instructions detail how to create a cross-reference to import incompatible data formats.

1. In the Template field, enter the name of the template that will utilize this cross-reference. Press F4 to see a list of available templates.

1. Enter the record type that the cross-reference applies to in the Record Typefield. Press F4 to see a list of record types associated with the template.

1. Enter a name for the cross-reference in the XRefName field.

1. Enter the identifier for the importing (final destination) field in the Target Identifier field. Press F4 for a list of field identifiers associated with the template (on the Template Detail tab of IM Template).

1. If you are using cross-references that were set up in the PM module, check the Use PM Import Cross Reference Values box and enter the PM template in the PM Template field.

1. On the Source Identifiers tab, in the Import Identifier field, enter the additional identifier that you created for the importing field in IM Template.

1. On the Cross References tab, enter the value that you are importing in the Import Value field. For blank (null) import values, enter [null].

1. In the Viewpoint Value field, enter the value as it should display in the Vista™. If value should display as blank (null), enter [null]. Note: If the field has multiple values associated with it, repeat steps 7 and 8 for each value. For example, you might use this option for a drop-down list field with multiple values.

1. Save the cross-reference record.

1. In IM Template, on the Template Detail tab, enter the cross-reference name from step 2 in the Cross Reference field for the import field and in the Cross Reference field for the additional identifier record that you created. Now, each time you import data with the template, the import process notes the cross-reference, locates the appropriate set of cross reference values, and uses the additional identifier record to convert the format.

Related information

- [About the IM Template Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form)

- [About the IM Cross Reference Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-cross-reference-form)

- [Creating an Import Cross Reference to Convert Data Values](/en/vista/vista/administration/imports/setup-and-maintenance/creating-an-import-cross-reference-to-convert-data-values)

- [Creating an Import Cross Reference for Multiple Data Records](/en/vista/vista/administration/imports/setup-and-maintenance/creating-an-import-cross-reference-for-multiple-data-records)

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)

- [Add Additional Import Identifiers](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/add-additional-import-identifiers)
