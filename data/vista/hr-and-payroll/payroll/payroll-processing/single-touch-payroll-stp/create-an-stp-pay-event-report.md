---
title: "Create an STP Pay Event Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/create-an-stp-pay-event-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/create-an-stp-pay-event-report"
---

# Create an STP Pay Event Report

Single Touch Payroll (STP) in Vista helps you align your payroll processes with your Australian Taxation Office reporting obligations. Each pay date (even an out-of-cycle pay date) you should generate and lodge your STP e-file using these steps.
Successful STP processing begins with the required setup. See [Single Touch Payroll (STP): Setup](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-single-touch-payroll-australia) for requirements to get started. Before you begin, take the following steps:

- Pay all employees for the current pay period.

- Run the ledger update for the current pay period.

- (Optional) Make sure the information in the HQ ATO Tax Years form is up to date.

This topic covers the steps to do the following:

- Generate STP data - this automated process gathers and synthesises existing payroll data and places it in the PR STP Process form, including the Employees tab.

- Verify the data - you have an opportunity to verify that your setup is resulting in the correct payroll data in the Info tab (applicable to your chosen pay date) and in the Employees tab (year-to-date amounts as at the date when you generate the amounts for the submission).

- Create the STP e-file - this automated process uses the synthesised data to create a file that is formatted in a manner acceptable to the ATO.

1. Generate the STP data.

1. In the PR STP Process form, in the Tax Year field, enter the tax year or press F4 to select from a list.

1. In the Submission field, enter '+' to create a new record.The system inserts information from the HQ ATO Tax Years form. You can opt to change any default values.

1. Select Generate Submission Data.The PR STP Generate Data form appears.

1. In the Submission Data Format field, select the data format to use.

- STP Phase 1 - Select this option if you are generating submission data for tax year 2021 or earlier. Note: You can also select STP Phase 1 to generate submission data for tax year 2022 or 2023 until you are ready to use STP Phase 2. However, once you switch to using STP Phase 2 and submit your data to the ATO, you can no longer use STP Phase 1 for 2022 or later.

- STP Phase 2 - Select this option if you are generating submission data for tax year 2024 or later.Note: You can also select STP Phase 2 to generate submission data for tax year 2022 or 2023, if you are ready to make the switch. However, once you create a submission using STP Phase 2 and submit your data to the ATO, you can no longer use STP Phase 1 for tax year 2022 or later.

1. Under Submission Options, select Pay Event.

1. In the Pay Date field, press F4 to select from a list of available paid dates.

1. (Optional) If you want to limit this submission's data to a single payroll group, enter the value in the PR Group field. If you want to further limit this submission's data to a single payroll ending date, enter the value in the PR End Date field.

1. Select Generate.The system gathers existing payroll data according to your selections and provides a confirmation message.

1. Dismiss the confirmation message.The system closes the PR STP Generate Data form and returns to the PR STP Process form, where it populates fields relevant to a 'Pay Event' submission type on the right side.

1. Verify the data that the STP process has gathered.

1. Select the Info tab and review the employer-level values for accuracy. These include Payee Count, Total Gross Payments, and others.

1. Select the Employees tab and review employee-level values for accuracy.

1. Double-click any employee record to view additional data.Note: If you discover errors in the employee data, you can opt to make manual corrections in the PR STP Employee form, but it is preferable for the integrity of the ongoing STP reporting process that you correct the underlying data in payroll history or payroll configuration and then re-generate the submission's data to take advantage of the corrections.Depending on the source of the erroneous data, you may need to do one or more of the following:

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

To lodge your submission, retrieve the file from the location you saved it and upload it according to the instructions provided by Ozedi. [Learn more about Ozedi](http://www.google.com).
After you have lodged your e-file with the ATO, revisit the PR STP Process form, select your submission, and change the Status value from 4 - E-File Created to 5 - E-File Lodged. This effectively locks down the submission and serves as an indication that it should not be edited or deleted. If any subsequent changes or corrections are needed, then you must create and lodge a new 'Replacement' e-file.

Related information

- [PR STP Process Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-process-form)

- [PR STP Employee (Phase 1) Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-employee-phase-1-form)

- [PR STP Employee Amounts Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-employee-amounts-form)
