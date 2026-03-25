---
title: "Deduction and Liability Based Routines: Australia | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-australia"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-australia"
---

# Deduction and Liability Based Routines: Australia

A table listing the available Australia-related deduction and
 liability based payroll routines in the PR Routines form.
In order to use these routines you will need to add them to the system or update existing ones (see [Initializing Routines](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/initialize-routines)).
PurposeRoutine NameProcedure NameAdditional Information for Setup
(XX in name represents year for tax routines)Forms UsedSetup Instructions
PAYG Tax
PAYG Tax
bspPR_AU_PAYGXX

For instructions, see [Set up PAYG Withholding for Employees](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-payg-withholding-for-employees).
Daily Ben
Daily Ben
bspPRDailyBen
PR Routines
Set up daily rates in the Misc Amt fields as follows:
Misc Amt #1 – Weekdays
Misc Amt #2 – Saturday
Misc Amt #3 – Sunday
You should only use this routine if you have varying hourly benefits depending on the day of the week (thatis, separate rates for Mon-Fri, Sat, and Sun/Holidays). It assumes there are no regular time hours on Saturday, Sunday, or holidays.

Exempt Rate of Gross
ExemptROG
bspPRExemptRateOfGross
PR Routines
Set up a separate routine for each applicable local, and assign bspPRExemptRateOfGross as the procedure.
Enter the exemption amount in the Misc Amt #1 field.

SuperannuationSuperMinbspPR_AU_SuperWithMinPR RoutinesEnter the current earnings threshold in the Misc Amt #1 field; that is, the minimum amount of monthly gross earnings. You must update this field every time the threshold changes.
PR Deductions / LiabilitiesSet up a liability code for superannuation. For more information, see [Setting Up Liability Codes for Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation/setting-up-liability-codes-for-superannuation).
For more information on setting up superannuation, see [Set Up Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation).
