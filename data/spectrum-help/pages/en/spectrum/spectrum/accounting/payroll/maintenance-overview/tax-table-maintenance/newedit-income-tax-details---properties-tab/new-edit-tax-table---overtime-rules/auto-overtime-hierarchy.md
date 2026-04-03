---
title: "Auto-Overtime Hierarchy | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/new-edit-tax-table---overtime-rules/auto-overtime-hierarchy"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/new-edit-tax-table---overtime-rules/auto-overtime-hierarchy"
---

# Auto-Overtime Hierarchy

The Federal setup will be used unless a State, Union or Job
 override is present.
State rules should only be set up when regulations in that locale supersede Federal
 standards. Likewise, Union and Job rules should only be set up if they exceed State and
 Federal requirements. If no rules have been set up at the Federal level, no records will be
 converted from regular to overtime during the update.
Note: The calculations will be based on Federal and State setup; any
 'overtime' entries recorded for County or Local jurisdictions will be disregarded.
Step 1: The
 Auto-Overtime Update will look first to the [New/Edit Union Overtime Rules](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/newedit-union-overtime-rules) to
 determine if the override by union or override by job will take priority.
This union overrides job rules? = Yes (checkbox selected)
This union overrides job rules? = No (checkbox clear)

- Union rules, if defined in [Union Overtime Rules](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/newedit-union-overtime-rules)

- Job rules, if defined in [Job Payroll Setup](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-payroll-setup)

- State rules, if defined in [New Edit Tax Table - Overtime Rules](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/new-edit-tax-table---overtime-rules)

-  Federal tax code of employee.

- Job, if defined in [Job Payroll Setup](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-payroll-setup)

- Union rules, if defined in [Union Overtime Rules](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/newedit-union-overtime-rules)

- State rules, if defined in [New Edit Tax Table - Overtime Rules](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/new-edit-tax-table---overtime-rules)

-  Federal tax code of employee.

Canadian users should configure the Auto-Overtime Rules in [Job Payroll Setup](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-payroll-setup) to match
 Federal (or other job-specific requirements).

Step 2: After Auto-Overtime Rules for the particular time card line are applied, the system will additionally look at the day of week when determining whether the time card line qualifies for overtime. If the day is Saturday or Sunday, the system will look at the respective overtime settings and double time settings and perform the calculation accordingly. If changing the line to overtime or double time, the message on the report will refer to the pay type (O or D).
