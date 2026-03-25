---
title: "Payroll Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/hr-and-payroll/payroll-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/hr-and-payroll/payroll-features"
---

# Payroll Features

Vista 2021 R1 delivers on user-requested Payroll enhancements, fixes, and other improvements.

## Updated Aatrix AUF to Current Aatrix Version (2.80)

Modified the stored procedures used for generating AUF files for ACAs, W-2's, 1099's (U.S.), and Canadian T5018's to meet current specifications.
Changes include the addition of the following columns to the AUF file:

- EEO Job Category

- EEO Ethnicity

- EEO Hours

- Hours Worked

- Clergy Members

These columns are set to NULL when not applicable for the selected reporting option.
Most notably, the system now calculates the Workers' Benefit Fund (WBF) hours and auto-updates the new Hours Worked column on the Oregon Form OQ (Quarterly Tax Report). Previously, you needed to manually fill in this value on the report.

## Extended Compliance for 401(k) Plans (U.S. only)

You now have the ability to set annual compensation limits for 401(k) employer match liabilities. In addition, you can now impose a limit on total catch-up contributions when multiple deductions are used.
The following changes were made to enable these functionalities:

- PR Deductions/Liabilities - Added a new 401k Liability checkbox to the Info tab. This checkbox is enabled only for liability codes with a limit type of Rate of Earnings, and should only be selected when the liability code is for a 401(k) employer match. Once selected, the Pre-Tax Group field is enabled, allowing you to specify the pre-tax group to use for determining the annual compensation limit.
For multi-tiered 401(k) employer matches, such as Safe Harbor 401(k) plans, or when you have employees that contribute to multiple plans, such as a traditional 401(k) and a Roth 401(k), you must assign the same pre-tax group to applicable employer match liabilities. This ensures that the annual compensation limit is applied across all applicable liabilities when calculating matching contributions.

- PR Pre-Tax Deduction Groups - Added a new Annual Compensation Limit field for specifying the maximum annual limit of employee earnings to which a 401k employer match can be applied. To ensure the system applies this limit across applicable employer-match liabilities, assign the same pre-tax group to the applicable 401(k) liabilities.
For employee catch-up contributions, added a Catch up Annual Contribution Limit field for specifying the annual limit for employee 401(k) catch contributions. The system will apply this limit across all 401(k) deductions for each employee. For example, if an employee contributes to both a traditional 401(k) and a Roth 401(k), with an annual limit of $6,000, the system applies this limit across both plans.
Also changed the label of the Annual Limit field to Standard Annual Contribution Limit for better clarification. You will still use this field to specify the maximum annual limit for employee 401(k) and Roth 401(k) contributions.

- Modified the payroll process to apply the annual compensation limit to 401(k) liabilities. The system will now stop computing the employer match once the annual compensation limit is met.
Also modified the payroll process to apply the catch up annual contribution limit to 401(k) catch-up deductions. The system will stop computing 401(k) contributions once the annual limit is met.

