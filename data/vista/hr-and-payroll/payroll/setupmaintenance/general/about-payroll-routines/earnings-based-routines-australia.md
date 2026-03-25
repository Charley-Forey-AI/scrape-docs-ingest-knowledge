---
title: "Earnings Based Routines: Australia | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/earnings-based-routines-australia"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/earnings-based-routines-australia"
---

# Earnings Based Routines: Australia

The system accommodates specific Australia earnings through
 the use of a routine.
Each of the routines needs to have an earnings code set up in the PR Earnings Codes form and then assigned to appropriate form(s) in the list below in order to calculate. For more information, see [Set Up Earnings Codes: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-australia).
The following table displays each routine, descriptions, and any additional information you need to set up to properly calculate the earnings.

Routine
Procedure
Description
Additional Information for Setup

Forms Used
Description

You can apply this procedure to multiple custom routines.
The system comes with one standard routine using this procedure:
Allowance
bspPR_AU_Allowance
Calculates allowances as add-on earnings based on a rate per hour of subject hours.
You can apply this procedure to multiple routines at once.
PR Routines
Create a routine with this procedure specified in the Procedure Name field. You can also use the standard Allowance routine.

PR Automatic Earnings
Enter a rate in the Rate/Amount field or check the Use regular hourly rate box.

PR Crafts
PR Craft Classes
PR Craft Class Templates
PR Craft Templates
Add the earnings code for this routine to the Add-On Earnings tab.

Enter the old/new rates as the amount to be applied for each day eligible for the allowance.

You can apply this procedure to multiple custom routines.
bspPR_AU_AmountPerDiemAward
Use this procedure to calculate an award for an amount per day (as either an addon or an automatic earning).
PR Routines
Create a routine with this procedure specified in the Procedure Name field.

In the Misc Amt #1 field, enter the hours threshold for generating the allowance on weekday.

In the Misc Amt #2 field, enter the threshold for generating the allowance on weekend days.

Enter 0 to generate an allowance if any number of hours were posted on day or enter 99 for no allowance.

PR Automatic Earnings
Enter a rate in the Rate/Amount field or check the Use regular hourly rate box to determine the amount to be applied for each day eligible for the allowance.

PR Crafts
PR Craft Classes
PR Craft Class Templates
PR Craft Templates
Add the earnings code for this routine to the Add-On Earnings tab.

Enter the old/new rates as the amount to be applied for each day eligible for the allowance.

You can apply this procedure to multiple custom routines.
The system comes with one standard routine using this procedure:
RateOfGross
bspPR_AU_ROSG

Calculates earnings (for example, leave loading) as a rate of gross based on subject earnings.
You can apply this procedure to multiple routines at once.
PR Routines
Create a routine with this procedure specified in the Procedure Name field. You can also use the standard RateOfGros routine.

In the Misc Amt #1 field, enter the exemption limit.

PR Earnings Codes
Create an earnings code for leave loading. Select R-Routine from the Method drop-down and enter the name of the routine you created in the Routine field.

On the Subject Earnings tab, enter all of the earnings that the leave loading earnings applies to.

If you are creating an earnings code for leave loading that is associated with a normal termination ETP, select ETPA - Normal Termination, Annual Leave from the ATO Category field on the Addl Info tab. For more information, see [About Unused Annual Leave Payments](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-unused-annual-leave-payments).

If you are creating an earnings code for leave loading that is associated with an ETP for termination due to redundancy, invalidity, or early retirement, select LSAR - Leave, Lump Sum A Type R from the ATO Category field on the Addl Info tab. For more information, see [About Unused Annual Leave Payments](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-unused-annual-leave-payments).

PR Automatic Earnings
Enter a rate in the Rate/Amount field or check the Use regular hourly rate box to determine the amount to be applied for each day eligible for the allowance.
For more information, see [Post Automatic Earnings](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-posting-automatic-earnings/post-automatic-earnings).

PR Crafts
PR Craft Classes
PR Craft Class Templates
PR Craft Templates
Add the earnings code for this routine to the Add-On Earnings tab.

You can apply this procedure to multiple custom routines.
The system comes with one standard routine using this procedure:
OTCrib
bspPR_AU_OTCribAllow
Overtime crib allowance computed as 20 minutes at doubletime rate of pay when employees work over a certain number of hours.
PR Routines
Create a routine with this procedure specified in the Procedure Name field. You can also use the standard OTCrib routine.

PR Earnings Codes
When setting up an earnings code for this routine, you do not need to specify a double time factor, as the procedure automatically calculates it.

Routines using this procedure can be applied to both weekday and weekend work, so take that into account when determining which subject earnings codes to include.

PR Automatic Earnings
You do not need to specify a rate in the Rate/Amount field; the procedure applies the allowance as 20 minutes at the employee's regular pay rate. Check the Use regular hourly rate box which determines the pay rate as the greater of the pay rate setup in PR Employees ( Hourly Rate field, Add'l Info tab) or the craft/class/template rate.

