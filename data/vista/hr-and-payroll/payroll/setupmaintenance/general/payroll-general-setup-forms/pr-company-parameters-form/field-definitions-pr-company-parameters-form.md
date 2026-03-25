---
title: "Field Definitions: PR Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form/field-definitions-pr-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form/field-definitions-pr-company-parameters-form"
---

# Field Definitions: PR Company Parameters Form

## PR Company

PR Company field on the PR Company Parameters
 form
Enter a valid company that has already been set up as a HQ company.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## GL Co #

GL Co # field on the PR Company Parameters
 form, Info tab.
Enter the default GL company to use when
 expensing Payroll, as well as validating and posting the deductions and liabilities credits
 (as set up in PR Deductions/Liabilities) and the debits that are set up in PR
 Departments.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Journal

Journal field on the PR Company Parameters
 form, Info tab.
Enter the GL journal to use for payroll
 entries. A description of the journal displays to the right of the code.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Interface PR to GL

Interface PR to GL checkbox on the PR Company
 Parameters form, Info tab.
Select this checkbox to have payroll distributions update General Ledger. When the Ledger Interface is run, distribution entries are summarized and one entry posts to GL for each account affected per month.
Do not select this checkbox if you are not updating payroll distributions to GL.

Related information

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Update Employees from AP

Update Employees from AP field on the PR Company Parameters
 form.
If this checkbox is selected, changes to the following sections in the AP
 Vendors form are automatically updated to the corresponding employee record in the PR
 Employees form:

- Name

- Address info

- Email address

- Phone

- Direct deposit info

## CM Co #

CM Co # field on the PR Company Parameters
 form, Info tab.
Enter the Cash Management company number that will be used when interfacing payments from Payroll to Cash Management. This number is also used for CM account validation.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## AP Co #

AP Co # field on the PR Company Parameters
 form, Info tab.
Enter the Accounts Payable company number that will be used when interfacing deduction and liability amounts to AP. This number is also used for vendor group and vendor validation.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Using Automatic Overtime

Using Automatic Overtime checkbox on the PR Company Parameters form, Info tab.
Select this checkbox to have overtime calculated automatically. If using automatic overtime, timecards can be processed, and overtime entries can be generated with the PR Automatic Overtime posting form. Warnings are not displayed if an employee exceeds the standard number of hours per day or 40 hours per week.
Do not select this checkbox if you want manually
 post overtime. If you are manually posting overtime, then warnings display if an
 employee exceeds the standard number of daily or weekly hours.

Related information

