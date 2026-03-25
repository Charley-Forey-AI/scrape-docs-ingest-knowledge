---
title: "Payroll Interface to Job Cost | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/payroll-interface-to-job-cost"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/payroll-interface-to-job-cost"
---

# Payroll Interface to Job Cost

When payroll entries are made to a job and phase code, both the direct earnings and the associated burden (liabilities) need to be added to your job costs.
The simplest way to do that is to have the entire amount go to the Labor cost type of the entered phase. However, if you want more flexibility, there are several ways to break out various parts of your labor costs to different phases and cost types, and to send a set burden rate to Job Cost instead of the exact amount calculated in PR. You can even send a flat fixed rate per employee to Job Cost rather than any direct earnings and liabilities.
Earnings
In Payroll’s Earnings Codes program, you designate to which cost type each earnings type is sent.
Liabilities
Using HQ Liability Types, you will define each of the liability types used by your company. Then, in the JC Liability Template form, you will define the following for each liability type:

1. Phase—Instead of following the phase the earnings are going to, you can designate a specific phase for this category of liabilities to go to.

1. Cost type—Instead of following the cost type the earnings are going to, you can designate a specific cost type for this category of liabilities to go to.

1. Calculation Method—You can have liability amounts calculated by Payroll (method E), or you can use a specified percentage of direct labor cost (method R). The Rate method can also be used for additional markup that is not tied to any payroll liabilities. For example, if you set up a liability type as a percentage method with a rate of 5%, and no liability codes are assigned to that liability type, this will cause an additional 5% of direct payroll to be added to Job Cost.

1. Basis Earnings Codes—For liability types with a calculation method of R-Rate, indicate the earnings that will be included in the basis of the calculation of the liability when interfacing payroll to Job Cost.

Note: Since liability assignments (phase, cost type, method) are set up by template, you can tailor the templates to meet the specific needs for various jobs.
Fixed Rate
In Payroll’s Employee Master, you may enter a fixed rate to charge to Job Cost for specific employees. This might be used so that actual supervisory personnel rates are not seen in Job Cost. The fixed rate will be used instead of both the actual earnings and liabilities.
