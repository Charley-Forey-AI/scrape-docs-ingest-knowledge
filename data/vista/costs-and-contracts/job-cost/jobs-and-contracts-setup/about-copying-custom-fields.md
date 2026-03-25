---
title: "About Copying Custom Fields | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-copying-custom-fields"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-copying-custom-fields"
---

# About Copying Custom Fields

If there are custom/user-defined fields on the job being
 copied, this information will be copied to the new job depending on the components you have
 selected to copy.
For example if custom fields exist at the
 Contract Item level, they will only be copied if you elected to copy Contract Items. The
 following is a list of tables from which custom fields will be copied (if they exist).

- JCCM (Contract Master)

- JCCH (Cost Header)

- JCCI (Contract Items)

- JCOH (Change Order Header)

- JCJM (Job Master)

- JCOI (Change Order Items)

- JCJP (Job Phases)

Once you have entered all the required criteria
 and clicked the Copy button, the information set up for the existing job in JCJM (JC
 Jobs) is copied to the new job. The new contract is set up in JCCM (JC Contracts) for
 the destination company, along with the contract items, if specified.

- If you selected to copy contract
 items and standard item codes exist for the source contract items, they will be
 copied to the new contract items, and the standard region copied to the contract
 header. This only applies if the phase groups match between the source and
 destination companies.

- If you do not elect to copy contract
 items, or the option is not available due to differing phase groups, the new
 contract will be set up with a single contract item #1.

- If copying phases, the phases
 assigned to the existing job will be copied to JCJP (JC Job Phases) for the new
 job, along with the cost types, if specified.

- If phases are locked for the source job (i.e.
 ‘Phases on This Job Are Locked’ option is checked in JC Jobs), they will also be
 locked for the destination job.

- If you do not select to copy item
 retainage, the new contract items will default the retainage percent defined for
 the contract during the copy process.

When the copy process is complete, a message
 displays telling you the job was successfully copied. If an error occurred during the
 copy process, a message displays with information about the error. A second message is
 then displayed informing you that the copy was not complete.
