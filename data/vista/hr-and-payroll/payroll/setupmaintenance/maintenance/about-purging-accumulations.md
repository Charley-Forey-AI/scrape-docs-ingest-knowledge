---
title: "About Purging Accumulations | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/about-purging-accumulations"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/about-purging-accumulations"
---

# About Purging Accumulations

Purging accumulations in the PR Purge form removes monthly earnings, deduction, and liability totals for employees through a specified month and year.
You will use the Accumulations tab on the PR Purge form to purge employee
 accumulations. When you purge accumulations, you must specify a prior month/year. If you
 specify any month within the current year, a warning displays notifying you that current
 year accumulations will not be purged. The system still allows the entry, but all
 accumulations for the current year (determined by system date) are skipped during the
 purge process.
 If you have specific deductions/liabilities you want
 purged, you can restrict purging by deduction/liability code. This
 allows for purging deductions/liabilities that are flagged for selective purging;
 that is, deductions/liabilities for which you have selected the Selectively purge accumulations checkbox in PR Deductions/Liabilities. If you do not restrict the purge by deduction/liability code, it will include all deductions/liabilities except those
 flagged for selective purging. In addition, if you are purging by
 deduction/liability code and the deduction/liability has a lifetime limit, you have
 the option to restrict the purge by employee.
During the purge process, the system purges accumulations through the month and year specified. For example, if you enter 12/21 in the Through Month field, the system deletes all accumulations records for 2021 through the month of December.

## Australian / Canadian Companies

For Australian and Canadian companies, each employee/month/type/EDL code accums record is associated with one or more accumulations detail records (stored in PR Employee Accums Detail). When you purge accumulations, the system deletes the accumulations record, along with all of its associated detail records.

For more information about purging accumulations, see [Purge Accumulations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/about-purging-accumulations/purge-accumulations).
