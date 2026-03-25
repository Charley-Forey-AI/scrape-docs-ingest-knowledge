---
title: "Field Definitions: PR Deductions Liabilities Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form"
---

# Field Definitions: PR Deductions Liabilities Form

The following is a list of field descriptions for the PR Deductions Liabilities form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Dedn/Liab Code

 Enter a number (0-32,767) to uniquely identify this deduction or liability.
Determining the Code Sequence

## Description

 Enter a description for this deduction or liability, up to 30 characters.
For Canadian users
If you want the descriptions on the pay stubs to appear in French and English, make sure that this field includes both French and English.
You should not create separate deductions/liabilities for French and English. Instead, create a bilingual description for the codes you want to use on the bilingual stubs.

## Type

Deduction – Select this option if this code defines an employee’s payroll deduction (e.g. federal tax, state tax, etc.).
Liability – Select this option if this code defines an employer’s payroll liability (e.g. FICA, FUTA, SUTA, etc.).

##  Liability Type

 Enter the liability type (from HQ Liability Types) for this liability code. The liability type determines which GL account to debit when expensing this liability to either a PR or JC department. You may want to group similar liabilities together (e.g., taxes, insurance, union benefits, etc.).

## Calculation Category

Specify the category for this
 deduction/liability that identifies the type of calculation that should occur during
 processing.

- Federal

- State

- Local

- Insurance

- Craft

- Employee

- Any

Note: For liability codes that will be added to the Capped
 Basis of a craft (in PR Crafts) or craft template (in PR Craft Templates), you must select
 a calculation method of C-Craft, E-Employee, or A-Any. In addition, you must select a
 method of A-Amount or H-Rate per hour.
When a payroll timecard batch is processed, the various routines that calculate federal, state, local, insurance, craft, and employee deductions check to make sure the D/L code is in the right category.

Related information

- [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction)

- [Set Up a Roth 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-roth-401k-deduction)

- [Set Up a Catch-Up 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction)

- [Set Up a 401(k) Employer Match](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-401k-employer-match)

- [Set Up a Multi-Tiered 401(k) Employer Match](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-multi-tiered-401k-employer-match)

## Federal Type (CA)

(Canada) The Federal Type drop-down on the PR Deduction and Liabilities form, Info tab.
Enabled only when the Calculation Category is F-Federal.
Specify the type of federal deduction or liability.

- 1-Withholding

- 2-CPP

- 3-QPP

- 4-Employment Insurance

- 5-QPIP

## Federal Type

For use with Federal 'Calculation Category'
 only.
Specify the type of federal deduction or liability.

- 1-Withholding

- 2-FUTA

- 3-Social Security

- 4 -Medicare

This option is only used to breakdown
 Withholding, Social Security, and Medicare amounts when making Federal tax payments via
 EFT. When the PR AP Update is run, if “Automatic Update to Accounts Payable” is in use and
 the vendor’s “Addenda Type” is ‘Tax Payment’ (in AP Vendors), one addenda tax payment
 record is created and the amount distributed to the appropriate addenda field (W/H, Soc
 Sec, or Medicare) for the transaction. A separate record will be created for FUTA EFT
 payments. If no ‘Federal Type’ is specified, amount is distributed to the withholding
 field.
Note: Viewpoint does not currently support state EFT tax payments.

##  GL Account

 Enter the GL account to credit for this deduction or liability code. It must be a valid account set up in the GL Chart of Accounts form of the GL Co# specified in PR Company Parameters and the subledger type must be blank.

## Method

Method drop-down on the PR Deductions/Liabilities form,
 Info tab.
Select how the deduction or liability is calculated from one of the following:

- A-Amount

- D-Rate per Day

- F-Factored Rate per Hour

- G-Rate of Gross

- H-Rate per Hour

- N-Rate of Net

- S-Straight Time Equivalent (earnings/factor)

- DN-Rate Based on Deduction Code (must enter a valid Deduction
 Code)

- V-Variable, Rate of Earnings Based On Factor

- R-Routine (must enter a valid Routine).

Note: For liability codes that will be added to the Capped
 Basis of a craft (in the PR Crafts form) or craft template (in the PR Craft Templates
 form), you must select a method of A-Amount or H-Rate per
 hour. Additionally, the Calculation Method must be C-Craft, E-Employee, or A-Any.

Related concepts

- [About Methods of Calculation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation)

- [Method of Calculation: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation/method-of-calculation-canada)

- [Method of Calculation: United States](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation/method-of-calculation-united-states)