PR Crafts
PR Craft Classes
PR Craft Class Templates
PR Craft Templates
You do not need to specify a rate; the procedure applies the allowance as 20 minutes at the employee's regular pay rate.

You can apply this procedure to multiple custom routines.
The system comes with one standard routine using this procedure:
OTCribWknd
bspPR_AU_OTWeekendCrib
Overtime meal/rest/crib allowance computed as 30 minutes at doubletime rate of pay when employee works over a certain number of hours.
PR Routine
 Masters
Create a routine with this procedure specified in the Procedure Name field. You can also use the standard OTCribWknd routine.

PR Earnings Codes
When setting up an earnings code for this routine, you do not need to specify a doubletime factor, as the routine automatically calculates it.

This routine is applied only to weekend work, so only include earnings codes used to post time on weekends as subject earnings.

PR Automatic Earnings
You do not need to specify a rate in the Rate/Amount field; the routine applies the allowance as 30 minutes at the employee's doubletime pay rate. Check the Use regular hourly rate box which determines the pay rate as the greater of the pay rate setup in PR Employees ( Hourly Rate field, Add'l Info tab) or the craft/class/template rate.

PR Crafts
PR Craft Classes
PR Craft Class Templates
PR Craft Templates
You do not need to specify a rate; the routine applies the allowance as 30 minutes at the employee's doubletime pay rate.

You can apply this procedure to multiple custom routines.
The system comes with one standard routine using this procedure:
OTMeal
bspPR_AU_OTMealAllow
Overtime meal allowance computed as an amount per weekday when employee works over a certain number of hours.
PR Routines
Create a routine with this procedure specified in the Procedure Name field. You can also use the standard OTMeal routine.

PR Earnings Codes
The earnings codes that you specify on the Subject Earnings tab determine when the threshold has been met or exceeded.

The overtime meal allowance is only applicable to weekdays, so only include earnings codes used to post time on weekdays as subject earnings.

PR Automatic Earnings
Enter a rate in the Rate/Amount field or check the Use regular hourly rate box to determine the meal allowance amount to be applied when the threshold has been met or exceeded.

PR Crafts
PR Craft Classes
PR Craft Class Templates
PR Craft Templates
Add the earnings code for this routine to the Add-On Earnings tab. Specify the rate as the meal allowance amount to be applied when the threshold has been met or exceeded.

AllowRDO
bspPR_AU_AllowWithRDOFactor
RDO allowance based on associated subject earnings hours, subtracting the RDO hours for the pay period.
PR Earnings Codes
Set up an RDO accrual earnings code associated with this routine. On the Subject Earnings tab, enter the earnings codes that are subject to this allowance.

PR Crafts
PR Craft Classes
PR Craft Class Templates
PR Craft Templates
Add the earnings code for this routine to the Add-On Earnings tab.

AllowRDO36
(For RDO Allowance calculations,  it is recommended that you use the AllowRDO routine.)
bspPR_AU_AllowRDO36
RDO allowance for 36 hour work weeks.
PR Crafts
PR Craft Classes
PR Craft Class Templates
PR Craft Templates
Add the earnings code for this routine to the Add-On Earnings tab.

AllowRDO38
(For RDO Allowance calculations, it is recommended that you use the AllowRDO routine.)
bspPR_AU_AllowRDO38
RDO allowance for 38 hour work weeks.
PR Crafts
PR Craft Classes
PR Craft Class Templates
PR Craft Templates
Add the earnings code for this routine to the Add-On Earnings tab.

AmtPerDay
bspPR_AU_AmtPerDay
Rate per day used for allowances such as fare, first aid, and travel.
PRAutomatic Earnings
Enter a rate in the Rate/Amount field or check the Use regular hourly rate box to determine the amount to be applied per day.

PR Crafts
PR Craft Classes
PR Craft Class Templates
PR Craft Templates
Add the earnings code for this routine to the Add-On Earnings tab. Specify the rate as the amount to be applied per day.

PR Employees
If you have checked the Posting to All box in PR Employees, the system uses the standard number of days specified in PR Pay Period Control. Otherwise, the system determines the number of days by each day with time posted to the subject earnings (in PR Earnings Codes).

You can apply this procedure to multiple custom routines.
The system comes with one standard routine using this procedure:
RDOAccrual
bspPR_AU_RDOAccrual
Calculates weekly RDO accrual amounts.
Click here for more information: [Track Rostered Days Off Accruals: Australia](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/track-rostered-days-off-accruals-australia).

You can apply this procedure to multiple custom routines.
bspPR_AU_RDOAccrualDaily
Calculates daily RDO accrual amounts.
Click here for more information: [Track Rostered Days Off Accruals: Australia](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/track-rostered-days-off-accruals-australia).

Related information

- [Associate Deductions and Liabilities with Earnings Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/associate-deductions-and-liabilities-with-earnings-codes)

- [Set Up Earnings Codes: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-australia)