- [About Setting up Automatic Overtime](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Overtime Earnings Code

Overtime field on the PR Company Parameters form, Info tab
Available only when 'Using Automatic Overtime' is checked.
 Enter the valid earnings code to use for weekly overtime calculations when posting automatic overtime earnings. This earnings code is also used as a default when setting up Level 1 hours in PR Overtime Schedule and PR Overtime Schedule by Shift.

Related information

- [About Setting up Automatic Overtime](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Audit Options

The Audit Options section on the PR Company Parameters form, Info tab.
The audit options determine when new records of changes are added to the HQ Master Audit (HQMA) database table. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. For more information about viewing audit records, see [View the Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log).

- Company Parameters – This audit option is display only and is always selected. Any additions, changes, or deletions made to PR Company Parameters are tracked in the Master Audit file.

- Accumulations – Select this checkbox to record additions, changes, and deletions to the PR Employee Accumulations form.Note: This only records manual changes/overrides made using the form. Processing updates to monthly total amounts do not result in new audit records

- Earns / Dedns / Liabs – Select this checkbox to record additions, changes, and deletions made in the PR Deductions/Liabilities and PR Earning Codes forms.

- Federal, State/Prov, and Local Tax – Select this checkbox to record additions, changes, and deletions made to Federal, State/Province, and Local tax information (PR Federal Info, PR State/Province Information, and PR Local Codes.)

- Employees – Select this checkbox to record additions, changes, and deletions to PR Employees, PR Employee Dedns/Liabs, PR Direct Deposit, and PR Automatic Earnings forms.

- Payment History – Select this checkbox to record additions, changes, and deletions to the PR Payment History form.

- Craft / Class Pay Rates – Select this checkbox to record additions, changes, and deletions made in PR Craft Class Templates, PR Craft Classes, PR Crafts, and PR Craft Templates.

- State/Prov Insurance Code – Select this checkbox to record additions, changes, and deletions made in PR State/Province Insurance Codes.

- W-2 Process (United States users only) – Select this checkbox to record additions, changes, and deletions made to the information in PR W-2 Process and PR W-2 Employee Edit.

- PAYG Process (Australian users only) – Select this checkbox to record additions, changes, and deletions made to the information in PR PAYG Summary Process and PR Employee PAYG Summaries.

- T4 Process (Canadian users only) – Select this checkbox to record additions, changes, and deletions made to the information in PR Canada T4 and PR Canada T4 Employees.

- Leave – Select this checkbox to record additions, changes, and deletions to both the Info tab and Accrual/Usage tab of both the PR Leave Codes and PR Employee Leave forms.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Attach Batch Reports to HQ Batch Control

The Attach Batch Reports to HQ Batch Control checkbox on the Company Parameters form
 for each module.
Select this check
 box to save batch (audit) reports and attach to the batch record when posting a batch.
 During the batch process, the system converts the related batch reports to a PDF file and
 attaches them to the HQ Batch Control record. The system stores the reports using the
 Attachment Storage Location and Subdirectory Structure parameters defined in DM Attachment
 Options. You can retrieve the reports later using the HQ Batch Control form (just enter the
 month and batch ID and click on the Attachments button).

- The system attempts to convert and attach batch reports before posting the batch. If the attempt is successful, the system posts the batch. However, if errors occur for any batch report, the system displays an error message and aborts the posting process. You must correct the errors before you can re-validate and post the batch.

- Because you can secure audit reports (in VA Report Security), access to attachments generated through this process is restricted to HQ Batch Control. If you have secured the HQ Batch Control form, users can only access batch reports if they have access to HQ Batch Control. Unlike regular attachments, indexes are not created for batch report attachments and you cannot access them using DM Attachment Search.

Do not select this checkbox if you do not want to save batch reports and attach them to HQ Batch Control records. Although not required, it is recommended that you print batch reports before posting the batch.

## Filing Status Alert

Filing Status Alert checkbox on the PR Company Parameters form, Info tab.
This checkbox defaults to selected.
For United States users, select this checkbox to have the system display a warning when you save edits to a record in PR Employees that does not have any data on the Filing Status tab.
Note: It is recommended that you deselect this checkbox during system implementation, and then select it when you are ready to begin processing.
For all other users, it is recommended that you deselect this checkbox.

Related information

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Timecard Stop Time must be greater than Start Time

Timecard Stop Time must be greater than Start Time checkbox on the PR Company Parameters form, Info tab.
This checkbox controls how you can enter time
 in the Start
 Time and Stop Time fields in PR Timecard Entry
 (which use a 24-hour time format.
If you have employees working a shift that begins in the evening of one day and finishing during the next (for example, 20:30 pm to 2:30 am), do not select this checkbox.
If you do not have employees starting a work shift on one day and finishing on another, select this checkbox to prevent accidental entry of a large number of hours on a timecard record.
For more information, see [Tracking Employee Start and Stop Times](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/tracking-employee-start-and-stop-times).

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Crew Timesheet Earnings Codes: Regular

Crew Timesheet Earnings Codes Regular field on
 the PR Company Parameters form, Info tab.
 Specify the earnings code to use for regular earnings when posting crew timesheets; may be overridden by crew in PR Crews.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Crew Timesheet Earnings Codes: Overtime

Crew Timesheet Earnings Codes Overtime field
 on the PR Company Parameters form, Info tab.
Specify the earnings code to use for overtime earnings when posting crew timesheets; may be overridden by crew in PR Crews.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Crew Timesheet Earnings Codes: Doubletime

Crew Timesheet Earnings Codes Doubletime field
 on the PR Company Parameters form, Info tab.
Specify the earnings code to use for double-time earnings when posting crew timesheets; may be overridden by crew in PR Crews.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## NAICS Code

NAICS Code field on the PR Company Parameters form
For Maryland payroll only.
Enter the NAICS code, up to 6 numbers long.
The entry in this field is used in the PR W-2 Process form when creating a new tax year.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## TCC

TCC field on the PR Company Parameters form, Info tab.
Enter the ACA transmitter control code, which is supplied by the IRS. This code is required for transmitting ACA 1094-C and 1095-C forms electronically and is not the same as your 1099 TCC transmitter code.

Related information

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Foreign Transmitter

Foreign Transmitter field on the PR Company Parameters form, Info tab.
Select this checkbox if this PR company is a foreign company operating in the United States.

Related information

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Payroll Program Account

Payroll Program Account field on the PR
 Company Parameters form, Info tab.
This field displays for Canadian companies only.
Required.
Enter the company's Canadian Business Number Payroll Program Account reference number. The number must begin with RP and be followed by four digits.
This field can be overridden for specific
 employees in the Payroll Program Account field in PR Employees.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Quebec File Number

Quebec File Number field on the PR Company
 Parameters form, Info tab.
This field displays for Canadian companies only.
Enter the company's Quebec File Number. The number must begin with RS and be followed by four digits.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## JC Co#

JC Co # field on the PR Company Parameters
 form, Job Cost/Service Mgmt tab.
 Enter the Job Cost company that will be used when posting job timecards.

Related information

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Allow Job Time Cards Without a Phase

The Allow Job Time Cards Without a Phase checkbox
 on the PR Company Parameters form, Job Cost/Service Mgmt tab.
Select this checkbox to allow posting timecards to a job without specifying a phase.
When you select this option, the job is not charged with the employee's time. The job is entered for reference only; this option is typically used if an
 employee is to be charged to an overhead account, but their time is required to be reported
 on a Certified Transcript for the job.
 If this is not a requirement of your company, we
 recommend leaving this checkbox unselected to avoid an inadvertent error.

Related information

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Insurance Based on Phase or SM Work Order
 Scope

The Insurance Based on Phase or SM Work Order
 Scope checkbox on the PR Company Parameters form, Job Cost/Service Mgmt tab.
 Select this checkbox to apply the insurance code
 based on the insurance template specified for the job (in JC Jobs) and the phase (job timecards) or work order scope (SM
 work order timecards) when entering timecard records in PR Timecard Entry. This checkbox
 works in conjunction with the Always use Employee's Work/Resident Insurance
 Code checkbox in PR Employees to determine how the Ins Code field
 in PR Timecard Entry defaults.
The following table displays how the
 Ins
 Code field defaults based on the settings of both checkboxes.
Insurance based on Phase/SMWO
Use Employee Insurance Code
Ins Code Default

Defaults from the Ins
 State field in PR Employees.

If you specify a job in the Job field (PR Timecard Entry), defaults from the Insurance
 Code field in JC Job Phases (if phase is an exact match). If
 no insurance code is specified for the phase in JC Job Phases, defaults from
 the Insurance Code field in JC Insurance Template. If no
 insurance code is specified for the phase in JC Insurance Template, or no
 insurance template is specified for the job, defaults from the Ins
 Code field in PR Employees.
If you do not specify a job in the Job field, defaults from the Ins
 Code field in PR Employees.
SM Work Orders:
If a job work order, defaults from the Insurance
 Code field in JC Job Phases. If no insurance code is
 specified in JC Job Phases, defaults from the Insurance
 Code field in JC Insurance Template. If no insurance code is
 specified for the phase in JC Insurance Template, or no insurance template
 is specified for the job, defaults from the Ins
 Code field in PR Employees.
If a customer work order, defaults from the
 Insurance Code field in SM Work Orders. If you do not
 specify an insurance code on the work order, defaults from the Ins
 State field in PR Employees.

Defaults from the Ins
 Code field in PR Employees.

Defaults from the Ins
 Code field in PR Employees.

Related information

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Interface Labor / Equipment / SM Work Order Costs to JC & Revenue to EM

Interface Labor / Equipment / SM Work Order Costs to JC & Revenue to EM checkbox on the PR Company Parameters form, Job Cost/Service Mgmt tab.
Select this checkbox to update job cost distributions for labor, burden, equipment, and SM work order costs to Job Cost and revenue to EM.
Do not select this checkbox if you are not updating job cost distributions for labor, burden, equipment, and SM work order costs to Job Cost or revenue to EM.

Related information

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Include in JC Detail

Include in JC Detail section on the PR Company Parameters form, Job Cost/Service Mgmt tab.
Select any of the following checkboxes to indicate what type of timecard detail is interfaced to JC. These options are generally determined by Job Billing requirements. Including craft/class, employee, earnings factor, and earnings code detail is important if you are using T & M billings that require this level of detail.
Craft / Class – Select this checkbox if
 crafts/classes are needed for billing rates instead of actual labor costs when using Time
 & Materials billings in JB.
Crew – Selecting this checkbox only affects JC detail; it has no affect on Job Billing.
Employee – Select this checkbox to interface the employee number to JC and to show timecard detail for each employee.
Use Timecard Date Instead of Pay Period Ending Date – Select this checkbox to use the timecard date as the JC transaction date, and to create at least one separate line of detail for each unique timecard date. If you have included other levels of detail, additional lines of detail may be created for each timecard date, depending on what detail you choose to include.
If you do not select this checkbox, then the pay period ending date is used and at least one summarized entry is created for the pay period ending date specified. Additional summarized lines of detail may be created depending on what other levels of detail are included.
Labor
Earnings Type – Select this checkbox to have earning types (401K, subsistence, etc.) broken out. This detail may be required for T &M billings, depending on how you bill out costs.
Earnings Factor – Select this checkbox to see overtime costs separately.
Shift – Select this checkbox to interface shift detail to Job Cost. This detail may be required for T & M billings, depending on how you bill out costs.
Burden
Liability Type – Select this checkbox to break down liability costs (for example, taxes, insurance, etc.). This detail may be required for T &M billings, depending on how you bill out costs.
Earnings Factor – Enabled only if Liability Type is checked. Select this checkbox to include earnings factor when updating burden to JC Cost Detail (JCCD). This links burden to its associated earnings.
Shift – Enabled only if Liability Type is checked. Select this checkbox to include shift when updating burden to JC Cost Detail (JCCD). This links burden to its associated earnings.
Usage
Equipment – Select this checkbox to see each piece of equipment that is used on the same job/phase separately.
Revenue Code – Select this checkbox to separate revenue codes on equipment usage. You should select this checkbox if T & M billings require equipment costing at the revenue code level. For example, a piece of equipment may be assigned a revenue code that identifies hourly rates and one that identifies standby rates.

Related information

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## SM Co #

SM Co # field on the PR Company Parameters form, Job Cost/Service Mgmt tab.
Enter the Service Management company that will
 be used when posting SM Work Order timecards in PR Timecard Entry or timesheets in PR My
 Timesheet. The company you enter here will default to the SM Co field in
 PR Timecard Entry or the SM Co field in PR My Timesheet.

Related information

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Interface Actual Labor Costs to SM

Interface Actual Labor Costs to SM checkbox on the PR Company Parameters form, Job Cost/Service Mgmt tab.
Check this box to interface actual labor costs
 to Service Management (SM) for technicians posting time to SM work orders (via Payroll or
 Service Management). When payroll is processed, the system will update the actual costs for
 each technician to the corresponding work completed labor line on the work order (in SM
 Work Orders).
Leave this box unchecked if you are not interfacing actual labor costs to SM. When payroll is processed, no updates of actual labor costs to SM will occur.

Related information

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## EM Co #

EM Co # field on the PR Company Parameters
 form, Equipment tab.
Enter the EM company that will be the default when entering equipment usage or mechanics timecards.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Enter Equipment Usage With Time Cards

Enter Equipment Usage With Time Cards checkbox on the PR Company Parameters form, Equipment tab.
Select this checkbox to allow entering equipment usage with job and service (SM work order) timecards in PR Timecard Entry. This enables the Post Equipment Usage option in PR Timecard Entry (Options menu), which must be selected before you can enter equipment usage with timecards.
 If you do not select this checkbox, equipment usage inputs will be unavailable for job and service timecards. To enter equipment usage for jobs, use [EM Usage Posting ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-usage-posting-form). To enter equipment usage for SM work orders, use [SM Work Completed Equipment](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-equipment-form).

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Include in EM Revenue Detail

Include in EM Revenue Detail section on the PR Company Parameters tab, Equipment tab
Check any of the following boxes to determine what type of timecard detail is interfaced to EM Revenue Detail.

- Employee – Select this checkbox to interface employee numbers to EM Revenue Detail and show timecard detail for each employee.

- JC Phase / CT – Select this checkbox to see timecard detail for each phase/cost type charged on the job. Job detail is always included whether you select this checkbox or not.

- Use Posting Date Instead of Pay Period Ending Date – Select this checkbox to use the timecard date as the EM Revenue Detail transaction date. When selected, at least one separate line of detail is created for each unique timecard date. If you have included other levels of detail, additional lines of detail may be created for each timecard date, depending on what detail you choose to include.

Do not select this checkbox if you want to use the pay period ending date. The system will create at least one summarized entry for the pay period ending date specified. Additional summarized lines of detail may be created depending on what other levels of detail are included.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

##  Interface Labor Costs to EM

Interface Labor Costs to EM checkbox on the PR Company Parameters form, Equipment tab.
 Select this checkbox to update payroll information (labor costs) from mechanics’ timecards to EM.
 Do not select this checkbox if you do not want payroll information (labor costs) from mechanics’ timecards updated to EM.

Related information

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Include Employee in EM Cost Detail

Include Employee in EM Cost Detail checkbox
 on the PR Company Parameters form, Equipment tab.
 Check this box if you want employee numbers included in the update to EM from mechanics’ timecards.
 Do not check this box if employee numbers will not be included when updating to EM from mechanics’ timecards.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Office State

Office State field on the PR Company
 Parameters form, State/Local tab.
If you selected the Use Job, SM Work Order or
 Office State for Tax State checkbox, enter the default tax state for
 non-job timecards. If you leave this field blank, the default in PR Timecard Entry is the
 employee's tax state (as indicated by the Work Office Tax State or Resident Tax
 State fields in PR Employees).
If you did not select the Use Job or Office State for
 Tax State checkbox, and you enter a state here, the system will check to
 see if this state has a reciprocal agreement with the employee's tax state (as indicated by
 the Work Office Tax
 State or Resident Tax State fields in PR
 Employees); the default in PR Timecard Entry is the employee's tax state.
For more information on how the system defaults the employee's tax state, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

Related information

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Office Local

Office Local field on the PR Company
 Parameters form, State/Local tab.
If you selected the Use Job, SM Work Order or
 Office Local for Local Tax checkbox, enter the default local code for
 non-job timecards. If you leave this field mblank, the default in PR Timecard Entry is the
 employee's local code (as indicated by the Work Office Local Code or Resident Local
 Code fields in PR Employees).
