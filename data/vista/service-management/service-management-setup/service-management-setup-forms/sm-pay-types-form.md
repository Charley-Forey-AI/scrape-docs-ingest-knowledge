---
title: "SM Pay Types Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-pay-types-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-pay-types-form"
---

# SM Pay Types Form

Use the SM Pay Types form to set up the pay types that represent the different labor costs for service work.
Pay types allow you to define anticipated labor costs for service work at different pay
 levels; for example, regular time, overtime, and double time. When creating work orders, pay types are used to derive labor cost estimates so that you can bill for service
 work before payroll is cut. The actual payroll costs are updated to the work order
 once you process your payroll.
For each pay type you set up, you must specify the cost method,
 factor, and the earnings code that will default when entering timesheets or timecards
 for technicians (in PR My Timesheet or PR Timecard Entry).
 The cost method defined for a pay type determines how the
 system derives the cost rate when adding labor entries for work completed on a work
 order. You can assign one of two cost methods to a pay type:

- Multiplier - With this method, you
 assign a factor (multiplier) to use in rate calculations. When a labor work
 completed line is added to a work order, the system calculates the estimated
 labor costs based on the technician's pay rate (defined in SM Technicians), the
 factor specified for the pay type, and the cost hours.
Example:
 Factor: 1.50
 Tech's Pay Rate: 35.00
 Cost Hours: 6.50
 Cost Rate: 52.50 (Tech's Pay Rate x Factor)
 Cost Total: 341.25 (Cost Rate x Cost Hours)

- Dollar Rate - With this method, you
 assign a flat rate to use in rate calculations. This rate overrides the pay rate
 defined for the technician (in SM Technicians). When adding labor work completed
 lines to a work order, the system calculates the estimated labor costs based on
 the pay type rate and the cost hours.
Example:
 Pay Type Rate: 42.50
 Tech's Pay Rate: 35.00 (not used)
 Cost Hours: 6.50
 Cost Rate: 42.50 (Pay Type Rate)
 Cost Total: 276.25 (Cost Rate x Cost Hours)

Click the following link for information about setting up pay types.
[Set Up SM Pay Types](/en/vista/vista/service-management/service-management-setup/set-up-sm-pay-types#task-2488--en__task-2488)

Related information

- [SM Technicians Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-technicians-form)

- [About the PR My Timesheet Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-my-timesheet-form)

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)
