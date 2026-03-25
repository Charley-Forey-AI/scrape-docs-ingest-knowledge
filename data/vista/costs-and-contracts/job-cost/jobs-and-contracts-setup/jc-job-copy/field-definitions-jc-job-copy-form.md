---
title: "Field Definitions: JC Job Copy Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-copy/field-definitions-jc-job-copy-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-copy/field-definitions-jc-job-copy-form"
---

# Field Definitions: JC Job Copy Form

The following is a list of field descriptions for the JC Job
 Copy form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Contract Items

The Change Orders checkbox on the JC Job Copy form.
This box is only enabled if the phase group for the destination company
 matches that of the source company.
Select this checkbox to copy the contract items from
 the source contract to the destination contract. Copy will include standard item codes (if
 applicable), description, UM, markup, and bill group/description. The system assigns a department, tax code,
 retainage, and start month as specified in the copy parameters. You may modify contract
 items as necessary via JC Contracts.
Do not select this checkbox if you are not copying
 contract items from the source contract. Instead, the system creates a single contract item #1 for the new contract. You may modify the contract item and add new contract items as necessary in JC
 Contracts.

## Item Departments

The Item Departments checkbox on the JC Job Copy form.
Enabled only if the phase group for the destination company matches that of the source company and you have selected to copy Contract Items.
Select this checkbox to copy the departments from the source contract items to the new contract items. When selected, the system displays a warning (in red) to the right indicating that you are copying source departments.
Do not select this checkbox if you are not copying item departments from the source contract. The system automatically assigns the department specified for the destination contract above to all items added for the new contract.

## Job Roles

The Job Roles checkbox on the JC Job Copy form.
Select this checkbox to copy role assignments from the source job to the destination job.
Do not select this checkbox if you are not copying role assignments from the source job to the destination job.
Note: Selecting this checkbox enables the Job Phase Roles
 checkbox, allowing you to copy roles at the job phase level.

## Phases/Cost Types

The Phases/Cost Types checkbox on the JC Job Copy form.
Enabled only if the phase group for the destination company matches that of the source company.
Select this check box to copy phases and cost types from the source job to the new job. You may modify copied phases and cost types as necessary.
Do not select this checkbox if you are not copying phases and cost types from the source job. You will need to set up phases and cost types manually for the new job via JC Job Phases or JC Original Estimates.

## JB Bill Groups

The JB Bill Groups checkbox on the JC Job Copy form.
Select this checkbox to copy bill groups defined for the source contract (in JB Bill Groups) to the new contract.
Do not select this checkbox if you are not copying bill groups from the source contract. No record will be set up in JB Bill Groups for the new contract.

## Job Phase Roles

The Job Phase Roles checkbox on the JC Job Copy form.
This checkbox is enabled only when the
 Job
 Roles box is checked.
Select this checkbox to copy job phase role assignments from the source job to the destination job.
Do not select this checkbox if you are not copying job phase role assignments to the new job.

## Orig Estimates/Contract Amt

The Orig Estimates/Contract Amt checkbox on the JC Job Copy form.
Enabled only if the phase group for the destination company matches that of
 the source company.
Select this checkbox to copy original estimates and contract amount from the source job to the new job. The system only copies estimates and contract amounts if you also elected to copy phases and cost types. You may modify copied estimates and contract amounts as necessary.
Leave this box unselected if you are not copying the contract amount and original estimates from the source job. You will need to
 manually set up the contract amount via JC Contracts and original estimates via JC Original
 Estimates.

## Item Retainage

 The Item Retainage checkbox on the JC Job Copy form.
This checkbox is only enabled when the Contract Items box is checked.
Select this checkbox to copy item retainage from the source contract items to the destination contract items.
Do not select this checkbox if not copying item retainage from the source contract items to the destination contract items. The destination contract items will default the retainage percent specified for the destination contract (above).

## Change Orders

The Change Orders checkbox on the JC Job Copy form.
This box is only enabled only if the phase group for the destination company matches that of the source company and you have selected to copy Contract Items.
Select this checkbox to copy change orders from the source job to the new job. The system will only copy change orders if you are also copying phases and cost types. You may modify change orders as necessary in JC Change Orders.
Leave this checkbox unselected if not copying change orders from the source job. You may set up change orders manually in JC Change Orders.

## Job Reviewers

The Job Reviewers checkbox on the JC Job Copy form.
Select this checkbox to copy the reviewer setup from the source job to the destination job.
Do not select this check box if you are not copying
 the reviewer setup from the source job to the destination job. You will need to set up Reviewers manually for the new job in JC Jobs (Reviewers tab).
