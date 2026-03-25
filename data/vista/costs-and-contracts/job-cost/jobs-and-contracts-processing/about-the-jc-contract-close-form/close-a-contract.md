---
title: "Close a Contract | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/close-a-contract"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/close-a-contract"
---

# Close a Contract

Use the JC Contract Close form to perform a soft close or a final close on contracts that have been completed.
Closing a contract will also close all of the related jobs. To be eligible for closing, there can be no costs or revenues posted to future periods that do not net to 0 (zero) by period for this contract/job, and there can be no transactions currently in any batch posting files that are for this contract/job.
The system will allow a contract with future postings to be soft-closed if you allow posting to soft-closed jobs (flag in JC Company Parameters). However, if you do not allow posting to soft-closed jobs or you are performing a hard close, the system will not allow the close and will throw an error during batch validation.
For more detailed information about contracts that are eligible for closing, see [Which contracts can be closed?](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/which-contracts-can-be-closed).

1. Verify that there are no open purchase orders and subcontracts on the contract(s) that you want to close. You cannot close a contract if there are remaining committed costs from purchase orders and subcontracts, so process these before closing the contract. If you allow closing jobs that include unprocessed purchase orders or subcontracts (that is, the Close Purchase Orders when Job Hard-Closed and Close Subcontracts when Job Hard-Closed checkboxes are selected in JC Company Parameters), the system asks you to confirm closure of the subcontracts or purchase orders before hard-closing the job. Open purchase orders and open subcontracts are listed on the JC Contract Close form's Open PO's and Open SL's tabs, respectively.

1. Decide if you want to soft close or final close the contract(s). For more information, see [Soft Close vs. Final Close](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/soft-close-vs.-final-close).

1. Open or create a JC Contract Close batch. Select [About the Batch Selection Form](/en/vista/vista/system-tools/user-interface-guide/system-forms/batch-processing/about-the-batch-selection-form) for information on the Batch Selection form.

1. [Add contracts to the batch](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/add-multiple-contracts-to-a-contract-close-batch).

1. Review the information in the Last Month Activity for Cost and Last Month Activity for Revenue sections.

1. Select File > Process Batch.

1. Use the JC Batch Process form to process the batch. You can also print the JC Contract Close Audit List to get a concise record of the contracts and jobs that you have closed in a given month. Select [About the JC Batch Process / PM Batch Process Forms](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-batch-process--pm-batch-process-forms) for general information about the JC Batch Process form.

The selected contracts are closed. You can see the status of a contract using the Contract Status field on the JC Contracts form. You can change the status of a contract using this field based on the following:

- If the "GL Close Interface" level (in JC Company Parameters) is set to 'No Update', status can be changed from Closed to Soft Close or Open.

- If the "GL Close Interface" level is set to 'Summary' or 'Detail', and there is existing cost detail or revenue detail for the contract, you cannot change the status from Closed to anything less. If no cost or revenue detail exists, changing the status from Closed to Soft Close or Open is allowed.

The JC Contracts form also shows the month closed. This field can be used to store the month you anticipate closing the contract, while it is still open. Once closed, you cannot change the month.
For additional information about closing contracts, see [About the JC Contract Close Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form).
