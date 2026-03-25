---
title: "About Use Est Out Date | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-use-est-out-date"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-use-est-out-date"
---

# About Use Est Out Date

If you have equipment that will be on a job for more than one
 billing cycle or an extended period of time, checking this box allows the system to use the
 equipment's 'transfer in' date and 'estimated out' date to determine the best revenue rate
 to use.
 With this method, the system totals the
 'billable estimate hours' from the last transfer In Date through the Est Out Date, and
 then determines the revenue code to apply from the usage rules table (based on where the
 'billable estimate hours' fall in the "more than, less than" hours ranges in the table).
 It will then apply that rate to the actual hours accrued to the job in the billing
 period. If the billable hours do not fall in any of the hours ranges, the system uses
 the last sequence/revenue code.
For example, a piece of equipment moves from
 the Yard to a job three times during the month of April (assume 8 hrs/day, Monday -
 Friday).
Date
From
To

06/03/10
Yard
Job 1000-

06/04/10
Job 1000-
Yard

06/17/10
Yard
Job 1000-

06/18/10
Job 1000-
Yard

06/30/10
Yard
Job 1000- (with Est Out
 Date of 07/15/10)

In this example, the equipment was on the
 job for three days (24 hours of actual usage). Typically, the daily rate would apply;
 however, with the Est Out box checked for the template, the system calculates the
 'billable estimate hours' from 06/30/10 through 07/15/10 (12 working days or 96 hours).
 According the usage rules table, the weekly rate applies rather than the daily rate;
 therefore, instead of converting the 24 hours into 3.0 days and applying the daily rate,
 the system converts the 24 hours into .06 weeks and applies the weekly rate.
Note: If the Hours Basis option is set to Job To
 Date for the usage rules table, any usage hours posted in previous periods for the
 equipment and job will be included in the 'billable estimate hours' and may affect which
 revenue code is applied.
