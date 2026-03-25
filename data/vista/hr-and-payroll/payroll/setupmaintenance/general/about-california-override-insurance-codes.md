---
title: "About California Override Insurance Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-california-override-insurance-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-california-override-insurance-codes"
---

# About California Override Insurance Codes

Currently only required in California.
The Posting
 Override section in PR State Insurance Codes allows you to indicate whether an override
 insurance code will default for timecard wages that exceed a threshold. If you select
 the Use Override
 Code When Pay Rate Exceeds Threshold Rate checkbox, you must then
 specify a threshold rate and an override insurance code. For example, concrete work has
 insurance codes based on the pay rate. Hourly wages for concrete work under $17 use
 insurance code 5201, whereas hourly wages for concrete work equal to or greater than $17
 use insurance code 5202. So in this case, you would set up insurance code 5201 with the
 checkbox selected, enter a threshold rate of 17.00, and enter 5202 as the override
 insurance code.
 When entering timecards, the system compares the employee's pay rate plus applicable add-on earnings to the threshold rate. Applicable add-on earnings are those where the earnings code is included in the liability's basis codes and where the calculation method is F-Factored Rate per Hour, H-Rate per Hour, or V-Variable Factored Rate.
 If the
 combined pay rate and add-on earnings are equal to or greater than the threshold rate,
 the override insurance code is used. If the combined pay rate and add-on earning are
 less than the threshold rate, the employee's insurance code (defined in PR Employees) is
 used.
Note: When determining the add-on earnings to include, the system
 uses the same hierarchy used to determine the pay rate (i.e. craft/class template, craft
 template, craft/class, craft, employee, respectively). It will use the highest rate
 found in the hierarchy and if applicable add-on earnings exist for that pay rate, they
 will be included.

Related information

- [Create Australia Earnings Routines](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/create-australia-earnings-routines)
