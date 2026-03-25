---
title: "Field Definitions: PR STP Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-process-form/field-definitions-pr-stp-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-process-form/field-definitions-pr-stp-process-form"
---

# Field Definitions: PR STP Process Form

The following is a list of field descriptions for the PR STP
 Process form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Tax Year

Tax Year field on the PR STP Process form
Displays the tax year for the current, existing record.
This field is not for entering new tax years. If you want to enter a new tax year, do so in the HQ ATO Tax Years form, or to select from existing records in that form, press F4.

## Submission

Submission field on the PR STP Process form
Displays the submission number assigned to the current, existing record.
If you want to create a new submission for the displayed tax year, enter 'N' or '+'.
The submission number becomes part of the Submission ID, which is used to uniquely identify each submission lodged with the ATO.

## STP Phase

The STP Phase field on the PR STP Process form.

This is a display-only field.
Indicates the STP Phase for the currently selected tax year/submission. This field populates during data generation based on the STP Phase selected in the Submission Data Format field in PR STP Generate Data (accessed by clicking Generate Submission Data in PR STP Process).

## Company Name

Company Name field on the PR STP Process form
This field defaults the Company Name defined for the specified tax year in HQ ATO Tax Years. You may override the company name if needed; however, changes are not updated to HQ ATO Tax Years.

## Address 1

Address 1 field on the PR STP Process form, Info tab.
This field defaults from the Address 1 field in HQ ATO Tax Years for the specified tax year. You may override this address if needed; however, the changes are not updated to HQ ATO Tax Years.

## Address 2

The Address 2 field on the PR STP Process form.
This field defaults from the Address 2 field in HQ ATO Tax Years for the specified tax year. You may override this address if needed; however, the changes are not updated to HQ ATO Tax Years.

## City

City field on the PR STP Process form, Info tab.
This field defaults from the City field in HQ ATO Tax Years for the specified tax year. You may override this city if needed; however, the changes are not updated to HQ ATO Tax Years.

## State

State field on the PR STP Process form, Info tab.
This field defaults from the State field in HQ ATO Tax Years for the specified tax year. You may override the state if needed; however, the changes are not updated to HQ ATO Tax Years.

## Country

Country field on the PR STP Process form, Info tab.
This field defaults as blank and assumes Australia. You will only need to enter a country here if you overrode the address information and the country is other than Australia.

## Postal Code

Postal Code field on the PR STP Process form, Info tab.
This field defaults from the Postal Code field in HQ ATO Tax Years for the specified tax year. You may override this postal code if needed; however, the changes are not updated to HQ ATO Tax Years.

## ABN

ABN field on the PR STP Process form, Info tab.
This field defaults from the Business # (ABN) field in HQ ATO Tax Years for the specified tax year. You may override this number if needed; however, the changes are not updated to HQ ATO Tax Years.
Your company's ABN becomes part of the Submission ID, which is used to uniquely identify each submission lodged with the ATO.

## Branch

Branch field on the PR STP Process form, Info tab.
This field defaults from the Branch # field in HQ ATO Tax Years for the specified tax year. You may override the branch number if needed; however, the changes are not updated to HQ ATO Tax Years.
Your entry in this field becomes part of the Submission ID, which is used to uniquely identify each submission lodged with the ATO.

## Previous BMS ID

(Australia) The Previous BMS ID field on the PR STP Process form, Info tab.

For use with STP Phase 2 only.
This field is enabled only when the Signature checkbox is unselected (that is, you have not clicked the Tick this box button in the Signature section of the form).
Enter the identifier for the previous STP-enabled payroll software solution (Business Management System software) that you used prior to using Vista.
Note: This field is intended to be used once (on a single submission of Type F-Fix YTD only).

## Name

The contact Name field on the PR STP Process form, Info tab.
Entry in this field is required for STP Phase 2 submissions.
This field defaults the contact name from the Given Name, Middle Name, and Surname fields in HQ ATO Tax Years for the specified tax year. You may override the contact name if needed; however, the changes are not updated to HQ ATO Tax Years.

## Email

Email field on the PR STP Process form, Employees tab
Defaults the email address for the employee from PR Employees. You may make changes to the email address if needed; however, changes do not update to PR Employees. If you want the change to be permanent, manually update the email address in PR Employees.

