---
title: "How the System Calculates Allowances | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances/how-the-system-calculates-allowances"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances/how-the-system-calculates-allowances"
---

# How the System Calculates Allowances

When the system calculates payroll allowances, it uses the
 rule sets that you define in PR Allowance Rule Sets.
The rules associated with a rule set determine how the system calculates the allowance amount. Rules are based on the rule/time period specified for the rule set: either daily or weekly.
The following list outlines how the system processes allowances:

- If a rule set has a daily rule period, the allowance amount will be applied to each day associated with the rule.

- If a rule set has a weekly rule period the allowance amount will be applied based on hours worked over an entire week's time, where day one is the first day of the pay period.

- If holidays require different rules, you will need
 to create a specific holiday rule and it will be calculated only if the day
 worked was a holiday (as specified in PR Crafts or PR Pay Period Control).
 If you want a holiday rule to be used in conjunction with another rule, you
 will need to create an additional rule set for the holiday.

- Each rule has a minimum number of hours (threshold) that an employee has to work to receive the allowance. This threshold amount is applied based on the rule set's rule/time period.

- Only a single rule per rule set will be used at a time. The system uses a hierarchy to determine which rule in the rule set will be applied to an employee. The hierarchy is as follows:

- The system will not process more than one rule in a rule set if the rules apply to the same rule period, day selection, and threshold hours. For example, if Rule #1 is set to daily with Monday, Wednesday, and Friday specified and the threshold amount is 8 hours, there cannot be another rule with any of those days specified with a threshold of 8 hours.

- If there are multiple rules that apply to a given day/week, the system will use the rule with the highest threshold achieved. Using the example above, you could create Rule #2 that is daily with Monday, Wednesday, and Friday specified with a threshold of 10 hours. If the employee worked 10.5 hours, the system would use Rule #2 and ignore Rule #1.

- If the day being calculated is a holiday, the holiday rule trumps the daily threshold rule.

The following table provides some rule examples on how the system would calculate an allowance amount, although the examples are not exhaustive.
Time Period Example
Calculation Method
Allowance Rate/Amount
Factor
Pay Rate
Specific Days
Threshold Hours
Explanation

1. Daily
Flat Amount
$25.00
N/A
N/A
Mon, Wed, Fri
8
In this case, the employee will receive $25 on each Monday, Wednesday, and Friday where the hours worked reached or exceeded 8 hours. If the employee works over 8 hours on any other day, no allowance will apply.

2. Weekly
Flat Amount
$200.00
N/A
N/A
N/A (assumes 7 days based on pay period)
37
The employee will receive $200.00 once the hours worked reached or exceeded 37 hours within the seven-day period.

3. Daily
Hourly Amount
$2.00
N/A
N/A
Monday - Friday
8
The employee will receive $2.00 for every hour worked for each day where the hours worked reached or exceeded 8 hours. In this case, if the employee worked 9 hours a day, Monday through Friday, the employee would receive a $90 allowance amount.

4. Holiday
Hourly Amount
$5.00
N/A
N/A
Holiday
0.01
The employee will receive $5.00 for every hour
 worked on a holiday. During payroll processing, the system will
 check PR Pay Period Control and PR Crafts to determine if a
 holiday applies. If the day is not a holiday, the system will
 use other rules that apply to the specific day of the week.
If you use weekly rule sets to determine allowance amounts, and you want to calculate holiday allowance amounts, create both a general weekly rule set and a daily rule set for the holiday. Apply both rule sets to the appropriate craft/class/template level. The system will then calculate a holiday allowance, as well as the weekly allowance.

5. Daily
Calculated Rate
.33 (.33 of an hour = 20 minutes)
1.5
$20.00
Tues, Thurs
8
The employee will receive $9.90 every Tuesday and Thursday where the hours worked reached or exceeded 8 hours. The system calculates the amount using this calculation:
Rate Amount * (Factor * Pay Rate)
or, specific to this example:
.33 * (1.5 * $20.00) = $9.90

If there is a maximum allowance amount that an employee can receive, you can apply a maximum amount based on a daily or weekly time period. The maximum amount time period is not tied to the rule set's rule/time period.
For example, if you were using example 1 in the table above, and needed to apply a maximum allowance of $50.00/week, you could set the maximum time period to weekly and set the maximum allowance to $50.00. Once the employee received $50.00 for the week, the system would stop applying allowance amounts to the employee, regardless of how many days the employee worked over 8 hours.
Similarly, if you were using example 3 in the table above and needed to apply a daily maximum of $4.00, you could set the maximum time period to daily and set the maximum allowance amount to $4.00. For every day that the employee worked over 8 hours, he could only receive a maximum allowance of $4.00
For more information on creating allowance rule sets, see [Creating Allowance Rule Sets](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances/create-allowance-rule-sets).
