---
title: "JB Progress Billing Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-progress-billing-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-progress-billing-form"
---

# JB Progress Billing Form

Use this form to enter or adjust billing amounts on a
 contract.
You can set up billings manually or automatically
 (by initialization). To initialize billings, select File > Initialize
 Billing. When you initialize a progress billing, all items on
 a contract with a Bill Type of 'Progress' or 'Both' are added to the
 billing and display on the Items tab.
When entering a bill manually, much of the
 information on this form defaults once you specify the contract.
 This information includes the customer, billing address, and payment
 terms. As with initialization, only contract items with a Bill Type
 of 'Progress' or 'Both' are added to the billing. All previous
 values for each item are included.
Previous bill values are initialized as the sum of
 the Previous and This Bill
 amounts for the contract's last billing (the billing whose bill month/number
 are prior to the current bill month/number). If there are no previous
 billings for the contract, the previous values default as 0.00.
Note: If you certify billings (that is, you
 have selected the Certify Progress Billing
 Claims checkbox in the JB Company Parameters
 form), additional fields are available for entering the claim date,
 flagging the bill as certified, and entering the certification date.
 For more information, see [Certifying Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-certifying-billings).
Once you have entered
 billing information, item information for the bill displays on the Items
 tab. You can edit existing items, add new ones, or delete items as needed.
 For more information, see [About Adding, Editing, and Deleting Bill Items](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-adding-editing-and-deleting-bill-items).

## Viewing Bill Items Information

The Bill Items Info section (above the grid) displays Previous and This Invoice values at the Contract and Item level. As you work on an item, the system automatically updates ‘this invoice’ values for Work Complete, Stored Materials, Total, and % Complete. Stored Materials purchased for a contract item increase the Total, whereas ‘installed’ materials decrease the total. Use the chevron buttons (/ ) to toggle the Bill Items Info section open and closed (respectively).

## Overriding Retainage

You can override retainage amounts for each item on a billing using the Items tab or at the contract level using the JB Progress Bill Retg Totals form (accessed by selecting the Retainage Totals option from either the File menu or the Tasks drop-down). For more information, see [About the JB Progress Bill Retg Totals Form](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-progress-bill-retg-totals-form).

## Printing the Worksheet

After entering or editing the information on a
 billing, you can view and/or print the information by selecting
 File > Print
 Worksheet. The JB Contract Progress Worksheet report will
 appear, displaying the Previous, This Billing, Current, and Stored
 Materials amounts for the current contract/billing. Use this
 worksheet to gather current billing information for creating
 invoices.

## Bill Status Tracking

The Bill Status Tracking section allows you to assign a JB reviewer group,
 and then track the review and approval process for Progress
 billings. Once you assign a reviewer group, the Reviewers tab shows
 the reviewers in the specified reviewer group. The Reviewer tab is
 display only.
Tip: You can change the field values in the Bill Status Tracking section only when the Status drop down value is either A-Active or C-Change.

## Recipients / Delivery Tracking

The Recipients and Deliver tabs are used in conjunction with the Invoice Delivery feature and provide information about the recipients and delivery history for each invoice (respectively).
Regardless of whether you initialize billings (in JB Bill Initialization) or add them manually, the Recipients tab automatically defaults the recipients you have defined for the contract in the [JC Contract Recipients Detail](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-recipients-detail-form) form. You can edit the delivery information for existing recipients (delivery method, name, email or mailing address), add new recipients, or delete recipients.
The Delivery tab allows you to track the delivery history for invoices associated with the billing. This tab is display only, and shows you the delivery ID, the date the invoice was sent (delivered), delivery status (Delivered or Failed), and the recipient, as well as the recipient's email and/or address information (depending on the delivery method).

For more information, see the following
 articles:

- [JB Bill Initialization Form](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-bill-initialization-form)

- [About Updating Previous Billed Amounts on
 Future Bills](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-updating-previous-billed-amounts-on-future-bills)

- [About the JB Progress Billing Change Orders Form](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-progress-billing-change-orders-form)

- [About the JB Progress Item SM and Tax Form](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-progress-item-sm-and-tax-form)

- [About the JB Miscellaneous Distributions Form](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-miscellaneous-distributions-form)

- [Progress Billing Invoice Notes](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/progress-billing-invoice-notes)

- [About Changing Interfaced or Closed-Month Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-changing-interfaced-or-closed-month-billings)

- [About Closed Contract Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-closed-contract-billings)
