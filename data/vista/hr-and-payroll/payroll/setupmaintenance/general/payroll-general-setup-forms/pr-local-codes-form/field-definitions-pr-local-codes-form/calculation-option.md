---
title: "Calculation Option | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-local-codes-form/field-definitions-pr-local-codes-form/calculation-option"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-local-codes-form/field-definitions-pr-local-codes-form/calculation-option"
---

# Calculation Option

Select a calculation option for the processing
 of local deductions and liabilities (associated with this local code) during payroll
 processing.
Note: The information below refers to posted local codes and
 resident local codes. Posted local codes are pulled from [JC Jobs](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form). Resident local codes are pulled from [PR Employees](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form).

- 0-Posted Local only - With this
 option, the system calculates and deducts only the posted job's local tax.

- 1-Full amount of both Posted and
 Resident - With this option, the system calculates both the employee's resident
 local tax and the posted job's local tax, and deducts both at the full amount.


- 2-Posted Local w/difference to
 Resident Local - With this option, the system calculates both the employee's
 resident local tax and the posted job's local tax. The full amount of the posted
 job's local tax is deducted, while the difference between the two is deducted for
 the resident local. For example, if the resident local tax is $70 and the posted
 job's local is $50, $50 is deducted for the posted job's local and $20 is deducted
 for the resident local ($70 - $50 = $20). On the other hand, if the posted job's
 local tax is higher or equal to the resident local, nothing goes to the resident
 local, while the posted job's local gets the full tax amount.

Note: When accumulations are updated, the subject and eligible wages are updated only to the posted job's local tax.

- 3-Posted Local using higher of Resident or Posted rate - With this option:

- If the posted job's local code and the employee's
 resident local code are both set to option 3, the system calculates the
 posted local tax using the higher of the employee's resident local tax rate
 or posted job's non-resident local tax rate. For example, if an employee's
 resident local tax rate (rate #1) is 1.5%, but his timecard is posted to a
 different local code with a 1.0% non-resident tax rate (rate #2), his posted
 local tax will be calculated using the higher (1.5%) tax rate.

- If the posted job's local code is set to this option 3, and the employee's resident local code is set to options 0, 1, or 2, then the system applies the calculation option for the resident local code to the posted local code. For example, if the posted local code is set to option 3, and the resident local code is set to 1, then calculation option 1 will be applied to the posted local code (even though it is set to option 3).
