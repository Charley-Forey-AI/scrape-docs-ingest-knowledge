---
title: "About Setting Up Default Reviewers for Unapproved Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-setting-up-default-reviewers-for-unapproved-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-setting-up-default-reviewers-for-unapproved-invoices"
---

# About Setting Up Default Reviewers for Unapproved Invoices

Creating and assigning reviewers is the central required
 element in the unapproved invoice process.
 In order for the review process to function, you must
 assign at least one reviewer to each line on each invoice that is being reviewed.
 The most efficient way to assign reviewers to invoices is by
 setting up default assignments in various locations so that reviewers default onto the
 line automatically. While you can add reviewers to lines (or edit) manually during
 invoice entry, the system is designed so that the vast majority of reviewers are
 assigned automatically.
Before proceeding, you must set up the necessary reviewers and groups in the HQ Reviewers and HQ Reviewer Group forms. Each reviewer's status in the HQ Reviewers form must be set to Active.

## Default Reviewer Groups/Reviewers to the Invoice Header

There is no recommended way to default reviewer
 groups to the invoice header in the AP Unapproved Invoice form. You can manually add a group to the Reviewer
 Group field in the header, which will cause the group's reviewers to
 appear on the Reviewers tab on the header and subsequently to the Reviewers tab on every
 line in the unapproved invoice.
Assigning reviewers to the header causes the same reviewers to subsequently appear on the Reviewers tab of each line. You can get reviewers to default onto the header in three ways:

- Manually add them in the Reviewers tab.

- Enter a value in the Reviewer Group field in the header; the group's reviewers will then default to the header Reviewers tab (except reviewers with thresholds assigned).

- Prior to invoice entry, in the AP Vendors form, enter a value in the
 Reviewer field (Add'l Info tab); the reviewer will then default
 to the header Reviewers tab for invoices to that vendor.

## Default Reviewers Groups/Reviewers to the Invoice Line

Defaulting reviewer groups to the line causes the reviewers from the group to appear on the Reviewers tab for that specific line. You can do this by assigning a reviewer
 group in the following locations:

- GL Chart of Accounts form, Info tab, Reviewer Group field

- EM Departments form, Info tab, Invoice Reviewer Group field

- IN Locations form, Info tab, Invoice Reviewer Group field

- JC Jobs form, Info tab, Reviewer Groups section, Invoices field

- PM Projects form, Info tab, Reviewer Groups section, Invoice field Note: Reviewer groups in the header do not default to the
 Reviewer Group
 field on the line(s) but the reviewers listed in the header group Reviewer tab
 still default on the Reviewers tab for each line.

Defaulting reviewers to the line saves you the effort of doing it manually. You can cause active reviewers to default automatically to the
 Reviewers tab on the invoice line from multiple sources:

- Any reviewer(s) in the Reviewers tab in the header

- Threshold reviewers from the reviewer group in the header whose
 threshold has been met on the line (or on the header, depending on the setting)

- The reviewer group on the line

- Any of these locations, if set up prior to invoice entry:

- EM Departments form, Info tab, Invoice Reviewer
 field

- IN Locations form, Info tab, Invoice Reviewer field

- JC Jobs form, Reviewers tab

- PM Projects form, Reviewers tab

- SM Work Orders

- SM Service Sites

- SM Customers

- SM Departments

- SM Service Centers

There are a few things to remember about reviewer and reviewer
 group defaults:

- You cannot assign a reviewer to any line more than once.

- There may be multiple reasons to justify a single reviewer's
 presence on an invoice line. For that reason, if you change any fields (group, job,
 etc.) on the invoice that may prompt removal of a reviewer, the system will check
 for other reasons to justify retaining them. If any are found, the reviewer will
 remain assigned to the invoice line.

- Reviewers that appear on invoice lines by default do not
 supplant or remove any reviewers already on the line.

- The only way to remove reviewers is manually or by changing the
 reason they defaulted onto the line.

Related information

- [About the HQ Reviewer Group Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form)