## Phone

Phone field on the PR STP Process form, Employees tab
Defaults the Phone number for the employee from PR Employees. You may make changes to the phone number if needed; however, changes will not update to PR Employees. You will need to manually update the Phone number in PR Employees.

## Submission Type

Submission Type field on the PR STP Process form
This is a display-only field.
 The value of this field is based on your selection in the Submission Options section of the PR STP Generate Data form. Allowed values are P-Pay Event, R-Full File Replacement, and F-Fix YTD.

## Payee Count

Payee Count field on the PR STP Process form
This is a display-only field. It displays the number of employees with payroll data captured and incorporated into this submission during the generate submission data process.
Note: The number displayed in this field may be higher than the number of employee names shown to you in the Employees tab due to your security access settings.

## PR Group

PR Group field on the PR STP Process form
This is a display-only field. The value of this field comes from the same-named field in the PR STP Generate Data form, if a value is entered there. Any value in this field indicates that only data for this single payroll group was included when this submission's data was generated.

## Total Gross Payments

Total Gross Payments field on the PR STP Process form
The value in this field represents the employer total pay period amount of reportable gross salary or wages for all employee pay sequences reported in the pay event.
This is equivalent to the BAS label W1.
The field is enabled when Amounts Status is U - Amounts Unlocked and Submission Type is not F-Fix YTD.
For Fix YTD submissions, this field always displays a zero (0.00) amount and is not editable.
Note: The value in this field does not account for manual overrides in the PR Employee Accumulations form. If you have any manual adjustments in accumulations, use the traditional BAS reporting mechanism to report them.

## PR End Date

PR End Date field on the PR STP Process form
This is a display-only field. The value of this field comes from the same-named field in the PR STP Generate Data form, if a value is entered there. Any value in this field indicates that only data for this single pay period ending date was included when this submission's data was generated.

## Total PAYG Tax Withheld

Total PAYG Tax Withheld field on the PR STP Process form
The value in this field represents the employer total pay period amount of PAYG withholding for all employee pay sequences reported in the pay event.
This is equivalent to the BAS label W2.
The field is enabled when Amounts Status is U - Amounts Unlocked and Submission Type is not F-Fix YTD.

For Fix YTD submissions, this field always displays a zero (0.00) amount and is not editable.
Note: The value in this field does not account for manual overrides in the PR Employee Accumulations form. If you have any manual adjustments in accumulations, use the traditional BAS reporting mechanism to report them.

## Pay/Fix Date

Pay/Fix Date field on the PR STP Process form.
This is a display-only field.
 The value of this field comes from the PR STP Generate Data form based on the submission type as follows:

- P (Pay Event) - Date comes from the Pay Date field, and indicates that only employees paid on this date were included when this submission's data was generated.

- R (Full File Replacement) - Date matches the Pay Date of the original Pay Event that you specified as the submission to replace.

- F (Fix YTD) - Date comes from the Date field, and indicates only the "as at date" that you chose to assign to this update event (Fix YTD submission).

## Run Date (UTC)

Run Date (UTC) field on the PR STP Process form.

This is a display-only field, populated once you click Generate Submission Data (STP Phase 2 submissions) or Create E-File (STP Phase 1 submissions).
For a Phase 1 submission, this date represents the date (in local time) that the submission e-file was created.

For a Phase 2 submission of Type P-Pay Event or R-Full File Replacement, this date represents the date (in Coordinated Universal Time (UTC)) of the pay run. For a Phase 2 submission of Type F-Fix YTD, this date represents the date (in Coordinated Universal Time (UTC)) that the submission data was generated.

## Submission ID

Submission ID field on the PR STP Process form
This is a display-only field.
The system populates this field as follows:

- P-Pay Event / F-Fix YTD submissions - When you click Create E-File, the system populates this field with a number that is unique to this submission as required by the ATO. The Submission ID value combines your company's ABN, branch number (B), submission number (S), and a time stamp in this manner: 12345678901_B_S_yyyymmddhhmmss.


