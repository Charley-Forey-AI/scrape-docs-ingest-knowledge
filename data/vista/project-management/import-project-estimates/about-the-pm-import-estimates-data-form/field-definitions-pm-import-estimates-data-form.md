---
title: "Field Definitions: PM Import Estimates Data Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-data-form/field-definitions-pm-import-estimates-data-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-data-form/field-definitions-pm-import-estimates-data-form"
---

# Field Definitions: PM Import Estimates Data Form

The following is a list of field descriptions for the PM
 Import Estimates Data form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Template

 Specify the template (from PM Templates) to
 use for importing third-party data.

##  Import File 1

 Enter the text file to import. You can either enter the file manually, making sure to include the entire path, or use the Browse button to locate and select the file.

##  Import File 2

 Enter the second text file to import. You will only need to enter a file here if the import template you specified (above) uses the HCSS import routine. The HCSS routine uses an older format that requires the entry of two text files: one for item, phase, and cost type records, and one for subcontract and material records. It is important to note that a newer routine, HCSSHeavy, is available and replaces the older HCSS routine. The new routine does not require two text files; all data is contained in one text file.

##  Import ID

 Enter the import ID, up to 10 characters. If you enter an existing import ID, a warning is displayed to the right notifying you of the date and time the file was last used, and that all data in the work file will be replaced. You will not be given a Yes/No option to this warning, so if you do not wish to overwrite existing data, use a different import ID.
[](/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-data-form/field-definitions-pm-import-estimates-data-form#ID-00027a96--en)Import

## Import

Click this button to start the import process. Once the import process is complete, a message displays showing the total item, phase, cost type, material, and subcontract records imported, along with any errors found. If errors were found, you will need to use the PM Import Edit program (Edit Work Tables button) to correct the errors before uploading your data. If no errors were found, you can upload your data without having to review the work files. However, it is recommended that you review your import data to ensure your data is correct.

## Enter Default Retainage Percentage

 The Enter Default Retainage Percentage field in the PM Import Estimates Data form
Enter the retainage percent you want assigned to contract items and subcontract detail, if applicable. The percentage specified here will be used to calculate retainage for contract items and subcontract detail once data is interfaced to accounting.
