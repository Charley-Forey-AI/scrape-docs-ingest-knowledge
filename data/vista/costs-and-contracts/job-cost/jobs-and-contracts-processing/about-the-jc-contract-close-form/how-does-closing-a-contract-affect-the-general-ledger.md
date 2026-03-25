---
title: "How does closing a contract affect the general ledger? | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/how-does-closing-a-contract-affect-the-general-ledger"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/how-does-closing-a-contract-affect-the-general-ledger"
---

# How does closing a contract affect the general ledger?

Soft closing has no effect on GL. Final (hard) closing has an
 effect on GL if you use separate accounts for open and closed jobs in the JC department
 file.
In that case, final closing means that any
 additional entries will go to the accounts for closed contracts/jobs. You can have the
 JC Contract Close program make automatic journal entries while closing each
 contract/job, so that all of the revenue and costs will be moved from the open accounts
 to the closed accounts. This is accomplished by selecting the Summary or Detail radio
 buttons on the GL Close tab in the JC Company Parameters program. This allows automatic
 entries to be made, either summarized by department or for every contract.
The automatic GL entries on closing should be used
 only if you are very consistent with how you post job costs to GL. The process looks
 only at the cost type accounts set up in the JC Departments. It does not look at the
 actual accounts you posted to or at the special Payroll accounts by Earnings and
 Liability type in the department file. For example, the total job-to-date labor cost
 will be transferred from the open labor account to the closed labor account currently
 shown in the JC Departments.
The following table summarizes the effects of the
 two closing steps, in conjunction with the Allow Posting to Soft-Closed Jobs and
 Allow
 Posting to Hard-Closed Jobs checkboxes in JC Company Parameters:
OpenSoft CloseHard Close
Enter Costs: YAllowedWarning, but
 allowedWarning, but
 allowed
Enter Costs: NAllowedNot allowedNot allowed
GL Accounts UsedOpenOpenClosed
