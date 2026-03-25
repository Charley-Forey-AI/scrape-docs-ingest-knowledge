---
title: "Create Allowance Rule Sets | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances/create-allowance-rule-sets"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances/create-allowance-rule-sets"
---

# Create Allowance Rule Sets

You can use PR Allowance Rule Sets to create allowance rule sets, along with the associated rules that determine how the system calculates payroll allowances.
Calculations are based on days/time period worked by the employee, the minimum hours (threshold) the employee must work to receive the allowance, the specified calculation method (rate or amount), and a factor if you are using a percentage rate to determine the allowance amount. For more information on how allowances are calculated, see [How the System Processes Allowances](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances/how-the-system-calculates-allowances).
The following instructions detail how to set up allowance rule sets and their associated rules.

1. In PR Allowance Rule
 Sets, enter the name for the rule set in the Allowance Rule
 Set Name field. Press F4 for a list of rule sets.


1. Enter a description for
 the rule set in the Description field.

1. From the Rule
 Period drop-down, select a period type for this rule set. You
 can select either Daily or Weekly. The choice you make determines whether the rule
 threshold number is based on an entire week, or one or more specific days in a
 week. You cannot change the Rule Period drop-down if
 there are rules associated with the rule set.

1. In the detail section of
 the form, enter a rule name in the Rule field and a description
 for the rule in the Description field.

1. Check the day boxes that
 this rule applies to (Sunday, Monday, Tuesday, etc.). If the rule period for
 this set is Weekly, the checkboxes will
 be disabled; in this case, proceed to the next step. If this is a rule for
 holiday allowances, check the Holiday box. In this case,
 the system will disable all other day boxes, and vice versa.

1. In the Threshold
 Hrs field, enter the minimum number of hours that the employee
 must work for the specified period in order to receive an allowance.

1. Select a calculation
 method from the Calc Method field. You can
 choose to have the system use a rate (R - Rate Calculation), hourly
 amount (H - Hourly Amount), or a flat amount (A-Amount). The system disables the Factor field if you select either H - Hourly
 Amount or A - Amount.

1. Enter either the rate or
 amount in the Rate/Amount field. When
 entering an amount, use a dollar value (25.00). When entering a rate, enter a
 value between 0.00 and 1.00 (with 1.00 representing 100% of an hour); -that is,
 the percentage of an hour of pay that will be awarded as an allowance.

1. If you are using a rate
 calculation, enter the factor in the Factor field, otherwise
 proceed to the next step. The system will use the number you enter here to
 multiply the rate for this calculation. For more information, see [How the System Processes Allowances](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances/how-the-system-calculates-allowances).

1. If there is a maximum
 allowance amount that an employee can receive for a time period, select the type
 of time period from the Max Amount Period drop-down:
 Daily or Weekly. In the Max
 Amount field, enter the maximum amount that the employee should
 receive. For more information, see [How the System Processes Allowances](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances/how-the-system-calculates-allowances).

1. Repeat steps 4 through 10 for any additional rules that you want to add to the rule set.

Related information

- [PR Race Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-race-codes-form)
