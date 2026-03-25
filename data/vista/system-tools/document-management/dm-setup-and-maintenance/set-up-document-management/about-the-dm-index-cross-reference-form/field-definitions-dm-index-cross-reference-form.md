---
title: "Field Definitions: DM Index Cross Reference Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/about-the-dm-index-cross-reference-form/field-definitions-dm-index-cross-reference-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/about-the-dm-index-cross-reference-form/field-definitions-dm-index-cross-reference-form"
---

# Field Definitions: DM Index Cross Reference Form

The following is a list of field descriptions for the DM
 Index Cross Reference form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Master Column Name

Specify the column name (from DM Attachment
 Index) for which to set up cross-references. Press F4 for a list of all columns contained in
 DM Attachment Index.

## Module

Enter the module or press F4 to select it
 from a list.
You will typically set up cross-references at this level when the master column name (specified above) applies to multiple modules and forms, but the related table column names differ from the master column name. For example, master column JCContractItem applies to the Item column in AR, JC, JB, and PM forms. So cross-references are set up at the module level for AR, JC, JB, and PM.

## Form

Specify the form to which the column name indicated to the right applies. For example, master column PMSMPItem applies to several forms: PM Submittal Entry, PM Meeting Minutes, PMPunchList, and PMPunchListDetail. In this case, the PMSMPItem column has multiple meanings; that is, it represents the submittal item, meeting minute item, or punch list item. Therefore, cross-references to PMSMPItem are set up for the PMSubmittal, PMMeetingMinutes, PMPunchList, and PMPunchListDetail forms.

## Column Name

Enter the column name of the field you are cross-referencing. Up to 30 characters allowed, with no spaces. If you do not know the column name for a field, access the field in the related form, press
 F3
 to open the Properties window, and locate the
 Column Name
 text box. Make sure you type the column name exactly as it is shown.
Note: Pre-defined cross-references (for standard fields) are provided by Viewpoint. You should only need to set up cross-references for user-defined fields.

##  Description

 Enter a description of the cross-reference, up to 30 characters. For example, you might indicate what form the field is associated with. So if the cross-reference is for a field in AP Transaction Entry, the description might be 'from AP Transaction Entry'.

##  Custom

 Display only. Indicates whether this is a user-defined field.

## Skip Index

Check this box to specify an exception to the index cross reference. When this box is checked, the system will not include this column during index creation for the Master Column.
