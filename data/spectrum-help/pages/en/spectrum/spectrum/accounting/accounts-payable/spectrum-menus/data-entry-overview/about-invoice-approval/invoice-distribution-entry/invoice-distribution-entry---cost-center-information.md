---
title: "Invoice Distribution Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-distribution-entry/invoice-distribution-entry---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-distribution-entry/invoice-distribution-entry---cost-center-information"
---

# Invoice Distribution Entry - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, when reviewing unapproved invoices Spectrum displays all invoices assigned to your operator and will permit approval, rejection, confirmation, and notes entry regardless of cost center setup. Spectrum disallows changes to invoices that you do not have cost center authorization to access.
In this window, Spectrum verifies revisions to the G/L account code of an unapproved invoice line are permitted. When a revision is made, Spectrum compares the G/L account's list of shared cost centers with cost centers in your assigned cost center scheme, and if there are no common cost centers, then that G/L account code is not allowed.

- For direct job cost lines, Spectrum verifies that revisions to the job or phase code of an unapproved invoice line are permitted. Spectrum first assures that your operator has permission for cost center specified in the phase file, if any. Entry of that phase will not be permitted if the cost center in the phase file is disallowed. If the cost center is not specified in the phase file, the cost center assigned to the job will be assigned, provided your operator has permission for that cost center. Entry of that job is not permitted if the cost centers in both the job and phase files are disallowed.

- For direct equipment cost lines, Spectrum verifies that revisions to the equipment or cost category code of an unapproved invoice line are permitted. Spectrum first assures that your operator has permission for cost center specified in the cost category file, if any. Entry of that cost category will not be permitted if the cost center in the cost category file is disallowed. If the cost center is not specified in the cost category file, the cost center assigned to the equipment will be assigned, provided your operator has permission for that cost center. Entry of that equipment code is not permitted if the cost centers in both the equipment and cost category files are disallowed.