Related reference

- [Method of Calculation: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation/method-of-calculation-australia)

Related information

- [Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes)

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

- [About Methods of Calculation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation)

- [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction)

- [Set Up a Roth 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-roth-401k-deduction)

- [Set Up a Catch-Up 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction)

## Garnishment Group

The system displays this field when you select “Rate of Net” from the Method drop-down field.
Enter the garnishment group for this deduction.

## Routine

This field only displays when Method is
 R-Routine.
Enter the routine (from PR Routines) that will
 be used to calculate the deduction or liability amount.

## Rate / Amount #1

Enter the “primary” rate or amount used when calculating a deduction or liability with a Method of Days, Hours, Rate, or Net. Also used as the “resident” rate for some state and local taxes. (If entering a rate, enter 5% as .05, 10% as .10, etc.)

## Rate / Amount #2

Enter the “secondary” or “nonresident” rate or amount that is used for some state and city taxes. (If entering a rate, enter 5% as .05, 10% as .10, etc.)

## Limit

Indicate how the annual deduction/liability limit will be interpreted.

- No Limit – Select this option if no limit applies. (Amount, Applied, and Rate fields are set to 'Null' and disabled.)

- Subject Amount – Select this option if the limit is applied on the subject amount. Subject amounts are typically earnings, but based on the calculation method. This option can be used either for deductions and liabilities with income limits and a single rate (e.g. FICA, SUTA), or for deductions or liabilities with an income limit and variable rate (e.g. Nevada Worker's Comp. State Unemployment (SUTA) must be set up using this limit amount.

- Calculated Amount – Select this option if the limit is applied on the deduction or liability's calculated amount. This option is used for deductions and liabilities with income limits and a single rate. However, do not use this for SUTA.

- Rate of Earnings – Select this option if the limit is a rate of total earnings (e.g. 401k employer's match). Total earnings will be based on the earnings codes assigned in the grid. If this is a 401k employer's match, this will typically be all earnings codes that are flagged as 'Subject Only'.

Note: The Rate of Earnings method is for use with Liabilities
 only. When selected, the following applies:

-  The Applied field is set to P (Pay Period) and disabled,
 as 'rate of earnings' liabilities are only applicable on a 'per pay period'
 basis.

- The Amount field is disabled, as it does not apply to
 'rate of earnings' liabilities.

- The 401k Liability checkbox is enabled; however, you
 should only select this checkbox if this is a 401k employer match
 liability.

##  Limit: Amount

 Enter either the total subject amount that is eligible or the calculated amount that can be made for this deduction or liability within the period specified. The limit basis (specified to the left) determines how this amount is interpreted. If no limit applies, or the limit basis is 'Rate of Earnings', this field is disabled.

## Applied

Required. (Enabled only if limit basis is 'Subject Amount' or 'Calculated Amount'.)
Specify the time frame for the limit amount from one of the following:
P -Pay Period - Limit is applied using amounts from the current pay period and sequence. (If limit basis is 'Rate of Earnings', this limit period is assigned automatically and cannot be changed.)
M-Monthly - Limit is applied using amounts from the current pay period and sequence, earlier sequences within the same pay period, and previous pay periods that used the same Limit Month (specified in PR Pay Period Control). Monthly limits are not applied based on employee accumulations.
Monthly limited deductions and liabilities may appear to exceed their limit when reviewing employee accumulations if a payroll is processed using a Limit Month that differs from the paid month (i.e. payroll is processed in one month, but paid the following month.)
Q-Quarterly - Limit is applied based on the amounts from the current pay period and sequences, as well as the employee accumulations for all months within the quarter. If not using a split-month pay period, limits are applied using the Payroll beginning month (i.e. 1st Month). If using a split-month pay period, the ending month (2nd Month) will be used for quarterly limits. If the employee is paid in the beginning month (e.g. layoff) and then reprocessed, limits will now be applied using the paid month (1st Month). This may result in different calculated amounts and resulting net pay. Therefore, you should review deductions to make sure they are accurate based on the quarterly limits.
A-Annually - Limit is applied based on the amounts from the current pay period and sequences, as well as the employee accumulations for all months within the year. If not using a split-month pay period, limits are applied using the Payroll beginning month (i.e. 1st Month). If using a split-month pay period, the ending month (2nd Month) will be used for annual limits. If the employee is paid in the beginning month (e.g. layoff) and then reprocessed, limits will now be applied using the paid month (1st Month). This may result in different calculated amounts and resulting net pay. Therefore, you should review deductions to make sure they are accurate based on the annual limits.
L-Lifetime - Limit is applied based on the amounts from the current pay period and sequence, and all previous payrolls, without regard to month or year.
Unlike monthly limits, quarter, annual, and lifetime limits are all based on amounts stored in the PR Employee Accumulations table. These amounts are always updated based on paid month.

##  Limit: Rate

 Enabled for 'Rate of Earnings' limit basis only.
 Specify the limit rate for this liability. This is the total rate of earnings that will be eligible for this liability per pay period.
 For example: If your plan pays 8% of the first 25% of earnings, the calculation for this rate would be .25 x .08 = .02. The .02 is the rate you enter in this field, and the Rate/Amount would be -.25.

## Auto-Correct if Limit is Exceeded

Check this box to correct the calculated deduction/liability amount if a limit has been exceeded. This might be used if there is a change to the limit and you want to correct a calculation for the limit period. This only applies when the pay period’s subject amount is positive. Using this option may result in a negative amount calculated.
Do not check this box if you do not want to automatically correct a calculation if a limit has been exceeded. If not checked, the calculated amount for the pay period is always zero when the limit has been exceeded.
Note: Do not use this option for SUTA.

## Calculate on Pay Sequence # 1 Only

Check this box if this deduction/liability is limited to payment sequence #1 only.
Do not check this box if this deduction/liability will be calculated on all payment sequences.

## Calculate as Rate of Gross on Bonus Sequence

 The
 Calculate as Rate of Gross on Bonus Sequence checkbox on the PR Deductions/Liabilities
 form, Info tab.
This
 field displays only for US companies (those set up in HQ Company Setup with a Default Country
 of US).
Select this checkbox to override the method of calculation when processing bonus payment sequences. This will apply to all employees that are subject to this deduction or liability and is typically used to override federal tax withholding calculations.
 Do not select this checkbox if the method of calculation should not be overridden when processing bonus payment sequences.

Related information

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

## Bonus Rate

 The
 Bonus Rate field on the PR Deductions/Liabilities form, Info tab.
This
 field displays only for US companies (those set up in HQ Company Setup with a Default Country
 of US).
 Enter a bonus rate if you are overriding the calculation method on bonus sequences. The bonus rate must fall between 0.00 and 1.00 (e.g. overriding federal tax with a .28 rate).

Related information

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

## Use YTD Accumulations to Correct Rounding Errors

The Use YTD Accumulations to Correct Rounding Errors checkbox on the PR Deductions and Liabilities form, Info tab.
Rounding errors that are insignificant in one pay period may accumulate to material amounts over several pay periods.
 Select this checkbox to have the the system calculate the YTD amount, compare it to what has been accumulated so far this year, and adjust the amount for this pay period accordingly.
The calculation for this pay period is *Amount =
 [(YTD Subject + Pay Period Subject) * Rate] – YTD Amount*
This adjusts the current pay period's amount so that the YTD amount is exactly what it should be.Note: The entire difference is applied to the current pay period. This amount may be more than just a few pennies, if for example, you've changed the rate since the last pay period.

Important: If you select this checkbox for a code whose rate should change during the year, the system will apply the new rate to all amounts for the year. Only select this checkbox on EDL codes that should be calculated from the beginning of the year. Do not select it for tax routines or for state unemployment codes.
Canadian companies: If the Calculation Category is Federal, this field is enabled only if the Federal Type drop-down is set to 1-Withholding or 4-Employment Insurance.

##  Round Result to Nearest Whole Dollar

 Check this box to have the final calculation amount for this deduction/liability rounded to the nearest whole dollar.
 Do not check this box if final calculations for this deduction/liability should not be rounded.

##  Accumulate Subject Amounts

 Check this box if this deduction or liability’s subject and eligible amounts are accumulated by employee and month. This option must be checked for all codes with subject amount limits, or those required for reports (e.g. federal and state taxes). Accumulations are always made in the month paid.
 Do not check this box if subject and eligible amounts are not kept.

##  Selectively Purge Accumulations

 Check this box to exclude accumulations for this deduction/liability from deletion when other employee accumulations are purged. Accumulations are left in the file until they are specifically deleted.
 Do not check this box if the accumulations for this deduction/liability should be deleted when other employee accumulations are purged.

## Pre-Tax Deduction

Enabled when the Type section is
 set to Deduction and either C-Craft or E-Employee is
 selected in the Calculation Category drop-down list.
Select this checkbox to specify that this deduction should not be included when the system processes tax-related deduction codes.
When this checkbox is selected and the
 Calculation
 Category drop-down is set to E-Employee, the system enables the
 Pre-Tax
 Group field.
If this deduction code has been added to the basis of another deduction (on the Basis Codes tab), you will be unable to clear this checkbox until you remove the code from the Basis Codes tab.

Related information

- [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction)

- [Set Up a Roth 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-roth-401k-deduction)

- [Set Up a Catch-Up 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction)

## Catch up Deduction

The Catch up Deduction checkbox on the PR Deductions/Liabilities form, Info tab.
Enabled when the Pre-Tax Deduction checkbox is selected.
Select this checkbox if using this deduction code for eligible employees (those meeting the age requirements defined by the IRS) who want to make catch-up contributions to their 401(k) or Roth plans. The setting of this checkbox applies to both [Catch-up Contribution Limit #1](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form/field-definitions-pr-deduction-groups-form#concept-5224--en) and [Catch-up Contribution Limit #2](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form/field-definitions-pr-deduction-groups-form#concept-a7532e13-f0ba-48ec-ba13-8e18886bd5da--en)
Note: The annual contribution limits for 'catch up' deductions are defined for the specified pre-tax group in PR Pre-Tax Deduction Groups. For more information, see [PR Pre-Tax Deduction Groups Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form). and [Set up a Pre-Tax Deduction Group](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-a-pre-tax-deduction-group).

Related information

- [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction)

- [Set Up a Roth 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-roth-401k-deduction)

- [Set Up a Catch-Up 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction)

## 401k Liability

The 401k Liability checkbox on the
 PR Deductions/Liabilities form, Info tab.
This field is only enabled when you select the Rate of Earnings Limit type.
Select this checkbox if this is a 401k employer match liability. When selected, the Pre-Tax Group field is enabled to allow specifying the pre-tax deduction group used to determine the annual compensation limit for 401k employer match liabilities.
Note: Annual employee compensation limits are specified for pre-tax groups in the PR Pre-Tax Deduction Groups form.

##  Pre-Tax Group

The Pre-Tax Group field on the PR Deductions/Liabilities form, Info tab.
This field applies to U.S. users only, and is
 enabled when either of the following applies:

- For deduction codes, when the Calculation Category
 drop-down is set to E-Employee and the Pre-Tax Deduction
 checkbox is selected.

- For liability codes, when the Limit type is Rate of Earnings and the
 401k Liability
 checkbox is selected.

Enter the pre-tax deduction group for this deduction or liability code, or
 press F4 to select from a list of valid pre-tax deduction groups.
You should enter a group here when you have multiple 401(k) deductions or 401k
 employer match liabilities that require a combined limit.
Note: For 401k employer match liability codes, this group is used to determine
 the annual compensation limit (defined in PR Pre-Tax Deduction Groups) used
 when calculating employer match contributions.

Related information

- [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction)

- [Set Up a Roth 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-roth-401k-deduction)

- [Set Up a Catch-Up 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction)

## Preserve Zero-Amount Records in Pay Sequence

The Preserve zero-amount records in pay sequence checkbox on the PR Deductions/Liabilities form, Info tab.
Select this checkbox to display zero-amount pay sequence records for this deduction or liability in PR Employee Pay Seq Control. Once you process a payroll, this deduction or liability code will display for the selected employee/pay sequence, even if all amounts are zero (that is, zero hours were posted to the earnings code).
If you leave this checkbox unselected, pay sequence records with zero amounts for this deduction or liability will not display in the PR Employee Pay Seq Control form.

## Basis code on other dedn/liab codes

The Basis code on other dedn/liab codes checkbox on the PR Deductions/Liabilities form, Info tab.
This field is only enabled for liability codes meeting the following
 criteria:

- The Calculation Category is set to C-Craft or E-Employee

- The Method is set to A-Amount, G-Rate of Gross, H-Rate per Hours, R-Routine, or S-Straight time equivalent.

Select this checkbox if this liability code can be included in the basis code list of specific deduction or liability codes where:

- The Calculation Category is set to F-Federal, S-State, L-Local, I-Insurance, or E-Employee, and

- The Method is set to G-Rate of Gross or R-Routine.

## ROE Insurable

Check this box if this is a Registered Retirement Savings Plan (RSRP) liability code. These are liabilities that you pay to the investment manager for the employee's retirement account, but the amounts are reported on the ROE report as insurable earnings for the employee.
By checking this box, you enable the system to include the amounts associated with this liability code when creating employee ROE records. For more information, see [Creating Employee ROE Records](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/canada-roe/create-employee-roe-records).

## Print as separate detail line on standard certified reports

Print as separate detail line on standard certified reports field in the PR Deductions/Liabilities form
Select this checkbox if you want Certified Payroll reports to print a separate line for this deduction or liability. If selected, the report includes the description entered for this deduction or liability.
Leave this checkbox cleared if you do not want a separate line for this deduction or liability on Certified Payroll reports. If not selected, the amount for this deduction or liability is included in the ‘Other’ category on Certified Payroll reports.

## LCPtracker: Dedn Class Type

LCPtracker: Dedn Class Type drop-down on the PR Deductions/Liabilities form.
(Optional) Select one of the following deduction type classifications:

- H - Health

- R - Retirement

- U - Union Dues / Vacation

- D - State Disability Insurance

- S - Savings

- X -Tax

-  O - Other

## LCPtracker: Fringe Benefit Type

LCPtracker Fringe Benefit Type field on the PR Deductions/Liabilities form
(Optional) Select one of the following fringe benefit classifications to be used with the LCPtracker export:

- H - Health and Welfare

- V - Vacation/Holiday/Dues

- A - Apprenticeship Fund

- P - Pension

- O - Other - individual rates for liability codes with this classification will be combined to determine the average rate used in the report.

## eMars: Dedn Class Type

eMars Dedn Class Type field on the PR Deductions/Liabilities form
For Deductions, this field is required and its default value is Other.
If you want to indicate the report column where amounts for a given deduction code should be reported, select one of the deduction type classifications for the PR Certified Export - eMars (ReportID 1315, U.S. only).
Any tax deduction code (Federal, Social Security, Medicare, Add’l Medicare, State, or Local) should be classified as X - Tax. The report determines which codes pertain to which type of tax and assigns amounts accordingly to appropriate report columns.
Note: If any row in the eMars report would have more than 10 non-zero-amount columns in use, the report groups lesser deduction column amounts in the Ded Other column so that each row has at most 10 deduction columns in use.

## eMars: Fringe Benefit Type

eMars Fringe Benefit Type field on the PR Deductions/Liabilities form
This field is enabled only for Liabilities.
If you want this liability to be reported as a fringe benefit, select one of the fringe benefit classifications for the PR Certified Export - eMars (ReportID 1315, U.S. only).
The report excludes any liability code that is left unclassified (blank).
Note: The non- AASHTO version of the eMars report supports up to 10 fringe benefit columns. If any row in the report would have more than 10 non-zero-amount columns in use, the report groups lesser fringe benefit column amounts in the Fr Other column so that each row has at most 10 fringe benefit columns in use. At no point are any amounts unreported.
AASHTO
Important: The AASHTO version of the eMars report only supports five fringe benefit columns:

- Fr H&W

- Fr Pension

- Fr App Training

- Fr Vacation/Holiday

- Fr Other

Important: Fringe benefit columns not among these five always display zero (0.00) since those liability amounts are transferred to the Fr Other column. At no point are any amounts unreported.

## Automatic Update to Accounts Payable

 Check this box to automatically create AP transactions from the amounts calculated for this deduction/liability. When payroll is processed, vendor information is assigned for updating Accounts Payable. Updates to AP can occur after the pay period is closed.
 Do not check this box if this deduction/liability is not to update AP.

##  Vendor

Enter the vendor used for creating AP
 transactions to pay this deduction or liability. The vendor can be overridden by Craft (PR
 Crafts, Dedns/Liabs tab) and/or employee (PR Employee Dedns/Liabs, Vendor field).

## Separate AP Transaction Per Employee

This field is enabled only when the Automatic Update to
 Accounts Payable box is checked.
Check this box to create a separate AP transaction for each Vendor/PR Group/PE Date/DL Code/Employee combination. This is used primarily for garnishments, and applies only to employee-based deductions and liabilities.
Uncheck this box to create a single AP transaction for each Vendor/PR Group/PE Date/DL Code combination.
Note: If the Create Separate Payment per Transaction
 box is checked in AP Vendors, one transaction will be created for each Vendor/PR Group/PE
 Date/DL Code/Employee combination, regardless of how this option is set. This is required
 when creating the EFT text file if multiple garnishments are remitted to the same vendor
 for one employee.

##  Payable Type

 Only used if updating Accounts Payable.
 Specify the payable type to credit when posting AP transactions with this deduction/liability.

##  Frequency

 Only used if updating Accounts Payable.
 Specify the frequency at which transactions posted with this deduction/liability will be updated to AP. Must be a valid frequency code set up in HQ Frequency Codes.

##  Aatrix Tax Type

The Aatrix Tax Type field in the PR Deductions and Liabilities form, Addl Info tab.
Enter the 4-digit Aatrix tax type for this deduction/liability code. Press F4 to look up and select from a list of valid tax types.
Note: You can use the Filter bar in the F4 Lookup to easily locate available
 tax types for a specific state or category. For example, filtering by specific state
 will show only the available tax types for that state. If you
 have locals that are included in W-2 reporting and those locals do not have a
 specific Aatrix Tax Type, use tax type 2000. The AUF files for
 Aatrix W-2 reporting will include records using tax type 2000.

Entry in this field is only required if the following are true:

- you are using Aatrix to file your state or local tax reports

- this deduction or liability code is subject to state or local tax reporting

- you are using Aatrix for unemployment reporting

Note: For Oregon users, you are required to enter tax type 5666 (Oregon Transit Tax) in this field when setting up a deduction code for the Oregon statewide transit tax, even if you are not using Aatrix. The system uses this tax type in the generation of W2s, as well as for the OR OR-STT-1/2 Form and OR OR-STT-V Form regulatory reports available in PR Aatrix Report Selection. For Canadian users: This field is not currently being used; however, it will be available for use in a future release.

Related information

- [About Regulatory Reporting Using Aatrix](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aatrix-reporting/about-regulatory-reporting-using-aatrix)

- [DUNS Number](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form/field-definitions-hq-company-setup-form#ID-0000ebcc--en)

## Include on W-2s as a Local Tax

The Include on W-2s as a Local tax checkbox on the PR Deductions/Liabilities form, Addl Info tab.
Enabled only for deductions with a Calculation Category of Employee or Any.
Select this checkbox to include this deduction as a local tax on W-2's. You should only select this checkbox if this deduction will not be assigned to any specific locality in PR Local Codes (for example, Ohio School District tax).
Note: You will typically only select this checkbox for employee-based deductions.
Do not select this checkbox if this deduction will be excluded as a local tax on W-2s or if this deduction should be included as a local tax, but will be assigned to a specific locality in PR Local Codes.

##  Reporting State

 Required. (Enabled only if "Include on W-2s as a Local Tax" option is checked.)
 Specify the reporting state for this deduction (i.e. the state to which this deduction applies). Must be a valid state set up in HQ States.

##  Local

 Required. (Enabled only if "Include on W-2s as a Local Tax" option is checked.)
 Specify the local to which this deduction applies, up to 10 characters. Must be a unique local not already set up in PR Local Codes that identifies the city, county, or other local taxing district for the specified reporting state.

## Tax Type

Required. (Enabled only if "Include on W-2s as a Local Tax" option is checked.)
Specify the tax type for this deduction. When W-2's are initialized, the tax type specified here will be used as the default tax type on Local Info tab (PR W-2 Employee Information). Options are:

- C -City Income Tax

- D-County Income Tax

- E-School District Tax

- F-Other

## Include In STP Gross Amounts

Include In STP Gross Amounts checkbox in the PR Deductions/Liabilities form, Addl Info tab (Australia only)
Not used for STP Phase 2.
Select this checkbox in order to include amounts for this deduction or liability within calculations of employees' year-to-date reportable gross earnings (PAYG Items 'INBGross' and 'HolidayGross') for STP reporting.
When you select this checkbox on a deduction code, the system subtracts each employee's calculated deductions amounts from their reportable gross earnings during STP processing.
When you select this checkbox on a liability code, the system adds each employee's calculated amounts to their reportable gross earnings during STP processing.

## ATO Category

(Australia) The ATO Category drop-down on the PR Deductions/Liabilities form, Add'l Info tab.
Not used for STP Phase 2.
Select the Australian Taxation Office (ATO) category to associate with this deduction/liability code.
 The selection in this field impacts other forms in the system:

- The system automatically limits the
 deduction/liability codes you can enter in fields in [PR FBT Summary Process](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-fbt-summary-process-form). ATO categories here map to
 one or more specific codes you can enter into the FBT Type
 field in the FBT Info and Reportable Amounts tabs.

- The system automatically limits the
 deduction/liability codes you can enter in fields in [PR PAYG Summary Process](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-payg-summary-process-form). ATO categories here map to
 one or more specific codes you can enter into the ATO/Super
 Item field on the ATO / Super Items tab and Misc Item
 field on the Misc Items tab.

- The system uses the deduction/liability codes that have ETP-related options set in this field to calculate the ETP summary amounts that are displayed on the [PR ETP Employee Amounts](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etp-employee-amounts-form) form.

ATO Category
Select this option:

FBT1 - Reportable Fringe Benefits - Type 1
For a code that allows you to take GST credits for goods and services you acquired when providing fringe benefits.

FBT2 - Reportable Fringe Benefits Type 2
For a code that does not allow you to take GST credits.

F - Fees
For codes you use to pay union or professional association fees on behalf of an employee.

G - Giving
For codes you use to pay deductible gift recipients on behalf of an employee.

S -Superannuation
For setting up liability or deduction codes for standard superannuation. This category is used for required super contributions paid by the employer (liability), as well as pre-tax salary sacrifice (deductions) made by the employee. For more information, see [Setting Up Liability Codes for Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation/setting-up-liability-codes-for-superannuation).

SE - Superannuation - Extra
For setting up liability or deduction code used for additional superannuation. This category is used for super contributions paid by the employer above the standard rate, as well as for any after-tax superannuation deductions made by the employee. For more information, see [Setting Up Liability Codes for Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation/setting-up-liability-codes-for-superannuation).

T - Tax Withheld
When you are creating a PAYG deduction code. For more information, see [Setting Up a PAYG Deduction Code](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-a-payg-deduction-code-australia).

TE - Tax Withheld, ETP
When you are creating a standard ETP deduction code. For more information, see [Preparing PAYG Employment Termination Payment Summaries](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etp-summary-process-form).

TED - Tax Withheld ETP Death
 When you are creating an ETP deduction code for payments for an employee's death. For more information, see [Preparing PAYG Employment Termination Payment Summaries](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etp-summary-process-form).

TER - Tax Withheld ETP Redundancy
When you are creating an ETP deduction code for redundancy. For more information, see [Preparing PAYG Employment Termination Payment Summaries](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etp-summary-process-form).

TEU - Tax Withheld ETP Unfair Dismissal
When you are creating an ETP deduction code for unfair dismissal. For more information, see [Preparing PAYG Employment Termination Payment Summaries](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etp-summary-process-form).

TEV - Tax Withheld ETP Invalidity
 When you are creating an ETP deduction code for invalidity. For more information, see [Preparing PAYG Employment Termination Payment Summaries](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etp-summary-process-form).

Note: If you select Superannuation or Superannution -
 Extra, the system enables the Fund field.

## Fund

(Australia) The Fund field on the PR Deductions/Liabilities form, Add'l Info tab.
The system enables this field when you select
 either Superannuation or Superannuation-Extra from the ATO Category
 field.
Enter the superannuation fund identification
 number for this deduction/liability code, or press F4 for a list of funds (set up in [HQ Super Funds](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/about-the-hq-super-funds-form)).

## Include in Employee Gross Amount Calculation

(Australia) The Include in Employee Gross Amount Calculation checkbox on the PR Deductions/Liabilities form, Add'l Info tab.
For use with STP Phase 2 only.
This field is only enabled for Liability codes.
Select this checkbox to include this liability in STP Phase 2 employee Gross amount calculations.
Leave this checkbox unselected if this liability should not be included in STP Phase 2 employee Gross amount calculations.

## Include in Reportable Fringe Benefits Amount (RFBA) Calculation

(Australia) The Include in Reportable Fringe Benefit Amount (RFBA) Calculation checkbox on the PR Deductions/Liabilities form, Add'l Info tab.
Used for STP Phase 2 only.
Select this checkbox to include this deduction or liability in the calculation of STP Phase 2 employee reportable fringe benefits amounts.
Leave this checkbox unselected if this liability or deduction should not be included in STP Phase 2 employee reportable fringe benefits amount calculations.

## Include in Reportable Employer Super Contribution (RESC) Calculation

(Australia) The Include in Reportable Employer Super Contribution (RESC) Calculation checkbox on the PR Deductions/Liabilities form, Add'l Info tab.
Used for STP Phase 2 only.
Select this checkbox to include this deduction or liability in the calculation of STP Phase 2 employee RESC amounts.
Leave this checkbox unselected if this liability or deduction should not be included in STP Phase 2 employee RESC amount calculations.

## STP Category

(Australia) The STP Category drop-down on the PR Deductions/Liabilities form, Add'l Info tab.
For use with STP Phase 2 only.
Select the appropriate category (if any) for STP Phase 2 reporting of this deduction or liability.

- F - Fees

-  W - Workplace Giving

- SSS - Salary Sacrifice, Superannuation

- SSO - Salary Sacrifice, Other Benefits

- SL - Superannuation Liability (Super Guarantee)

- T - Tax Withheld

- TE - Tax Withheld, ETP Other

- TED - Tax Withheld, ETP Death

- TER - Tax Withheld, ETP Redundancy

- TEU - Tax Withheld, ETP Unfair Dismissal

- TEV - Tax Withheld, ETP Invalidity.

## Include Payback in Auto Update to AP

The Include Payback in Auto Update to AP checkbox on the PR Deductions/Liabilities form, Arrears/Payback tab.
Enabled only for deductions with a Calculation Category of E-Employee and a Method of A-Amount, and where both the Automatic Update to Accounts Payable and Subject to Arrears checkboxes are selected.
Select this checkbox to include payback amounts for an employee in the update to Accounts Payable. If the employee is flagged as active for arrears (in PR Employees), payback amounts will be included with the calculated deduction amount when you run the PR to AP Update process. The system generates a single transaction line on the invoice that includes both the calculated or override deduction amount and the payback or override payback amount.
If you leave this checkbox unselected, payback amounts will not be included in the update to Accounts Payable.

## Basis: EDL Type

The EDL Type field on the PR Deductions/Liabilities form, Basis Codes tab.
Select the type of code to add to the calculation basis for this
 deduction/liability. The following options are available:

- E-Earnings - Select this option to include this earnings code's posted amounts in the deduction or liability's subject amount.

- D-Deduction - Select this option to specify a pre-tax deduction that the system should not include in the basis for calculating the deduction or liability.

- L-Liability - Select this option to include a liability in the basis
 calculation for a deduction/liability meeting the following criteria:

- The Calculation Category is set to F-Federal,
 S-State, L-Local,
 I-Insurance, or E-Employee

- The Method is set to G-Rate of Gross
 or R-Routine

Note: The liability code you specify must meet
 specific criteria. For more information, see [Basis: EDL Code](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-00036c28--en).

## Basis: EDL Code

Enter a valid earnings or deduction code,
 based on your selection in the EDL Type drop-down field. Press
 F4
 for a list of valid earnings or deduction codes.
If you specify an earnings code, the system will include its amount in the deduction or liability's subject amount.
Note: For liability distribution, you must add an earnings
 code to distribute the liability amount to. This earnings code must be set up in PR
 Earnings Code with the Include in Liability Distributions box
 checked. Additional true earnings codes (you checked the True Earnings for Payroll
 Reports box in PR Earnings Codes) must be added here. For these codes, you
 should check the Subject Only box so that the liability is not calculated on them, but they
 will be used in the liability distribution.
When adding deduction codes, you can only add
 pre-tax deductions (you checked the Pre-Tax box in PR
 Deductions/Liabilities). Additionally, you can only add pre-tax deductions to
 deduction/liability codes that have the Calculation Category drop-down set to
 F-Federal, S-State, L-Local, or
 I-Insurance, and the Method drop-down set to either G-Rate of Gross
 or R-Routine. When you add a pre-tax deduction here, the system will not include it in the
 basis for calculating the deduction or liability.
Note: Pressing F5 from this field will not work when you
 have the EDL
 Type drop-down set to D-Deduction, as you are already on the
 setup form for deductions (PR Deductions/Liabilities).

## Subject Only

Check this box if the earnings are to be included in the subject amounts only (and not the calculations) for this deduction or liability.
Do not check this box if the earnings are to be included in both the subject amount and the basis for calculation for this deduction or liability.
Examples of Typical Uses
For deductions, a typical example would be for federal withholding. Earnings that are 'subject only' will be included in the “Wages, Tips, and Other Compensation” amount on the W-2, but will not be included in the basis for calculating withholding tax on a pay check.
For liabilities, it is a method to distribute the liability to earnings without the earnings being a basis for the calculation. For instance, if you are setting up an employer's 401k matching liability, and you want the employer's liability to be distributed to the original earnings, you would set up the liability as follows:

- Assign the 401k earnings along with straight time, overtime, and other earnings in the grid.

- Flag all earnings, except the 401k earnings, as 'subject only'.

- Assuming that negative earnings are not included in
 liability distributions (you did not check the True earnings for Payroll Reports
 box in PR Earnings Codes), this will allow the liability to be distributed across the
 regular earnings rather than with the 401k earnings, and to be updated to JC.
