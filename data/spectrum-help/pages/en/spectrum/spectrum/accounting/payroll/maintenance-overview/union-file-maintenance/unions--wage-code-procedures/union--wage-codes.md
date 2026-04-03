---
title: "Union & Wage Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/unions--wage-code-procedures/union--wage-codes"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/unions--wage-code-procedures/union--wage-codes"
---

# Union & Wage Codes

Wage and union codes (and pay rate levels) are a method of
 easing time card entry.
Defaults may be defined so that pay rate information for each employee/job defaults into
 Pre-Time Card Entry and Time Card Entry. These codes are intended as a convenience for the
 user; they are optional.
First, a few guidelines for wage/union codes and non-union pay groups may help you determine which system best suits your needs:
If you run a partial union shop, union codes and possibly wage codes should be used. If you are not union, but have union-like accruals (for example, health and welfare, pension, and so forth) or deductions, you would again select the union method. If you have prevailing wage codes (Davis Bacon) as your basic level (no accruals or deductions), non-union pay groups would be selected. If in doubt, use the union set up in the Payroll Installation screen -- this provides more flexibility.
The non-union pay group allows for only one group code entry in the Job Maintenance screen. The pay group record does have nine pay levels and, in addition, does offer a special employee pay rate within that pay group, which would override the employee's pay rate in Employees -Rates.
The wage code/union codes are also entered in Job Maintenance. In this screen, you may enter the wage code and union code combination(s) that will be used on the job. You may enter only one wage code per job (for example, L1 can only be entered once, although union code LAB276 could be associated with multiple wage codes and thus be in the job file more than once). During Pre-Time Card Entry and Time Card Entry, the wage code will default from the employee file (for example, Laborer, Operator) or from the equipment file if an equipment code is entered in Time Card Entry. Once the job is entered and the wage code is defaulted, the software will automatically default the union code from the job file.
Another element in the rate default is the union and/or wage code level. The software first looks to the phase file and then the job file for a level number. If that field is blank, the software then uses the setting in Employees. If that field, too, is blank, the user will be prompted to enter a level number during Pre-Time Card Entry and Time Card Entry.
Finally, there is a special checkbox for unions that require the employer to add a fringe benefit into the employee's check and then deduct it back out. This checkbox, the gross payprompt in the Union File Maintenance screen, applies only to union deductions. Selecting the checkbox allows you to add the fringe to the employee's pay rate (which isn't shown separately on the paycheck), but set it up as a standard union deduction.

Related information

- [Union Files Examples](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/union-files-examples)

- [Wage Files Examples](/en/spectrum/spectrum/accounting/payroll/in-depth-overview/wage-files-examples)
