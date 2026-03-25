---
title: "About the CM PBA Reconciliation Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-the-cm-pba-reconciliation-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-the-cm-pba-reconciliation-report"
---

# About the CM PBA Reconciliation Report

Use the CM PBA Reconciliation Report to view actual and expected balances on PBA accounts and the trust account activity based on your setup and transactional activity.
 If there is a difference between the actual and expected balances displayed in this report, use it as a starting point to assist with reconciliation.
 For details on setup steps that you must take to make this report meaningful, see [Link a PBA Trust Account to a Contract](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-project-bank-accounts-au/link-a-pba-trust-account-to-a-contract).
 To reconcile this report to your bank balance, compare the activity reported by your bank to the activity tracked and reported by Vista. The following activities appear in the CM PBA Reconciliation report and their net result appears as the Project Balance:

- Receipts applied toward the principle contract using the AR Cash Receipts form

- Payments against subcontracts using the SL Subcontract Claims form

- Transfers of retention funds from the general PBA to the retention PBANote: You must manually transfer these retained funds from the General account to the Retention account.

The CM PBA Reconciliation report does not return non-PBA activity. For example, any invoice that is not coded as type 7-SL in the AP transaction entry forms is not reflected in the report, even if the contract itself has a PBA assigned to it.
 The Actual Balance displays the balance in the CM Account according to the through date you selected in the launcher.
If you have non-PBA activities in your bank report (for example, payments on invoices coded directly to the job, bank fees, interest earned), the net result displays as the Difference. If you want it to match the report or if PBA compliance requires it, make one or more transfers using the CM Transfers form.
