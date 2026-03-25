---
title: "Auto Importing Estimates from Third-Party Applications | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/auto-importing-estimates-from-third-party-applications"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/auto-importing-estimates-from-third-party-applications"
---

# Auto Importing Estimates from Third-Party Applications

You can set up, run, and resume automated imports and uploads of estimates from third-party applications (such as MEP, ProContractor, WinEst, Quest, AccuBid, and AutoBid) using PM VFE Auto Import.

1. Access the PM VFE Auto Import form using one of the following methods:OptionDescription
From PM Projects

1. Select the active or pending project to which you are importing an estimate.

1. Select Tasks and then select the appropriate Import from Viewpoint for Estimating option.

From PM Import Estimates

1. Click on the icon (at the top of the form).

1. If you opened the PM VFE Auto Import form via PM Projects, the Project field defaults the project you selected and is disabled.If you opened the PM VFE Auto Import form via PM Import Estimates, in the Project field, enter the project to which you are importing an estimate or press F4 to select from a list of valid projects.

1. In the Template field, accept the defaulted template or enter the import template to use. Press F4 to select from a list of applicable templates.Note: If you specified a Default VFE Estimate Template in the PM Company Parameters form, this field defaults that value. May be overridden.

1. In the Import File field, enter the text file to import or use the Browse button to locate and select the file.

1. In the Import ID field, enter the import ID to use or accept the defaulted ID. If you accept the defaulted ID or enter a previously used ID, the screen displays a warning to the right of this field, indicating that the data in the work file will be replaced. If this is not what you intended, use a new ID.
Note: Whether you keep the default value or enter your own, make note of it; you will need it to retrieve this import if you need to review or in case there are errors

1. In the Enter Default Retainage Percentage field, enter the retainage percent to assign to contract items and subcontract detail, if applicable.  The percentage you specify here is used to calculate retainage for contract items and subcontract detail once data is interfaced to accounting.

1.  If you want the import process to proceed immediately and automatically with the upload, select the Auto Upload checkbox.If you do not want to auto-upload the estimate after importing, leave the Auto Upload checkbox unselected.

1.  If you want to preserve the Work Edit file for an automatically imported file, select the Retain Work Edit checkbox. If you do not select this box, the Work Edit file is discarded for successfully imported and uploaded files but retained for import files with data errors.

1.  Click Import. If you selected the Auto Upload checkbox and there are no errors, the upload completes automatically and the PM VFE Auto Import Results form displays, indicating zero errors. Otherwise, proceed to the next step.

1. Resume the import / upload.If the auto import and upload process stopped due to errors in the import or if you did not select the Auto Upload checkbox (Step 7), do the following:

1. Launch the PM Import Estimates form.

1. Click Edit Work Tables.The PM Import Estimates Edit form displays.

1. In the Import ID field, enter the Import ID you specified earlier (in Step 5).

1. Go through each tab and correct any errors (shown in red). For more information, see [About the PM Import Estimates Edit Form](/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-edit-form).

1. Save the import.

1. Click Upload to PM to complete the upload process. For more information, see [About the PM Import Estimates Upload Form](/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-upload-form).

Related information

- [About the PM VFE Auto Import Form](/en/vista/vista/project-management/import-project-estimates/about-the-pm-vfe-auto-import-form)

- [PM Import Estimates Form](/en/vista/vista/project-management/import-project-estimates/pm-import-estimates-form)

- [About the PM Import Estimates Upload Form](/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-upload-form)

- [About the PM Import Estimates Edit Form](/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-edit-form)
