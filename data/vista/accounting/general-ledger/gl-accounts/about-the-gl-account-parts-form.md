---
title: "About the GL Account Parts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-accounts/about-the-gl-account-parts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-accounts/about-the-gl-account-parts-form"
---

# About the GL Account Parts Form

Use the GL Account Parts form to identify the different parts of your account code.
The format of your account code will have been defined by Viewpoint at the time of implementation.
Note: All parts of an account code need to be set up in this form before you can define the account code in GL Chart of Accounts.
The standard format, if not changed during implementation, is 5R.2LN2LN. In this format:

- Part 1 is the base account, which is the first 5-character right-justified part, followed by a period.

- Part 2 is a 2-character left-justified profit center part.

- Part 3 is a second 2-character left-justified profit center part.

After the parts are defined, instances of the accounts are set up.
Note: The instances for the base account are updated as you add your accounts into GL Chart of Accounts. The instances for all other parts must be manually created.

## Setting up account parts on the Info tab

Use the Info tab to set up account
 parts.
With the example above, on the Info tab,
 you might set up Part 1 to be “Account,” and Parts 2 and 3 could be the types of
 profit center, such as “Division,” “Department,” or “Location.”

## Setting up instances of the account parts on the Instances tab

Use the Instances tab to set up the
 instances of the base account and the profit centers. For example, Part 2 might be
 Division, with instance 01 being Commercial and instance 02 being Residential. Part
 3 might be Location, with instances representing different districts or counties, or
 even different areas of the country (e.g. 01 for West Coast, 02 for Mid-west, 03 for
 East Coast, etc.).

## Assigning major and minor categories to account part instances

You can also use the Instances tab to
 assign major and minor categories (set up in GL Report Categories) to each instance
 of a GL Account Part 1. These categories can then be used to categorize and group
 financial statement sections within specific reports. For more information, see
 [GL Report Categories](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form).

Related information

- [About the GL Report Categories Form](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form)
