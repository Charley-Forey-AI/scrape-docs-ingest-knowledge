---
title: "Which contracts can be closed? | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/which-contracts-can-be-closed"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/which-contracts-can-be-closed"
---

# Which contracts can be closed?

This topic provides an overview of how the system determines whether a contract is eligible to be closed.
A contract and its associated job(s) are closed together. To be eligible for closing, there can be no
 costs or revenues posted to future periods that do not net to 0 (zero) by period for
 this contract/job, and there can be no transactions currently in any batch posting files
 that are for this contract/job.
Note: The system will allow a contract with future
 postings to be soft-closed if you allow posting to soft-closed jobs (flag in
 JC Company Parameters). However, if you do not allow posting to soft-closed jobs or
 you are performing a hard close, the system will not allow the close and will throw an
 error during batch validation.
You can close a contract when unreleased
 retainage exists for the contract. Once the contract is closed, you will be able to
 release the retainage, as well as apply cash receipts to the released retainage
 transactions.
Once you specify a contract to close, the informational display below shows ‘last month activity’ for cost and revenue so that you can see at a glance whether future postings exist.
If there are future postings, the months are shown in red and a message displays (at the top of the screen) indicating that cost or revenue postings exist in future months and that you will be unable to close. The last month activity information will indicate where the future postings exist. For example, for each type of job cost (e.g. Actual, Original Estimate, Projected, Total Cmtd, etc.) it will show the last month activity for hours, units, and dollars. If the batch month is 06/07 and you have Total Cmtd units activity in 04/07, and Total Cmtd dollars activity in 07/07, the Units activity will show in black, but the Dollars activity will show in red and you will be unable to close the contract.

## Close Criteria: What the System Checks For

When a batch is validated, the system runs a series of checks to ensure the specified contracts are eligible for close. During this process, the system checks to see if:

- the jobs exist in any open batches;

- if jobs exist in any worksheets in SL Worksheet;

- there are any JB billings for contracts that have not been interfaced;

- payroll has been charged to any jobs that have not been interfaced;

- there are any unapproved invoices;

- assigned material detail and/or subcontract detail records exist:

- for original estimates that have not been interfaced;

- for approved change orders that have not been interfaced;

- that are attached to pending change orders with a status other than ‘final’ that have not been approved or interfaced.

- future postings exist for the contracts/jobs

Note: If future postings exist for the contract, the month will be highlighted in red where applicable (i.e., the Last Revenue, Last Cost, Last Month Activity for Cost, and/or Last Month Activity for Revenue sections). If you are performing a soft-close and you allow posting to soft-closed jobs (flag in JC Company Parameters), the system will allow the close. If you do not allow posting to soft-closed jobs or, if you are performing a hard-close, the system will not allow the close and will throw an error during batch validation. You will need to remove the contract from the batch before you can process the batch.
If you do not allow posting to closed jobs (i.e.,
 the Allow
 Posting to Soft-Closed Jobs and/or Allow Posting to
 Hard-Closed Jobs boxes are unchecked in JC Company Parameters), the
 system will also check:

- all purchase orders to make sure there are no remaining committed units or
 dollars, and if receiving, that invoiced units and dollars equal the received
 unit and dollars;

- all subcontracts to make sure that there are no remaining units or dollars
 that have yet to be invoiced,

- all billings in JB Bill Header (JBIN) to make sure contract does not exist
 on a billing with a status of A-Active, C-Changed, or D-Delete;

- all JB interface batches (JBAR) to make sure contract does not exist on a
 billing to be interfaced;

- all ticket batches (MSTB) to make sure contract/job does not exist on a
 ticket;

- all AR invoices batches (ARBH, ARBI, and ARBL) to make sure contract does
 not exist on an invoice.

Once you post the batch, you can print the JC
 Contract Close Audit List report for a list of all the contracts/jobs being closed.
 If errors exist, the Error list will show you what you need to correct. You must
 close out open batches, fill in missing information, and correct any errors before
 you can complete a soft or final close. Contracts with activity posted in a month
 later than the close month must be removed from the batch before it can be
 processed.
If you are updating GL (the GL Close Interface
 option set to Summary or Detail in JC Company Parameters), and this is a final
 close, the accounts affected are shown on the report. When you post the batch, the
 program makes the GL entries and flags the contract as closed.
If you are not updating GL, or if you are doing a soft close, then the update simply changes the status flag on the contracts.
