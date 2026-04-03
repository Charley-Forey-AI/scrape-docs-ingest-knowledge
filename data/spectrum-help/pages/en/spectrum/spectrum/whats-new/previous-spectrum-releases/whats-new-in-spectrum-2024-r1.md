---
title: "What's New in Spectrum 2024 R1 | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/whats-new/previous-spectrum-releases/whats-new-in-spectrum-2024-r1"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/whats-new/previous-spectrum-releases/whats-new-in-spectrum-2024-r1"
---

# What's New in Spectrum 2024 R1

Spectrum 2024 R1 contains more than a dozen improvements, each a time-saving enhancement aimed at making your job easier. This release also contains a regulatory change for Alabama and fixes to customer-reported issues.

## Trimble ID for Cloud users

Starting with this release, Trimble Viewpoint is upgrading your login so that you can log in to your Spectrum application using Trimble ID. Your Trimble ID is your set of single sign-on credentials which you can also use to log in to any other Trimble product.

## New checkbox supporting MFA enforcement

*This feature is enabled only after Trimble Viewpoint has migrated your organization to Trimble ID*.
Once your organization is using Trimble ID to log into Spectrum, an Admin may enforce multifactor authentication (MFA) for all users.
You can find the new MFA Required? checkbox in System Administration > Installation > System.

## Improved record searches

In this release, there are multiple contexts which now provide better visibility to existing records, so you can more easily get the information you need.
At-a-glance employment information
In Payroll > Employees, the search view now offers better visibility into key employee dates so you can more quickly verify employment and/or 401k eligibility. These fields have been added:

- Original hire dates

- Latest hire date

- Latest termination dateRemember: You can tailor this view by dragging and dropping columns in the order that works best for you.

Faster page loading
When you go to Job Cost > Job Phases, the focus now stays on the Search field instead of immediately bringing up the list of phases for the job. By waiting for your search entry before loading any phases, this screen now loads faster, especially when opening it on a job with many phases.
Use the search option to locate specific phases or groups of phases or select Go to retrieve all your phases.
Upgraded search windows
These search windows now retrieve and display greater detail so you can more quickly find the record you're looking for.Search windowContextField detail added
Search Current Invoice ReviewersInvoice Approval screen

- Reviewer name

Search Vendor LocationsWhen opting to remit payment to an alternate location using the More Invoice Information screen within Vendor Invoices.

- Address 1+ Address 2

- City

- State

- Postal code

- Telephone

- Fax

- Status

Search Warehouses for ItemPurchase Order Entry screen and several others

- Address

- City

- State

- Postal code

- Telephone

Search Service Contract Types Service Contract Main Properties

- Billing source

- Default earned revenue basis

## Running totals in plain sight

With this release, Spectrum provides an easy way to see the running totals of the respective fields in the entry tabs. In these screens, there are two new display-only fields: Total cost and Total hours.

- In Equipment Control > Data Entry, in both the Cost Transactions and Revenue Transactions screens.

- In Job Cost > Job Cost Transaction Entry

## Create archival copies of Instant Manual Checks

Instant manual checks are typically used to account for payments made before an invoice was received. With this release, you can opt to also generate an archival copy. Go to Accounts Payable > Data Entry > Invoice Entry > Instant Manual check and select the Include file copy? checkbox.

## New default option for data entry

When you go to Inventory Control > Data Entry > Job Requisition, the focus has always started in the Requisitions field.
With this release, you can override that default by selecting Operator Preferences > Batch code, which may help you complete your data entry faster.

## Faster access to Subcontract phase details

When you go to Job Cost > Job Cost Inquiries > Cost Activity, the Subcontract Commitments window opens. From there, you can now quickly view subcontract phase details by selecting the Subcontract phase details hyperlink.

## More flexibility when voiding direct deposit payroll

Now when you void payroll remitted via direct deposit, you are no longer required to print a replacement check. Instead, Spectrum now gives the voided payment the same treatment as when you void payroll checks, that is, retrieves the time card lines from history and voids the amounts.Remember: Similar to when voiding a payroll check, it's best practice to run a pay cycle for voiding direct deposits and a separate cycle for the corrections (if any).

## More report filtering options

When you run the Earned Revenue History Report, you'll see new Job status selections. By default, the report operates as it did prior to this enhancement, that is, all job statuses (Active, Inactive, and Complete) are selected. Now you can choose whichever combination will filter the report information down to what matters to you.

## Automated Overtime pay exemption for Alabama state income tax

Spectrum now supports [Alabama's legislation to exempt overtime wages](https://www.revenue.alabama.gov/individual-corporate/overtime-exemption/) from state income taxes. This release provides the necessary automation which can replace any manual methods you may be using.
There are setup components in Payroll > Maintenance > Tax Tables, and to run the utility on the entered time cards, there is a new AL OT Exempt button in the Time Card Entry screen and in the Layoff Check Entry screen.
For full details, see [Alabama Overtime Pay Exemption](/en/spectrum/spectrum/accounting/payroll/data-entry/alabama-overtime-pay-exemption).

## Spectrum 2024 R1 Bug Fixes

This release provides fixes to customer-reported issues. To see the list:

1. Log in to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues?tabset-d4f10=2) of the Viewpoint Customer Portal.

1. Make your selections in the product and module filter options.

1. In the Fixed in Version field, enter 2024 R1.

1. Select Apply Filters.
