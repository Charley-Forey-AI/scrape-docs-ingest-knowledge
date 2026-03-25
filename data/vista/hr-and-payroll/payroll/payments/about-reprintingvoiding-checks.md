---
title: "About Reprinting/Voiding Checks | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/about-reprintingvoiding-checks"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/about-reprintingvoiding-checks"
---

# About Reprinting/Voiding Checks

If a situation occurs that requires you to reprint employee paychecks (e.g. printer malfunctions, lost or damaged checks), you must first remove the existing employee payment information.
This is done using the Existing Checks tab on the PR Check Print form.
The Existing Checks grid displays existing computer checks for the pay period based on the range of check numbers specified above the grid. All entries are listed in order by check number. Before clearing or voiding any checks, make sure only those checks you want to reprint are listed in the grid. If not, re-enter a range of check numbers until the list contains only those checks that need to be reprinted. Select the desired option (Clear or Void Existing Checks) and click the Clear/Void button to process the entries in the grid. Once processed, checks can then be reprinted for those employee sequences using the normal check print process.

- Clear Existing Check #s - Use this option when the check numbers involved can be reused. Generally, this situation only occurs when no checks were actually printed, such as when doing a test run on plain paper. When a check is cleared, its payment information is removed from the Employee Sequence table (PRSQ). If the check has not been interfaced, its number can be reused immediately. However, if the check has been interfaced (via PR Ledger Update), it is added to the PR Void Payments table (PRVP). The check number cannot be reused until the PR Ledger Update is run again and the entry removed from CMDT (CM Detail Transactions) and PRPH (PR Payment History).

- Void Existing Check #s - Use this option when the check numbers involved cannot be reused; that is, checks were printed, but an error was found, and the checks are no longer valid. When voiding checks, you can enter a memo describing why the checks are being voided and the memo is recorded with each voided check in the PR Payment History and CM Detail Transactions tables. When a check is voided, its payment information is cleared from the Employee Sequence table (PRSQ) and an entry is added to the Void Payment table (PRVP), regardless of the interface status. When PR Ledger Update is run, the entry is used to add or update existing entries in CM Detail (CMDT) and PR Payment History (PRPH) as “void.”
