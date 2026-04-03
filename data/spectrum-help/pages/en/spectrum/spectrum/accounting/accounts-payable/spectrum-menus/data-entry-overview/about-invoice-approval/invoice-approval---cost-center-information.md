---
title: "Invoice Approval - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-approval---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-approval---cost-center-information"
---

# Invoice Approval - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, the following applies:

- Spectrum prevents changes to invoices that you do not have cost center authorization to access.

- When reviewing unapproved invoices, Spectrum displays all invoices assigned to you and permits approval, rejection, confirmation, and notes entry, regardless of cost center setup.

- You can set these overrides in your cost center scheme (in the Cost Center Scheme Maintenance screen) and expect these results:

- Job entries - the system validates the cost center assigned to direct job cost invoice detail lines.

- Equipment entries - the system validates the cost center assigned to direct equipment cost invoice detail lines.

- Non-job entries - the system validates the cost center assigned to non-direct invoice detail lines.The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum compares the cost center assigned in the entry screen detail with the applicable override cost centers in your assigned scheme, and if the cost center is not included, then the invoice entry line will not be allowed.
