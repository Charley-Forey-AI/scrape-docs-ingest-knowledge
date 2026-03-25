---
title: "Create an STP Finalisation File | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/create-an-stp-finalisation-file"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/create-an-stp-finalisation-file"
---

# Create an STP Finalisation File

Learn the reasons for using the Single Touch Payroll (STP) finalisation file and how to create the file.
Finalisations are only required under certain circumstances. Proceed with the steps below only if ALL the following apply:











- The employee(s) for which you are lodging a submission will not receive any
 further wages during this tax year

- You have run the ledger update for the final pay period after having created
 cheques/EFTs

While 'Pay Event' submissions are lodged regularly and routinely throughout the tax year, finalisations are typically only required under the following circumstances:











- At the end of the year after you have paid the year's final pay
 sequences

- Any time during the year when you want to indicate to the ATO that one or
 more employees will not receive any further wages from your company throughout the
 remainder of the year

What both these cases have in common is no further wages will be paid for the year to any employee(s) being finalised in the submission, and that the YTD information can be finalised officially at the ATO and released to the employee(s).
This topic covers the steps to do the following:




- Generate STP data - this automated process gathers and synthesises existing
 payroll data and places it in the PR STP Process form, including the Employees
 tab.

- Verify the data - you have an opportunity to verify the data in the Info tab
 and in the Employees tab (year-to-date amounts as at the date when you generate
 the amounts for the submission).

- Create the STP e-file - this automated process uses the synthesised data to
 create a file that is acceptable to the ATO.

1. Generate the STP Data.

1. In the PR STP Process form, in the Tax Year field, enter the tax year or press F4 to select from a list.

1. In the Submission field, enter '+' to create a new record.The system inserts information from the HQ ATO Tax Years form. You can opt to change any default values.

1. Click Generate Submission Data.The PR STP Generate Data form appears.

1. In the Submission Data
 Format field, select the data format to use.

- STP Phase 1 - Select this option if you are generating submission data for tax year 2021 or earlier. Note: You can also select STP Phase 1 to generate submission data for tax year 2022 or 2023 until you are ready to use STP Phase 2. However, once you switch to using STP Phase 2 and submit your data to the ATO, you can no longer use STP Phase 1 for 2022 or later.

- STP Phase 2 - Select this option if you are generating submission data for tax year 2024 or later.Note: You can also select STP Phase 2 to generate submission data for tax year 2022 or 2023, if you are ready to make the switch. However, once you create a submission using STP Phase 2 and submit your data to the ATO, you can no longer use STP Phase 1 for tax year 2022 or later.

1. Under Submission Options, select Fix YTD.Important: Press F1 to view additional
 information about the 'Fix YTD' submission type.

1. If you want to create and lodge a submission for a single employee, enter the Employee number.If you want to create and lodge a submission for all
 employees that have been paid in the tax year, leave the Employee field blank.If you want to create and lodge a submission for more
 than one employee but fewer than all employees that have been paid in the
 tax year, you must create and lodge one submission for each applicable
 employee.
Tip: There is an alternative option for
 finalising employees who happen to appear in a Pay Event submission. See
 the field help for the [Final](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-process-form/field-definitions-pr-stp-process-form#concept-3472--en) field in the PR STP Employee form.

1. In the Date field, enter the "as at" date you want to attribute the submission to.Note: Any entry in the Date field does not
 determine which payroll data the system includes in the submission. When
 using submission type F - Fix YTD, the system includes all YTD amounts paid
 since 1 July (or 1 April, for fringe benefit amounts).

1. Select the Final checkbox.

1. Click Generate.The system gathers YTD payroll data and provides a confirmation message.

1. Dismiss the confirmation message.The system closes the PR STP Generate Data form and
 returns to the PR STP Process form, where it populates fields relevant to a
 'Fix YTD' submission type on the right side.

1. Verify the data that the STP process has gathered.

1. Select the Info tab and review the employer-level Payee Count value for accuracy.Note: Total Gross Payments and Total PAYG Tax
 Withheld amounts are always 0.00 in any Fix YTD submission. Those amounts,
 when present in submissions of other types, pertain to a specific pay date,
 which is not relevant for a Fix YTD submission.

1. Select the Employees tab and review employee-level values for accuracy.

1. Double-click any employee record to view more detailed information.Note: If you discover errors in the employee data, you can opt to make manual corrections in the PR STP Employee form, but it is preferable for the integrity of the ongoing STP reporting process that you correct the underlying data in payroll history or payroll configuration and then re-generate the submission's data to take advantage of the corrections.Depending on the source of the erroneous data, you may need to do one or more of the following:

- recategorise earnings codes in the PR Earnings Codes form

- recategorise deduction or liability codes in the PR Deductions/Liabilities form

- make manual adjustments of accumulated payroll amounts in the PR Employee Accumulations form

- make corrections in the PR Timecard Entry form, re-process payroll, re-issue payments to affected employees (if needed), and re-run the ledger update

Regardless of your remedial approach, the next steps are:

1. revisit the same submission record in the PR STP Process form and re-generate the submission data. The system removes the previous data for the submission and generates new data.

1. verify the new values and resume the process.

1. Create the STP file.

1. In the Signatory field, enter your name.

1. In the Date Signed field, enter today's date.

1. Click Tick the box to complete your declaration.The system enables the Create E-File button while disabling nearly all other fields.

1. Click Create E-File.The system opens the PR STP Create E-File form. It also creates the e-file, runs it through a validation process, and prompts you to save it.Note: If the system encounters any validation errors, instead of prompting you to save, it displays the validation errors. To make corrections, make note of the errors, close the PR STP Create E-File form, and in the PR STP Process form, click Untick the box.

1. Save the file and close the PR STP Create E-file form to return to the PR STP Process form.On the right side of the form, the system populates additional fields relevant to this submission.

When you lodge this 'Fix YTD' e-file, the ATO finalises
 the employees' income and withholding information for the year and makes the information
 available to the employee(s). Providing the finalisation declaration for STP-reported
 information in this manner removes your obligation as an employer to provide your employees
 with payment summaries in relation to the STP reported information.
To lodge your submission,
 retrieve the file from the location you saved it and upload it according to the
 instructions provided by Ozedi. [Learn more about Ozedi](http://www.google.com).After you have lodged your e-file with the ATO, revisit the PR STP
 Process form, select your submission, and change the Status value from 4 - E-File
 Created to 5 - E-File Lodged. This effectively locks down the submission and serves
 as an indication that it should not be edited or deleted. If any subsequent changes or
 corrections are needed, then you must create and lodge a new 'Replacement'
 e-file.

Related information

- [PR STP Process Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-process-form)

- [PR STP Generate Data Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-generate-data-form)

- [PR STP Employee (Phase 1) Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-employee-phase-1-form)

- [PR STP Employee Amounts Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-employee-amounts-form)
