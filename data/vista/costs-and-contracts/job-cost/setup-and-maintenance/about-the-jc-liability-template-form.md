---
title: "About the JC Liability Template Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-liability-template-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-liability-template-form"
---

# About the JC Liability Template Form

Use this program to set up liability templates.
These templates are used to define how Payroll burden (Employer-paid liabilities) is charged to Job Cost. By using templates, you may define these liability costs differently for different jobs. For instance, you might burden T&M jobs differently than fixed price jobs. Or, because one of the options on calculating payroll burden is to use specified rates rather than actual costs, you might use different rates for jobs in one state versus another.

- Liability Types - Use this tab to set up each of the liability types that apply
 to this liability template. For each liability type, you specify the phase and
 cost type (if not using the earnings cost type) to which the burden costs
 associated with the liability will be posted. You must also specify the method
 that will be used to calculate the liability (i.e. rate or exact amounts as
 calculated in payroll).

- Basis Earnings Codes - Use this tab to identify the earnings
 that will be included in the basis of the calculation of the liability when
 Payroll is interfaced to JC. You will only need to set up earnings codes for
 liability types with a Method of R (Rate of Gross). Note: If you have one or more liability types flagged to use
 the ‘Rate’ calculation method and you do not define basis earnings codes for
 those liability types, a warning displays (in red) to the right of the
 template description indicating basis earnings codes are missing. Message
 will clear once you have set up at least one basis earnings code for each
 ‘rate’ liability type.
When PR is interfaced to Job Cost, any
 liability set up in PR with a liability type the same as defined in the
 liability template will be combined and interfaced to JC as a rate of gross
 using the rate in the Liability Rate column times the earnings codes set up here
 for the liability type. Note: Liability
 overrides (method R) do not affect the calculations in PR; only what is
 charged to the job.
Once you have defined the liability templates you plan to use, you can
 assign them to jobs in JC Jobs.

[](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)PR Deductions / Liabilities
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Job Master
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-liabilities-template-copy-form)Copy Template
