---
title: "Field Definitions: JC Projection Detail Insert Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-detail-insert-form/field-definitions-jc-projection-detail-insert-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-detail-insert-form/field-definitions-jc-projection-detail-insert-form"
---

# Field Definitions: JC Projection Detail Insert Form

The following is a list of field descriptions for the JC
 Projection Detail Insert form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Transaction

 Check this box to restrict the projection detail lines pulled into a batch by transaction number. Use the field to the right to specify the desired transaction.
 Leave this box unchecked if not restricting the detail lines pulling into a batch by transaction number.

##  Transaction

 This field is only enabled if you checked the Transaction box (to the left).
 Enter the transaction number of the projection detail line to add to this batch. Use F4 for a list of valid projection detail transactions for this job.

##  Budget Code

 Check this box to restrict the projection detail lines pulled into a batch by budget code. Use the Begin/End fields (to the right) to specify the desired budget code or range of budget codes.
 Leave this box unchecked if not restricting the detail lines pulling into a batch by budget code.

##  Begin/End

 Enter the beginning and ending budget code by which to restrict the projection detail transactions pulled into this batch. Only detail lines assigned a budget code within this range will be inserted into the batch.

##  Mark Transactions for 'Delete'

 Check this box to mark all projection detail lines pulled into a batch for deletion. The system will set the Action field to ‘D-Delete’ for all detail lines added to the batch. You may override this setting by detail line in the Projection Detail grid in JC Cost Projections.
 Leave this box unchecked if you do not want projection detail records marked for deletion. The system will set the Action field to ‘C-Change’ for all detail lines added to the batch. You may override this setting by detail line in the Projection Detail grid in JC Cost Projections.
