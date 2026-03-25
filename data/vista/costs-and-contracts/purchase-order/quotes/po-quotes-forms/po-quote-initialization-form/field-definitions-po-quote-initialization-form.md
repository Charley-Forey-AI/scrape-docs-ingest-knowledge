---
title: "Field Definitions: PO Quote Initialization Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/quotes/po-quotes-forms/po-quote-initialization-form/field-definitions-po-quote-initialization-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/quotes/po-quotes-forms/po-quote-initialization-form/field-definitions-po-quote-initialization-form"
---

# Field Definitions: PO Quote Initialization Form

The following is a list of field descriptions for the PO
 Quote Initialization form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## IN Company

 Enter the IN company for restricting quote initialization. Requisition lines will be initialized onto a quote only if they reference this IN company, meet all other selection criteria, and either:

- do not require approval and do not have any reviewers assigned or,

- require approval, but have been approved by all assigned reviewers.

 Leave blank if not restricting by IN company.
Note: IN company is required if restricting by Location Group and/or Location.

## Location Group

 Enter the location group (from IN Location Groups) for restricting quote initialization. Requisition lines will be initialized onto a quote only if they reference locations within this location group, meet all other selection criteria, and either:

- do not require approval and do not have any reviewers assigned or,

- require approval, but have been approved by all assigned reviewers.

Leave blank if not restricting by location group.

## Location

 Enter the location (from IN Locations) for restricting quote
 initialization. Requisition lines will be initialized onto a quote only if they reference
 this IN location, meet all other selection criteria, and either:

- do not require approval and do not have any reviewers assigned or,

- require approval, but have been approved by all assigned reviewers.

Leave blank if not restricting by location.

## EM Company

 Enter the EM company for restricting quote initialization. Requisition lines will be initialized onto a quote only if they reference this EM company, meet all other selection criteria, and either:

- do not require approval and do not have any reviewers assigned or,

- require approval, but have been approved by all assigned reviewers.

Leave blank if not restricting by EM company.
Note: EM company is required if restricting by EM Shop.

##  EM Shop

 Enter the shop (from EM Shops) for restricting quote initialization. Requisition lines will be initialized onto a quote only if they reference this shop, meet all other selection criteria, and either:

- do not require approval and do not have any reviewers assigned or,

- require approval, but have been approved by all assigned reviewers.

Leave blank if not restricting by EM shop.

## Material Category

 Enter the material category (from HQ Material Categories) for restricting quote initialization. Requisition lines will be initialized onto a quote only if they reference a material within this material category, meet all other selection criteria, and either:

- do not require approval and do not have any reviewers assigned or,

- require approval, but have been approved by all assigned reviewers.

Leave blank if not restricting by material category.

## JC Company

Enter the JC company for restricting quote initialization. Requisition lines will be initialized onto a quote only if they reference this JC company, meet all other selection criteria, and either:

- do not require approval and do not have any reviewers assigned or,

- require approval, but have been approved by all assigned reviewers.

 Leave blank if not restricting by JC company.
Note: JC company is required if restricting by job.

## Job

 Enter
 the job (from JC Jobs) for restricting quote initialization. Requisition lines will be
 initialized onto a quote only if they reference this job, meet all other selection
 criteria, and either:

- do not require approval and do not have any reviewers assigned or,

- require approval, but have been approved by all assigned reviewers.

Leave blank if not restricting by job.

## Shipping Location

 Enter the ship location (from PO Shipping Locations) for restricting quote initialization. Requisition lines will be initialized onto a quote only if they reference this ship location, meet all other selection criteria, and either:

- do not require approval and do not have any reviewers assigned or,

- require approval, but have been approved by all assigned reviewers.

Leave blank if not restricting by shipping location.

## Required Thru Date

Enter the required date through which to restrict quote initialization. Requisition lines will be initialized onto a quote only if their Req Date is less than or equal to the date specified here, they meet all other selection criteria, and either:

- do not require approval and do not have any reviewers assigned or,

- require approval, but have been approved by all assigned reviewers.

Leave blank if not restricting by 'required' date.

## Requisition ID

 Enter the requisition ID for restricting quote initialization. Requisition lines will be initialized onto a quote only if they exist on the requisition specified here, they meet all other selection criteria, and either:

- do not require approval and do not have any reviewers assigned or,

- require approval, but have been approved by all assigned reviewers.

Leave blank if not restricting by requisition ID.

## Add to Existing Quote

Check this box to initialize requisition lines onto an existing quote(specified to the right).
Do not check this box if you want to initialize requisition lines to a new quote.

## Quote ID

Enabled only if Add to Existing Quote option is Y (checked).
Enter the quote for initializing requisition lines. Press F4 for a list of existing quotes.

## Description

The system enables this field when you check the Add to Existing Quote box.
Enter a description of the quote, up to 60 characters. This defaults from the Description field in the quote header.

## Group Requisition Lines Into Quote Lines By

Select the appropriate radio button.

- Material Code – Select this option if you want requisition lines grouped together by material code. The system groups all requisition lines with the same material group, material code, and unit of measure together into one quote line.

- Material Code and Description – Select this option if you want requisition lines grouped together by material code and description. The system groups all requisition lines with the same material group, material code, unit of measure and description (description must be an exact match) together into one quote line.

## Assign Reviewer to These Quote Lines

Enter the reviewer (from HQ Reviewers) to assign to all quote lines generated during initialization. The system assigns this reviewer in addition to the default purchase reviewer specified in PO Company Parameters.
Press F4 in the Reviewer field for
 a list of active reviewers.
Press
 F5
 in the
 Reviewer
 field to access HQ Reviewers.
