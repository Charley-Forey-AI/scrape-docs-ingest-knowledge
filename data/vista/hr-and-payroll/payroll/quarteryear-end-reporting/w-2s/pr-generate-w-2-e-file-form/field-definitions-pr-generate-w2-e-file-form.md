---
title: "Field Definitions: PR Generate W2 e-File Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/pr-generate-w-2-e-file-form/field-definitions-pr-generate-w2-e-file-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/pr-generate-w-2-e-file-form/field-definitions-pr-generate-w2-e-file-form"
---

# Field Definitions: PR Generate W2 e-File Form

The following is a list of field descriptions for the PR Generate W2
 e-File form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Tax Year

The Tax Year field on the PR Generate W-2 e-File form.

 Enter the tax year for which to generate the Federal W2 electronic file.

## Third Party Income Tax Withholding

The Third Party Income Tax Withholding field on the PR Generate W-2 e-File form.

If any of your employees received sick pay from an insurance company or other third party and the third party notified you of the amount of the sick pay, you may need to report the information on employee W-2s.
Enter the total federal income tax withheld by third parties from sick or disability payments made to your employees.

## State Filter

The State Filter field on the PR Generate W-2 e-File form.

Only use this field if you want to filter the records in the e-file by state or local code.
Specify the state by which to filter employees included in the e-file or press F4 to select from a list of valid HQ states. Only employees with an entry for this state will be included in the e-file.
 To generate the e-file, select Export. The system generates a filename using a combination of the following:
 <4-digit tax year>efw2co<3-digit company #><state>
For example, for tax year 2022, company 33, and state of Oregon, the resulting filename would be: 2022efw2co033OR.txt
Note: Entry in this field is required if you are filtering by Local Code.

##  Local Code Filter

The Local Code Filter field on the PR Generate W-2 e-File form.

Only use this field if you want to filter the records in the e-file by local code. Entry in this requires that you also enter a state in the State Filter field.
Specify the local code by which to filter employees included in the electronic media file. Press F4 to select from a list of valid local codes for the state specified in the State Filter field. Only employees with an entry for the specified state/local code will be included in the export file.
To generate the e-file, click Export. The system generates a filename using a combination of the following:
 <4-digit tax year>efw2co<3-digit company #><state><local code>
For example, for tax year 2022, company 33, state of Oregon, and local code of MultCo, the resulting filename would be: 2022efw2co033ORMultCo.txt.
