---
title: "Equipment Management Updates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update/equipment-management-updates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update/equipment-management-updates"
---

# Equipment Management Updates

Each time the Equipment Management update is run, any Employee/Payment Sequence combination that requires processing or has non-posted timecards is skipped.
Equipment cost distributions from mechanics timecards are tracked, as is equipment revenue from usage. The values are maintained for both the current and last EM update run for each pay period. Current values are recalculated with each update. During the update, if the current and last updated values are equal, no entries are posted to EM. If they don’t match, a reversing entry is made to back out the old amounts and a new entry is added for the current amounts. After EM is updated, the current values are copied to the old ones and saved as the last interface values. All entries are saved until the pay period is purged.
Equipment costs may be interfaced to EM using several different options.

- Actuals — All earnings posted as mechanics time can
 be updated to EM exactly as posted in Payroll. The equipment and cost code on
 each timecard, along with the EM cost type assigned in EM Company Parameters,
 are used to update actual hours and costs in EM.

- Fixed Rate — If an employee has been assigned an EM Fixed Rate in PR Employees, then labor updates to EM using the hours posted times this rate. This rate is assumed to represent the fully burdened cost of the employee’s labor (i.e., actual burden is not interfaced to EM).

- Burden — If an EM Fixed Rate is not used, then labor
 burden can be updated to Equipment Management using the burden rate set up in EM
 Company Parameters. If the rate is not 0.00, then labor burden is calculated as
 earnings times this rate. If the burden rate is 0.00, then an add-on burden rate
 may be used. If this rate is not 0.00, then actual liabilities plus earnings
 times this rate updates as burden to EM.

Equipment Revenue is updated to EM using the Equipment, Revenue Code, and Usage Units posted with the timecard. Equipment revenue is calculated using the revenue code’s rate times the units of usage posted. The revenue updated to EM matches the equipment costs updated to JC.

## Equipment Usage with Service Timecards

When you run the ledger update for
 service timecards that include equipment usage, the system updates the usage as
 revenue to Equipment Management using the Equipment, Revenue Code, and Usage Units
 posted with the timecard. It also updates the usage as costs to the work order in
 Service Management, which can then be billed. The update to GL will create one
 revenue entry to the GL account specified for the revenue code in EM Departments,
 and one cost entry to the Cost account or Cost WIP account (if tracking WIP)
 specified for the work completed line in SM Work Completed.
If you change a timecard after it is
 posted, you will need to rerun PR Ledger Update to update the changes to EM, SM, and
 GL accordingly.
