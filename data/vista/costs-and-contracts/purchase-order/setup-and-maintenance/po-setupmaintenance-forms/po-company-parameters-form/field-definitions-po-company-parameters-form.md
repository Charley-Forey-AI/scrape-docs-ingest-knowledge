---
title: "Field Definitions: PO Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form/field-definitions-po-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form/field-definitions-po-company-parameters-form"
---

# Field Definitions: PO Company Parameters Form

The following is a list of field descriptions for the PO
 Company Parameters form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## PO Company

Enter a valid company number (as set up in HQ Company Setup). Each PO company you set up here must correspond to an identical AP company (to which PO’s in this company will be posted and paid).

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Automatically Generate PO #'s

Check this box if you want the system to
 automatically generate and assign PO numbers. All PO’s will be assigned the next available
 PO number based on the entry in the Next Auto PO # field.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Next Auto PO#

Enter the number the system should
 automatically assign to the next purchase order that is created. The entry in this field
 must be numeric.
 For example when you create a new PO in the PO Purchase Order Entry form, the system will automatically assign the new PO this number.
This field is only enabled when the Automatically Generate
 PO#'s box is checked. [More ](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form/field-definitions-po-company-parameters-form#ID-0002fba5--en)

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Specify Pay Type During PO Entry

Check this box to allow specifying a pay type
 when entering purchase orders. When checked, a Pay Type input is displayed at the item
 level in PO Purchase Order Entry. If you are using pay categories (flag in AP Company
 Parameters), a Pay Ctgy input will also be displayed.
Note: This option functions separately from the Allow
 Payable Type Overrides option in AP Company Parameters. Therefore, disallowing pay type
 overrides in AP will not affect pay type entry in PO. Only this option will control whether
 pay types can be entered with purchase orders.
Uncheck this box if you do not allow entering pay types during purchase order entry. The
 Pay Type
 field—and the
 Pay Ctgy
 field if using pay categories—will not display on the PO Purchase Order Entry form; pay types will be assigned to purchase order items when invoiced in AP Transaction Entry.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Attach batch reports to HQ Batch Control

Check this box if the batch reports should be attached to the batch record that displays in the [HQ Batch Control](/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form) form.
 The reports are stored using the Attachment Storage Location and Subdirectory Structure parameters defined in DM Attachment Options.

- The system will attempt to export batch reports before posting the batch. If the export is successful, it will then post the batch. However, if errors occur for any batch report, the system will display an error message and abort the posting process. You will need to correct the error before you can revalidate and post the batch.

- Because you can secure audit reports (in VA Report Security), access to attachments generated through this process is restricted to HQ Batch Control. If you have secured the HQ Batch Control form, users will only be able to access batch reports if they have access to HQ Batch Control. Unlike regular attachments, indexes are not created for batch report attachments and you cannot access them using DM Attachment Search.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Auto Close Purchase Orders on Final Invoice

Auto Close Purchase Orders on Final Invoice checkbox on the Info tab of the PO Company Parameters form.
Select this checkbox to auto-close purchase orders when fully invoiced
 (current = invoiced, and remaining committed costs in Job Cost are zero). Exceptions for
 JC cost types that you want to be excluded from auto-closing can be specified on the PO
 Close JC Exceptions tab; exceptions for SM cost types that you want to be excluded from
 auto-closing can be specified on the PO Close SM Exceptions tab.

## Enforce Phase/CT Estimate Limit

Enforce Phase/CT Estimate Limit checkbox on the Info tab of
 the PO Company Parameters form.

Select one of the following options from the drop-down list related to limiting PO entry:
No Limit Enforcement  - No restrictions will be made to PO entry
 when a job phase and cost type would go over budget
Warning Only - Users will only receive warnings for PO entry that
 would cause a job phase and cost type to go over budget
Prevent Post/Interface - Users will be prevented from posting a PO
 when it would push the estimate associated with the phase and cost type over
 budget

## Audit Options

The Audit Options section on the PO Company Parameters, Info tab.

The audit options in this section control tracking of changes to the PO company and to purchase order information. If an audit option is selected, the system creates a new record in the HQ Master Audit (HQMA) database table each time you add, change, or delete data. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
Tip: You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. For more information, see [View the Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log).

The PO audit options are as follows:

- Company Parameters – This option defaults as selected and is disabled. Changes made on the PO Company Parameters form will always create new entries in the HQMA table.

- PO Entry/Change Orders – Select this checkbox to record additions, changes, or deletions made to purchase orders (header and item detail) and PO change orders using the PO Purchase Orders and PO Change Orders forms. However, no audit records will be generated for purchase orders/PO change orders purged via PO Purge.

- PO Compliance – Select this checkbox box to record additions, deletions, and changes made to compliance codes in PO Compliance, as well as compliance codes initialized to a purchase order based on the default compliance group for the job, or added/deleted via AP Vendor Compliance. However, no audit records will be generated for compliance code changes due to purging purchase orders..

