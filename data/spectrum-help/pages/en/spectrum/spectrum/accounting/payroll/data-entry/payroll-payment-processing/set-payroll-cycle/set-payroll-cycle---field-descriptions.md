---
title: "Set Payroll Cycle - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/set-payroll-cycle/set-payroll-cycle---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/set-payroll-cycle/set-payroll-cycle---field-descriptions"
---

# Set Payroll Cycle - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Pay cycle

Employee cost group
If the cost center feature is enabled, enter an employee cost group or press F4 to select from a list of available cost groups. The employee cost group entered on this screen determines which employees may be entered (jobs may be entered for cost centers not included here). Only employees with cost centers that are valid for this cycle may be entered in Time Card Entry or updated from pre-time cards. The Check Calculation, Check Print, Auto Deposit, and Payroll Update may only be run by an operator who has an employee security override for all cost centers entered for the cycle. Operators with limited cost center security are NOT permitted to set the Employee cost group field to ALL cost groups.

Check cost center
If the cost center feature is enabled, enter the check cost center. The check cost center must be valid for your operator.
If you select the Yes, continue this cycle, but reset parameters option while a payroll cycle is currently in progress, you can then modify the Check cost center and Bank account fields, but you will not be able to change the Employee cost group field.

Entity
If cost center entities are being used, the entity assigned to the specified check cost center displays (if no entity code is present, the main company defaults). The 'Employee cost group' setting and assigned entity control which employees can be included in the pay cycle. The calculations are performed based on setup and year-to-date figures for that particular entity, and when updated, the checks included in the cycle will be stored in entity-specific history records.

Bank account
If the check cost center entered has a payroll bank account assigned, then this bank account displays (and must be valid in the current company, even if you are processing a check run in a different company). Otherwise, the bank account defaults from the Cash Management Installation screen (and may be overridden). Spectrum automatically disallows any accounts that are not bank accounts from being entered into this field. In other words, credit card accounts are not permitted in this field.
Note: The Cash Management bank account will only display if the
 Cash Management module is installed and set to "post payroll transactions."

- For void checks, the Check Calculation step uses the original bank account, regardless of where the check is voided from, and when transferring a void check from Pre-Time Card Entry, the current cycle bank account is used.

- For manual checks, in Pre-Time Card Entry the Check Calculation step uses the (original) stored bank account. In Time Card Entry, a Bank account field displays where you can specify what reconciliation account to use.

If the reporting currency of the current (payroll) company is different than the reporting currency of the destination company and the Multi-Currency module is present, validation will be provided to ensure that a valid currency code is assigned to the specified account and is the same as the reporting currency of the current company.

Period end date
Enter the pay period end date. If the Utilize pay cycle calendar checkbox on the Payroll Installation – Defaults tab is selected, the next period-end date defaults.
 If the Accrue expense to field on the Payroll Installation – Properties tab is set to Pay period-end date or Work date, the date entered in this field will be used for G/L expense, Job Cost, and Equipment Control entries.

Check date
Enter the check date, which is used for General Ledger to determine the correct accounting period for cash and liabilities. Multiple pay cycles can be run using the same payroll check date and period-end date. The fiscal year and period for the check date display to the right of this field.
 If you attempt to enter a check date that is later than the current payroll year, an error message will display and you will not be allowed to continue until the year-end clear is run.
The check date is also the date that appears in Job Cost and Equipment Control if the Accrue expense to field is set to Check date in Payroll Installation.

-  If the Utilize pay cycle calendar checkbox in Payroll Installation – Defaults tab is selected, the next check date defaults. A warning window will appear if another date is specified, but the user may continue.

Period start date
Entries in this optional field will display on pay stubs to make it easier for employees to verify that they have been paid properly. The pay stub also displays the sum of all hours worked on this check for added convenience and to comply with CA and NY legislation.

- If the Utilize pay cycle calendar? option is selected in Payroll Installation, and the specified Period end date is present in the pay cycle calendar, then this field defaults to one day later than the previous period end date.

- If the Require period start date on payroll cycle? option is selected in Payroll Installation, a date must be entered in this field.

Selections

Departments
Enter the code of the payroll department for which the payroll is to run, or press Enter for ALL departments. Following entry of a valid department code, the department description displays.

Deduction week #
Enter the deduction week number of the payroll cycle for which the payroll is to run, or press Enter for ALL weeks.

Automatic cycle?
Select this checkbox to have Spectrum automatically create time cards for active non-casual employees whose home department is not a job or equipment department.
 If an automatic cycle is used, then time cards for employees fitting the following three parameters will be created:

- Active status

- Home department is not direct

- The Part-time? checkbox is cleared in Employee Pay Rates.

The pay rate for the employee will be set based on the salary or hourly rate stored in Employee Pay Rates unless the employee is assigned a union code. In that case, the pay rate will be determined based on the union file, wage code file, and the current setting of the Default pay rate field in Payroll Installation.
Any [related tax codes](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/newedit-tax-table---related-taxes-tab) are automatically created on time card lines
 when this option is selected.

Accrue hourly banks?
Select this checkbox to accrue vacation, holiday, and sick hours; otherwise, leave the checkbox clear to bypass accrual of vacation, holiday, and sick hours. Normally, this checkbox is selected. It is most frequently left clear during special payroll cycles, such as for bonuses, where certain deductions may not be desired.

Pay annual bonus?
Select this checkbox if you want the system to annualize the standard pay plus the bonus amount to determine the Federal income tax amount.
Note: This feature does not affect the calculation of state,
 county, and local taxes (unless based on a percent of Federal tax).
