---
title: "Service Management Update | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update/service-management-update"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update/service-management-update"
---

# Service Management Update

Each time the Service Management update is run, any Employee/Payment Sequence combination that needs reprocessing or has non-posted timecards is skipped.
Labor costs are updated to the work order. For job work orders, labor costs are updated to both the work order and Job Cost.
Labor costs may be updated to Job Cost using several different options.

- Actuals — All earnings can be updated to JC exactly as posted in Payroll. The job and phase on each timecard along with the JC cost type assigned in PR Earnings Codes are used to update actual hours and costs in JC.

- Fixed Rate — If an Employee has been assigned an SM Fixed Rate in PR Employees, then labor and burden are updated to the SM work order based on this rate, the posted hours, and the SM pay type assigned to the time entry. This rate is assumed to represent the fully burdened amount cost.If there has been a JC Fixed Rate Template assigned, the form searches for fixed rates there instead of PR Employees.

- Burden — If a JC Fixed Rate is not used, labor burden can be updated to Job Cost based on Liability Template and Liability Type as either actual amounts, or a rate of earnings. Furthermore, burden may be redirected to a specific phase and/or cost type on the job. Liability templates are maintained in Job Cost. If a liability template has not been assigned to the job, or the liability type has not been set up on the template, then actual burden costs are updated to JC.

- Premium Time — If a JC Fixed Rate is not used, the portion of earnings exceeding its straight time equivalent can be redirected to a specific phase and/or cost type. If a Premium Time Phase or Cost Type is set up in the liability template assigned to the job, the straight time portion (i.e., earnings amount/factor) posts to the earnings code's standard cost type (assigned in the PR Earnings Codes form). The overtime portion (that is, the earnings amount–straight time equivalent) posts to the Premium Phase and Cost Type.

- Equipment Costs — All equipment usage updates to JC as actual hours and costs. The job and phase entered with the timecard, along with the JC equipment cost type, is used for the update. Equipment costs are calculated using the revenue code's rate times the units of usage posted. Usage units are converted to hours using the hours per unit factor that was set up with the revenue code.
