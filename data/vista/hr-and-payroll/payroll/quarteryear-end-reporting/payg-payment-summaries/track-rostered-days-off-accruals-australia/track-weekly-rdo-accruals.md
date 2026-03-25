---
title: "Track Weekly RDO Accruals | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/track-rostered-days-off-accruals-australia/track-weekly-rdo-accruals"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/track-rostered-days-off-accruals-australia/track-weekly-rdo-accruals"
---

# Track Weekly RDO Accruals

Set up and process weekly Rostered Days Off (RDO) accruals in
 the system.
To calculate weekly RDO accrual amounts, the system takes the maximum number of RDO hours an employee can earn in a day (RDO hours per week divided by the number of days in the week) and multiples that number by the number of days that the employee worked the specified number of hours.For example, an employee works 5 days a week and can receive 4.00 hours of RDO per week. The system divides the hours by the number of work days (4.00/5). The result is that the employee can earn .80 hours of RDO per day. If the employee must work a minimum of 8 hours per day, and ends up working 8 hours Monday through Thursday, and only works 4 hours on Friday, the system will only accrue RDO for the four days he worked 8 hours (.80 x 4 = 3.20 hours RDO). RDO will not accrue for Friday.
To set up and process weekly RDO accruals in the system.

1. In the PR Routines form,
 create a new routine, making sure to specify the bspPR_AU_RDOAccrual procedure in the Procedure field. In the Misc Amt #1 field, enter the
 minimum number hours per day that an employee must work to accrue RDO.Note: You can use the standard RDOAccrual
 routine and modify it as necessary. If you decide to use this routine, you
 will need to initialize routines in the PR Routines form in order for it to
 be available. For more information, see [PR Routines Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-routines-form).

1. In the PR Earnings Codes form, create an earnings code for RDO accrual. When creating this code, select R-Routine from the Method drop-down and, in the Routine field, specify the routine that you created in step 1 above. On the Subject Earnings tab, specify any normal earnings codes that the system will base the accrual on. For more information, see [Set Up Earnings Codes: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-australia).

1. In the PR Earnings Codes form, create an earnings code to be used for RDO taken. When creating this code, select H-Rate per hour from the Method drop-down field.

1. In the PR Leave Codes form, create a leave code for tracking RDO. When creating this code, select the Rate of Earnings or Hours option from the Accrual Type section. On the Accrual/Usage Info tab, setup the RDO accrual and taken codes from steps 1 and 2. The RDO accrual code should be set up as an accrual type (Type field), hourly basis (Basis field), and a rate of -1.00000 (Rate field). The RDO taken code should be set up as a usage type, hourly basis, and a rate of 1.00000.

1. In the PR Employee Leave form, assign the RDO tracking leave code to all applicable employees.

1. In the PR Automatic Earnings form, add RDO accrual entries for the employees. Make sure to select the Override Pay Period's standard hours checkbox and enter the number of weekly hours the employee is required to work in the Hours field. The RDOAccrual routine uses this number to determine the factor of normal hours to post as RDO hours and works regardless of the pay frequency (weekly, fortnightly, etc.). Additionally, make sure to select the Use regular hourly rate checkbox so that the system uses the rate setup for the employee (Hourly Rate field, PR Employees form) or the employee's regular earnings code (Earnings Code field, PR Employees form) from the craft/class/template hierarchy; the system uses the highest of the two rates.

1. Post all normal earnings in the PR Timecard Entry form. Make sure to post 8 hours a day, even though some of the hours are considered RDO accrual. For more information, see [Posting Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/posting-timecards).

1. Post automatic earnings using the PR Post Auto Earnings form. For more information, see [Post Automatic Earnings](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-posting-automatic-earnings/post-automatic-earnings). The system posts RDO accruals as a rate per hour using the employee's standard rate of pay and negative hours, which removes some of the normal wages and stores them in the leave code you set up in step 4.

1. Use the RDO taken code from step 3 to post RDO usage in the PR Timecard Entry form. For more information, see [Posting Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/posting-timecards). Note: Make sure to allow for a normal work week of less than 40 hours when entering hours. For example, a 36 hour week requires employees to work 7.2 hours per day (36 divided by 5 days), so you only need to post 7.2 hours of RDO taken. For a 38 hour week, you should post 7.6 hours.

1. Run PR Auto Leave Accrual/Usage as necessary, using the Usage and Rate Based Accruals option. For more information, see [Update Usage and Rate-Based Accruals](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/update-usage-and-rate-based-accruals).