- R-Full File Replacement submissions - When you click Generate Submission Data, the system populates this field with the Submission ID of the original pay event submission that you selected to replace. Replacement submissions must use the same Submission ID as the original Pay Event submission in order to enable correct processing by the ATO.


## Status

Status field on the PR STP Process form.

This drop-down is disabled during the normal course of generating submission data and creating the e-file, and is updated automatically throughout the process. Once you create and save the e-file, this field is enabled.

- 0-Submission Initiated - Assigned to new tax year/submission record.

- 1-Submission Generated - Assigned when you generate submission data in PR STP Generate Data (accessed by clicking Generate Submission Data).

- 2-Validated - With error (s) - Assigned when validation (in PR STP E-File) encounters errors and user does not save the e-file.

- 3-Validated - Success - Assigned when no errors are found during validation, but user does not save the e-file.

- 4-E-File Created - Assigned when user saves the e-file, regardless of whether errors were encountered during validation. At this point, this field is enabled, allowing you to manually change the status to 5-E-File Lodged when appropriate.

- 5-E-File Lodged - Select this option when you have successfully lodged the e-file with the ATO.

Note: Once the e-file is saved and this field is enabled, you can only set the status to 4-E-File Created or 5-E-File Lodged. If you need to edit or delete a submission, click Untick the box. This deselects the Signature checkbox and resets the Status to 1-Submission Generated.

## Status: Amounts

Status: Amounts drop down on the PR STP Process form.
This drop down is enabled only when the submission Status is 1 - Submission Data Generated and the Signature checkbox is not selected.
 Once you click Tick the box (which selects the Signature checkbox), the system sets this drop down to Amounts Locked and disables it.Note: Note that for submissions with a Submission Type of F-Fix YTD, the Total Gross Payments and Total PAYG Tax Withheld fields remain locked even when this drop down is set to Amounts Unlocked. Those fields are always zero (0.00) and always locked for any submission of type F-Fix YTD.

## Signatory

Signatory field on the PR STP Process form.

This field is disabled for new submissions (those with a submission Status of 0-Submission Initiated) and submissions with the Signature checkbox selected.
Once you generate submission data (via the Generate Submission Data button), the Status changes to 1-Submission Data Generated and this field is enabled.
Enter your name if you agree with the conditions stated above (beginning with "I am notifying the ATO. . .").
Once you enter your name and date, click Tick the box to sign the declaration with your specified credentials and enable the Create E-FIle button. Once the Signature checkbox is selected, this field is disabled again.

## Date Signed

Date Signed field on the PR STP Process form

This field is disabled for new submissions (those with a submission Status of 0-Submission Initiated) and submissions with the Signature checkbox selected.
Once you generate submission data (via the Generate Submission Data button), the Status changes to 1-Submission Data Generated and this field is enabled.
Enter the date if you agree with the conditions stated above (beginning with "I am notifying the ATO. . .").
Once you enter your name and date, click Tick the box to sign the declaration with your specified credentials and enable the Create E-FIle button. Once the Signature checkbox is selected, this field is disabled again.

## Signature checkbox

Signature checkbox in the Signature section of the PR STP Process form
This is a display-only checkbox. Use the adjacent Tick button to select or deselect the checkbox.
The Tick button is enabled when the submission Status is greater than '0 - Submission Initiated' and less than '5 - E-File Lodged', but only after you enter values in the Signatory and Date Signed fields.