- PO Receipts – Select this checkbox box to record additions, deletions, and changes made to receipts in PO Receipts Entry.

## GL Expense Interface Level

Select one of the options below to indicate
 how GL is to be updated when PO expense entries are posted.

- Summary - If this option is selected, Expense PO
 entries will be summarized and one GL/Subledger entry will be posted for each unique
 GL account. Enter the description that will be used for each of these transactions in
 the
 Summary GL
 Description
 field below.

- Detail - If this option is selected, one
 GL/Subledger entry will be created for each Expense PO transactions in a batch. Use
 the "Select Available Items for Detail Level GL Descriptions” box to define the
 detail description that will be used for these entries.

- The interface level selected here will also be used
 when updating Cost and WIP accounts for work completed purchase lines (type
 5-Purchase).

- If the
 In
 Use
 checkbox is selected, you can change the interface level from
 'Summary' to 'Detail or vice-versa; however, changing the interface level to or from
 None must be done using the PO Receipt Expense Initialize form, accessed by selecting

 File
 Initialize Expenses on Receipt
 . When None is selected on the PO Receipt Expense Initialize form, the

 In
 Use
 checkbox is not selected and you cannot toggle between Summary and
 Detail on this form.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Summary GL Description

Used for 'Summary' GL Expense Interface Level.
Enter the description to use when summarized Expense PO entries are interfaced to GL. Up to 60 characters allowed.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Detail Level GL Description

Using the selection box to the right, indicate
 the fields you want included as part of the GL transaction description each time a detailed
 expense PO entry is interfaced to GL. Available fields are:

- Vendor#

- SortName

- Receiver#

- ReceiptDate

- PO#

- POItem

- Trans#

Items will be added to the description in the
 order they are selected. To remove an item from the description, unselect the item. When
 the GL entry is made, the system pulls the data from each of the fields and creates the
 description from the information.
Note: If the Interface Detail box is checked for the
 GL account (in GL Chart of Accounts), this description will be used when receiving PO's
 with an Expense line type only—all other line types will use the GL description specified
 in AP Company Parameters. However, if the Interface Detail box is not checked, this
 description will be used for all PO line types.
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Accrual Account

Specify the accrual account to be updated when Job, Equipment, Inventory, and Expense PO transactions are interfaced to GL. This account will also be updated when receiving materials (via PO Receipts Entry) that were purchased for an SM work order.
Note: The GL account specified here must be set up GL Chart of Accounts with a subledger type of “P” or null.
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Automatically Generate RQ #

Check this box if you want the system to
 automatically generate requisition numbers. When entering requisitions in PO Requisition
 Entry, the system assigns all requisitions a sequential number based on the
 Last Used RQ
 #
 field.

- The [PO Requisition Initialization ](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form) form assigns
 requisition numbers based on the highest number in the system, even if this box is
 not checked. The only exception is when you initialize lines to an existing
 requisition, in which case the system bases the number on the
 Last Used
 RQ #
 field.

- If you enter requisitions in PM Material Detail and
 have checked this box, the PM initialization process will assign requisition numbers
 using the
 Last Used
 RQ #
 field. If this box is not checked, requisition numbers are initialized
 using the highest requisition number plus one (alpha/alphanumeric numbers are
 ignored).

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Last Used RQ #

The system enables this field when you check
 the
 Automatically
 Generate RQ#
 box.
Enter a starting requisition number, up to 10 digits. When entering requisitions (PO Requisition Entry), the system will assign requisition numbers sequentially based on this number. After the initial setup, you should not need to edit this field, as it updates automatically each time the system generates a requisition number. Manually assigned requisition numbers do not update this field.
Note: If you enter requisitions via the PM module (PM
 Material Detail), the PM initialization process will assign requisition numbers using the

 Last Used RQ
 #
 field. If you have not checked this box, requisition numbers are initialized
 using the highest requisition number plus one (alpha/alphanumeric numbers are
 ignored).
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Approval Required on RQ for Quote

Check this box if you require approval of requisition lines before they can be initialized to a quote or purchase order. You must assign at least one reviewer to each requisition line, and all assigned reviewers must approve the requisition line before you can initialize it onto a quote or purchase order (if bypassing the quote process). You can specify a default reviewer in the Quote Reviewer field.
Uncheck this box if you do not require requisition approval before initialization onto a quote or purchase order (if bypassing the quote process). Requisitions routed to a quote will automatically be set to a status of '1-Approved for Quote'. Requisitions routed directly to purchase will be set to a status of '4-Approved for Purchase'.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Quote Reviewer

