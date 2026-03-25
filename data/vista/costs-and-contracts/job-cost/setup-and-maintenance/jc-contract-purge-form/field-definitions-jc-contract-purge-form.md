---
title: "Field Definitions: JC Contract Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-contract-purge-form/field-definitions-jc-contract-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-contract-purge-form/field-definitions-jc-contract-purge-form"
---

# Field Definitions: JC Contract Purge Form

The following is a list of field descriptions for the JC
 Contract Purge form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Purge Option

The Purge Option field on the JC Contract Purge form, Purge Contract tab.
 Specify which method to use for purging contracts.

- Purge By Month - Select this option to purge contracts by month. Only contracts where the Month Closed (in JC Contracts) is equal to or less than the Month specified below and the status is ‘3’ (Hard Closed) will be purged.

- Purge By Contract - Select this option to purge a specific contract (indicated below). Only contracts with a status of ‘3’ (Hard Close) will be purged.

For more information about purging contracts and contract history, see [JC Contract Purge Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-contract-purge-form).

##  Purge Contract: Contract

The Contract field in the JC Contract Purge field, Purge Contract tab.
Enabled only when purging by contract.
Enter the contract to purge. If the contract is eligible for purging (that is, has a Hard Closed status), it is added to the contracts grid in the lower part of the form. If the contract is not eligible for purging (that is, it has an Open or Soft Closed status), a message is displayed indicating the contract has not been closed and cannot be purged. It will not be added to the contracts grid. You will need to close the contract before you can purge it.
For more information about purging contracts or contract history, see [JC Contract Purge Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-contract-purge-form).

##  Month

The Month field on the JC Contract Purge form, Purge Contract tab.
This field is only enabled when purging by month.
 Specify the month (must be equal to or less than last month closed in subledgers) to which the Month Closed defined for each contract (in JC Contracts) will be compared when determining contracts eligible for purging. If a contract's Month Closed is equal to or less than this month and the contract has a Hard Closed status, it is added to the contracts grid below. You can leave the Purge checkbox unselected for any contracts in the grid that you do not want purged.
For more information about purging contracts, see [JC Contract Purge Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-contract-purge-form).

##  Update Summary History Tables

The Update Summary History Tables checkbox on the JC Contract Purge form, Purge Contracts tab.
 Select this checkbox to update the summary history tables when this contract/job is purged. All units (Actual, Original, Current, and Projected) for phases/cost types on the job with the Item Unit Flag selected in JCCH and a unit of measure matching that of the related contract item will be rolled into JCHC (JC History by Contract). If you have selected cost types in the Update Contract History Hours for Cost Types selection box, the Actual, Original, Current, and Projected hours for each selected cost type will also be rolled up into JCHC (JC History by Contract).
Note: If you select this option and history already exists in the JCHC (JC History by Contract) and JCHJ (JC History by Job) tables for the contract/job, you will receive a message informing you that the job has already been purged and asking if you want to replace the existing data. Select Yes to delete the existing contract/job history and replace it with the history of the contract/job currently being purged. Select No to leave the existing history intact. The specified contract/job will not be purged.
Leave this checkbox unselected if you do not want to update the summary history tables when this contract/job is purged.
For more information about purging contracts and contract history, see[JC Contract Purge Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-contract-purge-form).

##  Update Contract History Hours for Cost Types

The Update Contract History Hours for Cost Types selection box on the JC Contract Purge form, Purge Contracts tab.
Enabled only if the Update Summary History Tables checkbox is selected.
Select all cost types for which you want the Actual, Original, Current, and Projected hours rolled up into JCHC (JC History by Contract).
For more information about purging contracts and contract history, see[JC Contract Purge Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-contract-purge-form).

##  Purge Contract History: Contract

Contract field in the JC Contract Purge field, Purge Contract History tab.
Enter the contract to purge from the summary history tables.
When you purge a contract/job using the Purge Contract tab, the system writes contract/job information in the JCHC (JC History by Contract) and JCHJ (JC History by Job) tables. If you want to reuse the contract and job numbers, you must purge these system-created records.
For more information about purging contracts or contract history, see [JC Contract Purge Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-contract-purge-form).