When you use this button to select the checkbox, the system locks your submission and all fields are disabled, with the exception of the Tick button itself, the Create E-File button, and later (after you've created the e-file), the submission Status drop-down.
If you wish to make changes to any other fields, use the Tick button to clear the Signature checkbox first. This reverts the Submission status to '1 - Submission Data Generated', and unlocks most fields.

## Employee

Employee field on both the PR STP Employee form and the PR STP Process form, Allowances tab
The PR STP Employee form is accessible from the PR STP Process form (Employees tab) by double-clicking any employee record in the grid.
This field displays the employee name for each record (row). The system does not allow manual adds, edits, or deletes in this field.
The grid becomes populated with data during the data gathering process that occurs when you click the Generate button on the PR STP Generate Data form.

## TFN

TFN field on the PR STP Process form, Employees tab.

Defaults the Tax File Number specified for the employee in PR Employees.
Changes to the TFN are permissible in this form; however, you should only need to do so if the value here does not match the TFN number for the employee in PR Employees.
 For example, the employee's TFN is incorrect in PR Employees, but you discover the error after you have already generated submission data. In which case, you must first change the TFN in PR Employees, and then either regenerate the submission data or manually change the TFN in this field. If you opt to manually change it here, the system only allows the entry if it matches the TFN in PR Employees.

## Surname

Surname field on the PR STP Process form, Employees tab
Defaults the Last Name specified for the employee in PR Employees. You may override the surname if needed; however changes are not updated to PR Employees. You will need to manually update the Last Name in PR Employees.

## Given Name

Given Name field on the PR STP Process form, Employees tab
Defaults the First Name specified for the employee in PR Employees. You may override the given name if needed; however changes are not updated to PR Employees. You will need to manually update the First Name in PR Employees.

## Middle Name

Middle Name field on the PR STP Process form, Employees tab
Defaults the Middle Name specified for the employee in PR Employees. You may override the middle name if needed; however changes are not updated to PR Employees. You will need to manually update the Middle Name in PR Employees.

## Date of Birth

Date of Birth field on the PR STP Process form, Employees tab
Defaults the Birth Date specified for the employee in PR Employees. You may override the date of birth if needed; however changes are not updated to PR Employees. You will need to manually update the Birth Date in PR Employees.

## Address 1

The Address 1 field on the PR STP Process form, Employees tab.

Defaults the address for the employee from PR Employees. You may make changes to the address if needed; however, changes will not update to PR Employee. You will need to manually update the address in PR Employees.

## Address 2

The Address 2 field on the PR STP Process form, Employee tab.

This field displays for STP Phase 2 submissions only.
Defaults the Add'l Address for the employee from PR Employees. You may make changes to the address if needed; however, changes will not update to PR Employees. You will need to manually update the Add'l Address in PR Employees.

## City

City field on the PR STP Process form, Employees tab
Defaults the City for the employee from PR Employees. You may change the city if needed; however, changes will not update to PR Employees. You will need to manually update the City in PR Employees.

## State

State field on the PR STP Process form, Employees tab
Defaults the State for the employee from PR Employees. You change the state if needed; however, changes will not update to PR Employees. You will need to manually update the State in PR Employees.

## Postal Code

Postal Code field on the PR STP Process form, Employees tab
Defaults the Postal Code for the employee from PR Employees. You may change the postal code if needed; however, changes will not update to PR Employees. You will need to manually update the Postal Code in PR Employees.

## Country

Country field on the PR STP Process form, Employees tab
Defaults the Country for the employee from PR Employees. You may change the country if needed; however, changes will not update to PR Employees. You will need to manually update the Country in PR Employees.

## Email

Email field on the PR STP Process form, Info tab.
Entry in this field is required for STP Phase 2 submissions.
This field defaults from the Email field in the HQ ATO Tax Years form for the specified tax year. You may override the email address if needed; however, the changes are not updated to the HQ ATO Tax Years form.

## Phone

Phone field on the PR STP Process form, Info tab.
This field defaults from the Phone field in HQ ATO Tax Years for the specified tax year. You may override the phone number if needed; however, the changes are not updated to HQ ATO Tax Years.

## Commencement Date

Commencement Date field on the PR STP Process form, Employees tab.
Entry in this field is required for STP Phase 2 submissions.
This field's value comes from the Most Recent Hire Date field in the PR Employees form.

## Cessation Date

Cessation Date field on the PR STP Process form, Employees tab
This field's value comes from the Termination Date field in the PR Employees form.

## Cessation Reason

The Cessation Reason field on the PR STP Process form, Employees tab.

This field displays for STP Phase 2 submissions only.
This field defaults from the Cessation Reason field in PR Employees (Add'l Info tab), and indicates the reason employment has ceased for the employee. You may change this value if needed; however, changes made here are not updated to PR Employees. You will need to manually change the Cessation Reason in PR Employees.

## Period Start Date

Period Start Date field on the PR STP Process form, Employees tab
For submission types 'P - Pay Event' and 'R - Full File Replacement', this field displays the start date of the pay period associated with the PR Group and PR End Date values that you supplied on the PR STP Generate Data form when generating data for this submission or for the original submission being replaced.
If you supplied no such values, this field displays the start date of the pay period associated with the Pay Date value that you supplied on the PR STP Generate Data form when generating data.
For submission type 'F - Fix YTD', this field displays the value in the Date field that you supplied on the PR STP Generate Data form when generating data for this submission.

## Period End Date

Period End Date field on the PR STP Process form, Employees tab
For submission types 'P - Pay Event' and 'R - Full File Replacement', this field displays the ending date of the pay period associated with the PR Group and PR End Date values that you supplied on the PR STP Generate Data form when generating data for this submission or for the original submission being replaced.
If you supplied no such values, this field displays the ending date of the pay period associated with the Pay Date value that you supplied on the PR STP Generate Data form when generating data.
For submission type 'F - Fix YTD', this field displays the value in the Date field that you supplied on the PR STP Generate Data form when generating data for this submission.

## Final

Final field on the PR STP Process form, Employees tab
Select this checkbox only for employees that meet these criteria:

- no further wages will paid for this tax year, AND

- the YTD information can be finalised by the ATO and released to the employee

For each employee for whom you select this checkbox, you do not need to create a separate finalisation submission.

## Term Before TFND

Term Before TFND field on the PR STP Process form, Employees tab
This field displays for STP Phase 1 submissions only.
Vista’s STP data generation process always leaves this checkbox unselected.
You should only select this box if the employee was terminated before you had an opportunity to complete reporting of the employee’s TFN declaration to the ATO.

## Residency Status

Residency Status field on the PR STP Process form, Employees tab
This field displays for STP Phase 1 submissions only.
Vista's STP data generation process selects one of the following three values, according to the configuration encountered in the PR Employees form when you click the Generate Submission Data button:
R-Resident

- the PAYG Income Type field is set to S - Salary or wages, AND

- the Nonresident Alien checkbox is not selected

N-Non-resident

- the PAYG Income Type field is set to S - Salary or wages, AND

- the Nonresident Alien checkbox is selected

W-Working Holiday Maker

- the PAYG Income Type field is set to H - Working holiday maker

Tip: If you opt to make changes in this field, consider making changes at the source in the PR Employees form so that subsequent STP data generation processes will take advantage of your changes.
Important: If the employee's status has changed from working holiday maker to regular employee (or vice versa), you must update PAYG Income Type in the PR Employees form prior to generating data for your STP submission in order for the employee's gross earnings amounts and PAYG withholding amounts to be reported under the correct categories within the STP e-file.

## Payment Basis

Payment Basis field on the PR STP Process form, Employees tab
This field displays for STP Phase 1 submissions only.
If the present submission is the first ever for an employee, by default the system sets the value to F-Full Time. You can opt to change the value in this field.
If you make a manual change to this field for the present submission, the next time this employee appears in a submission, the system will use the value you set now as the default for that submission.

## Tax-free Threshold

Tax-free Threshold field on the PR STP Process form, Employees tab
This field displays for STP Phase 1 submissions only.
If the rebate has been claimed, Vista selects this checkbox.
Vista’s STP data generation process determines whether the rebate has been claimed (and whether the checkbox should be selected) based upon the employee’s Filing Status in the PR Employees form at the time you click the Generate Submission Data button:

- the system selects the checkbox only if the value in the Scale field for the
 employee's federal tax deduction code (PAYG tax) is set to 2 or 92.

- if the value in the Scale field is any other value (including null), the system leaves the checkbox unselected

Tip: If you opt to make changes in this field, consider making changes at the source in the PR Employees form so that subsequent STP data generation processes will take advantage of your changes.

## Study/Training Loan

Study/Training Loan field on the PR STP Process form, Employees tab.
This field displays for STP Phase 1 submissions only.
Vista selects this checkbox if an individual has any of the following study or training loans:

- Higher Education Loan Program (HELP) loan

- Student Start-up Loan (SSL)

- ABSTUDY Student Start-up Loan (ABSTUDY SSL)

- Trade Support Loan (TSL)

Vista’s STP data generation process determines whether the employee has any of these loans (and whether the checkbox should be selected) based upon the employee’s Filing Status in the PR Employees form at the time you click the Generate Submission Data button:

- the system selects the checkbox only if the value in the Scale field for the
 employee's federal tax deduction code (PAYG tax) is set to 91, 92, 93, 95,
 or 96.

- if the the value in the Scale field is any other value
 (including null), the system leaves the checkbox unselected.

Tip: If you opt to make changes in this field, consider making changes at the source in the PR Employees form so that subsequent STP data generation processes will take advantage of your changes.

## SSFS Loan

SSFS Loan field on the PR STP Process form, Employees tab.
This field displays for STP Phase 1 submissions only.
As of July 2019, this checkbox is disabled at all times. It is displayed on the form so
 that you can continue to review settings in historical submission data from tax year
 2018-19. Beginning with tax year 2019-20, the system intentionally leaves the checkbox
 unselected for all new records.
The ATO's current TFN declaration form, effective 1 July 2019, collects information about
 an employee's income contingent loans (ICLs) using one question instead of two, no longer
 asking a separate question about SSFS loans specifically. ICLs include:

- Higher Education Loan Program (HELP)

- VET Student Loan (VSL)

- Financial Supplement (FS)

- Student Start-up Loan (SSL)

- Trade Support Loan (TSL)

If an employee indicates 'Yes' to the ICL question on the new TFN
 declaration form, set the employee's Scale field to 91, 92, 93, 95,
 or 96, whichever is most appropriate to the employee's circumstances. Similarly, if an
 employee has an outstanding FS obligation as a result of a prior SSFS loan, set the
 employee's Scale field to 91, 92, 93, 95, or 96.
In response, during STP data generation, Vista selects the
 Study/Training Loan checkbox on the PR STP Process form,
 Employees tab. The system will leave the SSFS Loan checkbox
 unselected from this point forward, per ATO guidelines.

## Employment Basis

The Employment Basis drop-down on the PR STP Process form, Employees tab.

This field displays for STP Phase 2 submissions only.
Defaults from the Employment Basis field in PR Employees (Add'l Info tab), and indicates whether the employee is Full Time, Part Time, or Casual. You may change this value if needed; however, changes made here are not updated to PR Employees. You will need to manually change the Employment Basis in PR Employees.

## Tax Treatment Code

The Tax Treatment Code field on the PR STP Process form, Employees tab.

This field displays for STP Phase 2 submissions only.
Defaults the six-character tax treatment code computed for this employee during submission data generation. This code informs the ATO about the factors influencing the amount withheld for this employee.
The tax treatment code is a combination of the following components, based on the employee's TFN declaration:
ComponentPlacement in Tax Treatment Code
Category of Tax ScaleCharacter 1
Option (within each tax scale category)Character 2
Study and Training Support Loan (STSL)Character 3
Medicare Levy Surcharge (MLS)Character 4
Medicare Levy Exemption (MLE)Character 5
Medicare Levy Reduction (MLR)Character 6

For example:, Employee 100 has the following settings:

- Tax Scale Category = R (Regular)

- Option = D (Daily casual employee)

- Study and Training Support Loan = X (No STSL)

- Medicare Levy Surcharge = X (No surcharge)

- Medicare Levy Exemption = X (No exemption)

-
Medicare Levy Reduction = X (No reduction)

In this case, the generated tax treatment code for this employee would be RDXXXX.

## Tax Offset Amount

The Tax Offset Amount field on the PR STP Process form, Employees tab.

This field is visible for STP Phase 2 submissions only.
Defaults the annual Tax Offset amount specified for the PAYG deduction code in PR Employees (Filing Status tab) for this employee. You may override this value if needed; however, the change will not be updated to PR Employees. You must manually update the Tax Offset amount in PR Employees.

## Previous Payroll ID

The Previous Payroll ID field on the PR STP Process form, Employees tab.

This field displays for STP Phase 2 submissions only.
If applicable, enter the previous payroll identifier for this employee. This number can be either:

- the prior ID (Employee number) used for this employee previously within Vista or,

- the employee's ID within the previous STP-enabled payroll software solution used by the employer prior to Vista

Note: This field is intended to be used once (on a single submission of Type F-Fix YTD only).
