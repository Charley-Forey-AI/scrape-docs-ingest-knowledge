---
title: "Reviewers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/reviewers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/reviewers"
---

# Reviewers

The Reviewers tab on JC Jobs is used to set up reviewers for
 the job.
Reviewers assigned here are used for the
 review and approval of job-related unapproved invoices (AP) and/or purchase
 requisitions (PO requisition forms).

- Sequence # - For each reviewer you set
 up, you must specify a sequence number. When reviewing requisitions, the
 sequence number has no special meaning and can be set to '1' for all
 reviewers authorized to review requisitions only. However, when reviewing
 unapproved invoices, the sequence number determines the order in which each
 reviewer should review and approve invoice lines. For example, if you set up
 three reviewers that must each review and approve lines in a specific order,
 you would assign sequence numbers to identify the order in which they must
 review and approve each line.

- Reviewer 300 = Seq 3


- Reviewer 200 = Seq 2


- Reviewer 100 = Seq 1


Reviewer 100 must review and approve each invoice line before Reviewer 200,
 and Reviewer 200 must review and approve each invoice line before Reviewer 300.
 If you do not use a hierarchical approval system for unapproved invoices, you
 can assign all reviewers a sequence of '1'. Note: If a reviewer is authorized to review both unapproved
 invoices and requisitions, assign the sequence number based on the system
 you are using for unapproved invoices.

- Reviewer Type - The reviewer
 type assigned to each reviewer identifies whether they are authorized to
 review unapproved invoices (AP) and/or purchase requisitions (PO
 requisition forms) related to the specified job.

- Invoice – Reviewers
 assigned this type are authorized to review and approve
 unapproved invoices only, and are automatically assigned to any
 unapproved invoice lines referencing the specified job.

- Purchase – Reviewers
 assigned this type are authorized to review and approve
 requisitions only, and are automatically assigned to any
 requisition lines referencing the specified job.

- Both – Reviewers
 assigned this type are authorized to review and approve both
 unapproved invoices and requisitions. They will be assigned
 automatically to any unapproved invoice lines or requisition
 lines referencing the specified job.

[](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewers-form)HQ
 Reviewers
[](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-review-form)AP
 Unapproved Invoice Review
[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-reviewer-form)PO
 Requisition Reviewer
