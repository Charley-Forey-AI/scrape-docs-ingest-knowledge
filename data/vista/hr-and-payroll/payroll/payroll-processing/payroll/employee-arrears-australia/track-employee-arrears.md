---
title: "Track Employee Arrears | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/track-employee-arrears"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/track-employee-arrears"
---

# Track Employee Arrears

If you want to cover medical (or other) deductions for laid-off employees that you plan to rehire, you can set up the system to keep an arrears history.
This arrears history will continue to accumulate as you process a payroll for each pay period. Once you rehire the employee, the system will stop tracking arrears and you can initiate a payback plan for the employee.
This topic provides an overview of how to track and process arrears and payback. Click on any related links to access more detailed information.

1. Determine which deduction codes are subject to arrears, as well as the standard payback amount/rate for each deduction code. See [Set Deductions as Subject to Arrears](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/set-deductions-as-subject-to-arrears) for more information.

1. Activate arrears calculations for eligible employees. See [Activate Arrears Calculations for Employees](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/activate-arrears-calculations-for-employees) for more information.

1. In the PR Arrears/Payback History form, enter any historical arrears records that still require payback. For more information, see [Manually Enter Arrears and Payback Records](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/manually-enter-arrears-and-payback-records).Important:Before entering historical arrears records, make sure that all current payrolls are closed. If a payroll is open, and an arrears-eligible employee has a timecard record, the system will deduct payback amounts.

1. During payroll processing, the system calculates arrears for employees that:

- are active for arrears

- are associated with a deduction code that is subject to arrears

- do not have timecard records for the current pay period.
Once processing is complete, the system updates the PR Arrears/Payback History form with the arrears amounts. The system will continue to calculate arrears for employees during payroll processing until they have timecard records for the current pay period.

Note:There may be a time that you lay off an employee who is active for arrears, but they still have timecard records in the current pay period. In some instances, the employee may not have enough earnings to cover their standard deductions. If the employee's earnings are negative, the system will start reversing any deductions that are subject to arrears one at a time until the total earnings amount is positive.
For example, an employee has a total earnings of $125 and deductions totaling $235 (two of which are arrears-subject deductions of $100 each). The system would reverse the first arrears transaction bringing the total deductions to $135. Since the deductions are still greater than the earnings, the system would reverse the second arrears transaction of $100, bringing the employee to a positive earnings amount of $90. The system would then add the reversals to the PR Arrears/Payback History form as arrears records to be paid in the future.
If the employee's earnings are still negative after the system has reversed all arrears-subject deductions, the system will not reverse any other deductions. In this case, you may need to manually adjust the deductions for the employee.

1. You can view arrears and payback records, as well as an employee's life-to-date balance using the PR Arrears/Payback History form. For more information, see [About Viewing Arrears and Payback History](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/about-viewing-arrears-and-payback-history).

1. When an employee starts working again, and has a timecard record in the current pay period, the system will deduct the full payback amount from the employee's earnings during payroll processing (after all other deductions have been processed). This payback amount is based on the rate/factor set up for the deduction code (PR Deductions/Liabilities form) or the employee/deduction code combination (PR Employee Dedns/Liabs form). If the employee has multiple deductions that require payback, the system applies the full payback amount one deduction at a time.Note: If the employee does not earn enough to cover a payback amount, the system will reverse the payback and add it as an arrears record to the PR Arrears/Payback History form to be paid in the future.
For example, an employee has an outstanding arrears balance of $1,000 based on two deduction codes. Both deduction codes have a payback amount of $100 per pay period. If the employee earns $150, the system will deduct $100 for the first deduction code, but will not deduct the $100 for the second deduction code. Instead, that $100 will become an arrears record, and the employee will receive a check for $50.

1. If you want to review calculated payback amounts for an employee, use the Deductions tab in the PR Employee Pay Seq Control form. From here, you can adjust the payback amounts and then reprocess the payroll. Using the example from step 4 above, you could manually add a payback record so that the employee could pay some portion of the second deduction code arrears amount. See [About Reviewing Processed Payrolls](/en/vista/vista/hr-and-payroll/payroll/payments/about-reviewing-processed-payrolls) for more information.

1. During payroll processing, the system updates the PR Arrears/Payback History form with the payback records. Once the employee has paid back the entire arrears amount (the Life to Date balance is zero), the system stops deducting payback amounts from the employee's earnings.

1. At any time during the arrears and payback process for an employee, you can enter manual arrears or payback records in the PR Arrears/Payback History form. For more information, see [Manually Enter Arrears and Payback Records](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/manually-enter-arrears-and-payback-records).

1. You can purge arrears and payback history records when purging closed pay periods using the PR Purge form. For more information, see [Purge Pay Periods](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/purge-pay-periods).
