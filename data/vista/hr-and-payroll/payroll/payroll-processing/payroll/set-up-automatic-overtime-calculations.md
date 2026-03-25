---
title: "Set up Automatic Overtime Calculations | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-automatic-overtime-calculations"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-automatic-overtime-calculations"
---

# Set up Automatic Overtime Calculations

You can manually determine overtime before entering timecards and enter it to specific overtime earnings codes for each line of entry.
If you prefer, you can have the system automatically calculate overtime after your entries are made based on specific rules set up by company, employee, job, and craft. Use the following steps to set up automatic overtime calculations.

1. In PR Company Parameters, do the following:

1. Select the Using Automatic Overtime checkbox. If not selected, you will receive warnings during timecard entry if hours exceed the daily or weekly limit.

1. In the Overtime Earnings Code field, enter the appropriate earnings code.

1. In PR Overtime Schedule, set up one or more schedules for daily overtime.You may need to set up multiple schedules if different jobs or different crafts (unions) have different rules. For example, one might pay overtime over 8 hours per day, another over 10 hours, or one might pay 1½ time on Saturday and the other double time.

1. In PR Employees, use the Overtime drop-down to select the employee's basis for overtime. This determines if either a warning is given in PR Timecard Entry or if overtime is automatically calculated. Choose from the following:

- N-None - No overtime is calculated. Employee is exempt.

- D-Daily - This employee is always paid overtime based on the standard hours per day and based on the overtime schedule assigned in the next field.

- W-Weekly - This employee is always paid overtime for hours worked over 40 per week.

- C-Craft - Overtime is based on the craft or craft template that this employee works under. If the craft or craft template has been assigned an overtime schedule, then the daily “rules” at either of those levels is used. All of an employee’s time posted to the craft for a day is accumulated to see if overtime should be calculated. Weekly overtime is applied after all of the daily overtime calculations are complete. If different overtime rules apply to the various templates this employee has worked under, then the order of timecard entry becomes important in determining how much overtime is calculated and for which jobs or work orders (SM Work Order timecards).

- J-Job - Overtime is calculated based on the overtime schedule assigned to the job in JC Jobs. Each job is processed independently (i.e., overtime is applied only after working more than the maximum number of regular time hours on a single job). Weekly overtime is applied after all of the daily overtime calculations are complete.

1. In PR Crafts, in the OT Schedule field for each applicable craft, specify the overtime schedule that will be used to calculate overtime. This applies to employees set up with an automatic overtime option of C (craft/class)

1. In PR Craft Classes, do the following:

1. Select the Use Weighted Average Overtime Rates checkbox for each craft/class that will be using this feature to determine overtime rates

1. In the Average By field, select whether to use a Week or Day calculation method.
Note: Make sure you select the corresponding options for every job on which the craft/class will be used (see In the JC Jobs section below). Otherwise, standard overtime rates will be used. See Related Topics below for more information about using weighted-average overtime rates.

1. In PR Craft Templates, for each applicable craft on the template, do the following:

1. Select the Override Overtime checkbox. If you do not select this checkbox, the overtime schedule designated in the PR Crafts will be used.

1. In the OT Schedule field, enter the override overtime schedule to use for this craft. This will apply to all employees with this designated craft that are set up with an automatic overtime option of C (Craft).

1. In JC Jobs, for each applicable job, do the following:

1. In the PR Overtime Schedule field (PR Info tab), enter the overtime schedule to be used for the job. Each job will be treated independently. An employee working on 2 jobs within a day would have to work on either job more than the standard pay hours before receiving overtime.Note: If a combination is needed of both craft and job to determine overtime, use the PR Craft Template to accomplish this. This will allow the maximum flexibility in which different crafts may follow different rules on the same job, and those same employees may have different rules on different jobs.

1. If the job is using weighted average overtime rates, select the Use Weighted Average Overtime Rates checkbox (PR Info tab) checkbox.

1. In the Average By field, select whether to use a Week or Day calculation method.
Note: You must select the Use Weighted Average Overtime Rates checkbox and an Average By option for both the job and each craft/class used on the job; otherwise, regular overtime rates will be used.