- Modified the PRDednLiab import template to include a new Is401kLiabilityYN identifier (#161).

Note: Once you install this release, the system will no longer use PR Deductions/Liabilities to determine annual limits for catch-up contributions and employer-match liabilities. You will need to do the following:

- In PR Pre-Tax Deduction Groups, set the current annual compensation and catch-up contribution limits for each applicable pre-tax group and,

- In PR Deductions/Liabilities, for employer-match liabilities, select the 401k Liability checkbox and specify the applicable pre-tax group. For more information, click on the following links.

For more information, click on the following links:[Set Up a 401(k) Employer Match](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-401k-employer-match)
[Set Up a Catch-Up 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction)
[Set Up a Multi-Tiered 401(k) Employer Match](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-multi-tiered-401k-employer-match)

## Support for JobMaker Hiring Credit (JMHC) in STP (AU)

The Single Touch Payroll (STP) feature in Vista now supports the JobMaker Hiring Credit (JMHC) program administered by the Australian Taxation Office (ATO).
If your company participates in the JobMaker program, you can now nominate employees for participation in the JobMaker program, report those nominations to the ATO, and then claim credits for each eligible employee for applicable JobMaker periods.
There are several requirements that an employee must meet in order for your company to claim the JobMaker credit for that employee, such as the age of the employee, recent receipt by the employee of certain kinds of income support, and completion by the employee of a JobMaker Hiring Credit employee notice for the employer. For a complete list of the requirements, see the ATO website.
The following changes were made to enable this functionality:

- In PR Employees, added a new JobMaker Hiring Credit Eligibility section to the Add'l Info tab. This section contains the following new fields:

- New Hire - This drop-down contains two options: MNM - Nominate employee and MNMX - Revoke prior nomination. You will use the MNM - Nominate employee option to nominate new hires for participation in the JobMaker program or to nominate rehires that have never participated in the JobMaker program as your employee.You will use the MNMX - Revoke prior nomination option to revoke an employee's nomination in the JobMaker program that was made in error.
Once you nominate an employee or revoke a nomination, run the PR STP Process form to generate your submission data and create the e-file. The data generation process creates a single pseudo-allowance record representing the nomination or revocation in the employee's allowance collection for the submission.

-  Recent Rehire - This drop-down contains two options: MRM - Renominate employee and MRMX - Revoke prior renomination. You will use the MRM - Renominate employee to renominate a recent rehire who is participating in the JobMaker Hiring Credit (JMHC) program for the second time as your employee.You will use the MRMX - Revoke prior renomination option to revoke an employee's renomination in the JobMaker program that was made in error.
Once you renominate an employee or revoke a renomination, run the PR STP Process form to generate your submission data and create the e-file. The data generation process creates a single pseudo-allowance record representing the nomination or revocation in the employee's allowance collection for the submission.

- Period 1 thru Period 8 - Each of these drop-downs contain two options: M0# - Declare employee met minimum hours test and M0#X - Revoke prior declaration (where # represents the period number).The M0# - Declare employee met minimum hours test option is used to confirm the employee's eligibility for the specified reporting period. Eligible employees are those who have satisfied the minimum hours requirement for the period; that is, completed a minimum of 20 hours of work per week on average for that period (either the hours for which the employee is being paid or the hours the employee worked).
You will use the M0#X - Revoke prior declaration option to revoke an employee's eligibility confirmation made in error for the selected period.
Once you confirm or revoke an employee's eligibility for a JobMaker period, run the PR STP Process form to generate your submission data and create the e-file. The data generation process creates a single pseudo-allowance record representing the confirmation or revocation in the employee's allowance collection for the submission.

For more information about setting the JobMaker options for an employee, click the following links:

- [Nominate / Renominate Employees for JobMaker Hiring Credit (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/nominate--renominate-employees-for-jobmaker-hiring-credit-au)

- [Revoke an Employee's JobMaker Nomination / Renomination (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/nominate--renominate-employees-for-jobmaker-hiring-credit-au/revoke-an-employees-jobmaker-nomination--renomination-au)

- [Confirm an Employee's Eligibility for a JobMaker Period (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/confirm-an-employees-eligibility-for-a-jobmaker-period-au)

- [Revoke an Employee's Eligibility Confirmation for a JobMaker Period (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/confirm-an-employees-eligibility-for-a-jobmaker-period-au/revoke-an-employees-eligibility-confirmation-for-a-jobmaker-period-au)

- In PR STP Employee, updated the Other Type drop-down to include the new JobMaker options (as shown below). The system automatically generates an Other record for the applicable JobMaker options based on the selections made in the new "JobMaker Hiring Credit Eligibility" section in PR Employees. Although you can override a generated option, the system does not update the selection in PR Employees.

- PR STP Generate Data - The generation process will now create a single pseudo-allowance record representing each JobMaker option selected in PR Employees within the employee's allowance collection for the submission. Each record is assigned a type of Other, the appropriate Other Type value, and a YTD Amount of 0.00.

- PR STP Create E-File - The e-file generation process will now include records within each employee's allowance collection for each of the applicable JobMaker options selected for that employee.

## Added the Ability to Set Leave Codes as Active/Inactive

You can now set leave codes as Inactive to prevent leave from accruing when a leave code is no longer in use by the company or applicable to an employee.
The following changes were made to support this functionality:

- PR Leave Codes / PR Employee Leave - These forms now include a new Active checkbox. When you add a new leave code in PR Leave Codes, the system automatically sets the code to Active. You can then assign the leave code to employees in PR Employee Leave, with the status remaining as Active.
Once you determine the code is no longer applicable to an employee, you can deselect the Active checkbox in PR Employee Leave to deactivate the leave code for that employee only. Once deactivated, leave will no longer accrue for that employee/leave code.
When you deactivate a leave code in PR Leave Codes, the system displays a message indicating that there are active employee leave codes associated with the specified leave code that will be disabled. If you select OK to continue, the leave code is deactivated for all applicable employees, as well as for the company. Once deactivated, you can no longer assign that code to employees, nor can you edit existing employee leave code records.

- PR Leave Entry - Updated to prevent entry of inactive leave codes.

- PR Auto Leave Accrual/Usage - Updated the auto leave process to exclude inactive leave code records.

- PR Leave Code Reset - Modified to support active/inactive leave codes as follows:

- If you elect to reset limits for a specific leave code, the system now displays a "Leave code is inactive" message when you enter a leave code that is flagged as inactive in PR Leave Codes.

- If you elect to reset limits for all leave codes, the system now skips any leave codes that are flagged as inactive in PR Leave Codes and PR Employee Leave. Leave codes must be active in both places to be included in the reset process.

- F4 Lookups - Modified the Leave Code lookups in the following forms to include an "active leave codes" lookup option:

- PR Leave Codes

- PR Employee Leave

- PR Leave Entry

- PR Auto Leave Accrual Usage

Note: When you install this release, the system sets all existing leave codes to Active. You will need to manually deactivate any leave codes that are not applicable to employees, as well as those that are no used by the company.

## Allow Resetting Leave Codes for a Selected Employee

You can now reset leave code limits for a single employee or for all employees.
A new Employee section was added to the PR Leave Code Reset form that includes All and Employee options, as well as a new Employee field that is enabled when the Employee option is selected. If specifying a single employee, that employee must be flagged as Active in PR Employees.
Other changes were made to the PR Leave Code Reset form as follows:

- Changed the positions of the Reset Accrual Amounts to 0.00 and Reset Available Balances to Carryover Limit checkboxes and enclosed them in a new Reset Type section.

- Moved the Delete any reset transactions currently posted to this date field to the bottom of the form.

- Changed the labels of the following fields for better clarity:Previous LabelNew Label
Reset Accrual Amounts to 0.00Reset Accrual Amounts to 0.00 hours for the next frequency period
Reset Available Balances to Carryover LimitReduce Available Balances to Carryover Limit
Selected (option in Leave Code section)Leave Code
Selected (option in Frequency section)Frequency

- Changed the label of the Update button to Create Batch. Once you create the batch, you are prompted to "post the batch". If you select No, this button changes to Update Batch, allowing you to continue adding records to the batch until you are ready to post or to exit the form so you can review the batch in PR Leave Entry. However, once you close the PR Leave Code Reset form, you can only post the batch using PR Leave Entry.

## Improved Leave Processing Workflow

Several other changes were made to improve leave processing to support best practices and ease of use. These changes include the following:

- Moved the PR Auto Leave Accrual / Usage form under the PR Leave Entry form. You will now access this form by selecting File  > Leave Accrual Usage Init in PR Leave Entry. Now when you generate accrual and/or usage entries, the system displays a message indicating entries were added to the batch. When you close the form, you are returned to the PR Leave Entry form where you can access the entries and post the batch.Note: If you run the process for a single leave code that is not assigned to any employees, a message displays that there was nothing to update. If you run the process for all leave codes, the system skips any leave codes that are not assigned to at least one employee. Additionally, the system will also skip any leave codes flagged as inactive in PR Leave Codes or PR Employee Leave.

- In the PR Leave Code Reset form, when you select to delete leave code reset transactions (that is, you select the Delete any reset transactions currently posted to this date checkbox), if there are transactions with 0.00 amounts, the system now updates the Last Date Reset (in PR Employee Leave) from prior entries. Previously, it would only set the Last Date Reset if the amounts were less than or greater than 0.00.

- Modified leave entry processing to improve performance and to support the new leave code active/inactive status.

## Reset Beginning Check Number by CM Account

You can now override the beginning check number used when printing checks by CM Account.
A new Beginning Check # field was added to the CM Accounts form to allow resetting the beginning check number default for printed checks. The value entered in this field applies to both Accounts Payable and Payroll checks using the same CM account.
When printing checks in PR Check Print, the Beginning Check # field defaults the beginning check number value specified for the CM account. Once you complete the check run, the system updates the Beginning Check # field in CM Accounts based on the last check number used plus one.
If the Beginning Check # field in CM Accounts is blank, the system uses standard defaulting; that is, it defaults the beginning check number based on the highest check number in the system.
In addition to this change, the Ending Check # field in PR Check Print now defaults based on the number of checks being printed for the specified CM Account/batch. For example, if the beginning check number is 100 and you are printing 10 checks, the ending check number defaults to 110.
 For additional information, see the [Cash Management](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/accounting/cash-management-features) release notes.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
