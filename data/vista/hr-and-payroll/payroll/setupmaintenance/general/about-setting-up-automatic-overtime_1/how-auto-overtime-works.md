---
title: "How Auto Overtime Works | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime_1/how-auto-overtime-works"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime_1/how-auto-overtime-works"
---

# How Auto Overtime Works

Automatic Overtime calculations are dependent upon settings in
 PR Company Parameters and PR Employees.
If the Automatic Overtime Option is checked in PR
 Company Parameters, then the option for each employee in the PR
 Employees form will be used to determine how and if automatic
 overtime will be calculated for the employee. These options are used
 as follows:
PR Employees Overtime Selection
OT Calculations

N-None
No overtime is calculated.

D-Daily
Overtime is calculated on a daily basis using the OT Schedule assigned in PR Employees. If the maximum number of regular time hours for that day of the week is exceeded, then overtime is posted. Overtime is distributed in reverse posting sequence order. The posted earnings code is either changed to the OT Earnings Code and its corresponding rate or the regular hours are reduced and a new entry is created using the OT Earnings Code. After all days have been processed, weekly overtime calculations are also made.

W-Weekly
Overtime is calculated on a weekly basis only (40 hours). If greater than 40 hours, overtime is distributed in reverse posting sequence order similar to the daily process.

C-Craft
Overtime is based on the Craft and Craft Template that the Employee works under. Only Crafts or Craft Templates assigned a daily OT Schedule are included in the processing. For each day of the week, regular time hours are examined (all regular hours posted to the Craft are accumulated). If the total regular hours exceed the maximum allowed for the day, overtime is posted using the daily overtime earnings codes.
If different overtime rules apply to the various Templates that the Employee has worked under, the order of timecard entry becomes important in determining how much overtime is calculated and for which jobs or work orders (SM Work Order timecards). Weekly overtime is applied after all of the daily overtime calculations are made.

J-Job
Overtime is based on the Job(s) to which the
 Employee has posted. Only jobs assigned a daily OT Schedule (in
 the JC Jobs) are included in the processing. For each day of the
 week, regular time hours posted to each job are examined. If the
 total regular hours exceed the maximum allowed for the day, then
 overtime will be posted using the daily overtime earnings code.
 Overtime is distributed in reverse order beginning with the last
 timecard posted. The maximum must be met for each job before
 overtime is calculated.

The following is an example of a Craft or Craft Template–based overtime calculation. Four timecards, all entered as regular earnings, are posted to a single employee and date, but to different craft templates with different overtime schedules. This table shows how overtime would be calculated.
Post Seq#
Posted Hrs
Template
OT Limit
Regular Hrs
OT Hrs
Total Hrs

1
6
A
8
6
0
6

2
5
B
10
5
0
5

3
2
C
8
2
0
2

4
1
D
None
1
0
1

The overtime limit is based on the Craft, but may be overridden by the Craft Template. This employee worked 14 total hours; however, since a different overtime schedule was used for each sequence, no overtime is posted.
If the same hours were posted to crafts or craft templates using the same overtime schedule, overtime would be calculated as follows:
Post Seq#
Posted Hrs
Template
OT Limit
Regular Hrs
OT Hrs
Total Hrs

1
6
A
8
6
0
6

2
5
B
8
2
3
5

3
2
C
8
0
2
2

4
1
D
8
0
1
1

In the first example, there is no overtime calculated per day. In the second example, overtime is calculated because the same overtime schedule is being used for all sequences. Beginning with the highest posting sequence number for the day, and working in descending order, posted earnings are changed from regular to overtime (with corresponding rate and amount changes). Overtime is posted to the overtime earnings code from the overtime schedule for the sequence to which you are posting. A new entry is added for the balance.
Post Seq#
Posted Hrs
Regular Hrs
OT Hrs
Total OT

4
1
0
1
1

3
2
0
2
3

2
5
2
0
3

New Seq

0
3
6

1
6
6
0
6

Using the same daily pattern for the entire week, if the employee were to exceed 40 hours within the week, then overtime is calculated starting with the last craft posted and calculates in reverse order until all hours in excess of 40 have been converted `to overtime.
Note: Dates posted outside the range of the pay period, as well as any negative hours, are ignored.

Related information

- [About Setting up Automatic Overtime](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime)

- [Weighted Average Overtime Rates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime/weighted-average-overtime-rates)

- [About the PR Craft Templates Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-templates-form)

- [PR Overtime Schedule Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-overtime-schedule-form)
