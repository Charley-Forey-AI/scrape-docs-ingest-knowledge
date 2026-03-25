---
title: "Payroll Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/hr-and-payroll/payroll-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/hr-and-payroll/payroll-features"
---

# Payroll Features

Vista 2021 R2 delivers on user-requested Payroll enhancements, fixes, and other improvements.
Important:Vista Year-End Requirements Information for 2021 Tax YearYear-end regulatory reporting for US and Canadian Vista customers, including W-2, ACA, and T4 forms printing and eFiling for the tax year 2021, will require Aatrix. Please review the following Knowledge articles and make sure you are prepared in advance:

- [Vista Year-End 2021 Full Transition to Aatrix Reporting](http://go.viewpoint.com/NjIzLU5EQS00ODcAAAF-bjsPmJruf_aUi80Sk7avugNAaZGjDO_Ei9n9XLBgLn_kC75xcMln2CndaO-3WMKKkB2zK18=)

- [What is Aatrix](http://go.viewpoint.com/NjIzLU5EQS00ODcAAAF-bjsPmNS_gJN2H7uvJgCB8MCyOtHHByPnLmthlJRREvAiRP1eW3SlKFSPhgl_mDk6qVk3onw=)

Click [here](https://partner.aatrix.com/vista) for information about enrolling with Aatrix.

## Proportional Salary Distribution for Auto Earnings

If you use the auto earnings feature and multiple entries exist for an employee/earnings code in PR Automatic Earnings, when changes are made to an employee's salary, the system now distributes the change proportionally to the applicable auto entry sequences. However, this update only occurs if you selected the Update Auto Earnings checkbox for the employee/earnings code in PR Employees.
The system bases the proportional distribution on the Rate/Amt defined for each sequence for the specified earnings code (in PR Automatic Earnings) and the Salary specified for the employee (in PR Employees).
 For example, say an employee's Salary is $1,000 and you have set up two sequences for Earn Code 1 in PR Automatic Earnings: one for Job 100 with a Rate/Amt of $400 and one for Job 300 with a Rate/Amt of $600. In this case, the first entry is 40% of the Salary and the second entry is 60% of the Salary. If you then update the Salary to $1500, the system determines there is a difference between the new salary amount and the total amount for the existing auto entry sequences, and updates the auto entry sequences as follows:
Earn Code 1, Seq 1: $600 ($1,500 x .40 = $600)
Earn Code 1, Seq 2: $900 ($1,500 x .60 = $900)
If the system calculation results in amounts that do not fully equal the new Salary amount, the system then adjusts the highest earn code sequence to ensure the total amount reflects the specified Salary.Note: If multiple entries exist for an earnings code in PR Automatic Earnings, but the entries all have Rate/Amt values of zero, when you update the employee's salary in PR Employees, the system will not distribute amounts to each sequence; rather, it will update the full salary amount to the first sequence for that earnings code. For instance, using the example above, if both entries had zero amounts, the system would apply the full $1,500 to Earn Code 1, Seq 1 and leave Earn Code 1, Seq 2 at zero.
If you change the earnings code for an employee and/or select the Update Auto Earnings checkbox in PR Employees, the system updates PR Automatic Earnings as follows:

- If the earn code exists for the employee in PR Automatic Earnings, the system updates the specified salary amount to the specified earnings code, distributing the amount proportionally if multiple sequences exist for the earning code.

- If the earn code does not exist in PR Automatic Earnings, no update occurs.

For more information, see [About Updating Salary Changes to Auto Earnings](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-updating-salary-changes-to-auto-earnings).

## Non-Binary Gender Designations

You can now assign non-binary genders to Employees in the Payroll module.
In some states, employers are required to identify employees based on the genders with which they identify. Adding new gender information fields to the PR Employees form allows employers to comply with gender identification requirements.
To implement this functionality, the following changes were made to the PR Employees form:

- Gender Identity - Use this new field to specify the gender an employee identifies with. Options are: Male, Female, Non-Binary, and Other. Selecting Other enables the gender Description field (unlabeled).

- Description (unlabeled) - This new field is used to enter a gender description for employees with an "Other" gender identity designation (for example, Agender, Androgyne, Bigender, etc.).

- Gender - Changed the label of this field to "Reporting Gender", as this field is currently used for gender designation on EEO reports.

The new Gender Identity and gender Description fields are informational only; they are not currently used for EEO reporting.
Note: Changes to an employee's gender information are updated to HR Resources automatically if the Name update option is selected in HR Company Parameters and the Active PR Employee and Exists in PR checkboxes are selected for the employee in HR Resources.

For information about the gender information changes in HR Resources and HR Resource Dependents, see the [Human Resources](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/hr-and-payroll/human-resources-features) release notes.

## New Oregon Tax Routines (U.S.)

 In accordance with Oregon state requirements, the following local income tax routines were added for Oregon. In order to use these tax routines, you must initialize them via PR Routine Master. For more information, see Initializing Routines. For more information, see [Initialize Routines](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/initialize-routines).United States
State/RegionProcedure Name / DetailsEffective Date
Multnomah County Income Tax (Oregon)bspPRMultnomahORC21For information about the setup needed for this routine, see the [Multnomah County Income Tax](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-united-states/north-carolina-philadelphia#ID-000332be--en__OR_Multno) section of the tax routine tables.
Immediately
Portland OR Metro Income Tax (Oregon)bspPRPDXMetroORC21For information about the setup needed for this routine, see the [Portland OR Metro Income Tax](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-united-states/north-carolina-philadelphia#ID-000332be--en__OR_Metro) section of the tax routine tables.
Immediately

## Support Banker's Rounding for Timecards

 If you import timecards into a PR Timecard Entry batch (via the Imports module) and you use 'banker's rounding', the batch validation process (in PR Batch Process) now accommodates the small differences that may occur when rounding timecards to the penny (for example, rounding 0.035 to 0.04).

## Improved Ledger Update Processing

The PR Ledger Update process now runs server side. This was done to prevent Client network disconnections from interfering with the ledger update.

## Improved F4 Lookups for PR Leave Code Reset

The F4 lookups in the PR Leave Code Reset form now include new options to improve F4 functionality. These options are as follows:

- Leave Code - Added a new Leave Reset: Active Lv Codes option to the Leave Code lookup to show only leave codes flagged as Active in PR Leave Codes for the current company. The Leave lookup option remains unchanged.

- Frequency - Added a new Leave Reset: Active Freq Codes option to the Frequency lookup to show only active frequency codes that are in use in any of the Frequency fields on the PR Leave Codes or PR Employee Leave forms. If you selected a specific leave code to reset (in the Leave Code field), the lookup shows only frequency codes in use in PR Leave Codes or PR Employee Leave for the specified leave code. The Frequency Codes lookup option remains unchanged.

- Employee - Added a new Leave Reset: Active Employees option to the Employee lookup to show employees that have active records on the PR Employee Leave form for the current company. If you selected a specific leave code to reset (in the Leave Code field), the lookup shows only employee records in PR Employee Leave that reference the specified leave code. The Employees by Sort Name lookup option remains unchanged.

## Improved Updates to Last Timecard Post Date

When you post any timecard in PR Timecard Entry, regardless of the timecard type (job, non-job, mechanic, SM work order), the system now updates timecard post date for the employee in PR Employees.
As part of this change, the Last Updated field in PR Employee is now labeled Last Timecard Post Date. When you enter a timecard, if the timecard date is equal to or later than the Last Timecard Post Date in PR Employees, the system updates the field equal to the timecard date. If you also entered a JC company, job, and/or Crew on the timecard, the system updates the corresponding fields in PR Employees.
If you enter a new timecard or updated an existing timecard with a timecard date earlier than the Last Timecard Post Date, no update will occur, even if the JC company, job, and crew differ from what is shown in PR Employees.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
