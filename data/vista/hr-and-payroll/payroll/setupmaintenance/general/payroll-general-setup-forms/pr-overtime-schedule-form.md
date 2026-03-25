---
title: "PR Overtime Schedule Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-overtime-schedule-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-overtime-schedule-form"
---

# PR Overtime Schedule Form

Use this form to maintain daily overtime rules to be applied by employee, craft, or job.
Here you can set up, by day, the maximum number of hours that are worked before overtime is calculated. The number of hours must be between 0 and 24, with 8 being used for an 8-hour day and 0 being used if all hours worked in a day should be treated as overtime. The earnings code that will be used when overtime is calculated is entered in the OT Code column.
You can set up multiple levels of hours and OT codes. Typically, you will only need to set up multiple levels when more than a single premium rate may be applied in a single day. For example, you may have employees that receive time and a half after 8 hours (OT) and double-time after 10.5 hours (DT). Therefore, you would set up the levels as follows:

Level 1 Hrs
OT Code
Level 2 Hrs
OT Code

Mon
8.0
2 (OT)
10.5
3 (DT)

Tues
8.0
2 (OT)
10.5
3 (DT)

Wed
8.0
2 (OT)
10.5
3 (DT)

Thurs
8.0
2 (OT)
10.5
3 (DT)

Fri
8.0
2 (OT)
10.5
3 (DT)

Sat
0.0
2 (OT)
8.0
3 (DT)

Sun
0.0
2 (OT)
8.0
3 (DT)

Holiday
0.0
3 (DT)

Note: If you set Level 1 hours to 0.00, and Level 2 hours are greater than 0.00 (as shown in the example for Sat and Sun above), all Level 1 hours are treated as overtime up to the number of hours specified for Level 2, at which point they are paid as indicated by the OT code.
You can also set up multiple overtime schedules. These schedules are then referenced in the Job Master, the Employee Master, Craft Master, and/or the Craft Template. The schedule used is based on the overtime option set up for each employee on the Additional Information tab in PR Employees.
Overtime schedules are maintained by day of the week, so if you have employees that work four 10-hour days, with some employees working Monday through Thursday and others are working Tuesday through Friday, you need to enter 10 hours for each day of the week (Monday-Friday). This allows for overtime to be paid when an employee works in excess of 40 during the week.
For example:

Lvl 1 Hrs
OT Code

Mon
10
2 (OT)

Tues
10
2 (OT)

Wed
10
2 (OT)

Thurs
10
2 (OT)

Fri
10
2 (OT)

Sat
0
2 (OT)

Sun
0
2 (OT)

Holiday
0
3 (DT)

Using the overtime schedule in the example above, if Employee #1 worked five 10-hour days, 40 hours will be paid regular time, and 10 will be converted to overtime and paid at the overtime rate.
Note: You can also set up overtime schedules by shift, which overrides the standard overtime rules defined here. If shift overrides have been set up, a “Shift overrides in effect” message is displayed in red at the top of the screen. For information about setting up overrides by shift, see Related Topics below.

Related information

- [Set up Separation Payments](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-separation-payments)

- [PR Overtime Schedule by Shift Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-overtime-schedule-by-shift-form)

- [Set up Automatic Overtime Calculations](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-automatic-overtime-calculations)
