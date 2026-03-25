---
title: "Job Cost and General Ledger | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/job-cost-and-general-ledger"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/job-cost-and-general-ledger"
---

# Job Cost and General Ledger

All cost transactions that update Job Cost need to make
 corresponding entries to General Ledger. You can set this up to be automatic so that you
 don’t have to worry about JC being out of balance with GL.
Each contract item on a contract is assigned to a department, which defines the GL accounts that are updated when posting revenue or costs to the contract. The job (or jobs) linked to that contract automatically follow the contract.
For example, you might have a commercial division and a residential division, each with its own contracts and jobs, with separate sets of income and expense accounts. You would use separate departments to ensure that the appropriate GL accounts were updated.
If you have divisions within a company that work on the same job(s), you can assign a different department to each contract item. The job cost phases will update GL accounts based on the department of the contract item they are linked to. If you do not have such divisions, you would only need to set up one department to which you would assign all contracts.
Departments are set up in the JC Departments. For
 open jobs/contracts, the Department file stores one account for revenue and one account
 for each cost type. You also have the option to set up override accounts by phase if you
 require separate accounting by phase/cost type. These accounts are always used when you
 update Job Cost and the contract is still open, unless you have allowed the account to
 be overridden when posting or one of the special Payroll accounts is used (see below).
A second set of accounts can be set up to use when posting to closed contracts/jobs. When closing a contract/job, the closing process will automatically transfer the balances from the open accounts to the closed accounts (if you have the GL Close interface level set to Summary or Detail). For more information, select the Closing Contracts and Jobs topic in Related Topics below.
How you use open and closed accounts depends on your accounting method. If you use asset and liability accounts to collect job revenue and costs as they occur, your Department setup will look something like this:
Open Contracts/Jobs
Closed Contracts/Jobs

Liability Account (contract revenue):
2400 Billings on Construction
Income Account (contract revenue):
4000 Revenue Billings

Asset Accounts (job costs):
1210 Work in Progress, Labor
1220 Work in Progress, Material
1230 Work in Progress, Equipment
1420 Work in Progress, Subcontracts
Expense Accounts (job costs):
5010 Cost of Construction, Labor
5020 Cost of Construction, Material
5030 Cost of Construction, Equipment
5040 Cost of Construction, Subcontracts

If you post all job costs directly into income and expense accounts, set up those accounts (the right column in the above example) as both the open and closed job accounts.
In addition to setting up GL accounts for Cost Types, you can also set up the GL accounts used for certain types of payroll costs. The Liability Types and Earnings Types tabs are used to set up these special accounts when you do not want them to go to the regular accounts for the cost type.
[](/en/vista/vista/costs-and-contracts/job-cost/payroll-interface-to-job-cost)Payroll Interface to Job Cost
[](/en/vista/vista/costs-and-contracts/job-cost/payroll-interface-to-general-ledger)Payroll Interface to General Ledger
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/close-a-contract)Close a contract
