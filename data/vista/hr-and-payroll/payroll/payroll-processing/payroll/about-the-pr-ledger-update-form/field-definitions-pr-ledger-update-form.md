---
title: "Field Definitions: PR Ledger Update Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-ledger-update-form/field-definitions-pr-ledger-update-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-ledger-update-form/field-definitions-pr-ledger-update-form"
---

# Field Definitions: PR Ledger Update Form

The following is a list of field descriptions for the PR
 Ledger Update form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  PR Group

 Enter the PR group to process.

##  Pay Period Ending Date

 Enter the pay period ending date that, when combined with the PR Group, identifies an open pay period. Initially defaults the last accessed pay period for the current user.

## Available Updates

If the pay period is open, then all update options are enabled. If the pay period is closed, only the updates that have not had a final run are enabled. Select those updates that you want to run:

- Job Cost / Equipment Usage / SM Labor Costs

- Equipment Costs

- General Ledger / Cash Management / Accumulations

Note: If you check the General Ledger/Cash Management/Accumulations option, the Job Cost/Equipment Usage option is checked automatically. GL distributions related to EM revenue breakdown require processing of EM revenue performed with the JC/EM update.

## Distribution Reports

After validation, you can preview and print distribution reports to
 examine the date before running the update. Check the Job Cost List, Equipment Revenue
 List, Equipment Cost List, General Ledger
 List, Service Management Cost List, and
 Error
 List boxes as necessary and then press either Preview or
 Print to view the report.
Note: If you have checked the Attach GL ledger update
 reports to pay period box in PR Groups, the system will attach copies of the
 distribution reports to the pay period control record for the specified group. In order for
 reports to be attached, the corresponding box must be checked in the Distribution Reports
 section of the form.

##  Posting Date

 After validating and examining the reports, you are ready to run the PR Ledger Update form. Enter the posting date and press Post to update the modules. You may want to override the posting date from today’s date to the payroll ending date to provide reporting by payroll period. When finished the modules selected in the Available Updates section are updated.