If you did not select the Use Job, SM Work Order or
 Office Local for Local Tax checkbox, and you enter a local code here, the
 default in PR Timecard Entry is the employee's local code.
For more information on how the system defaults the employee's local code, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

Related information

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [PR Local Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-local-codes-form)

## Use Job, SM Work Order or Office State
 for Tax State

Select this checkbox to use the job state
 (PR
 State field, JC Jobs), work order state (PR State field,
 SM Work Orders), or office state (Office State field) for the default tax
 state when entering timecards. This checkbox works in conjunction with the Always use Employee's
 Work/Resident Tax State checkbox in PR Employees to determine how the
 Tax
 State field in PR Timecard Entry defaults.
The following table displays how the
 Tax
 State field defaults based on the settings of both checkboxes.
Use Job, SM WO, or Office State
Use Employee State
Tax State Default

Defaults from the Work Office
 Tax State field in PR Employees. If blank, the system
 defaults from the Resident Tax State
 field.

If you specify a job in the Job field (PR Timecard Entry), defaults from the PR
 State field in JC Jobs. When processing payroll, the system
 checks for reciprocity with the state specified in the Work Office
 Tax State or the Resident Tax State fields
 in PR Employees.
If you do not specify a job in the Job field, defaults from the Office
 State field in PR Company Parameters. When processing
 payroll, the system checks for reciprocity with the state specified in the
 Work Office Tax State or the Resident Tax
 State fields in PR Employees.
