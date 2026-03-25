---
title: "About Craft Templates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-customer-service-site/about-craft-templates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-customer-service-site/about-craft-templates"
---

# About Craft Templates

If you have different craft/class
 requirements based on the type of services performed by technicians for a service site, you can use craft templates to determine technician pay rates.
 Craft templates are set up in the Payroll module and allow you to override selected craft information, such as reciprocal agreement settings, add-on earnings, and/or deductions and liabilities. The system uses the craft template to
 determine pay rates, add-on earnings, and deductions and liabilities for employees.
You can assign a default craft template to each customer service site in SM Service Sites so that each time a work order is
 created for that service site, it defaults the specified craft template you specified. When
 you enter work completed labor lines, the system sends the labor entries to PR My Timesheet, along with the craft template
 designation. Once you approve the timesheets and send them to a timecard batch (via PR Timesheet Send), the system uses the craft template
 to determine the pay rate for the technician based on the craft and class specified on
 the timecard.
When processing payroll for service
 technicians (in PR Payroll Process), the system uses the work order's craft template
 to apply add-on earnings, deductions, and liabilities for the payroll period.

## Reciprocal Agreements

Reciprocal agreements are used when
 employees from one union are working on a job within the jurisdiction of another
 union, and control which pay rates are used, which deductions and liabilities are
 calculated, and to which craft they are reported.
There are two types of reciprocal
 agreements: Partial and Override. When entering SM-related timecards, craft and pay
 rate defaults are handled as follows:

- Partial - The system defaults
 the employee's standard craft and calculates all earnings using the posted
 craft; however, deductions and liabilities will accumulate under the Job
 Craft specified on the craft template.

- Override - The system defaults
 the Job Craft specified on the craft template rather than the employee's
 standard craft. The system uses the Job Craft to calculate earnings and
 accumulate deductions and liabilities.

For information about setting up
 reciprocal agreements for a craft template, see [Set Up Reciprocal Agreements for Crafts](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-reciprocal-agreements-for-crafts).

Related tasks

- [Enable Overtime Calculations for Work Completed Labor](/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-customer-service-site/about-craft-templates/enable-overtime-calculations-for-work-completed-labor)

Related information

- [Set Up Craft Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-templates)

- [Set Up a Customer Service Site](/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-customer-service-site)

- [PR Auto Overtime Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-auto-overtime-form)

- [Post Automatic Overtime](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/post-automatic-overtime)

- [How Auto Overtime Works](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/how-auto-overtime-works)
