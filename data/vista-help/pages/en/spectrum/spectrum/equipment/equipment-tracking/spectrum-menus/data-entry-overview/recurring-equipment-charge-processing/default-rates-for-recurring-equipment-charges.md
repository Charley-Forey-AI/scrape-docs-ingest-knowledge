---
title: "Default Rates for Recurring Equipment Charges | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/data-entry-overview/recurring-equipment-charge-processing/default-rates-for-recurring-equipment-charges"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/data-entry-overview/recurring-equipment-charge-processing/default-rates-for-recurring-equipment-charges"
---

# Default Rates for Recurring Equipment Charges

Learn about the detaul rates for recurring equipment
 charges.

##  Determining Quantity

Once the billing period and corresponding rate has been determined, the quantity will be determined. If the billing period is in days, then the quantity is just the number of days since the last update. If the billing period is weekly (or monthly), then the quantity will be based on the number of days since the last update, divided by the number of days in a week (or month) from the rate schedule. For example, if the equipment has been out for nine working days since the last update and the rate schedule determines that this should be billed at the weekly rate, with a week based on five working days per week, then the quantity would be 9 / 5 = 1.8 weeks.

## Determining Billing

When a piece of equipment is returned, the system will also automatically
 create an E/C transaction for the final billing when the update is processed. For this
 final billing, the system will add the total number of days since the issue date, and
 determine the billing period based on the rate schedule in the Equipment Tracking
 Installation. It will then determine the quantity (based on number of working days
 divided by the number of working days in the billing period, see above), and then
 multiply this quantity times the rate to determine what the total bill should be. The
 equipment rate information will default the amount set up in the Job-Specific
 Equipment Charge Rates screen. If no job-specific record is found (or
 rate is blank), the system will determine if this job is a sub job of a master job and
 use the job-specific rate from the master job. If there is no job-specific rate for the
 job or master job, the system will read for the standard job rate of the equipment code.
 If the amount to be billed is less than or equal to the amount billed to date, then no
 final bill is created. Otherwise, the final bill will be equal to the total expected
 bill, minus the amount billed so far.

## Determining Sub-Job Rates

If this is a sub-job billed from a master job, the software will read for job-specific setup rates for the master job, and if none are found use standard settings. If this is a sub-job billed at the sub-job level, the software will read for job-specific setup rates for the sub-job first, and if billing rates are not found then the master job, and if none are found there use standard settings.

## Determining Stand-by Rates

The billing rate assigned to the equipment and any attachments will default
 from the stand-by rates defined on the Time + Material > Job Equipment Billing Rate Maintenance screen, based on Hourly, Daily, Weekly or Monthly rates. If there is no
 rate defined there, Spectrum will look to the Equipment Billing Rate Maintenance table
 for the stand-by billing rate. If no rate is defined there, the billing rate is
 zero.