If you do not specify a job in the Job field, and the Office State field in PR
 Company Parameters is blank, defaults from the Work Office
 Tax State field in PR Employees. If that field is blank,
 defaults from the Resident Tax State field
 in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR
 State field in JC Jobs.
If a customer work order, defaults from the
 PR State field in SM Work Orders. If you do not specify a PR
 State on the work order, defaults from the Work Office
 Tax State field in PR Employees. If that field is blank,
 defaults from the Resident Tax State field
 in PR Employees.

Defaults from the Work Office
 Tax State field in PR Employees. If that field is blank,
 defaults from the Resident Tax State field
 in PR Employees.

Defaults from the Work Office
 Tax State field in PR Employees. If that field is blank,
 defaults from the Resident Tax State field
 in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

Related information

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Use Job or SM Work Order State for
 Unemployment State

Use Job or SM Work Order State for
 Unemployment State checkbox on the PR Company Parameters form, State/Local tab.
Select this checkbox to use the job state
 (PR
 State field, JC Jobs) or work order state (PR State field, SM Work Orders)
 as the default unemployment state when entering timecards. This checkbox works in
 conjunction with the Always use Employee's Work/Resident Unemployment
 State checkbox in PR Employees to determine how the Unemp State
 field in PR Timecard Entry defaults.
