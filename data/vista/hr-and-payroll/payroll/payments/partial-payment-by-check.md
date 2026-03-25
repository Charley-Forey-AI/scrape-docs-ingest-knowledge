---
title: "Partial Payment by Check | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/partial-payment-by-check"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/partial-payment-by-check"
---

# Partial Payment by Check

Below are steps to follow if you need to produce a physical
 check for an employee that is routinely paid by direct deposit.

1. Create a dummy deduction
 code in PR Deductions and Liabilities for direct deposit adjustments. This code
 may use any GL expense account you prefer because your entries should create
 both a credit and debit of equal value, with a net effect of 0 to GL.

1. Find the employee in PR
 Employee Pay Seq Control. On the Deductions tab, add the dummy deduction code.
 Use the amount for the manual check to be issued as the deduction amount. This
 amount cannot be the entire net check because a direct deposit of 0 is not
 allowed.

1. Click Process.

1. In PR Timecard Entry
 create another sequence for this employee with a timecard line of a zero amount.


1. Find the employee in PR
 Employee Pay Seq Control for this new sequence. On the Deductions tab, enter a
 negative deduction to the same dummy code for the same dollar value (creating a
 positive payment amount).

1. Select C-Computer from the Check Type drop-down field.


1. Click Process.

1. Carefully review this PR
 Employee Pay Period Control screen again after you process and override to 0 any
 Deductions or Liabilities that may have carried over from the standard setup.
 The two deduction adjustments must net to zero. All correct accumulations,
 taxes, and basis amounts will be retained on the sequence with the direct
 deposit record. The system will now generate a physical check and a direct
 deposit.
