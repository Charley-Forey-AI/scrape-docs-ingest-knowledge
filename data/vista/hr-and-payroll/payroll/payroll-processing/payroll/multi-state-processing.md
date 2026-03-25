---
title: "Multi-State Processing | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/multi-state-processing"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/multi-state-processing"
---

# Multi-State Processing

The Payroll module easily accommodates payroll for multiple states, with default flags that direct the system to use either the state in which the job is located or the resident state of the employee for state tax and unemployment deductions and liabilities.
The subject amount of each tax is maintained by
 state. Employees working in multiple states in the same pay period or in the same day
 will have taxes and subject amounts calculated by state. Unemployment taxes may be based
 on resident state or job state, but will always consider year-to-date subject wages
 across all states in applying the limits. The default flags are located in the PR
 Employees and PR Company Parameters forms, and are described below.
In PR Employees
Always Use Employee’s Tax,
 Unemployment, and Insurance States — If this flag is checked, the
 employee’s standard Tax, Unemployment, and Insurance States are always used. If
 unchecked, then the State/Local options in the PR Company Parameters form control the
 defaults.
In PR Company Parameters

- Use Job, SM Work Order, or Office State for Tax State —
 If this flag is checked, and the Always Use Employee’s Tax, Unemployment, And
 Insurance States flag (PR Employees) is unchecked, then the tax state for
 withholding defaults to the state of the job. If no job is entered, the PR
 Company’s Office State is used. If no Office State has been set up, then the
 employee’s standard tax state is used. If this flag is unchecked, then the
 default is always the employee’s standard tax state.Note: If this flag is checked, but the job or office state
 has a reciprocal agreement with the employee's tax state, the employee's tax
 state will be used.
For time posted to SM work orders, the tax state for withholding defaults
 to the PR State specified on the work order. If the work order does not
 specify a PR State or if this flag is unchecked, then the default is either
 the employee’s work office tax state or resident tax state (if work office
 tax state is blank) in PR Employees.

- Use Job or SM Work Order State for Unemployment State —
 If this flag is checked, and the Always Use Employee’s Tax,
 Unemployment, and Insurance States flag (PR Employees) is
 unchecked, then the unemployment state will default to the state of the job. If
 no job is entered, the employee’s standard unemployment state will be used. If
 not checked, then the default will always be the employee’s standard
 unemployment state. Although the subject amount for an employee is maintained by
 state, the year-to-date subject amount across all states is used before
 determining if a wage limit has been exceeded.For time posted to SM work orders, the unemployment state
 for withholding defaults to the PR State specified on the work order. If the
 work order does not specify a PR State or if this flag is unchecked, then
 the default is always the employee’s standard unemployment state.

- Use Job or SM Work Order State for Insurance State — If
 this flag is checked, and the Always Use Employee’s Tax,
 Unemployment, and Insurance States flag (PR Employees) is
 unchecked, then the insurance state will default to the state of the job. If no
 job is entered, then the employee’s standard insurance state will be used. If
 not checked, then the default will always be the employee’s standard insurance
 state.For time posted to SM
 work orders, the insurance state for withholding defaults to the PR State
 specified on the work order. If the work order does not specify a PR State
 or if this flag is unchecked, then the default is always the employee’s
 standard insurance state.
Note: You can
 override the Tax, Unemployment, and Insurance states in PR Timecard
 Entry.