The following table displays how the
 Unemp
 State field defaults based on the settings of both checkboxes.
Use Job or SM WO State
Use Employee State
Ins State Default

Defaults from the Unemp
 State field in PR Employees.

If you specify a job in the Job field (PR Timecard Entry, defaults from PR
 State field in JC Jobs.
If you do not specify a job in the Job field, defaults from the Unemp
 State field in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR
 State field in JC Jobs.
If a customer work order, defaults from the
 PR State field in SM Work Orders. If you do not specify a PR
 State on the work order, defaults from the Unemp
 State field in PR Employees.

Defaults from the Unemp
 State field in PR Employees.

Defaults from the Unemp
 State field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

Related information

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Use Job or SM Work Order State for
 Insurance State

Use Job or SM Work Order State for Insurance
 State checkbox on the PR Company Parameters form, State/Local tab.
Select this checkbox to use the job state (PR
 State field, JC Jobs) or work order state (PR State, SM Work Orders) as the default
 insurance state when entering timecards. This checkbox works in conjunction with the
 Always use
 Employee's Work/Resident Insurance State checkbox in PR Employees to
 determine how the Ins State field in PR Timecard Entry defaults.
The following table displays how the
 Unemp
 State field defaults based on the settings of both checkboxes.
Use Job or SM WO State
Use Employee State
Ins State Default

Defaults from the Ins
 State field in PR Employees

If you specify a job in the Job field (PR Timecard Entry), defaults from PR
 State field in JC Jobs.
If you do not specify a job in the Job field, defaults from the Ins
 State field in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR
 State field in JC Jobs.
If a customer work order, defaults from the
 PR State field in SM Work Orders. If you do not specify a PR
 State on the work order, defaults from the Ins
 State field in PR Employees.

Defaults from the Ins
 State field in PR Employees.

Defaults from the Ins
 State field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

Related information

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Use Job, SM Work Order or Office Local
 for Local Tax

Select this checkbox to use the job local
 code (PR Local
 Code field, JC Jobs, PR Info tab), work order local code (PR Local Code
 field, SM Work Orders), or office local code (Office Local field) for the default local
 code when entering timecards. This checkbox works in conjunction with the Always use Employee's
 Work/Resident Local Code checkbox in PR Employees to determine how the
 Local field in PR Timecard Entry defaults.
The following table displays how the
 Local field defaults based on the settings of both checkboxes.
Use Job, SM WO, or Office Local
Use Employee Local
Local Default

Defaults from the Work Office
 Local Code field in PR Employees. If blank, the system
 defaults from the Resident Local Code
 field.

If you specify a job in the Job field (PR Timecard Entry) and the PR
 Local Code field (JC Jobs) is not blank, defaults from the
 PR Local Code field in JC Jobs.
If you specify a job in the Job field, and the
 PR Local Code field (JC Jobs) is blank, the default value is the Resident
 Local Code field in the PR Employees form.
If you do not specify a job in the Job field, defaults from the Office
 Local field in the PR Company Parameters form, if it is not
 blank.
If you do not specify a job in the Job field, and the Office Local field in PR
 Company Parameters is blank, defaults from the Work Office
 Local Code field in PR Employees. If that field is blank,
 defaults from the Resident Local Code field
 in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR Local
 Code field in the JC Jobs form, if it is
 not blank. If the job's PR Local Code field is
 blank, the default
 value is the Resident Local Code
 field in the PR Employees form.
If a customer work order, defaults from the
 PR Local Code field in SM Work Orders. If you do not specify
 a PR Local Code on the work order, defaults as blank.

Defaults from the Work Office
 Local Code field in PR Employees. If that field is blank,
 defaults from the Resident Local Code field
 in PR Employees.
 If both the Work Office Local Code and
 the Resident Local Code fields in PR Employees are blank,
 defaults as blank.

Defaults from the Work Office
 Local Code field in PR Employees. If that field is blank,
 defaults from the Resident Local Code field
 in PR Employees.
 If both the Work Office Local Code and
 the Resident Local Code fields in PR Employees are blank,
 defaults as blank.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

Related information

- [PR Local Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-local-codes-form)

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Document Password Format

Document Password Format drop-down on the PR Company
 Parameters form, Report Info tab.
From the drop-down menu, select the format to use
 when auto-generating passwords for documents electronically transmitted from
 Payroll (such as pay stubs, direct deposit advice stubs, and tax documents
 (Australia only)).

- Blank - Not used.

- 1
 - Birth date YYYYMMDD and ending digits of SSN/TFN/SIN

(For single-digit months or days, the system will always include a zero in front of the month/day in the password. For example, if the birth date is 1/1/1985, the password will be 19850101, plus the ending digits of the SSN/TFN/SIN).

- 2
 - Employee number and ending digits of SSN/TFN/SIN

- 3
 - First 4 of Last Name (lowercase) and ending digits of
 SSN/TFN/SIN (If the employee's last name is four characters or less,
 the password will include the entire last name.)

During the email notification process, the system
 will automatically generate a document password for each employee based on the
 format you selected and the employee's information (from PR Employees). It will
 then embed the password in the PDF being attached to the email.
Note: This feature only applies to employees with the Method of Pay
 Stub Delivery option (in PR Employees) set to A-Email with
 attachment.

Related information

- [Set Pay Stub Attachment Options](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information/set-pay-stub-attachment-options)

- [Set Tax Document Attachment Options: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation/set-tax-document-attachment-options-australia)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

- [Method of Pay Stub Delivery](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-0003828f--en)

## Enable Non Negotiable Check Print

The Enable Non Negotiable Check Print (US) or Enable Non Negotiable Cheque Print (AU/CA) checkbox on the PR Company Parameters form, Report Info tab.

Select this checkbox if you want the option to print non-negotiable copies of checks/cheques. When you complete a check run, a message displays asking if you want to print non-negotiable copies. You can specify to print copies or exit without printing copies.
Leave this checkbox unselected if you do not want the option to print non-negotiable checks/cheques.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Exclude SSN from Checks/Direct Deposits

 The Exclude SSN from Checks/Direct Deposits (U.S.), Exclude TFN from Cheques/EFTs (AU), or Exclude SIN Number from Cheques/DirectPay (CA) checkbox on the PR Company Parameters form, Report Info tab.
United States: Exclude SSN from Checks/Direct DepositsSelect this checkbox to exclude social security numbers from payroll checks/stubs (including non-negotiable copies) and direct deposit advices.
Note: Selecting this option does not prevent social security numbers from printing on W-2s, certified reports, or other payroll reports.

Do not select this checkbox if you want to include social security numbers on payroll check/stubs and direct deposit advices.
Australia: Exclude TFN from Cheques/EFTsSelect this checkbox to exclude tax file numbers from payroll cheques/stubs (including non-negotiable copies) and direct deposit advices.
Note: Selecting this option does not prevent tax file numbers from printing on PAYG summaries, certified reports, or other payroll reports.
Do not select this checkbox if you want to include tax file numbers on payroll cheque/stubs and direct deposit advices.
Canada: Exclude SIN Number from Cheques/DirectPaySelect this checkbox to exclude social insurance numbers from payroll cheques/stubs (including non-negotiable copies) and direct deposit advices.
Note: Selecting this option does not prevent social insurance numbers from printing on T4s, certified reports, or other payroll reports.
Do not select this checkbox if you want to include social insurance numbers on payroll cheque/stubs and direct deposit advices.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Report Title for Check Print

The Report Title for Check Print (US) or Report Title for Cheque Print (AU/CA) field on the PR Company Parameters form, Report Info tab.
Accept the default report or enter the report to use for printing payroll checks/cheques.
United States: Report Title for Check PrintYou can specify a standard report (those provided by Vista™) or a user-created report. Available standard reports are:

- PR Check Print - Use for printing on pre-printed checks with pre-printed check stubs

- PR Check Print Stub (default) - Use for printing on pre-printed checks with blank check stubs.

If this field is blank, the system uses the PR Check Print Stub report.
Australia: Report Title for Cheque PrintEnter the report you want to use to print payroll cheques. You can specify a standard report (those provided by Vista™) or a user-created report. Available standard reports are:

- PR Cheque Print - A/NZ - Use for printing on pre-printed cheque stock with pre-printed cheque stubs

- PR Cheque Print Stub - A/NZ (default) - Use for printing on pre-printed cheque stock with blank cheque stubs.

If this field is blank, the system uses the PR Cheque Print Stub - A/NZ report.
Canada: Report Title for Cheque PrintEnter the report you want to use to print payroll cheques. You can specify a standard report (those provided by Vista™) or a user-created report. Available standard reports are:

- PR Cheque Print - Use for printing in English on pre-printed cheque stock with pre-printed cheque stubs

- PR Cheque Print Stub (default) - Use for printing in English on pre-printed cheque stock with blank cheque stubs.

- PR Cheque Print - CA Bilingual - Use for printing in French or English on bilingual pre-printed cheque stock with pre-printed cheque stubs. If you want to print cheques on this form for an employee in French, you must select the Print Paycheque in French checkbox for that employee on the Add'l Info tab of the PR Employees form. If you want to print cheques on this form for an employee in English, leave the checkbox unchecked.

- PR Cheque Print Stub - CA Bilingual - Used for printing in French or English on bilingual pre-printed cheque stock with blank cheque stubs. If you want to print cheques on this form for an employee in French, you must select the Print Paycheque in French checkbox for that employee on the Add'l Info tab of the PR Employees form. If you want to print cheques on this form for an employee in English, leave the box unchecked.

If this field is blank, the system uses the PR Cheque Print Stub report.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Report Title for EFT Print

The Report Title for EFT Print checkbox on the PR Company Parameters form, Report Info tab.
Specify the report for printing direct deposit stubs.
United StatesIf you leave the field blank, the system uses the PR EFT Remittance report.
To choose a different report, enter the standard or custom report for printing direct deposit stubs. Press F4 for a list of available reports.
AustraliaIf you leave the field blank, the system uses the PR EFT Remittance - A/NZ report.
To choose a different report, enter the standard or custom report for printing direct deposit stubs. Press F4 for a list of available reports.
CanadaIf you leave the field blank, the system uses the PR Cheque EFT Remittance report.
To choose a different report, enter the standard or custom report for printing direct deposit (EFT) stubs> Press F4 for a list of available reports. Available standard reports are as follows:

- PR Cheque EFT Remittance — Use for printing direct deposit (EFT) stubs on plain paper in English.

- PR EFT Remittance - CA Bilingual — Use for printing direct deposit (EFT) stubs on plain paper in French or English. To print direct deposit (EFT) stubs for an employee in French using this report, select the Print Paycheque in French checkbox for that employee on the Add'l Info tab of the PR Employees form.To print direct deposit (EFT) stubs for an employee in English using this report, leave the checkbox unselected.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Attach Pay Stub to Employee Pay Sequence

Attach Pay Stub to Employee Pay Sequence check
 box on the PR Company Parameters form, Pay Info tab.
 Select this checkbox to attach employee payment information (pay stubs or direct deposit remittance information) to the employee’s pay sequence.
 When you check this box, the system enables
 the Report Title
 for Check Attachment, Report Title for EFT Attachment, and the
 Stub Attachment
 Type fields.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Report Title for Check Attachment

The Report Title for Check Attachment (US) or Report Title for Cheque Attachment (AU/CA) checkbox on the PR Company Parameters form, Report Info tab.
Specify which report to use for creating the check stub that is attached to an employee's pay sequence.
United States: Report Title for Check AttachmentDefaults to the PR Check Print Stub by Employee report. It is the only standard report. If you leave this field blank, the system uses this report.
To use a custom report you have created, enter the report title, or press F4 to locate it.
Australia: Report Title for Cheque AttachmentDefaults to the PR Cheque Print Stub by Employee - A/NZ report. This is the only standard report. If you leave this field blank, the system uses this report.
To use a custom report you have created, enter the report title, or press F4 to locate it.
Canada: Report Title for Cheque AttachmentDefaults to the PR Cheque Print Stub by Employee report. If you leave this field blank, the system uses this report. You can specify a standard report (those provided by Vista) or a user-created report. Available standard reports are:

- PR Cheque Print Stub by Employee – Use for creating cheque stubs in English

- PR Cheque Print Stub By Employee - CA Bilingual – Use for creating cheque stubs in French or English. If you want to create cheque stubs for an employee in French using this report, you must select the Print Paycheque in French checkbox for that employee on the Add'l Info tab of the PR Employees form. If you want to create cheque stubs for an employee in English using this report, leave the checkbox unselected.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Report Title for EFT Attachment

The Enable Non Negotiable Check Print (US) or Enable Non Negotiable Cheque Print (AU/CA) checkbox on the PR Company Parameters form, Report Info tab.
Specify the report to use for creating the direct deposit (EFT) stub that is attached to an employee's pay sequence.
United StatesDefaults to the PR EFT Remittance by Employee report. This is the only standard report. If you leave this field blank, the system uses this report.
If you have created your own custom report, enter the report name or press F4 to locate it.
AustraliaDefaults to the PR EFT Remittance by Employee - A/NZ report. This is the only standard report. If you leave this field blank, the system uses this report.
If you have created your own custom report, enter the report name or press F4 to locate it.
CanadaDefaults to the PR Cheque EFT Remittance by Employee report. If you leave this field blank, the system uses this report. You can specify one of the standard reports below (those provided by Vista) or a custom report.

- PR Cheque EFT Remittance by Employee — Use for creating direct deposit (EFT) stubs in English.

- PR EFT Remittance By Employee - CA Bilingual — Use for creating direct deposit (EFT) stubs in French or English. To create direct deposit (EFT) stubs for an employee in French using this report, select the Print Paycheque in French checkbox for that employee on the Add'l Info tab of the PR Employees form. To create direct deposit (EFT) stubs for an employee in English using this report, leave the checkbox unselected.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Stub Attachment Type

Stub Attachment Type field on the PR Company
 Parameters form, Pay Info tab.
Enter the attachment type for attachments that the system is assigning to employee pay sequences. Attachment types allow you to set security based on the type. If you do not enter an attachment type, all users can potentially access this attachment.

Related information

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Parallel Direct Deposit

Parallel Direct Deposit checkbox on the PR Company Parameters form, Report Info tab.
Select if you want permit Vista to process direct deposit for more than one employee at a time, which may reduce the overall time required by Vista to process all employees paid via direct deposit.

- If not selected - Vista processes direct deposit records one at a time, completing all processing tasks for one employee record before proceeding to any other employee record.

- If selected - Vista doesn't necessarily wait until each employee direct deposit is done processing before starting on any other employee direct deposit records.

## PAYG INB Summary

This topic explains enabling PAYG INB Summary attachments for employee PAYG Summary records so they are included when emailing tax documents to employees.
PAYG INB Summary checkbox on the PR Company
 Parameters form, Report Info tab.
This field displays for Australian companies only.
Select this checkbox to enable attaching the
 PAYG INB Summary Report to employee records in PR Employee PAYG Summaries. If selected, the
 system enables the PAYG INB Summary checkbox in PR Employees (Add'l Info tab). You can have
 the system automatically select this checkbox for employees (with a valid email address)
 by answering Yes to the prompt displayed once you select this checkbox, enter a valid
 PAYG attachment type, and save the record. However, you can also set the checkbox manually
 in PR Employees.
Note: Employees with this checkbox selected in PR Employees
 will receive their PAYG summaries via email.
Leaving this checkbox unselected disables the
 "attach PAYG INB Summary to employee records" feature.

Related information

- [Set Tax Document Attachment Options: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation/set-tax-document-attachment-options-australia)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## PAYG Attachment Type

(Australia only) The PAYG Attachment Type field on the PR Company Parameters form, Report Info tab.
This field is enabled when the PAYG INB Summary checkbox is selected.
Required.
Enter the attachment type to use for PAYG summary attachments assigned to employee PAYG summary records. Press F4 to select from a list of valid attachment types.
Once you enter the attachment type and select Save, you are presented with a message asking if you want to update employees with a valid email address in PR Employees to receive their PAYG INB Summary tax documents via email. If you select Yes, the system automatically selects the PAYG INB Summary checkbox in PR Employees (Add'l Info, Tax Document Email Settings section) for all employees with a valid email address. If an employee does not have an email address, the checkbox is enabled, but not selected. You must enter an email address for the employee to enable the employee to receive their PAYG tax documents via email.

Related information

- [Set Tax Document Attachment Options: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation/set-tax-document-attachment-options-australia)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Use Secure File Path (PR EFT)

The Use Secure File Path checkbox in the PR Company Parameters form, Reports Info tab.
You can optionally specify a secure network location where all PR EFT data files are saved upon creation to restrict access to the EFT data file, even to the user prompting its creation.
Select this checkbox to specify a secure network location for PR EFT data files. This enables the Secure File Path field, allowing you to enter the secure file path.
If you leave this checkbox unselected, the system prompts the user to select a location for each newly created PR EFT data file.
Note: Once you enter a valid file location, the system sends the EFT data file to that location instead of offering the user a Save As dialog box.

Related information

- [Secure File Path](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form/field-definitions-ap-company-parameters#ID-000519f6--en)

- [Secure EFT Data Files](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information/secure-eft-data-files)
