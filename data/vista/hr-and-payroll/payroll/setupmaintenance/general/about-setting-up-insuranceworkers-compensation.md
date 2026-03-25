---
title: "About Setting Up Insurance/Worker's Compensation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-insuranceworkers-compensation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-insuranceworkers-compensation"
---

# About Setting Up Insurance/Worker's Compensation

​Vista™ assigns insurance codes to timecard entries to track the
 basis of worker’s compensation and other labor-related insurance, and to calculate these
 costs.
There are many options to determine how these insurance codes are assigned and how they
 are calculated.
The insurance code associated with a timecard entry is made up
 of two parts: (1) the state and (2) the standard insurance code. Each combination that
 will be used must be set up in PR State Insurance Codes where the rates are established.

1. PR Deductions/Liabilities — Set up one or more liability and deduction codes for
 Worker's Compensation insurance. Typically, worker's compensation is set up as a
 liability with a method of Straight Time Equivalent. Only one liability code is
 required, even if working in multiple states with many comp codes, as long as they
 share the same liability General Ledger account. One is needed for each different
 method of calculation at a minimum. Some states may use a deduction or other method.
 You may choose to also set up a code for General Liability that can be calculated
 based on labor along with worker's compensation.

1. HQ Insurance Codes — Set up the standard insurance codes describing the work
 performed.

1. PR Company Parameters, Job Cost/Service Mgmt tab — If the default insurance code
 should be based on the work performed, check the
 Insurance Based on Phase or SM Work Order
 Scope
 option. Leave it unchecked if the standard insurance code specified
 for each employee should always be used.
 If insurance is typically based on the job phase
 (job timecards) or the work (SM work order timecards), but you have some
 employees whose standard insurance code should always be used, you can
 override the
 Insurance Based on Phase or SM Work
 Order Scope
 option by checking the
 Always Use Employee’s Standard
 Insurance Code
 option for each applicable employee in PR Employees.

1. PR Company Parameters, State/Local tab — If the state portion of the insurance code
 should be based on the job state, check the
 Use Job or SM Work Order State for
 Insurance State
 option. Enter the state in which your office is located on this tab
 also. This will be used on timecards that are not posted to jobs. If the

 Use Job or SM Work Order State for
 Insurance State
 option is unchecked, the state code designated for each employee (in
 the Ins State field in PR Employees) is used. If the job state is normally used, but
 you have some employees whose resident state should be used, you can override the

 Use Job or SM Work Order State for
 Insurance State
 option by checking the
 Always Use Employee’s Tax, Unemployment,
 and Insurance State
 option for each applicable employee in PR Employees.
 For SM Work Orders, you can specify to have
 the state portion of the insurance code based on the work order state by
 checking the Use Job or SM Work Order State for Insurance State option.
 Timecards posted to a work order will default the insurance state from the
 PR State in SM Work Orders. If you do not specify a PR State
 on the work order or if the Use Job or SM Work Order State for
 Insurance State option is not checked, the system will use the employee's
 insurance state (from PR Employees).

1. JC Insurance Template — If insurance is based on the job phase, link the standard
 insurance codes to the phases. At least one template must be set up if the link of
 insurance code to phase is the same on all jobs. However, if they are different, set
 up as many templates as needed. For instance, there may be a template for each state
 you work in if the codes are different in each state.

1. JC Jobs — If insurance is based on the job phase, link the
 Insurance Template to the job.

1. PR State Insurance Codes — Set up all combinations of states and insurance codes
 that could be used. Link any deductions or liability codes that may apply to each
 code and establish the rates.

1. PR Employees — Set up the standard insurance code for each employee. This will be
 used if:

- doing insurance by phase, but the timecard
 cannot find a link by job phase or template phase.

- doing insurance by work order, but no insurance
 code is defined for the work order.

- a timecard is not posted to a job (job
 timecards only).

- the
 Insurance by Phase or
 SM Work Order Scope
 option is not selected.

- the
 Always Use Employee’s Standard
 Insurance Code
 option is checked.

1. PR Employees - Enter the employee’s resident state in the
 Ins State
 field. If basing insurance on the job and/or job state, you may
 override these options by employee by checking the two override flags.

As timecards are entered, the insurance code including state
 will default based on these options. The insurance code may be overridden during
 timecard entry.
[About Processing Insurance/Worker's Comp](/en/vista/vista/hr-and-payroll/payroll/payments/about-processing-insuranceworkers-comp#concept-865--en__concept-865)
