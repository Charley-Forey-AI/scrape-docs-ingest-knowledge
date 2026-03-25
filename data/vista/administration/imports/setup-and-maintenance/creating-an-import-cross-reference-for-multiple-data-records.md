---
title: "Creating an Import Cross Reference for Multiple Data Records | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/creating-an-import-cross-reference-for-multiple-data-records"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/creating-an-import-cross-reference-for-multiple-data-records"
---

# Creating an Import Cross Reference for Multiple Data Records

In some cases, there may be fields in an import data file that do not have an equivalent field in Vista™. However, as a group, these fields may indicate a value for another field. These fields can be cross-referenced to, and populate, a field in the software.
In other words, one field in the system can cross-reference with multiple fields in the data file.
For example, a user is importing a data file into the EMBF table (the EM Cost Adjustments form). Vista™ has a Material field, but the data file does not have an equivalent field. However, the data file does have fields for Site, Hose, and Tank. While there is no equivalent field in the system for these fields, together they indicate a Material. To be specific, when the Site code is 10, the Hose code is 5, and the Tank code is 2, the material used is diesel. By setting up an additional identifier for each of these fields, the user can cross-reference the three fields to the Material field.
Note: To see a visual representation of this example, refer to the Gasboy template in the IM Template form. The Site, Hose, and Tank fields display at the bottom of the Template Detail grid as additional identifiers.
To create cross-reference, use IM Cross Reference. However, prior to creating an import cross-reference for multiple data records, you will need to create an additional identifier in IM Template on the Template Detail tab. This additional identifier is associated with the identifier of the importing field and the system uses it as a temporary location as data is imported and converted into an appropriate format for Vista software. For more information on creating an additional identifier, see [Adding Additional Import Identifiers](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/add-additional-import-identifiers).
The following instructions explain how to create a cross-reference for multiple data records. For more information on specific fields, refer to the F1 (field) help.

1. In the Template field, enter the name of the template that will utilize this cross-reference. Press F4 to see a list of available templates.

1. Enter the record type that the cross-reference applies to in the Record Typefield. Press F4 to see a list of record types associated with the template.

1. Enter a name for the cross reference in the XRefName field.

1. Enter the identifier for the importing field in the Target Identifier field. Press F4 for a list of field identifiers associated with the template (on the Template Detail tab of IM Template).

1. If you are using cross-references that were set up in the PM module, check the Use PM Import Cross Reference Values box and enter the PM template in the PM Template field.

1. On the Source Identifiers tab, in the Import Identifier field, enter the additional identifiers that you created for the importing field in IM Template.

1. On the Cross Reference
 tab, enter the imported value in the Import Value field. For blank
 (null) import values, enter [null].Note: This value equals the value of each
 field linked (concatenated) together. Using the example above, “1052” would
 be entered here (where 10=Site, 5=Hose, and 2=Tank).

1. In the Viewpoint Value field, enter the value as it should display in the Vista™. If value should display as blank (null), enter [null]. Note: Using the example above, you would enter the material code for diesel here (as are set up in [HQ Materials](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form))

1. In IM Template, on the Template Detail tab, enter the cross reference name (from step 3) in the Cross Reference field for the importing field and in the Cross Reference field for the additional identifiers that you created. Now, each time you import data with the template, the import process notes the cross-reference, locates the appropriate set of cross reference values, and uses the additional identifier record to convert the multiple fields into one.

Related information

- [About the IM Template Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form)

- [About the IM Cross Reference Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-cross-reference-form)

- [Creating a Cross Reference to Import Incompatible Data Formats](/en/vista/vista/administration/imports/setup-and-maintenance/creating-a-cross-reference-to-import-incompatible-data-formats)

- [Creating an Import Cross Reference to Convert Data Values](/en/vista/vista/administration/imports/setup-and-maintenance/creating-an-import-cross-reference-to-convert-data-values)

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)
