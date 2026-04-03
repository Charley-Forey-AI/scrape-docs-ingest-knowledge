---
title: "Worker's Compensation Hierarchy | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/workers-compensation-hierarchy"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/workers-compensation-hierarchy"
---

# Worker's Compensation Hierarchy

Spectrum automatically computes worker's compensation costs and applies them to jobs, using one of several methods (for example, dollars per hundred, rate per hour, and so forth).
If applicable, different rates can be entered for one employee for different types of work.
Worker's compensation is a burden cost that in some states is shared by both employee and employer; this calculation is based on the work performed. Each line of Pre-Time Card Entry and Time Card Entry includes a worker's compensation code (see also base code). The combination of work state and code is how the file tells the software what rate to charge.
The software defaults information in this order:

- If the employee has the Always use this worker's comp code on time card? checkbox selected, the software uses this code from Employees.

- Phase File Maintenance

- Job File Maintenance

- Site File Maintenance

- Department Expense Maintenance

- Wage Code File Maintenance

- In Time Card Entry, the software will perform the following steps to determine whether the worker's compensation code is assigned from Wage Code File Maintenance, and if so, from which particular wage code.

- Step A: Determine whether wage codes are in use in the current company • If Yes, go to Step B • If No, Assign employee's worker's compensation code (last step of Worker's Compensation Hierarchy)

- Step B: Determine whether a wage code has been assigned to this time card line • If Yes, go to Step C • If No, Assign employee's worker's compensation code (last step of Worker's Compensation Hierarchy)

- Step C: Determine whether the wage code + union code on the time card line has a worker's compensation code assigned in Wage Code File Maintenance • If Yes, Assign the worker's compensation code found in Wage Code File Maintenance • If No, Assign employee's worker's compensation code (last step of Worker's Compensation Hierarchy)

- Employees

## Additional Information

- Composite rate is the full amount per hour to be remitted to the state for states in which calculation is based on dollars per hour.

- Deduct rate is that portion of the total composite rate being deducted from the employee's check based on an amount per hour.

- Class code is the last digits of the worker's compensation identifying number.

Related information

- [Worker's Compensation Limit Hierarchy](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/wage-code-file-maintenance/workers-compensation-limit-hierarchy)
