---
title: "Field Definitions: PR Earnings Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form/field-definitions-pr-earnings-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form/field-definitions-pr-earnings-codes-form"
---

# Field Definitions: PR Earnings Codes Form

The following is a list of field descriptions for the PR Earnings Codes form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Earnings Code

Enter a number (1-32,767) that identifies this earnings code.

## Description

Enter a description for this earnings code, up to 30 characters.
For Canadian users
If you want the descriptions on the pay stubs to appear in French and English, make sure that this field includes both French and English.
You should not create separate earnings codes for French and English. Instead, create a bilingual description for the codes you want to use on the bilingual stubs.

## Method

Select one of the following methods for calculating earnings. See [Determining Earnings Code Calculation Methods](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/earnings-code-calculation-methods) for more information.

- A-Amount

- D-Rate per Day

- F-Factored Rate per Hour

- G-Rate of Gross

- H-Rate per Hour

- S-Rate of STE

- V-Variable Factored Rate

- R-Routine (for Australian and Canadian users only)

- L-Allowance

## Routine

This field appears when you select the
 R-Routine option from the Method drop-down.
Enter the routine that the system will use to
 calculate this earnings code. Press F4 to see a list of initialized routines
 (in PR Routines).
For more information, see [Routines](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines).

## Factor

Factor field on the PR Earnings Codes form
If applicable, enter the factor (number) by
 which to multiply the rate for this calculation. Enter 0.5 for half time, 1.0 for regular
 time, 1.5 for time and one half, and 2.0 for double time. You can also enter
 0.00
 if you want to track hours where a rate/amount is not added into PR Timecard Entry.
Note: Earnings codes with a factor greater than 1 are considered premium time on cost reports.

## Subject to Auto Earnings

Check this box if these earnings are subject to auto earnings (i.e., included in the basis amount for calculating automatic earnings).

## Subject to Craft/Class Add-ons

Check this box if this is a standard earning code that you want to include in the basis amount for calculating craft and class add-on earnings.

## True Earnings for Payroll Reports

The True Earnings for Payroll Reports checkbox in the PR Earnings Codes form.
The True Earnings for Payroll Reports checkbox in the PR Earnings Codes form
Select this checkbox if you want these earnings to be considered true earnings on the PR Certified Payroll Transcript, PR Certified Payroll Transcript With Class Info, and JC Cost reports.
When you select this checkbox, the system
 disables the Include in Liability Distributions box.
Do not select this checkbox for negative earnings codes (salary reductions) or other "earnings" like per diems, that are not taxed as an earning.
Note: Negative non-true earnings (salary reductions) are always included in the certified payroll reports, where they are reported as deductions.
Note: Positive non-true earnings (such as per diems or
 reimbursements) are generally excluded from the certified payroll reports, but you can
 include them among reported earnings by selecting the Include Detail on certified reports check
 box on the PR Earnings Codes form.

Related information

