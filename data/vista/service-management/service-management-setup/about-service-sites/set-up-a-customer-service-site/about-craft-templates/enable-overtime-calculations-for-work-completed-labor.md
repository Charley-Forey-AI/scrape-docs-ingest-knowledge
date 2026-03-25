---
title: "Enable Overtime Calculations for Work Completed Labor | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-customer-service-site/about-craft-templates/enable-overtime-calculations-for-work-completed-labor"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-customer-service-site/about-craft-templates/enable-overtime-calculations-for-work-completed-labor"
---

# Enable Overtime Calculations for Work Completed Labor

You can have the system calculate overtime for labor hours
 associated with an SM work order based on the craft template assigned to the work order in
 SM Work Orders.

Enabling this functionality requires the following
 setup:

1. In PR Company Parameters, select the Using Automatic
 Overtime checkbox and specify the Overtime Earnings Code to
 use.

1. In PR Earnings Codes, for each earnings code that you use for regular earnings:

1. For each earnings code that you use for regular earnings, set the
 Factor field to
 1.000000 and select the Include
 in OT Calculations checkbox.

1. Set up additional earnings codes for overtime (for example, Overtime,
 Double, etc.), and set the Factor field to the
 appropriate factor (for example, 1.5, 2.0, etc.).

1. In PR Overtime Schedule, set up the appropriate overtime schedules.

1. In PR Craft Template, select the Override Overtime checkbox
 and specify the OT Schedule to use for each applicable craft on the template.  If the craft template specifies a Job Craft, you will need to set up the job
 craft for Override Overtime as well.

1. In PR Employees, set the Overtime drop-down to
 C-Craft for each applicable employee.

1. In SM Service Sites, assign the appropriate craft
 template to each applicable customer service site.The craft template automatically defaults
 for each customer work order created for the service site.
For job service sites, the system uses the craft
 template associated with the job. Therefore, make sure you assign the
 appropriate craft template to each applicable job in JC Jobs. Although the work
 order will not show the craft template, it will be used in overtime calculations
 for labor hours posted to the work order.

You are now set up for automatic overtime and can
 begin entering labor hours against work orders in SM Work Orders, PR My Timesheet, or PR
 Timecard Entry.Note: Regardless of where you initially enter hours, you must post them
 via a PR Timecard Entry batch. You can then run PR Automatic Overtime to calculate
 and post overtime based on the hours posted in PR Timecard Entry. For more
 information about automatic overtime calculations, see [Automatic Overtime Calculations](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-automatic-overtime-calculations).

Related concepts

- [About Craft Templates](/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-customer-service-site/about-craft-templates)

- [PR Auto Overtime Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-auto-overtime-form)

- [How Auto Overtime Works](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/how-auto-overtime-works)

Related tasks

- [Set Up Craft Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-templates)

- [Set Up a Customer Service Site](/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-customer-service-site)

- [Post Automatic Overtime](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/post-automatic-overtime)
