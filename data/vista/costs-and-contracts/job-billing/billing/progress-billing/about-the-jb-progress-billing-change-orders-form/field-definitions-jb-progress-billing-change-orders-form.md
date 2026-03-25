---
title: "Field Definitions: JB Progress Billing Change Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-progress-billing-change-orders-form/field-definitions-jb-progress-billing-change-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-progress-billing-change-orders-form/field-definitions-jb-progress-billing-change-orders-form"
---

# Field Definitions: JB Progress Billing Change Orders Form

The following is a list of field descriptions for the JB
 Progress Billing Change Orders form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Job

 If change orders were included during initialization of this billing, this field defaults to the first job for which a change order exists on this billing.
 If adding a change order, specify the job that the change order applies to.

##  ACO

ACO field in the header grid of the JB Prog Bill Chg Order Items form.
 Specify the approved change order to review/edit. This field initially defaults to the first approved change order existing for this job on this
billing.
 If adding a change order, specify the approved change order (JC Change Orders).
Note: New change orders cannot be entered here; only approved change orders already existing for this job (in JC Change Orders) can be added. Additionally, only approved change orders posted to contract items that are part of this billing can be added.

##  ACO Item

 Specify the approved change order item to review/edit.
 If adding a change order, specify a valid approved change order item. The change order item must be posted to a contract item that exists on this billing before it can be added here.

##  Change Units

 This field displays the number that the change order updates the contract units with. Defaults to the change units entered for the change order item in JC Change Orders. This value may be overridden; however, be aware that changes to the change order units will not recalculate the Change Amount, nor will the Unit Price (display only) be recalculated.

##  Change Amounts

 This field displays the total amount this item changes the contract dollars by. Defaults the change amount entered for the change order item in JC Change Orders. This value may be overridden; however, be aware that changes to the change order amount will not recalculate the Change Units, nor will the Unit Price (display only) be recalculated.
