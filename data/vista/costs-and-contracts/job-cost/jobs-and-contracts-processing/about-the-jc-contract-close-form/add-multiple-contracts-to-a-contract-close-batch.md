---
title: "Add Multiple Contracts to a Contract Close Batch | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/add-multiple-contracts-to-a-contract-close-batch"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/add-multiple-contracts-to-a-contract-close-batch"
---

# Add Multiple Contracts to a Contract Close Batch

You can add multiple contracts to a contract close batch using
 the JC Contract Initialize form.
The following steps will guide you through adding
 multiple contracts to a contract close batch using the JC Contract Initialize form.

1.  From the [JC
 Contract Close ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form) form, select File >
 Initialize Contracts. The JC Contract Close Initialize form will display.

1.  Select an option in the Initialize By section.

- Contract Range – Use
 this option to initialize a range of contracts. The initialization
 process will pull all contracts within the specified range having a
 status of 1 (Open) or 2 (Soft Close) and add them to the close batch.

- As of Close Month –
 Use this option to select contracts based on the close month (JC
 Contracts Info tabMonth Closed field).
 All contracts with a close month that is equal or less than the selected
 close month will be added to the batch. Only contracts with an open or
 soft close status, and a contract start month (JC Contracts Info
 tabContract Start Month
 field) is equal to or less than the batch month. Note: If performing a Hard Close, initialization
 will include contracts with a 'soft close' status. Contracts with a
 'hard close' status will be skipped, regardless of whether
 performing a soft or hard close.

1. Use the Close Date field to enter the
 actual close date of the selected contracts.

1. Date field shortcuts
T or
 tSet the date to the current
 date.
MMDDFour digit month and day
Enter a four digit month and date
 (MMDD) and the system will automatically add the current
 year.
+The system will automatically set the
 date to tomorrow.
+5The system will automatically set the
 date to 5 days in the future. You can enter any value after the +,
 for example you can enter +7 to
 set the date to next week.

-The system will automatically set the
 date to the previous day.
-5The system will automatically set the
 date to 5 days in the past.Just like with +, you can enter any
 value after the -, for example you can enter -7 to
 set the date to the previous week.

1.  Select the Status that will be assigned
 to the selected contracts.
 Soft Close

- The status for selected contract is set to Soft
 Close.

- If you allow posting to closed jobs (i.e. Allow
 Posting to Closed Jobs option is checked in JC Company Parameters), any
 costs posted to the contract/job will update the open accounts specified
 in the Department file. If the Allow Posting to Closed Jobs option is
 unchecked, no posting to the contract/job is allowed.

- The status may be changed (in JC Contracts) to Open
 only. If you need to Final Close the contract, it must be done using
 this program.
 Final Close

- The status for selected contract(s) is set to Final
 Close.

- If you allow posting to closed jobs, costs posted to
 the contract/job will update the closed accounts specified in the
 Department file. If you do not allow posting to closed jobs, posting to
 the contract/job cannot occur.

- If the GL Close Interface (JC Company Parameters) is
 set to Summary or Detail, all existing detail will be moved from the
 open accounts to the closed accounts.

- If you allow closing a job including any purchase
 orders or subcontracts that have not been interfaced (JC Company
 Parameters > Info tab > Close Purchase Orders when Job
 Hard-Closed and Close Subcontracts when Job
 Hard-Closed checkboxes), the system will ask you to
 confirm closure of the subcontracts or purchase orders before
 hard-closing the job. Open purchase orders and open subcontracts are
 listed on the JC Contract Close form's Open PO's and Open SL's tabs,
 respectively.

- If the GL Close Interface (JC Company Parameters) is
 set to Summary or Detail, the status can only be changed to Soft Close
 or Open (in JC Contracts) if no cost or revenue detail exists for the
 contract.

1.  Click the Initialize button when
 complete. Contracts that meet the selected criteria are added to the JC Contract
 Close form. You can also remove any contracts that were accidentally included.

1.  Click [here](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form) for information about processing the JC Contract Close batch.

 [](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form)JC Contract Close
