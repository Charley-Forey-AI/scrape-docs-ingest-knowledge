---
title: "Field Definitions: PR STP Generate Data Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-generate-data-form/field-definitions-pr-stp-generate-data-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-generate-data-form/field-definitions-pr-stp-generate-data-form"
---

# Field Definitions: PR STP Generate Data Form

The following is a list of field descriptions for the PR STP
 Generate Data form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Submission Data Format

The Submission Data Format field on the PR STP Generate Data form.

Select the data format to use for the specified tax year and submission.

- STP Phase 1 - Select this option if you are generating submission data for tax year 2021 or earlier. Note: You can also select STP Phase 1 to generate submission data for tax year 2022 or 2023 until you are ready to use STP Phase 2. However, once you switch to using STP Phase 2 and submit your data to the ATO, you can no longer use STP Phase 1 for 2022 or later.

- STP Phase 2 - Select this option if you are generating submission data for tax year 2024 or later.Note: You can also select STP Phase 2 to generate submission data for tax year 2022 or 2023, if you are ready to make the switch. However, once you create a submission using STP Phase 2 and submit your data to the ATO, you can no longer use STP Phase 1 for tax year 2022 or later.

Once you generate submission data (by clicking the Generate button), the system populates the STP Phase field in PR STP Process with the option you selected here.

## Submission Options

The Submission Options selection buttons on the PR STP Generate Data form.
Access the PR STP Generate Data form by clicking the Generate Submission Data button on the PR STP Process form.

- Pay Event - for typical use on or before each payday, including out-of-cycle paydays. This submission type includes all required pay-period-specific payroll data, in addition to employee YTD amounts.

- Full File Replacement - use this type to create a replacement of a defective original 'Pay Event' type submission that you lodged recently. You may replace a previous original 'Pay Event' submission only if no employee in that original submission has been included in a subsequent submission of type 'Pay Event' or 'Fix YTD'.
Note: Only one Full File Replacement submission is allowed per original submission. If you select this option and a Full File Replacement submission already exists in the same PR company and Tax Year as the specified original submission (submission to replace), no data is generated and an error displays indicating that there is already a Full File Replacement submission for the specified submission to replace.

- Fix YTD - for use when it is suitable to submit only YTD amounts. This selection is for 'Update' events, as well as 'Fix' events as defined by the ATO. This submission type does not include all pay-period-specific payroll data that is required for a 'Pay Event' submission.
Note: You can only use the Fix YTD submission type for a prior tax year if your company reported through STP for that year. If you select this option and no Pay Event submission exists in the specified tax year with a status of 4-E-File Created or greater, and at least one submission exists in a tax year later than that of your current submission, no data is generated and an error displays indicating that you cannot generate data for a Fix YTD submission for the specified tax year because you did not report through STP for that year.

Tip: When you are ready to finalise all employees for the tax year, use the Fix YTD submission type in conjunction with the Final checkbox.

Your selection in this field populates the Submission Type field in the PR STP Process form.

## Pay Date

Pay Date field on the PR STP Generate Data form
Access the PR STP Generate Data form by clicking the Generate Submission Data button on the PR STP Process form.
Enter the paid date for the payday. The data generation process only includes employees paid on this date.
The value you enter in this field populates the Pay/Fix Date field in the PR STP Process form.

## PR Group

PR Group field on the PR STP Generate Data form
Access the PR STP Generate Data form by clicking the Generate Submission Data button on the PR STP Process form.
If you want to restrict this submission to a single payroll group, enter it here or press F4 to select from a list.

If you enter a value in this field, the same value populates the same-named (display-only) field in the PR STP Process form.

## PR End Date

PR End Date field on the PR STP Generate Data form
Access the PR STP Generate Data form by clicking the Generate Submission Data button on the PR STP Process form.
The system enables this field after you make an entry in the PR Group field.
If you want to restrict this payroll group's submission to a single payroll end date, enter it here or press F4 to select from a list.
If you enter a value in this field, the same value populates the same-named (display-only) field in the PR STP Process form.

## Submission to Replace

Submission to Replace field on the PR STP Generate Data form
Access the PR STP Generate Data form by clicking the Generate Submission Data button on the PR STP Process form.
This field is enabled when you select Full File Replacement. Press F4 to select the recent 'Pay Event' submission lodged previously by your company that you now wish to replace with this submission.
Note:The F4 lookup only displays submissions of type 'Pay Event' because that is the only type that may be replaced.
The F4 lookup only displays a subset of all 'Pay Event' submissions. A previous original 'Pay Event' submission only appears if no employees in the original submission have been included in any subsequent submission of type 'Pay Event' or 'Fix YTD'.
The F4 lookup does not display any original 'Pay Event' submissions that include an employee that has also been included in a subsequent submission because 'Pay Event' submissions with one or more employees in a subsequent submission cannot be replaced.

## Employee

Employee field on the PR STP Generate Data form
Access the PR STP Generate Data form by clicking the Generate Submission Data button on the PR STP Process form.

This field is enabled when you select Fix YTD.
If you want to create a submission for only one employee, enter the number or press F4 to select from a list.

If you are creating a 'Fix YTD' submission that includes all employees that are present in payroll records for the year, leave this field blank.

## Date

Date field on the PR STP Generate data form
Access the PR STP Generate Data form by clicking the Generate Submission Data button on the PR STP Process form.
This field is enabled when you select Fix YTD.
Enter the "as at" date you want to attribute the submission to.
All YTD amounts paid since 1 July (or since 1 April, for fringe benefit amounts) are included when using submission type F (Fix YTD).Note: Your entry in this field does not affect which payroll data the system includes in the submission. All YTD amounts paid since 1 July are included when using submission type F (Fix YTD).
The value you enter in this field populates the Pay/Fix Date field in the PR STP Process form.

## Final

Final checkbox on the PR STP Generate Data form
Access the PR STP Generate Data form by clicking the Generate Submission Data button on the PR STP Process form.
This checkbox is typically used in a year-end Fix YTD type submission in order to "finalise" the year's data for all employees that are present in payroll records for the year. This checkbox may also be used mid-year to "finalise" the year's data for a terminated employee that you will not be paying again in the year.
Select this box to mark all employees as "Final" in generated data, which indicates for each employee that YTD values for the entire year have been (or are presently being) submitted, and that the ATO is free to release annual summary information to interested employees.
After generating data, if you want to remove the "Final" designation from specific employees prior to creating the e-file, deselect the checkbox on individual employee records on the PR STP Process form, Employees tab.
