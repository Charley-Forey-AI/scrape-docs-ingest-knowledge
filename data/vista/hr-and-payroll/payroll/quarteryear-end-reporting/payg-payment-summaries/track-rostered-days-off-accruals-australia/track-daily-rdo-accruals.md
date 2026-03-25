---
title: "Track Daily RDO Accruals | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/track-rostered-days-off-accruals-australia/track-daily-rdo-accruals"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/track-rostered-days-off-accruals-australia/track-daily-rdo-accruals"
---

# Track Daily RDO Accruals

Set up and process daily Rostered Days Off (RDO) accruals in the system.
To calculate daily RDO accrual amounts, the system determines if the employee has met the minimum number of hours worked and, if so, the system will accrue the appropriate number of RDO hours for the employee.For example, your employees might accrue .40 RDO hours for every 7.6 hours worked. The following table illustrates how an employee would accrue RDO using such a rate. You can see that the employee only accrued RDO for three days, so the total RDO hours would be 1.20.
MonTuWedThursFri
Hrs Worked7.66.57.68.06.5
RDO Accrued.400.00.40.400.0

To set up and process daily RDO accruals in the system.

1. In the PR Routines form, create a new routine, making sure to specify the bspPR_AU_RDOAccrualDaily procedure in the Procedure field. In the Misc Amt #1 field, enter the minimum number hours per day that an employee must work to accrue RDO. In the Misc Amt #2 field, enter the RDO hours accrued if the minimum number of hours worked is met.

1. In the PR Earnings Codes form, create an earnings code for RDO accrual. When creating this code, select R-Routine from the Method drop-down and, in the Routine field, specify the routine that you created in step 1 above. On the Subject Earnings tab, specify any normal earnings codes that the system will base the accrual on. For more information, see [Set Up Earnings Codes: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-australia).

1. In the PR Earnings Codes form, create an earnings code to be used for RDO taken. When creating this code, select H-Rate per hour from the Method drop-down field.

1. In the PR Leave Codes form, create a leave code for tracking RDO. When creating this code, select the Rate of Earnings or Hours option from the Accrual Type section. On the Accrual/Usage Info tab, setup the RDO accrual and taken codes from steps 1 and 2. The RDO accrual code should be set up as an accrual type (Type field), hourly basis (Basis field), and a rate of -1.00000 (Rate field). The RDO taken code should be set up as a usage type, hourly basis, and a rate of -1.00000.

1. In the PR Employee Leave form, assign the RDO tracking leave code to all applicable employees.

1. Select the Use regular hourly rate checkbox so that the system uses the rate setup in the PR Routines form for the routine you created in step 1.

1. Post all normal earnings in the PR Timecard Entry form. Make sure to post 8 hours a day, even though some of the hours are considered RDO accrual. For more information, see [Posting Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/posting-timecards).

1. Post automatic earnings using the PR Post Auto Earnings form. For more information, see [Post Automatic Earnings](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-posting-automatic-earnings/post-automatic-earnings). The system posts RDO accruals as a rate per hour using the employee's standard rate of pay and negative hours, which removes some of the normal wages and stores them in the leave code you set up in step 4.

1. Use the RDO taken code from step 3 to post RDO usage in the PR Timecard Entry form. For more information, see [Posting Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/posting-timecards).Note: Make sure to allow for a normal work week of less than 40 hours when entering hours. For example, a 36 hour week requires employees to work 7.2 hours per day (36 divided by 5 days), so you only need to post 7.2 hours of RDO taken. For a 38 hour week, you should post 7.6 hours.

1. Run PR Auto Leave Accrual/Usage as necessary, using the Usage and Rate Based Accruals option. For more information, see [Update Usage and Rate-Based Accruals](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/update-usage-and-rate-based-accruals).
