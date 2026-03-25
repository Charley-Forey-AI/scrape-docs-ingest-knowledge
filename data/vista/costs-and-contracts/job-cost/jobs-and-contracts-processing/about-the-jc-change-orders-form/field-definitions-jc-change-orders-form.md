---
title: "Field Definitions: JC Change Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form/field-definitions-jc-change-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form/field-definitions-jc-change-orders-form"
---

# Field Definitions: JC Change Orders Form

The following is a list of field descriptions for the JC
 Change Orders form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Job

 Specify the job for which you are setting up this change order. Once entered, the job’s contract and status are displayed to the right.
Note: If you enter a soft- or hard-closed job and you do not allow posting to closed jobs, you can view existing change orders, but you cannot enter new change orders.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  ACO

 Enter the approved change order number, up to 10 characters.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Description

 Enter a description of this change order, up to 60 characters.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Approved By

 Enter the name or initials of the person who approved this change order. Up to 30 characters allowed.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Approval Date

 Enter the date this change order was approved.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  ACO Seq

 Enter the sequence number that indicates the order in which this change order is to be processed. Defaults the next sequential number for the job.
 The sequence number entered here will determine the amount to be included on the Approved Change Order form in the “Net change by previously authorized change orders was” line. Any change orders with a sequence number less than this one will be included on this line.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Change in Days

 Display only, the total number of days by which this change order will affect the contract’s original completion date. This total is the sum of ‘change in days’ for all change order items.
 If change order was interfaced from PM, this field defaults the “change in days” specified for the approved change order. If changes to this value occur due to changes made at the change order item level, this value and the modified item values will be updated to PM.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  New Completion Date

 Specify the new estimated date of completion. Entry here will
 automatically update the Projected Completion Date in the JC Contracts.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Bill Group

 Enter the bill group for this change order. Although not validated, the bill group can be used to group like items together for billing purposes.
Note: Enter NB if this change order is not to be billed. This allows you to use this program for internal budget changes that do not appear on the billing.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Internal/External

 I = Internal change order. Use this option to identify this change order as one that will only affect the contractor’s internal budget.
 E = External change order. Use this option to identify this change order as one that will affect the owner’s schedule of values.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  ACO Item

 Enter a number for this change order item, up to 10 characters.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Contract Item

 Specify the contract item for this change order item. If you enter a
 contract item that does not already exist for the contract, the contract item description
 displays as ‘Contract Item is not on file!” and the JC Contract Item form is automatically
 displayed. You can then set up the new contract item as necessary (with the exception of
 units, unit price, and amount, which are disabled). Once you exit the JC Contract Item
 form,the contract item’s description and unit of measure default for the change order item.
Note: You can enter edit the units, unit price, and amount
 for the new contract item as necessary via the JC Contract.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Description

 Enter a description of this change order item, up to 60 characters. Defaults the contract item’s description.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Change in Days

 Enter the change in days for this contract item. This will be the number of days by which the contract completion date has been changed by this item.
 If the change order was interfaced from PM, this field defaults the “change in days” specified for the approved change order item. If this value is changed here, it will update the change order item in PM.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

## Month Approved

Enter the month this change order item was approved.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Bill Group

 Enter the bill group for this change order item. Although not validated, the bill group can be used to group like items together for billing purposes.
 Enter NB for non-billable items.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Units

 Enabled only if UM is not ‘LS’.
 Enter the number of units by which this change order item changes the contract’s total units.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Unit Price

 Enabled only if UM is not ‘LS’ and no unit price is defined for the contract item.
 Enter the unit price for this contract item. Unit price will be updated for the contract item in JC Contract Items (JCCI).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Amount

 For items with a ‘LS’ unit of measure, enter the total amount by which this change order item changes the contract’s total dollars.
 For items with a UM other than ‘LS’, amount defaults based on the specified units x unit price. You can override this amount if necessary; however, because units are not recalculated, this may cause the contract amount to not be equal to the units x unit price. In addition, you will receive a message warning you that Job Billing will display only the original unit price.
Note: Amount entered here will update the contract’s Current amount.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Phase

 Enter the phase this change order item affects. The phase description displays to the right of this field.
What happens if you select a phase not on the job
 You may specify a phase not already on the job, even if this job’s phases are locked. Because you are adding estimated costs rather than actual costs, this program works somewhat like the Job Estimates program in that it overrides the normal rules for locked jobs and allows you to add new phases even if the job's phases are locked. The new phases will be cross-referenced to the contract item for the change order item.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Cost Type

 Specify a cost type for this phase. Cost type
 must be set up for the phase in JC Phases or JC Job Phases.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Phase Description

 Enter the phase
 description, up to 30 characters. Initially defaults the description defined for this phase
 in JC Phases or JC Job Phases.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Ins Code

 For existing job phases, this field is disabled and displays the insurance code assigned to the phase in JC Job Phases or blank, if no insurance code assigned in JC Job Phases.
 For new phases, enter the insurance code (from HQ Insurance Codes) that applies to this phase, if applicable. Once record is saved, phase and insurance code will be updated to JC Job Phases (applies to ‘locked phases’ jobs as well).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Month

 Specify the month this change order was added to the contract.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  U/M

 Enter the unit of measure for the phase.
 Defaults the unit of measure defined for the phase in JC Phases or JC Job Phases.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Est Hours

 Enabled only if tracking hours for the specified cost type.
 Specify the estimated number of hours needed to complete this phase on the change order item.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Estimated Units

 Enabled only if unit of measure is not ‘LS’.
 Specify the estimated number of units needed to complete this phase on the change order item.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Unit Cost

 Enabled only if unit of measure is not ‘LS’.
 Specify the unit cost for this phase on this change order item.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders

##  Est Cost

 Specify the estimated cost for this change order item. For non-LS cost types, defaults an amount based on the estimated units x unit cost. This amount will be the estimated cost of this phase on this change order item.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form)JC Change Orders
