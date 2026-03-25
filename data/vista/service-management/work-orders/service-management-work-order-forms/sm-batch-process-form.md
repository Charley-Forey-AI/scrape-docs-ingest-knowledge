---
title: "SM Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-batch-process-form"
---

# SM Batch Process Form

Use the SM Batch Process form to post work completed batches.
You can access this form by clicking Post in the SM Batches form or from the Programs menu of Service Management.
Work completed batches are posted automatically (if using auto-batching) or manually in SM Work Order Cost Posting (if not using auto-batching). Therefore, you will only need to use this form for batches that are in an "unposted" status due to validation errors or interruptions during the validation or posting process (for example, batch processing was interrupted by power failure and batch is stuck at a status of 4-Processing).
Note: The Auto Post New Work Completed checkbox in SM Company Parameters controls whether work completed lines are automatically created and posted when entering work completed (in SM Work Orders) or processed manually in SM Work Order Cost Posting. For more information about this option, see [Auto Post New Work Completed](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form#ID-00042832--en).

## Batch Sources

If you access this form via SM Batches, the Batch# field automatically defaults from the batch you selected in SM Batches. However, if you access this form from the Service Management Programs menu and are using the F4 lookup to select your batch, the batch source will help identify where each batch came from.
 It is important to note that the list will include other batches that are not for work completed lines (such as invoice and agreement amortization). The following is a list of batch sources that you may encounter, along with the type of transaction to which each is associated:
Batch SourceType of Transaction

SMEquipUseWork Completed Equipment
SM InvWork Completed Inventory
PO ReceiptsWork Completed Purchase
SMLedgerUpWork Completed Misc
SM InvoiceWork Order & Agreement Invoices
SMAmortizeAgreement Revenue Amortization
SMGLChangeChanges to call types on a work order that require new GL account updates
SM WIPWIP transfers that occur when closing a work order scope

## Audit Reports

Once you click Validate, the form runs through all the data in the batch and creates Audit Reports that you can preview and/or print before posting the batch.
It is recommended that you print the audit reports before posting the batch, as reports are no longer available once you post the batch. For a list of audit reports and their descriptions, see [Audit Reports](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-batch-process-form/audit-reports).

## Clearing a Batch

When you create a batch, the system adds the data to a batch table and stores it until you are ready to post the batch. Data is not updated online; therefore, you can delete it completely without affecting any modules, including the module in which you created the batch. To clear a batch table of stored data, select File > Clear Batch. The system will clear/delete all data from the batch.

- The system creates an audit record each time you clear a batch. For information about cleared batches (i.e. user who cleared batch, as well as the date and time the batch was cleared), use the VA 'Other Events' Statistics report.

- The Clear Batch option is disabled if the batch’s status is 4 (Posting in Progress). This is to prevent partially updated batches from being deleted should the update process be interrupted (i.e. power outage, system failure, etc.). When a batch update is interrupted, only a portion of the intended updates may occur. If a user later clears the batch, there is no way to determine the updated data

Related tasks

- [Post a Batch Using SM Batch Process](/en/vista/vista/service-management/work-orders/about-posting-work-completed-batches/post-a-batch-using-sm-batch-process)

Related information

- [SM Batches Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-batches-form)
