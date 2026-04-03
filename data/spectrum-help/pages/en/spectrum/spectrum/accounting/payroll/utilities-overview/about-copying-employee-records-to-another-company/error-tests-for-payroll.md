---
title: "Error Tests for Payroll | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/about-copying-employee-records-to-another-company/error-tests-for-payroll"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/about-copying-employee-records-to-another-company/error-tests-for-payroll"
---

# Error Tests for Payroll

Spectrum performs the following tests to find errors
 associated with Payroll setup when copy update is run.
If any errors are found, they will display on the [Copy Employee Listing - Payroll Exceptions](/en/spectrum/spectrum/accounting/payroll/utilities-overview/about-copying-employee-records-to-another-company/copy-employee-listing---payroll-exceptions) report.

- Verify that the employee code is not already present in destination company

- Verify that the employee's non-union pay group code is not present in destination company

- Verify that the employee's department code is not present in destination company

- Verify that the employee's worker's compensation code is not present in destination company

- Verify that the employee's union code is not present in destination company

- Verify that the employee's wage code is not present in destination company

- Verify that the employee's EEO classification code is not present in destination company

- Verify that the employee's vacation accrual code is not present in destination company

- Verify that the employee's holiday accrual code is not present in destination company

- Verify that the employee's sick accrual code is not present in destination company

- Verify that the employee's status code is not present in destination company

- Verify that the employee's T+M billing code is not present in destination company

- Verify that the employee's Federal tax code is not present in destination company

- Verify that the employee's resident state code is not present in destination company

- Verify that the employee's permanent work state code is not present in destination company

- Verify that the employee's resident county code is not present in destination company

- Verify that the employee's resident local code is not present in destination company

- Verify that the employee's recurring deduction/add-on code(s) is not present in destination company

- Verify that for assigned deduction/add-on codes the tax effects match

- Verify that for assigned deduction/add-on codes the direct costs match

- Verify that for assigned deduction/add-on codes the week numbers match

- Verify that for assigned deduction/add-on codes the year-end clears match

- Verify that for assigned deduction/add-on codes the A/P invoice details match

- Verify the employee-specific rates in Non-Union Pay Group

- Verify there are no layoff checks present for this employee in Layoff Check Entry (PR.LCXE) in the current company

- Verify there are no replacement checks present for this employee in Replacement Check Entry (PR.RPCKE) in the current company

- Verify there are no pre-time card entries present for this employee in Pre-Time Card Entry (PR.PTCE) in the current company

- Verify there are no recurring deductions or add-ons currently set up in Employee Deduction/Add-on Maintenance (PA.EVDM) for this employee in the current company that are calculated using a formula not present in the destination company 5) Verify that this employee's supervisor code is not an invalid supervisor code in the destination company

- Verify that no company-specific user-defined fields have been assigned data for this employee

-  Verify that this employee's assigned cost center is not an invalid cost center code in the destination company (blank code OK)

- Verify that this employee code is not currently being changed (PR.XCHFM)