- [Include Detail on certified reports](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form/field-definitions-pr-earnings-codes-form#ID-00036f99--en)

## Track Hours for ACA

Track Hours for ACA checkbox on the PR ACA Process form, Transmission History tab
Select this checkbox to track hours for the Affordable Care Act (ACA) on the PR ACA 1095-C Employees and HR Look Back Analysis reports. Selecting this checkbox flags the earnings code that represent hours of service or will be used in lieu of hours of service, such as for vacations or personal time off. The system then looks at timecards posted to these earnings codes.

Related information

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

- [Set up Earnings Codes: United States](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-united-states)

- [Initialize ACA Data Automatically from Payroll](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s/initialize-aca-data-automatically-from-payroll)

## Supplemental Earnings

(U.S. only) The Supplemental Earnings checkbox on the PR Earnings Codes form, Info tab.
Select this checkbox if these earnings are considered supplemental earnings for Federal tax calculations.
 When selected, Federal tax will calculate on supplemental earnings associated with both regular and bonus pay sequences based on the [YTD Supplemental Earnings Threshold](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-federal-info-form/field-definitions-pr-federal-information-form#concept-52a7ad3e-3b9c-4ba8-b660-b0bdb9208902--en) and [Tax Rate](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-federal-info-form/field-definitions-pr-federal-information-form#concept-e7bdb08b-9bf7-424e-a094-958d6f137b2d--en) defined in PR Federal Info. If an employee's supplemental wages exceed the threshold for the tax year, the system applies the supplemental tax rate
Note: When supplemental earnings tied to a regular pay sequence (where the Bonus checkbox is unselected) exceed the threshold, they are taxed using the Tax Rate in PR Federal Info. The remaining supplemental wages for that pay period (those not flagged as supplemental earnings) are taxed via the standard Federal tax routine. The taxes calculated using the PR Federal Info rate are then added to the taxes generated by the standard Federal routine..

## Include in Liability Distributions

The system enables this checkbox when you do not check the True Earnings for Payroll Reports checkbox.
Check the Include in Liability Distributions box to have the system include the earnings code in liability distributions to the job. If you do not check this box, the system does not distribute the earnings to the job, but the payroll department associated with the employee (PR Employees) receives the benefit.

## Include in OT Calculations

Check this box if you want to include this earnings code in determining the basis for overtime calculations.
Note: The system disables this checkbox for factors greater than 1.0.

## Include in Salary Distribution Calculations

The system enables this checkbox if you select A-Amount from the Method drop-down.
Check this box to include this earning code in determining salary earnings.
Note: If you check this box and use this code to post hours by job, equipment, or account, the salaried employee’s pay rate and amount default to zero. When you process the PR Salary Distribution form, the system calculates the correct rate and amount. Employee timecards that are still in a batch are not included in processing.

## Include in Remote Timesheet Entry

Check this box if you want foremen and
 employees to be able to use this earnings code when entering timesheets in PR My Timesheet.
 For more information, see [Entering Timesheets](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-timesheets).

## Earnings Type

Enter the earnings type (from HQ Earn Types) that determines which GL Account the system expenses when updating earnings to GL.
If you post earnings to a job, the system uses the GL accounts set up for the JC department. If you do not post earnings to a job, then the system references the PR department to find the GL account.

## JC Cost Type

Enter the cost type (from JC Cost Types) that the system uses for interfacing earnings to JC.

## Limit Period

Specify the limit period to apply to automatic earnings. Initially defaults as 'None'.

- N-None

- A-Annual

- P-Pay Period

- M-Monthly

If the limit specified in the Limit for Auto Earnings field is greater than 0.00, the system calculates the accumulated earnings for the time period specified here when calculating auto earnings.

## Limit Amount

The Limit Amount field on the PR Earning Codes form, Info tab.
Enter the limit amount for this earnings code
 or 0.00 if no limit applies. The Limit Period field determines whether
 this limit applies annually, monthly, or by pay period. If the Limit Period
 field is set to is N-None, this field defaults as 0.00 and is disabled. If the earnings type
 associated with this code (Earnings Type field) has a limit
 (Annual
 Limit field, HQ Earn Types), then the field initially defaults that
 limit.
The amount specified here will be used as a default for each employee to which this code applies when posting automatic earnings. This amount may be overridden by employee in PR Automatic Earnings.

## Include Detail on certified reports

The Include Detail on certified reports checkbox in the PR Earnings Codes form.
Select this checkbox to break these earnings out on their own detail line of the PR Certified Payroll Transcript or the PR Certified Payroll Transcript With Class Info reports.
Leave this checkbox unselected to summarize these earnings in the “Other Taxable” or “Other Non-Taxable” fields on the Certified Payroll reports.
Note: Negative non-true earnings (salary reductions) are always included in the certified payroll reports, where they are reported as deductions. These amounts are printed on a separate detail line (if this checkbox is selected) or summarized in the "Other" fields (if this checkbox is not selected).
Note: Positive non-true earnings (such as per diem or reimbursements) are generally excluded from the certified payroll reports, but you can include them among reported earnings by selecting this checkbox.

Related information

- [True Earnings for Payroll Reports](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form/field-definitions-pr-earnings-codes-form#ID-00036f3b--en)

##
 Fringe Benefit Type

The Fringe Benefit Type drop-down on the PR Earnings Codes form
(Optional) Select one of the following fringe benefit classifications to be used with the LCPtracker or eMars (U.S. only) report:

- H - Health and Welfare

- V - Vacation/Holiday/Dues

- A - Apprenticeship Fund

- P - Pension

- O - Other

- C - Cash

- T-Travel and Subsistence (eMars only)Important: If you select T, also clear (deselect) the following check
 boxes:

- True Earnings for Payroll Reports

- Include Detail on certified reports

This combination of settings causes the report to display weekly total
 amounts for the employee in the Reimbursement column, and without creating
 additional rows in the report (since rows are intended to represent normal
 hourly “true earnings”).
These “reimbursement” (per diem, etc.) amounts
 are displayed in the report for informational purposes only and are not used by
 eMars for adjustments to reported weekly gross pay or net pay, nor for any
 other purpose.

## Automatic Update to Accounts Payable

Check this box to automatically create AP transactions from the amounts posted to this earnings code. Typically, you will only check this box for negative earnings.
Do not check this box if this earnings code will not processed for Accounts Payable.
Note: While you can set up salary reductions as negative earnings, it is recommended that you set up salary reductions as pre-tax deductions. For more information, see [Setting Up Pre-Tax Deductions](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions).

## Vendor

Enabled only when Automatic Update to Accounts
 Payable option is checked.
Specify the vendor (set up in AP Vendors) that
 will be used when creating AP transactions to pay this earnings code. Entry is
 required.

## Separate AP Transactions Per Employee

This field is enabled only when the Automatic Update to Accounts Payable checkbox is selected.
 Select this checkbox to create separate and multiple AP transactions for each Vendor/PRGroup/PE Date/Earn Code/Employee combination.
Do not select this checkbox if you want a single AP transaction created for each Vendor/PR Group/PE Date/Earn Code combination.

## Payable Type

Enabled only when Automatic Update to Accounts Payable option is checked.
Specify the payable type (set up in AP Payable Types) for this earnings code. The payable type specified here determines the GL Payable Account to credit when the AP transaction is posted. Entry is required.

## GL Account

Enabled only when Automatic Update to Accounts Payable option is checked.
Specify the GL Account to debit when the AP transaction is posted. Entry is required.

## Frequency

Enabled only when Automatic Update to Accounts Payable option is checked.
Enter the frequency code (set up in HQ Frequency Codes) that identifies how often transactions posted with this earnings will be updated to AP. Entry is required.

## Include In STP Gross Amounts

Include In STP Gross Amounts checkbox in the PR Earnings Codes form, Addl Info tab (Australia only)
Not used for STP Phase 2.
Select this checkbox in order to include these earnings amounts within calculations of employees' year-to-date reportable gross earnings (PAYG Items 'INBGross' and 'HolidayGross') for Single Touch Payroll (STP) reporting.
When you select this checkbox on an earnings code, the system adds each employee's calculated earnings amounts to their reportable gross earnings during STP processing.

## ATO Category

This field displays for Australian companies only.
Not used for STP Phase 2.
Select the Australian Tax Office category to associate with this earnings code. The selection you make here does not impact payroll processing, but it is required to ensure that amounts are accurately included in your year-end reporting to the ATO.
The following table details the relationships between the ATO categories and the associated year-end reports.
ATO Category
Relationship to Year-End Reporting

ETPA – Employment Termination, Annual Leave (Payment After 17Aug1993)
Individual Non-Business Summary – Gross Payments

ETPL – Employment Termination, Long Servvice Leave (Payment After 17Aug1993)
Individual Non-Business Summary – Gross Payments

LSAR – Leave, Lump Sum A Type R (Leave Payment After 15Aug1978 when termination is for reason of Redundancy)
Individual Non-Business Summary – Lump Sum A, Type R

LSAT – Leave, Lump Sum A Type T (Long Service Leave Payment after 15Aug1978 and before 18Aug1993)
Individual Non-Business Summary – Lump Sum A, Type T

LSB – Long Service Leave, Lump Sum B
Not supported by Viewpoint

LD – Leave (Annual and Long), Death
Non-Taxable, Not recorded on a Payment Summary

ETP – Employment Termination Payment
This code does not directly correspond to a report.
 However, the earnings code with this category should be included in the
 basis of a deduction code with an ATO category of TE, which will be associated with a year-end report. For
 more information on the ATO category setup for a deduction code, see the F1
 help for the [ATO Category](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-00036b98--en) help on the PR
 Deductions/Liabilities form.

ETPV – Employment Termination, Invalidity
This code does not directly correspond to a report.
 However, the earnings code with this category should be included in the
 basis of a deduction code with an ATO category of TEV, which will be associated with a year-end report. For
 more information on the ATO category setup for a deduction code, see the F1
 help for the [ATO Category](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-00036b98--en) help on the PR
 Deductions/Liabilities form.

ETPD – Employment Termination, Death
This code does not directly correspond to a report.
 However, the earnings code with this category should be included in the
 basis of a deduction code with an ATO category of TED, which will be associated with a year-end report. For
 more information on the ATO category setup for a deduction code, see the F1
 help for the [ATO Category](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-00036b98--en) help on the PR
 Deductions/Liabilities form.

ETPR – Employment Termination , Redundancy/Early Retirement
This code does not directly correspond to a report.
 However, the earnings code with this category should be included in the
 basis of a deduction code with an ATO category of TER, which will be associated with a year-end report. For
 more information on the ATO category setup for a deduction code, see the F1
 help for the [ATO Category](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-00036b98--en) help on the PR
 Deductions/Liabilities form.

ETPU – Employment Termination , Unfair Dismissal/Harassment/Discrimination
This code does not directly correspond to a report.
 However, the earnings code with this category should be included in the
 basis of a deduction code with an ATO category of TEU, which will be associated with a year-end report. For
 more information on the ATO category setup for a deduction code, see the F1
 help for the [ATO Category](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-00036b98--en) help on the PR
 Deductions/Liabilities form.

## Allowance Type

Allowance Type field in the PR Earnings Codes form, Addl Info tab (Australia only)
Not used for STP Phase 2.
This field is enabled when you select AT - Allowance, Taxable or ANT - Allowance Non-Taxable from the ATO Category field.
Select from the list.
If you select O - Other, you must also make a selection in the Other Allowance Type field.
Note: If your company participates in the JobKeeper program and you need to report "top-up"payments made to your employees within the designated fortnightly periods, you must set up a dedicated JobKeeper earnings code for "top-up" payments and select O-Other in this field.

## Other Allowance Type

Other Allowance Type drop down in the PR Earnings Codes form, Addl Info tab, Australia only.
Not used for STP Phase 2.
This field is enabled when you select O - Other from the Allowance Type field.
Select from the list.

## Include in Employee Gross Amount calculation

(Australia) The Include in Employee Gross Amount calculation checkbox on the PR Earnings Code form, Add'l Info tab.
For use with STP Phase 2 only.
Select this checkbox to include earnings posted to this earnings code when calculating gross amounts for an employee.
If not selected (default), earnings posted to this earnings code will not be included in gross amount calculations for an employee.

## Include in Reportable Fringe Benefits Amount (RFBA) calculation

(Australia) The Include in Reportable Fringe Benefits Amount (RFBA) calculation checkbox on the PR Earnings Codes form, Add'l Info tab.
For use with STP Phase 2 only.
Select this checkbox to include earnings posted to this earnings code when calculating reportable fringe benefit amounts for an employee.
If not selected (default), earnings posted to this earnings code will not be included in reportable fringe benefit amount calculations for an employee.

## STP Category

(Australia) The STP Category drop-down on the PR Earnings Codes form, Add'l Info tab.
For use with STP Phase 2 only.
From the drop-down, select the appropriate category (if any) for STP Phase 2 reporting of this earnings code.
If you select one of the following options, additional entry is required (as indicated):

- LSE - Lump Sum E (requires entry in the Lump Sum E Financial Year field)

- AT - Allowance, Taxable (requires entry in the Allowance Code field)

- ANT - Allowance, Non-Taxable (requires entry in the Allowance Code field)

## Allowance Code

(Australia) The Allowance Code drop-down on the PR Earnings Codes form, Add'l Info tab.
For use with STP Phase 2 only.
This field is enabled only when you select AT (Allowance, Taxable) or ANT (Allowance, Non-Taxable) from the STP Category drop-down.
Select the appropriate allowance code for STP Phase 2 reporting of this earnings code.

- CD - Cents per Kilometre

- AD - Award Transport Payments

- LD - Laundry

- MD - Overtime Meals

- RD - Travel and Accommodations

- TD - Tools

- KN - Tasks and Services

- QN - Qualifications

- OD - Other (requires selection in the Other Allowance Code drop-down)

## Other Allowance Code

(Australia) The Other Allowance Code drop-down on the PR Earnings Codes form, Add'l Info tab.
For use with STP Phase 2 only.
This field is enabled only when you select OD (Other) from the Allowance Code drop-down.
Select the appropriate other allowance code for STP Phase 2 reporting of this earnings code.

- ND - Non-deductible

- U1 - Uniform

- V1 - Private Vehicle

- H1 - Home Office

- T1 - Transport and Fares

- G1 - General

## Lump Sum E Financial Year

(Australia) The Lump Sum E Financial Year field on the PR Earnings Codes form, Add'l Info tab.

For use with STP Phase 2 only.
This field is enabled only when you select LSE - Lump Sum E option from the STP Category drop-down.
Enter the prior financial year (YYYY) to which the arrears payment applies for this earnings code.

## Insurable Earnings

(Canada only) Insurable Earnings field on the PR Earnings
 Code form, Addl Info tab
Select this checkbox to include the amounts
 for this earnings code in Insurable Earnings for ROE reporting. You should only select this
 checkbox if this is an earnings for which EI premiums are paid or if the Canada Revenue
 Agency rules specify this earnings to be insurable.
Do not select this checkbox if the earnings associated with this earnings code should always be excluded from Insurable Earnings for ROE reporting.

Related information

- [Set up Earnings Codes: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada)

- [Set up Separation Payments](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-separation-payments)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

## Insurable Hours

Insurable Hours checkbox on the PR Earnings
 Code form, Addl Info tab.
This topic only applies to Canada.
Select this checkbox to include the hours for
 this earnings code in Insurable Hours for ROE reporting. You should only select this check
 box if the hours worked for this earnings are insurable per Canada Revenue Agency
 rules.
Do not select this checkbox if the hours associated with this earnings code should always be excluded from Insurable Hours for ROE reporting.

Related information

- [Set up Earnings Codes: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada)

- [Set up Separation Payments](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-separation-payments)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

## Separation

Separation checkbox on the PR Earnings Code
 form, Addl Info tab.
This topic only applies to Canada.
Select this checkbox if the earnings
 associated with this earnings code are paid to the employee due to separation (vacation,
 statutory holiday, or other monies). Requires selection in the Category
 drop-down. Earnings with this earnings code will be reported as a separation payment in ROE
 reporting.
Do not select this checkbox if the earnings
 code does not represent a separation payment that needs to be reported as such in ROE
 reporting.

Related information

- [Set up Earnings Codes: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada)

- [Set up Separation Payments](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-separation-payments)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

## Category

Category drop-down on the PR Earnings Code
 form, Addl Info tab.
This topic only applies to Canada.
Enabled only if the Separation
 checkbox is selected.
From the drop-down list, select the separation payment category.

- V-Vacation - Select for earnings that will be
 reported as vacation pay due to separation. Requires entry in the Vacation Pay
 Type field.

- SH-Statutory Holiday - Select for earnings that will be reported as statutory holiday pay due to separation.

- OM-Other Monies - Select for earnings that will be
 reported as separation pay other than vacation or statutory holiday pay. Requires
 entry in the Other Monies Code drop-down.

Related information

- [Set up Earnings Codes: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada)

- [Set up Separation Payments](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-separation-payments)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

## Other Monies Type

Other Monies Type drop-down on the PR Earnings
 Code form, Addl Info tab.
Enabled when you select the OM-Other Monies separation payment category.
From the drop-down list, select the appropriate other monies type.
B05-Bonus (Holiday)
J00-Retroactive pay adjustment

B06-Bonus (Production/Incentive)
O00-Other

B07-Bonus (Event)
Q00-Profit sharing

B08-Bonus (Staying/Contract complete/EOS)
R00-Retiring allowance/leave credits

B09-Bonus (Separation or retirement)
S00-Settlement pay

B10-Bonus (Closure)
T00-Payout of banked overtime

B11-Bonus (Other)
U12-SUB Maternity/Parental/etc.

E00-Severance Pay
U13-SUB Layoff

G00-Gratuities
U14-SUB Illness

H00-Honorariums
U15-SUB Training

I00-Sick leave credits
Y00-Pay in lieu of notice

Related information

- [Set up Earnings Codes: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada)

- [Set up Separation Payments](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-separation-payments)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

## Vacation Pay Type

Vacation Pay Type drop-down on the PR Earnings
 Code form, Addl Info tab.
Enabled when you select the V-Vacation separation payment category.
From the drop-down list, select the vacation payment type.

- 2-Paid because no longer working - Vacation pay paid to the employee due to layoff or termination of employment.

- 3-Paid for a vacation leave period - Vacation pay
 paid to the employee for a specific period of leave falling after the last day for
 which the employee was paid (i.e. Last Day for Which Paid field in PR
 Employee, Info tab), when the employee plans to take vacation leave that has been
 granted by the employer and will occur during the interruption of earnings.

- 4-Anniversary - Vacation pay paid to the employee for a specific date each year (i.e. anniversary payments that fall within an interruption of earnings).

Related information

- [Set up Earnings Codes: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada)

- [Set up Separation Payments](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-separation-payments)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

## Special

Special checkbox on the PR Earnings Code
 form, Addl Info tab.
This topic only applies to Canada.
Select this checkbox if the earnings
 associated with this earnings code are paid to the employee for a special leave of absence
 (e.g. paid sick leave, maternity leave, or wage-loss indemnity). Requires selection in the
 Type
 and Period drop-downs below. Earnings with this earnings code will be reported
 as a special payment in ROE reporting.
Do not select this checkbox if this earnings code does not represent a special payment that needs to be reported as such in ROE reporting.

Related information

- [Set up Earnings Codes: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada)

- [Set up Separation Payments](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-separation-payments)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

## Type

Type drop-down on the PR Earnings Code form,
 Addl Info tab.
Enabled when you select the Special checkbox.
From the drop-down list, select the appropriate special payment type.

- PSL01-Paid Sick Leave - Insurable sick leave paid by the employer to the employee.

- MAT01-Maternity - Insurable maternity, parental, compassionate care, or parents of critically ill children leave paid by the employer to the employee after the employee stops working.

- WLI01-Wage Loss Indemnity (Not EI Insurable) -
 Non-insurable wage-loss indemnity plan payments paid to the employee by a third party
 after the employee stops working.

- WLI02-Wage Loss Indemnity (EI Insurable) - Insurable
 wage-loss indemnity plan payments paid by the employer to the employee after the
 employee stops working.

Related information

- [Set up Earnings Codes: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada)

- [Set up Separation Payments](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-separation-payments)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

## Period

Period drop-down on the PR Earnings Code form,
 Addl Info tab.
Enabled when you select the Special checkbox.
From the drop-down list, select the frequency at which this special payment will be made to the employee.

- D-Per Day

- W-Per Week

Related information

- [Set up Earnings Codes: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada)

- [Set up Separation Payments](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-separation-payments)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

## DL Code

Enter the deduction and liability codes that include these earnings in their subject accumulations and basis amounts for calculations. The D/L’s type and description are displayed to the right of this field.

## Subject Only

This box applies to United States users only.
Check this box if the earnings are to be included in the subject amounts only (and not the calculations) for this deduction or liability.
Do not check this box if the earnings are to be included in both the subject amount and the basis for calculation for this deduction or liability.
Examples of typical uses

- For deductions, a typical example would be for federal withholding. Earnings that are 'subject only' will be included in the “Wages, Tips, and Other Compensation” amount on the W-2, but will not be included in the basis for calculating withholding tax on a pay check.

- For liabilities, it is a method to distribute the liability to earnings without the earnings being a basis for the calculation. For example, you might assign a '401k matching' liability to all earnings codes that are subject to the liability, including the 401k earnings. Then, for all earnings except the 401k earnings, you would check the 'subject only' box for the 401k liability.

Assuming that negative earnings are excluded from liability distributions (you
 did not select the True earnings for Payroll
 Reports checkbox in PR Company Parameters), this will allow the
 liability to be distributed across the regular earnings rather than with the
 401k earnings, and to be updated to JC

## Subject Earnings: Subject Earn Code

Enter the earnings code that is subject to this
 allowance or earnings routine. Press F4 for a list of earnings codes.