The system enables this field when you check the Approval Required on RQ for Quote box.
Enter the default reviewer for requisition
 lines, or leave blank to assign reviewers to requisition lines manually. Press
 F4
 to see a list of valid reviewers. Press
 F5
 to connect to HQ Reviewers.
The system assigns this reviewer to each
 requisition line added manually or via initialization. If the requisition line is routed to
 a quote, this reviewer must approve the requisition line before it can be initialized to a
 quote. If the requisition line is routed directly to purchase (bypassing the quote
 process), this reviewer must approve the requisition line before it can be initialized to a
 purchase order.
Note: Default reviewers can also be set up at the job, IN
 location, and/or EM department levels; however, reviewers assigned at these levels will
 only default for job, inventory, or equipment-related requisition lines, respectively.
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Approval Required on RQ for Purchase

Check this box if you require approval of quote lines or requisition lines (that have bypassed the quote process) before initializing them to a purchase order. You must assign at least one reviewer to each quote line (or requisition line if bypassing the quote process), and all assigned reviewers must approve the quote or requisition line before it can be initialized onto a purchase order. You can specify a default reviewer in the Purchase Reviewer field.
Uncheck this box if you do not require quote lines (or requisition lines if bypassing the quote process) to be approved before they are initialized to a purchase order. Quote lines will automatically be set to a status of 'Ready for Purchase', and requisition lines routed directly to purchase will be set to a status of '4-Approved for Purchase'. Both can be initialized to purchase orders.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Purchase Reviewer

The system enables this field when you check the Approval Required on RQ for Purchase box.
Enter a default reviewer for quote lines, or
 leave blank to assign reviewers to quote lines manually. Press
 F4
 to see a list of active reviewers (from HQ Reviewers). Press
 F5
 to access HQ Reviewers.
The system assigns the specified reviewer to
 each requisition line initialized to a quote or routed directly to purchase (bypassing the
 quote process). Reviewer must approve the quote or requisition line before you initialize
 it to a purchase order.
Note: Default reviewers set up at the job, IN location,
 and/or EM department levels will automatically be assigned to requisition lines routed
 directly to purchase; however, reviewers assigned at these levels will only default for
 job, inventory, or equipment-related requisition lines, respectively.
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

##  Threshold Amount

 Enter the threshold amount for purchases (must be a positive dollar amount). Purchase totals (on quote lines or requisition lines routed directly to purchase) that exceed this amount will require approval and will automatically be assigned the to the reviewer specified in the Threshold Reviewer field. The reviewer must approve the quote line or requisition line before initialization to a purchase order.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Threshold Reviewer

The system enables this field when you enter an amount in the Threshold Amount field.
Enter a reviewer to assign to all quote or
 requisition lines (if bypassing quote process) with purchase totals exceeding the threshold
 amount specified in the Threshold Amount field. Press
 F4
 for a list of valid reviewers (from HQ Reviewers). Press
 F5
 to access HQ Reviewers. Reviewer must approve quote or requisition lines
 before initialization to a purchase order.
Note: The system assigns this reviewer in addition to any
 quote or purchase reviewers (assigned in the Quote Reviewer and Purchase Reviewer fields,
 respectively).
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Audit Options

The Audit Options section on the PO Company Parameters form, Requisition Info tab.

The audit options in this section control tracking of changes to requisition information. If an audit option is selected, the system creates a new record in the HQ Master Audit (HQMA) database table each time you add, change, or delete requisition data.
Tip: You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. For more information, see [View the Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log).

 The requisition audit options are as follows:

- Requisitions – Select this checkbox to record additions, changes, or deletions made to header and detail levels in PO Requisition Entry.

- Review – Select this checkbox to record additions, changes, or deletions made to quote or requisition lines in PO Requisition Reviewer.

- Quote – Select this checkbox to record additions, changes, or deletions made to header and detail levels in PO Quote Edit.

## JC Co

JC Co column on the PO Close JC Exceptions tab of the PO Company Parameters form.
Enter a job company for the JC cost type that you want to be excluded from auto-closing purchase orders on final invoice. Press F4 for the JC Companies Lookup for a list of job companies from which to choose.

## JC Cost Type

JC Co st Type column on the PO Close JC Exceptions tab of the PO Company Parameters form.
Enter a JC cost type that you want to exclude from auto-closing purchase orders on final invoice. Press F4 for Cost Type Lookup from which to choose a cost type.

## SM Co

SM Co column on the PO Close SM Exceptions tab of the PO Company Parameters form.
Enter an SM company for the SM cost type that you want to be excluded from auto-closing purchase orders on final invoice. Press F4 for the SM Company Lookup for a list of companies from which to choose.

## SM Cost Type

SM Cost Type column on the PO Close SM Exceptions tab of the PO Company Parameters form.
Enter an SM cost type that you want to exclude from auto-closing purchase orders on final invoice. Press F4 for the SM Cost Types Lookup for a list of cost types from which to choose.
