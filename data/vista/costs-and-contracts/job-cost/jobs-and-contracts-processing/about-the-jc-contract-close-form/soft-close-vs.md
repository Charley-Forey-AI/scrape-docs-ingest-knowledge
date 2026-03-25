---
title: "Soft Close vs. Final Close | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/soft-close-vs.-final-close"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/soft-close-vs.-final-close"
---

# Soft Close vs. Final Close

What is the difference between soft close and final
 close?
Soft Close

- The status of the contract is set to Soft Close. The job associated with the
 contract will also change to Soft Close.

- If posting to jobs with a soft close status is allowed (JC Company
 Parameters > Info tab > Allow posting to soft-closed
 jobs box), any costs posted to the contract/job will
 update the "open" GL accounts associated with the department on each
 contract item (JC Contracts > Items tab> Department field). If the Allow
 Posting to soft-closed jobs option is not checked, you
 cannot post to the contract/job.

Final Close

- The status of the contract is set to Final Close. The job associated with
 the contract will also change to Final Close.

- If posting to final closed jobs is allowed (JC Company Parameters > Info
 tab >Allow posting to hard-closed
 jobs box), any costs posted to the contract/job will
 update the "closed" GL accounts associated with the department on each
 contract item (JC Contracts > Items tab > Department field). If the Allow
 Posting to hard-closed jobs option is not checked, you
 cannot post to the contract/job.

- If closing a job including any unprocessed purchase orders or subcontracts
 is allowed (JC Company Parameters > Info tab > Close
 Purchase Orders when Job Hard-Closed and Close
 Subcontracts when Job Hard-Closed), the system will ask
 you to confirm closure of the subcontracts or purchase orders before
 hard-closing the job. Open purchase orders and open subcontracts are
 listed on the JC Contract Close form's Open PO's and Open SL's tabs,
 respectively.

- If the GL Close Interface (JC Company Parameters>GL Close tab) is set
 to summary or detail, all existing detail will be moved from the open
 accounts to the closed accounts.

- If the GL Close Interface (JC Company Parameters>GL Close tab) is
 set to summary or detail, the status can only be changed to Soft Close
 or Open (in JC Contracts) if no cost or revenue detail exists for the
 contract.
