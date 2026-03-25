---
title: "About Setting Limits for Deductions/Liabilities | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-setting-limits-for-deductionsliabilities"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-setting-limits-for-deductionsliabilities"
---

# About Setting Limits for Deductions/Liabilities

When setting up deductions and liabilities in PR Deductions/Liabilities, you can specify whether to set a limit and what type of limit to apply.
 When setting limits, you must indicate how the system interprets and applies limits. This is done by setting a limit type, limit amount or rate, and a time frame for the limit.

## Setting the Limit Type

The following list discusses each of the available limit options:

- No Limit – Select this option if limits do not apply to the deduction or liability.

- Subject Amount – Select this option to apply the limit to the subject amount. Subject amounts are typically earnings and are based on the calculation method. Use this option for deductions and liabilities with income limits and a single rate (e.g. FICA, FUTA, SUTA), or for deductions or liabilities with an income limit and variable rate (e.g. Nevada Worker's Comp). State Unemployment (SUTA) must be set up with the limit based on Subject Amount to handle multi-state limits.

- Calculated Amount – Select this option to apply the limit to the deduction or liability's calculated amount. Use this option for deductions and liabilities with income limits and a single rate. United States users: Do not use this for SUTA.Note: For both Subject Amount and Calculated Amount limit types, use the Amount field to enter the total subject amount that is eligible, or the calculated amount that for the deduction or liability within the specified period. The system disables this field if the limit type is No Limit or Rate of Earnings. The limit's rate is the maximum rate of earnings eligible for the liability in the pay period.

- Rate of Earnings – For liabilities only, use this option to apply the limit as a rate of total earnings (e.g. 401k employer's match). The system bases total earnings on the earnings codes assigned on the Subject Earnings tab. Enter the limit rate in the Rate field.

You set up a 401k Employer's Match liability. You define the calculation method for the liability as 'rate of gross', with a rate of -.50000. You set the limit method to Rate of Earnings, with a limit rate of .020000 (Rate field). When setting up the earnings on the Subject Earnings tab, check the Subject Only check for all earnings subject to the liability (except the 401k earnings). The system will exclude the 'subject only' earnings from the calculation basis for the liability, but includes them when distributing the liability back to the earnings.
When you process an employee (with earnings of $1000 and a 401k contribution of -$100), the system calculate the 'rate of earnings' liability as $50.00 (-.50 x -$100.00). The limit amount would calculate as $20.00 (.02 x $1000.00). Since the calculated amount ($50.00) exceeds the limit ($20.00), the system uses the limit value.Note: The subject amount of a 401k-match liability with a 'rate of earnings' limit is equal to the 401k contribution. However, the system prorates the eligible amount when using the rate of earnings limit. The calculation for eligible becomes Eligible Amount = Liability Limit Amount / Liability Rate. In the example above, this calculation is -40.00 = (.02 * 1000) / -.50.

## Setting a Time Frame for Limits

The following time frame options are available:

- P-Pay Period – Select this option to apply the limit using amounts from the current pay period and sequence, and earlier processed sequences within the same pay period.

- M-Monthly – Select this option to apply the limit using amounts from the current pay period and sequence, earlier processed sequences within the same pay period, and previous pay periods that used the same limit month (Limit Month field in PR Pay Period Control). Monthly limits are not applied based on employee accumulations.Note: Monthly limited deductions and liabilities may appear to exceed their limit when reviewing employee accumulations if a payroll is processed using a limit month that differs from the paid month (that is, payroll is processed in one month, but paid the following month.)

- Q-Quarterly – Select this option to apply the limit based on the amounts from the current pay period and sequences, as well as the employee accumulations for all months within the quarter. If a split-month pay period, the system applies limits using the Payroll ending month. If you are not using a split-month pay period, the system applies limits using the Payroll beginning month.

- A-Annually – Select this option to apply the limit based on the amounts from the current pay period and sequences, as well as the employee accumulations for all months within the year. If a split-month pay period, the system applies limits using the Payroll ending month. If not using a split-month pay period, the system applies limits using the Payroll beginning month (i.e. 1st Month).Note: When processing an employee in a split-month pay period, the system uses the ending month for both quarterly and annual limits. If you pay the employee in the beginning month (e.g., layoff) and then reprocess, the system applies limits using the paid month. This may result in different calculated amounts and resulting net pay. Therefore, you should review deductions to make sure they are accurate based on the quarterly or annual limits.

- L-Lifetime – Select this option to apply the limit based on the amounts from the current pay period and sequence, and all previous payrolls, without regard to month or year.

Note: The Auto Correct If Limit Is Exceeded checkbox controls how the system calculates the deduction/liability amount when its limit is exceeded. This box only applies when the pay period’s subject amount is positive. If you check this box, then the calculated amount may be negative. If you do not check this box, the calculated amount is always 0.00 if the limit has been exceeded. United States users: Do not use this checkbox for SUTA.

Related information

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

- [Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes)
