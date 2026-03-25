---
title: "Create an STP Full File Replacement (Australia) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/create-an-stp-full-file-replacement-australia"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/create-an-stp-full-file-replacement-australia"
---

# Create an STP Full File Replacement (Australia)

(Australia only) If you need to replace a Single Touch Payroll (STP) 'Pay Event' submission that you have already lodged with the ATO, create a new submission of type 'Full File Replacement'.
Make all necessary corrections in payroll configuration or payroll history for the pay date of the original 'Pay Event' submission that you now need to replace. Depending on the source of the erroneous data, you may need to do one or more of the following:

- re-categorise earnings codes in the PR Earnings Codes form

- re-categorise deduction or liability codes in the PR Deductions/Liabilities form

- make manual adjustments of accumulated payroll amounts in the PR Employee Accums Detail form

- make corrections in the PR Timecard Entry form, re-process payroll, re-issue payments to affected employees (if needed), and re-run the ledger update

Note: Only previous Pay Event e-files are eligible to be replaced; you cannot replace Fix YTD or Full File Replacement e-files. A previous Pay Event e-file may be replaced only if no employee in the e-file has already been included in a more recent Pay Event or Fix YTD e-file lodged with the ATO.

This topic covers the steps to do the following:

- Generate STP data - this automated process gathers and synthesises existing payroll data and places it in the PR STP Process form, including the Employees tab.


- Verify the data - you have an opportunity to verify that your setup is resulting in the correct payroll data in the Info tab (applicable to your chosen pay date) and in the Employees tab (year-to-date amounts as at the date when you generate the amounts for the submission).


- Create the STP replacement e-file - this automated process uses the synthesised data to create a file that is formatted in a manner acceptable to the ATO.


1. Generate the STP data.

1. In the PR STP Process form, in the Tax Year field, enter the same tax year as you used for the previous 'Pay Event' submission that you now wish to replace. (Replacement submissions must be in the same tax year as the original Pay Event submission they are replacing.)

1. In the Submission field, enter '+' to create a new record for the replacement submission.The system inserts information from the HQ ATO Tax Years form. You can opt to change any default values.

1. Click Generate Submission Data.The PR STP Generate Data form appears.

1. In the Submission Data Format section, select the data format (STP Phase 1 or STP Phase 2) that was used for the Pay Event submission you are replacing.For more information about these data format options, see [Submission Data Format](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-generate-data-form/field-definitions-pr-stp-generate-data-form#concept-4650--en).

1. Under Submission Options, select Full File Replacement.

1. In the Submission to Replace field, enter the submission number of the previous 'Pay Event' submission that you now want to replace. You may also press F4 to select that previous 'Pay Event' submission from a list.Note: The F4 lookup only displays submissions of type 'Pay Event' because that is the only type that may be replaced.The F4 lookup only displays a subset of all 'Pay Event' submissions. A previous original 'Pay Event' submission only appears if no employees in the original submission have been included in any subsequent submission of type 'Pay Event' or 'Fix YTD'.
The F4 lookup does not display any original 'Pay Event' submissions that include an employee that has also been included in a subsequent submission because 'Pay Event' submissions with one or more employees in a subsequent submission cannot be replaced.

1. Click Generate.The system gathers existing payroll data (using the same selection criteria you used when you created the original 'Pay Event' submission that is now being replaced) and provides a confirmation message.

1. Dismiss the confirmation message.The system closes the PR STP Generate Data form and returns to the PR STP Process form, where it populates fields relevant to a 'Full File Replacement' submission type on the right side.
Note: The values in the Pay/Fix Date, PR Group, PR End Date, and Submission ID fields of this replacement submission are identical to the respective values of those fields in the original 'Pay Event' submission.The Submission ID value for the replacement submission must match the Submission ID value for the original 'Pay Event' submission; this is what permits the ATO to replace the previously lodged e-file with the new replacement e-file.

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

To lodge your submission, retrieve the file from the location you saved it and upload it according to the instructions provided by Ozedi. [Learn more about Ozedi](https://www.ozedi.com.au/products-and-services/single-touch-payroll-stp/).
After you have lodged your e-file with the ATO, revisit the PR STP Process form, select your submission, and change the Status value from 4 - E-File Created to 5 - E-File Lodged. This effectively locks down the submission and serves as an indication that it should not be edited or deleted.
If any subsequent changes or corrections are needed, then you must create and lodge a new 'Replacement' e-file.

Related information

- [PR STP Process Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-process-form)

- [PR STP Generate Data Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-generate-data-form)

- [PR STP Employee (Phase 1) Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-employee-phase-1-form)

- [PR STP Employee Amounts Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-employee-amounts-form)
