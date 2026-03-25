---
title: "Payroll Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.6/hr-and-payroll/payroll-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.6/hr-and-payroll/payroll-features"
---

# Payroll Features

Vista 2025.6 delivers on user-requested Payroll enhancements, fixes, and other improvements.

## Support Multiple 401k Catch-up Contribution Limits (U.S. only)

Effective January 1, 2025, the Secure Act 2.0 catch-up contribution limit for employees aged 60 through 63 increases to $11,250. To support this change, Vista now allows you to set up an additional 401k catch-up contribution limit in PR Pre-Tax Deduction Groups.
Changes to the PR Pre-Tax Deduction Groups form are as follows:

- Added a Secure Act 2.0 Annual Limit group box, which includes the following new fields:

- [Catch-up Contribution Limit #2](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form/field-definitions-pr-deduction-groups-form#concept-a7532e13-f0ba-48ec-ba13-8e18886bd5da--en)

- [Minimum Age](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form/field-definitions-pr-deduction-groups-form#concept-034a36a1-46d2-49f2-9ea6-410d1b161879--en)

- [Maximum Age](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form/field-definitions-pr-deduction-groups-form#concept-cfcxicvd--en)

- Relabeled the existing fields and moved them into a new Annual Limits group box.Existing Field:Changed To:
Standard Annual Contribution LimitStandard Contribution Limit
Catch up Annual Contribution LimitCatch-up Contribution Limit #1
Annual Compensation LimitCompensation Limit

Note: Catch-up Contribution Limit #1, previously applicable to employees aged 50 and over, now applies to employees aged 50-59 and 64 and over.

In addition to the changes made in PR Pre-Tax Deduction Groups, payroll processing has also been updated to apply the appropriate catch-up limit based on the employee's age within the year processed. For example, based on current IRS specifications, Catch-up Contribution Limit #1 will be applied to employees aged 50 and 59 or 64 and over and Catch-up Contribution Limit #2 will be applied to employees aged 60-63.

## Improved Handling of Federal Income Tax Withholding on Supplemental Earnings (U.S. only)

Per US Federal tax withholding rules on employee YTD supplemental wages greater than $1 million, you can now flag applicable earnings codes as supplemental, specify a YTD wage threshold, and tax rate. Payroll processing will automatically use the supplemental wage tax rate when the YTD threshold is exceeded.
To implement this functionality, the following changes were made:

- The PR Earnings Codes form now includes a new [Supplemental Earnings](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form/field-definitions-pr-earnings-codes-form#concept-242af983-4b5f-423b-a2b2-0db6c45c0dd2--en) checkbox (Info tab). Select this checkbox for all earnings considered supplemental earnings for Federal tax calculations.

- The PR Federal Info form now includes a new Federal Tax on Supplemental Earnings group box housing two new fields:

- [YTD Supplemental Earnings Threshold](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-federal-info-form/field-definitions-pr-federal-information-form#concept-52a7ad3e-3b9c-4ba8-b660-b0bdb9208902--en) - Use to specify the maximum YTD amount of supplemental wages earned by an employee that can be calculated using the standard Federal tax routine. (The IRS has set this at $1MM for 2025.)

- [Tax Rate](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-federal-info-form/field-definitions-pr-federal-information-form#concept-e7bdb08b-9bf7-424e-a094-958d6f137b2d--en) - Use to specify the Federal tax rate on supplemental earnings when an employee's YTD supplemental earnings exceed the threshold. This should be set equal to the current year's tax rate for the highest Federal tax bracket. (The rate for 2025 is 37%.)

 During payroll processing, supplemental earnings (those flagged for Supplemental Earnings in PR Earnings Codes) are handled as follows:

- If an employee's YTD supplemental earnings exceed the YTD threshold, the system calculates Federal tax on those earnings using the Tax Rate specified in PR Federal Info. This applies to both regular and bonus pay sequences.

-  If the employee's YTD supplemental earnings do not exceed the YTD threshold, Federal tax is calculated:

-  using the Federal tax routine when posted to a regular pay sequence.

- using the bonus rate specified at the Federal tax deduction level when posted to a bonus pay sequence.

Note: Supplemental earnings can be posted with regular earnings in a regular (non-bonus) pay sequence. When this occurs, supplemental earnings less than or equal to the YTD supplemental earnings threshold will be combined with regular earnings and taxed using the Federal tax routine. If supplemental earnings exceed the YTD threshold, they will be taxed using the supplemental tax rate and combined with the tax calculated on remaining earnings using the Federal tax routine.

For information about the setup for supplemental earnings, see [Required Setup for Supplemental Earnings](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/required-setup-for-supplemental-earnings-u.s.-only).

## Improved Leave Accruals/Balances

This release enhances the precision of employee leave calculations and balances. The system now supports up to 5 decimal places for accrual and available balance amounts, ensuring greater accuracy in leave processing.
 To implement this change, the datatype of selected columns used to store these values was changed from bHrs to bUnitCost. This modification prevents rounding errors during calculations, resulting in more precise and reliable leave balance values.
 The following is a list of the tables/columns affected by this change:
TableColumnName
PREL (PR Employee Leave)AvailBal
Cap1Accum
Cap2Accum
PRLH (PR Leave History)Amt
Accum1Adj
Accum2Adj
AvailBalAdj
PRAB (PR Leave Accrual Batch)Amt
Accum1Adj
Accum2Adj
AvailBalAdj
OldAmt
OldAccum1Adj
OldAccum2Adj
OldAvailBalAdj

Note: The Available Balance and Accrual #1 & #2 Limit values shown in PR Leave Codes and PR Employee Leave will remain at a 2 decimal place precision.

Additional changes made for this enhancement include:

- In PR Employee Leave, the Balance: Current Amount, Accrual Limit #1: Current Amount, and Accrual Limit #2: Current Amount display-only fields show amounts with five decimal places.

- In PR Leave Entry, the Accrual Limit #1, Accrual Limit #2, and Available Balance fields in the entry grid and the informational display above the grid now show values with five decimal places. In addition, the Amount field (on the Grid and Info tabs) now accommodates entry of five decimal places.

- Several stored procedures and computations now accommodate the new five decimal precision for available balances and accrual accumulations.

For a list of reports affected by this change, see the [Updated Leave Accrual / Leave Balance Reports](/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.6/system-tools/vista-reports#concept-9prn32v2--en__UpdatedLeaveReports) section of the Vista Reports release notes.

## Allow Using Liabilities with STE Calculation Method in Basis of Another Deduction/Liability

You can now link Craft and Employee liabilities that use the Straight Time Equivalent (STE) calculation method to other deductions and liabilities, enabling you to base the calculation of one liability on the STE amount of another. This is especially useful for liabilities that are a percentage of an employee's straight time equivalent earnings and are considered for pension, insurance, or tax purposes.
Changes implemented for this functionality include:

- For existing and new Craft and/or Employee liabilities, you can now select the Basis code on other dedn/liab codes checkbox in PR Deductions/Liabilities.Note: If you already have STE liabilities set up, the system no longer deselects the Basis code on other dedn/liab codes checkbox when you update the liability records. You must do that manually if applicable.

- When setting up the Basis codes for a deduction or liability, you can now include liabilities with an STE calculation method.

For Canadian users: This update supports scenarios where liability codes are both calculated based on a percentage of STE earnings and are pensionable (for CPP), insurable (for EI), taxable, or assessable for taxation purposes.

## Allow Zero-Amount Pay Sequence Records

You now have the option to include zero-amount pay sequence records in PR Employee Pay Seq Control.
A new Preserve zero-amount records in pay sequence checkbox was added to the PR Deductions/Liabilities form. If you select this checkbox for a deduction or liability code, employee/pay sequence records in PR Employee Pay Seq Control will include the deduction/liability, even if all amounts are zero (that is, zero hours were posted to the earnings code associated with the deduction/liability).
For more information, see [Set up Deductions/Liabilities to Allow Zero-Amount Pay Sequence Records](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-deductionsliabilities-to-allow-zero-amount-pay-sequence-records).

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