Example: Hourly employee paid weekly, married ($20/hour or $41,600 annualized) Zero exemptions, bonus $7500.
Total earnings including bonus = $49,100
$49,100 - 0 Exemptions ($2,650 x 0) = $49,100
7,500/49,100 = .15 This is the portion of the annualized income including bonus that is attributable to the bonus. Rounded to two decimals.
Calculate tax for $49,100 = $9,951
(based on 1997 tax rates: 3,525 + 28% above $26,150 = $9,951)
9,951 x .15 = 1,492.65 tax on bonus check

Override federal withholding?
Select the checkbox to override the Federal Income Tax Withholding percentage.
 If you select this checkbox, enter the withholding percentage to be applied to whatever Federal code the employee is assigned. The [Check Calculation](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/check-calculation) uses this instead of the tax table and any overrides, including the tax adjustment feature.
During a given pay cycle, an employee will only have one Federal tax code. The software will not provide the ability to assign different Federal codes on each time card line (the way 'work state', 'work county' and 'work local' code may vary by time card). Instead, the Federal code recorded in Employee Tax Setup will be used for all time cards in that particular pay cycle
This field is used during special cycles, such as for bonuses when it is desirable to calculate a fixed percentage of Federal income tax instead of using the tax table. When the checkbox is selected, the screen will prompt for the percentage to be applied (for example, 28.00) to the "US subject to" income tax amount. This will supersede the tax table and any employee overrides specified in the Employee Tax Setup screen.
At the time of pay cycle setup, an option (Pay annual bonus) to calculate bonus checks based on annualizing the payroll tax withholding for the year is available. The Pay annual bonus option uses the total pay to date, including the bonus, and withholds taxes based on the calculation instead of withholding a fixed percent.
Example:
Hourly employee paid weekly, married ($20/hour or $41,600 annualized) Zero exemptions, bonus $7500.
 Total earnings including bonus = $49,100
$49,100 - 0 Exemptions ($2,650 x 0) = $49,100
7,500/49,100 = .15 This is the portion of the annualized income including bonus that is attributable to the bonus. Rounded to two decimals.
Calculate tax for $49,100 = $9,951
(based on 1997 tax rates: 3,525 + 28% above $26,150 = $9,951)
9,951 x .15 = 1,492.65 tax on bonus check

Turn off auto deposit payments?
Select this checkbox if you want to override the Payroll auto-deposit feature for the current pay cycle. This is a one-time override; next time you set the pay cycle, the auto-deposit feature will be activated.
 If you select this checkbox, the For check seq field displays. Specify a check sequence, or press Enter to accept the default of ALL.

"True up" recurring deductions and add-ons?
Select this checkbox to compute certain deduction or add-on codes on a year-to-date basis rather than for the current payroll cycle only. The special calculation will occur only for codes that are assigned a status of Recurring or One time in the Employee Recurring Deductions/Add-ons screen and have been marked as Eligible for true up in the Deduction / Add-on Maintenance screen. The sequence in which the recurring deductions and add-ons are computed will not change when a true up pay cycle is performed. True up calculations are not applicable during Layoff Check Calculation.
Note: The 'true up' calculations will only be performed for
 employees receiving a regular check during the pay cycle in which this check
 box is selected.
This checkbox is provided for deduction and add-on codes computed as a "percent of gross" and a "percent of a related code." When this checkbox is selected, monthly limits (if any) specified in Employee Recurring Deductions/Add-ons will be ignored. Likewise, any 'per cycle limits' specified in Deduction / Add-on Code Maintenance will be disregarded during this cycle for 'true up' codes. Instead, the 'true up limit' specified on the Limits tab of the Deduction / Add-on Code Maintenance screen will be applied, if applicable.
The calculation during a 'true up' Payroll cycle will be as follows for '% of gross':

- Year-to-date gross + current check gross = Total gross

- Total gross X employee's specified % = Maximum allowable YTD deduction / add-on amount

- The maximum allowable amount is compared to the annual limit (if any) in Employee Deduction / Add-on Code Maintenance

- The maximum allowable amount is compared to the 'true up' limit (if any) in Deduction / Add-on Code Maintenance

- The minimum of the allowable amount and the two limits is determined to be the 'YTD eligible amount'

- The 'YTD eligible amount' minus the 'YTD amount taken' = 'true up' amount granted on pay check

The calculation during a 'true up' payroll cycle will be as follows for '% of related code':

- Year-to-date taken on related code + related code amount on current check = 'Total related code amount' '

- Total related code amount X employee's specified percentage = Maximum allowable YTD deduction / add-on amount

- The maximum allowable amount is compared to the annual limit (if any) if Employee Recurring Deductions/Add-ons

- The maximum allowable amount is compared to the 'true up' limit (if any) in Deduction / Add-on Code Maintenance

- The minimum of the allowable amount and the two limits is determined to be the 'YTD eligible amount'

- The 'YTD eligible amount' minus the 'YTD amount taken' = 'true up' amount granted on pay check

Pay frequencies

Select the applicable pay frequencies: Daily, Weekly, Bi-Weekly, Semi-Monthly, Monthly, Quarterly, or Annually. You can select one or a combination of types, as necessary.

Pay types

Select the applicable payroll type(s): Hourly, Salary, Overtime Salary, or Commission. You can select one or a combination of types, as necessary.

Recurring deductions and add-ons

Select which recurring deductions and add-ons to take during check calculation:

- Calculate all recurring and one-time codes

- Suppress all

- Make selections

If the Make selections option is selected, a selection window will open to select which add-ons and deductions to include. Use this window to manually select which deductions or add-ons to include during check calculation, or click the 'Select All' and 'Clear All' buttons for ease of use when working with a large number of deductions or add-ons.
