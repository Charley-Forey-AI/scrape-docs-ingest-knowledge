---
title: "Non-Union Pay Group Phase Overrides - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/non-union-pay-group-maintenance/non-union-pay-group-phase-overrides/non-union-pay-group-phase-overrides---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/non-union-pay-group-maintenance/non-union-pay-group-phase-overrides/non-union-pay-group-phase-overrides---field-descriptions"
---

# Non-Union Pay Group Phase Overrides - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/ Buttons
Descriptions

Phase rate overrides ALL other rates?
Select this checkbox ONLY if you want the phase override rate entered in this window to override any other pay group rates. If you select this checkbox, you must enter a non-zero rate in the phase rate fields. This command receives the highest priority in the software, even if the Payroll Installation prompt for Default pay rate field is set to Employee pay rate or Higher of the two rates.
To view a table showing how Spectrum's pay group default hierarchy is affected when you select this checkbox, click [Pay Group Rate Default Hierarchy](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/non-union-pay-group-maintenance/non-union-pay-group-phase-overrides/pay-group-rate-default-hierarchy)

Phase
Phase overrides entered here will override existing pay group rates and affect all employees.

Regular
Overtime
Double time
Enter the various pay rates for each phase override.

Burden

- Enter the burden percentage rate for this phase.

- The burden amount refers to the employer's additional payroll costs (FICA, FUTA, SUTA, worker's compensation costs and other burden components).

 More info For more information on pay groups burden hierarchy, refer to the [Pay Groups Burden Hierarchy](/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/pay-groups-burden-hierarchy) topic.

Billing code
Enter the time and material billing code for this phase. This is only used if the Time + Material module is installed and a Time + Material job is used.

Fringe

- You can only enter a fringe override here when there is a prevailing wage add-on code entered in the Pension or Cash fringe benefit fields of the Prevailing Wage window.

- When adding rate overrides, the fringe rate associated with the first pay level will default from the Prevailing Wage window, this fringe amount can be overwritten manually (if the fringe is blank then the fringe for this override rate will be zero <$0>). In addition, fringe rules and the certified status can be disabled by phase, employee, or employee phase.

 More info For more information on the fringe rate hierarchy and Prevailing Wage processing, refer to the [Prevailing Wage and Davis-Bacon Processing](/en/spectrum/spectrum/accounting/payroll/in-depth-overview/summary-of-prevailing-wage-benefits/prevailing-wage-and-davis-bacon-processing) topic.

DB/PW?
If Davis-Bacon and prevailing wages are not applicable, select this checkbox to post the time card line as a private job and to ensure the employee will be paid based on the base pay of the pay group (no fringe, prevailing wage, prevailing wage adjustment or pension would apply). Any company 401(k) employee and employer amounts will be calculated, as they would be for a private job.

Disable cert?
Select this checkbox to designate the time card line (that uses this phase) as non-certified. This checkbox can be selected even if the job indicates the line is certified.

Edit/New/Delete buttons
Use these to keep your Spectrum data current. Primary actions will display as
 a larger, green button on the toolbar, while secondary actions will display
 as smaller, gray buttons.

Related information

- [Time Card Entry Certified Hierarchy](/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/time-card-entry-certified-hierarchy)
