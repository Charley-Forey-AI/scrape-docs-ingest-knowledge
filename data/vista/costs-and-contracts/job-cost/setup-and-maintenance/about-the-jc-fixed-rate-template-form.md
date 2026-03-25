---
title: "About the JC Fixed Rate Template Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-fixed-rate-template-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-fixed-rate-template-form"
---

# About the JC Fixed Rate Template Form

Use this form to set up fixed rate templates. These templates
 allow you to define the rates that will be used when charging labor and burden to jobs.

Rates can be defined by craft, class, shift, earnings factor, and/or employee, providing greater granularity. The more factors you define, the more specific the search will be when determining the rate to use when charging labor and burden to a job. For example, rates defined at the craft level are less specific than rates defined at the craft/class/shift level.
Once you have set up a template, you can assign it
 to jobs in JC Jobs (PR Info tab). When posting job timecards, the template assigned to
 the job will be used to determine the rate to use (based on timecard values). If no rate
 is found (or no template is assigned to the job), the fixed rate defined for the
 employee (in PR Employees) is used. If the employee’s fixed rate is 0.00, wages will be
 based on actual pay rates and burden will be based on the liability template assigned to
 the job.
The fixed rate detail (displayed on the Rate Template Detail tab) is searched using posted timecard values in a specific hierarchy to determine an employee’s rate. The following table displays the hierarchy, where “X” indicates a value has been entered

PRCo
Craft
Class
Shift
Earn Factor
Employee

1
X
X
X
X
X
X

2
X
X
X

X
X

3
X
X
X
X

X

4
X

X
X
X

5
X

X
X

6
X

X

X

7
X

X

8
X
X
X
X
X

9
X
X
X

X

10
X
X
X
X

11
X
X
X

12
X
X

- Effective Date - This date is used to determine the effective date for labor/burden rates. This will allow you to define new rates ahead of time, while preserving the current rates until the new ones are in effect. When charging labor and burden to jobs, timecards with dates prior to the effective date will use the old rate, timecards with dates on or after the effective date will use the new rate.

- Move New Rates to Old Rates - After the Effective Date has passed, the ‘new’ rates are in effect and 'old' rates are no longer valid. If you no longer need the old values, you can replace them with the new values using the ‘Move Template Rate from New to Old’ option in the File menu. This will set all old rate values to the new rate values. You can then reset the Effective Date and enter new rates as necessary.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-fixed-rate-template-copy-form)JC Fixed Rate Template Copy
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs
[](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)PR Employees
