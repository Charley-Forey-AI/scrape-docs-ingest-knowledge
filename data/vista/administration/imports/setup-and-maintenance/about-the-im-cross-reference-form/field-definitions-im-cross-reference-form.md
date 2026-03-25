---
title: "Field Definitions: IM Cross Reference Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-cross-reference-form/field-definitions-im-cross-reference-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-cross-reference-form/field-definitions-im-cross-reference-form"
---

# Field Definitions: IM Cross Reference Form

The following is a list of field descriptions for the IM
 Cross Reference form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Template

 Enter the template for setting up the cross-reference names. Press F4 for a list of valid templates created in IM Template.

## Record Type

Record Type field in the IM Cross Reference form.
Enter the record type for this cross-reference name. Press F4 for a list of valid record types set up for the specified template.

##  XRefName

 Enter the cross-reference name, up to 10 characters. The import process uses this name to locate cross reference values for the import data file and will be linked to identifiers on the Template Detail tab of IM Template.

##  Target Identifier

Specify the target field identifier for the
 importing field. Press F4 for a list of valid target identifiers. The target identifier is
 where the resulting Viewpoint Value is stored during the import.

##  Use PM Import Cross References Values

 Check this box to use cross templates that have already been set-up in PM Import Menu. This eliminates the need to configure an import in multiple places.

##  PM Template

Available if the Use PM Import Cross
 Reference Values checkbox is selected and there are applicable templates
 set up in the PM Import Menu.
Enter the PM template that already have the cross referencing established. Press F4 for a list of valid PM templates.

##  Import Identifier

Enter the import field identifier. Press
 F4
 for a list of identifiers.
When converting data values during the import,
 enter the identifier that you entered in the Target Identifier field on the Info
 tab.
When importing incompatible data formats, or linking multiple fields in the import data file with a single Vista software field, enter the additional identifiers that you created. For more information, see [Adding Additional Import Identifiers](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/add-additional-import-identifiers).

##  Import Value

 Enter the import value for this cross reference value, up to 30 characters.
 To set up a cross-reference for situations where the import process encounters a blank value, enter [null] (in lower case with brackets). When the import process encounters a blank (null) value, the system will use the specified cross-reference.

##  Viewpoint Value

Enter the Viewpoint value that will replace the import value during the import process. This must be a valid Viewpoint value, as the system validates values during the upload and when processing batches (if applicable).
To replace the import value with a null value,
 enter [null] in this field.
