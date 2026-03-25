---
title: "PO Quote Initialization Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/quotes/po-quotes-forms/po-quote-initialization-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/quotes/po-quotes-forms/po-quote-initialization-form"
---

# PO Quote Initialization Form

Use the PO Quote Initialization form to initialize quotes.
You cannot enter quotes manually; therefore, use of this form is necessary if you require requisitions to go through the quote process.
Quotes are created from requisition lines. The initialization process selects lines based on specified criteria and groups them together on a quote that can be sent to vendors for pricing.
Requisition lines are only initialized onto a quote if they meet the specified criteria and either:

- do not require approval for quote and do not have any reviewers assigned or,

- require approval, but have been approved by all assigned reviewers.

## Create Quotes Based On

Use this section to specify criteria for selecting requisition lines. For example, you can specify to select requisitions based on JC company and job, and all requisition lines referencing that JC company and job will be combined on a single quote, grouped by material (that is, requisition lines for Material #1000 would be grouped on one quote line, requisition lines for Material #5500 would be grouped on another quote line, and so forth).
Note: The more criteria you enter, the more restrictive the selection will be. However, there are some options that cannot be used together. For example, you cannot restrict by Location and Job. Because initialization would look for all requisition lines specifying both the Location and the Job, no requisition lines would ever be eligible, since these options are specific to different line types.

## Add to Existing Quote

You have the option to specify whether quote lines created during initialization will be added to an existing quote or a new quote. If you opt to add to an existing quote, an additional input is displayed to allow specifying the quote to which the lines will be added. If you opt to create a new quote, the initialization process generate a quote using the next highest quote number in the system. If a description is entered (for new quotes only), it is used in the quote header.

## Group Requisition Lines Into Quote Lines By

This option allows you to specify how requisitions with the same material will be grouped together on quotes.

- Material Code – Select this option if you want requisition lines grouped together by material code. All requisition lines with the same material group, material code, and unit of measure will be grouped together into one quote line.

- Material Code and Description – Select this option if you want requisition lines grouped together by material code and description. You would only need to use this option if you have materials that use the same material code but have differing descriptions. All requisition lines with the same material group, material code, unit of measure and description (description must be an exact match) will be grouped together into one quote line.

.

## Assigning Reviewers

This option allows you to assign an "active" reviewer (setup in the HQ Reviewers form) to each quote line created during initialization. The reviewer specified here is assigned in addition to the default Purchase Reviewer designated in PO Company Parameters (if one is assigned).
Note: If you do not require approval of quote lines before they are initialized to purchase orders (flag in company file), you should not need to assign a reviewer here. However, if you do assign a reviewer, the quote lines will need to be approved (or the reviewer deleted from the Reviewers tab in PO Requisition Entry) before you can add them to a purchase order.
