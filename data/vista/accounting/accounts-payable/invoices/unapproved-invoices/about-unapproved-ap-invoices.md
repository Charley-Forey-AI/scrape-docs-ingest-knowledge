---
title: "About Unapproved AP Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-unapproved-ap-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-unapproved-ap-invoices"
---

# About Unapproved AP Invoices

An overview of the AP invoice approval workflow
 process.
You can use Accounts Payable to enter unapproved invoices, have those invoices reviewed and approved, and then process them as you would any other AP transaction. Use the following forms to complete the unapproved invoice process:

- AP Unapproved Invoice Entry

- AP Unapproved Invoice Review

- AP Unapproved Invoice Status

- AP Unapproved Invoice Posting

## Entering Unapproved Invoices

In order for the review and approval workflow to function, one or more reviewers must be assigned to invoice lines. If you define reviewers at the header level, those reviewers automatically default to all invoice lines; when using reviewer groups, reviewers may not default depending on threshold amounts.
You can also pre-assign reviewers or reviewer groups in certain forms so that they are assigned by default when applicable invoice lines are created:

- JC Jobs

-
PM Projects

-
EM Departments

-  IN Locations

-
GL Chart of Accounts (groups only)

-  AP Vendors (reviewers only)

These defaults to the line(s) are in addition to any reviewers defaulting from the header. For more information, see [Entering Unapproved AP Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/enter-unapproved-invoices).

## Reviewing Unapproved Invoices

When reviewing invoices in the AP Unapproved Invoice Review form, each reviewer must log in with the appropriate user name, or as any of the logins registered for the reviewer in HQ Reviewers, in order to set an invoice status. If you are using a hierarchical structure, reviewers must approve invoice lines sequentially, meaning AP Unapproved Invoice Review does not display an invoice/line until all reviewers assigned with lower sequences have approved it. For more information see [Reviewing Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/review-unapproved-invoices).

## Viewing the Status of Unapproved Invoices

If you are using reviewer groups, the group's responsible person can use the AP Unapproved Invoice Status form to review the status of each invoice or line assigned to the group. From this form, the responsible person can access AP Unapproved Invoice Entry to update the invoice, view attachments associated with the invoice, or email reviewers. For more information, see [Reviewing the Status of Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/check-the-status-of-ap-invoices-in-the-approval-workflow).

## Posting Unapproved Invoices

Once all invoice lines are approved by reviewers, use the AP Unapproved Invoice Posting form to select invoices from one or more months to create a batch of the invoice transactions. Because the system adds the transactions to an AP Transaction Entry batch, they can be validated and posted as normal from either form. If editing is needed, you can exit the unapproved posting form and make changes in the AP Transaction Entry form. For more information, see [Posting Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/posting-approved-invoices).

## Running AP Unapproved Invoices Reports

AP provides a series of reports that you can use to track information about unapproved invoices.

- Check to see if outstanding unapproved invoices still exist in AP at the end of the month by running the AP Unapproved Invoices report. This report provides a list of all outstanding unapproved invoices for a given month.

- Track the progress of unapproved invoices using the AP Unapproved Invoice Update Check report. This report indicates what information is missing and required in order for the invoice to be posted.

- Use the AP Unapproved Invoices with Reviewers report to quickly review all of the unapproved invoices assigned to each reviewer and check to see which invoices they have approved and which they have not.

Related information

- [Create Reviewer Groups for AP Unapproved Invoices](/en/vista/vista/administration/headquarters/reviewer-setup/create-reviewer-groups-for-ap-unapproved-invoices)
