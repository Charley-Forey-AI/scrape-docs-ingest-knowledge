---
title: "Field Definitions: PM VFE Auto Import Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-the-pm-vfe-auto-import-form/field-definitions-pm-vfe-auto-import-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-the-pm-vfe-auto-import-form/field-definitions-pm-vfe-auto-import-form"
---

# Field Definitions: PM VFE Auto Import Form

The following is a list of field descriptions for the PM VFE
 Auto Import form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

The Project field in the PM VFE Auto Import form
If you open the VFE Auto Imports form within
 the

- PM Import Estimates form, select a project that the import applies
 to. Press F4 to select from a list of projects.

- PM Projects form, the project in context defaults and this field is
 read-only.

## Template

The Template field on the PM VFE Auto Import form
 If a selection is made in the Default VFE Estimate
 Template field in the PM Company Parameters form, it defaults here. You can
 override this to specify a different template (from PM Templates) to use for importing
 third-party data.

## Import File

 The Import File field in the PM VFE Import Form
 Enter the text file to import. You can either
 enter the file manually, making sure to include the entire path, or use the Browse button
 to locate and select the file.

## Import ID

 The Import ID field in the PM VFE Auto Import form
You can override the default import ID that is created for you, up to 10 characters. Make note of this value; you can use it to retrieve this import to review or in case there are errors.

Related information

- [Auto Importing Estimates from Third-Party Applications](/en/vista/vista/project-management/import-project-estimates/auto-importing-estimates-from-third-party-applications)

## Enter Default Retainage Percentage

 The Enter Default Retainage Percentage field in the PM VFE Auto Import form
Enter the retainage percent you want assigned to contract items and subcontract detail, if applicable. The percentage specified here will be used to calculate retainage for contract items and subcontract detail once data is interfaced to accounting.

## Auto Upload

 The Auto Upload checkbox in the PM VFE Auto Import form
If you check this box, the imported file will upload automatically and immediately after import if no data errors are detected. If unchecked, even error-free import processes will stop after the import step and you will need to manually prompt the upload process.

Related information

- [Auto Importing Estimates from Third-Party Applications](/en/vista/vista/project-management/import-project-estimates/auto-importing-estimates-from-third-party-applications)

## Retain Work Edit

The Retain Work Edit checkbox in the PM VFE Auto Import form
If you select this box, the Work Edit will be saved for auto imports whether they are successfully uploaded or not.
If you do not select this box, then the Work Edit will be

- discarded upon successful import and upload

- retained if data errors are detected in the import file.
