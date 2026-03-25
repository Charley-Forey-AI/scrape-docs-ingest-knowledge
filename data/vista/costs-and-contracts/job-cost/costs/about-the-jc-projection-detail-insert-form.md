---
title: "About the JC Projection Detail Insert Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-detail-insert-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-detail-insert-form"
---

# About the JC Projection Detail Insert Form

Use this form to pull projection detail records back into a cost projections batch.
Access this form by selecting File > Projection Detail Insert in JC Cost Projections.
Note: In order to use this feature, you must be using the projection detail feature (Activate Projection Detail Feature box checked in JC Company Parameters), projection detail must exist for the selected job, and the current Cost Projections batch month must equal the original Cost Projections batch month.
 You can specify to insert detail records based on transaction or budget code. If selecting by transaction, you will need to add each projection detail line individually, as they will each have their own transaction number. If selecting by budget code, you can specify a single code or range of codes, and the system will pull in all projection detail lines for the job that are assigned a budget code within the specified range.
 If you wish to delete projection detail records, check the Mark Transactions for Delete box. This will set the Action field for all detail lines pulled into the batch to ‘D-Delete’. You can manually change this setting by detail line on the Projection Detail grid (in JC Cost Projections).
Note: Deleting detail records in this manner will delete the transactions from the JC Projection Detail Transaction table (JCPR), making them unavailable for any future projection batch. To delete a transaction from the Projection Detail grid, but not from the JCPR table, highlight the detail line in the Projection Detail grid and then press the Delete key or click the Delete button (red X) in the toolbar.  
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections
