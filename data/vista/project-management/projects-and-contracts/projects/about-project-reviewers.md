---
title: "About Project Reviewers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/about-project-reviewers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/about-project-reviewers"
---

# About Project Reviewers

Reviewers set up for a project are used to approve unapproved invoices (in AP) or
 purchase requisitions (in PO) associated with the project.
The Reviewers tab in PM Projects is used to
 set up reviewers for the project. Each reviewer is assigned a 'reviewer type' to
 identify whether they are authorized to review unapproved invoices and/or purchase
 requisitions related to the specified project. Reviewer types are:

- Invoice – Reviewers assigned this type are authorized
 to review and approve (or reject) unapproved invoice lines only, and are
 automatically assigned to any job-related invoice lines referencing the
 specified project (in AP Unapproved Invoice Entry).

- Purchase – Reviewers assigned this type are authorized
 to review and approve (or reject) purchase requisition lines only, and are
 automatically assigned to any 'requisition' material line (in PM Material
 Detail) referencing the specified project.

- Both – Reviewers assigned this type are authorized to
 review and approve both unapproved invoice lines and purchase requisition lines.
 They will be assigned automatically to unapproved invoice lines or 'requisition'
 material lines referencing the specified project.

When setting up reviewers, you must specify a sequence number.
 (If left blank, the sequence defaults as '1'). For unapproved invoices (only), the
 sequence number determines in what order each reviewer should review and approve invoice
 lines. For example, if you set up three reviewers, and each reviewer must review and
 approve lines in a specific order, you would assign sequence numbers to identify in
 which order they must review and approve each line.

- Reviewer 100 = Seq 1

- Reviewer 200 = Seq 2

- Reviewer 300 = Seq 3

Reviewer 100 must review and approve each invoice line before
 Reviewer 200, and Reviewer 200 must review and approve each invoice line before Reviewer
 300. If you do not use a hierarchical approval system, just assign Seq 1 to all
 reviewers.

Related concepts

- [About the HQ Reviewers Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewers-form)

- [AP Unapproved Invoice Review Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-review-form)

Related tasks

- [PO Requisition Reviewer Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-reviewer-form)
