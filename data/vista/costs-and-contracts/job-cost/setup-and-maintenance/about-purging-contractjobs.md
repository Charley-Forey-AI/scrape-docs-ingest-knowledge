---
title: "About Purging Contract/Jobs | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-purging-contractjobs"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-purging-contractjobs"
---

# About Purging Contract/Jobs

You can purge closed contracts/jobs using the Purge Contract tab in the JC Contract Purge form.
There are two methods by which you can purge contracts/jobs:

- Purge By Month – Use this method to purge contracts based on a specified month. Contracts with a Closed Month (defined in JC Contracts) less than or equal to the specified month are purged.

- Purge By Contract – Use this method to purge a selected contract.

Regardless of which method you use, contracts must have a status of 3-Hard Closed in order to be purged.
The Update Summary History Tables checkbox allows you to update the summary history tables when the contract/job is purged. If you select this option and history exists for the contract/job in the Contract History by Job (JCHJ) and/or Contract History by Contract (JCHC) tables, a prompt displays informing you that the job has already been purged and asking if you want to replace the existing data.

- If you answer No, the existing history remains and the specified contract/job will not be purged.

- If you answer Yes, the existing contract/job history is deleted and replaced by the history of the contract/job being purged.

Actual, Original, Current, and Projected units for all phases/cost types on the job that have the Item Unit Flag checkbox selected in JCCH (JC Cost Header) and have a unit of measure matching that of the related contract item will be rolled into JCHC (JC History by Contract).
Note: Jobs are purged when the Contract to which the job is assigned is purged. If a contract has multiple jobs, there is no way to purge just one job and still leave the contract and its other jobs on record. If, however, a job does not yet have any costs posted to it, you can delete that job in JC Jobs.

Also, if you are using Job Billing (that is, the Use Job Billing checkbox is selected in JC Company Parameters), you cannot purge a contract/job if any open billings exist (those with a status of Active, Changed, or Deleted). All billings for the contract must be flagged as 'Interfaced' before the contract/job can be purged.
The Update Contract History Hours for Cost Types selection box (enabled when you select the Update Summary History Tables checkbox), allows you to designate the cost types for which to roll up hours when purging contracts. When you run the purge process, the Actual, Original, Current, and Projected hours for each selected cost type are rolled up into JCHC (JC History by Contract).
Contracts selected for purging are listed in the grid at the bottom of the screen, along with their associated jobs. The Purge checkbox automatically defaults as unselected for each contract/job, so you can either individually select this checkbox for each contract/job to purge or select the Check All button to select all contracts at once. Once you select the Check All button, it changes to Uncheck All, allowing you to deselect all contracts if needed.
Note: All jobs associated with a contract must be purged with the contract; therefore, if you uncheck the Purge flag for one job, it will automatically uncheck the flag for the contract and all of its associated jobs.

When you are ready to purge, select Purge Contracts to implement the purge process. Once the process is complete, the Message column in the grid will indicate the contract/job has been purged. If a contract/job could not be purged due to errors, the Message column will list the errors so they can be corrected. You will need to correct all errors before you can purge the contract/job.
