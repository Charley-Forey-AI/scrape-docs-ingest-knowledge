---
title: "Weighted Average Overtime Rates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/weighted-average-overtime-rates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/weighted-average-overtime-rates"
---

# Weighted Average Overtime Rates

You can use weighted-average overtime rates when applying auto overtime to timecards posted to jobs, crafts, and classes.
If you are using weighted-average overtime rates (that is, you selected the Use weighted average overtime rates checkboxes in both PR Craft Classes and JC Jobs), the system uses a weighted-average rate adjustment when applying auto overtime to timecards posted to jobs, crafts, and classes.
However, the Average By option specified for the job (in JC Jobs) and the craft/class (in PR Craft Classes) determines how the system handles overtime rate calculations as follows:

- If the Average By field is set to Day for either the Job or the Craft/Class on the timecard, the system uses the daily weighted-average rate to calculate the overtime rate.

- If the Average By field is set to Week for both the Job and the Craft/Class on the timecard, the system uses the weekly weighted-average rate to calculate the overtime rate.

The Overtime setting for an employee in PR Employees (Additional Info tab) determines whether the employee is eligible for overtime and if so, whether they receive daily and weekly overtime or weekly only. It does not affect whether the system uses a daily or weekly weighted-average rate (or neither) when processing any specific overtime hours for the employee.
During auto-overtime processing (in PR Auto Overtime), the system starts with the daily overtime calculations first (for applicable employees), and then calculates weekly overtime for any remaining overtime hours not already processed. In each case, the system uses the specified weighted-average overtime calculation method to determine the overtime rate.
The following discusses how the system handles overtime calculations based on the Average By method.

## Overtime Calculations Using Weighted-average by Day

1. The system calculates a weighted-average regular rate for each day as the sum of the employee’s straight-time earnings for the day divided by his total hours for the day (only earnings subject to OT with a factor of 1.0 are included).

1. When processing a timecard for a given day (based on posted date), the system sets an overtime rate adjustment as the average regular rate for that day times the OT factor less one. For example, if the OT factor is 1.50, the overtime rate adjustment is calculated as: daily average regular rate x .50 (1.50 - 1.00).

1. As either daily or weekly overtime hours are processed, if both the Job and the Craft/Class posted on the timecard indicate that weighted-average overtime should be applied, and either the Job or the Craft/Class indicate weighted-average overtime by day in particular, then this overtime rate adjustment is added to the posted rate on the timecard to yield the overtime rate. If it is not the case that both the Job and Craft/Class indicate weighted-average overtime, then regular overtime rates are used.

For example:
Posted Timecards for the Day
Post SeqHoursEarn CodeRateEarningsWghtd Avg OT
14125.00100.00Y
26130.00180.00Y
Total10280.00

Daily weighted-average regular rate = straight-time earnings divided by total hours
 280.00 / 10 = $28.00
OT Factor = 1.50
OT Rate Adjustment = 14.00 (28.00 x .50 (1.50 - 1.00))
After OT is processed
Post SeqHoursEarn CodeRateEarnings
14125.00100.00
24130.00120.00
3 (New)2244.00 (posted rate + OT rate adj (30.00 + 14.00))88.00
TOTAL308.00

Total Reg Hours for the Day = 8
Total OT Hours for the Day = 2 (2 hrs of reg earnings are converted to OT)
Total Earnings for the Day = $308.00
Posting Seq 2 is subject to weighted-average OT by day (say, based on its Job and Craft/Class), so when its hours are reduced by the 2 hours of OT, Seq 3 is added using the posted rate plus the overtime rate adjustment.

## Overtime Calculations Using Weighted-average Rate by Week

1. The system calculates a weighted-average regular rate for the week for each employee subject to overtime. This average is calculated as the sum of the employee’s straight-time earnings for the week divided by his total hours for the week (only earnings subject to OT with a factor of 1.0 are included).

1. An overtime rate adjustment is then set as the average regular rate for the week times the OT factor less one. For example, if the OT factor is 1.50, the overtime rate adjustment is calculated as: weekly average regular rate x .50 (1.50 - 1.00)

1. As either daily or weekly overtime hours are processed, if both the Job and the Craft/Class posted on the timecard indicate that weighted-average overtime should be applied, and both the Job and the Craft/Class also indicate weighted-average overtime by week in particular, then this overtime rate adjustment is added to the posted rate on the timecard to yield the overtime rate. If it is not the case that both the Job and Craft/Class indicate weighted-average overtime, then regular overtime rates are used.

For example:
Post SeqHoursEarn CodeRateEarningsWghtd Avg OT
130110.00300.00Y
21518.00120.00N
3518.0040.00Y
Total50460.00

Weekly weighted-average regular rate = straight-time earnings divided by total hours
 460.00 ÷ 50 = $9.2
OT Factor = 1.50
OT Rate Adjustment = $4.60 (9.20 x .50 (1.50 -1.00))
After OT is processed:
Post SeqHoursEarn CodeRateEarnings
130110.00300.00
21018.0080.00
35212.60 (posted rate + OT rate adj (8.00 + 4.60))63.00
4 (new)5212.00 (posted rate x 1.560.00
TOTAL503.00

Total Reg Hours = 40
Total OT Hours = 10 (10 hrs of reg earnings are converted to OT)
Total Earnings = $503.00
Posting Seq 3 is subject to weighted-average OT by week (say, based on its Job and Craft/Class), so it uses the posted rate plus the overtime rate adjustment.
The remaining 5 hours of OT are pulled from Seq 2, which is not subject to weighted-average overtime of any kind. A new Seq is added using the posted rate times the OT earnings factor (1.5), and the hours on Seq 2 are reduced accordingly.
