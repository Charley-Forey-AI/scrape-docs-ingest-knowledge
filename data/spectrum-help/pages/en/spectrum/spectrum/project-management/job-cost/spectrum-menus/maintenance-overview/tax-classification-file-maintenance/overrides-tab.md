---
title: "Overrides tab | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/tax-classification-file-maintenance/overrides-tab"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/tax-classification-file-maintenance/overrides-tab"
---

# Overrides tab

Use this tab to exempt individual cost types from use tax. You can add, edit, or delete A/P tax overrides by cost type. As a best practice, set up all cost types your company uses. This will make it easier to determine the overrides later on.
The priority for determining the tax status of an Accounts Payable invoice line item or Purchase Order detail line is below:

- If the phase and cost type combination is in the table, the taxable flag for this combination is used.

- If a cost type appears on the override list, the taxable flag for this cost type is used.

- Otherwise, the default rate for the tax code is used.

For example, on a tax-exempt job, some material is taxable at 6.5%. The default rate for the tax code would be set to 6.5%. All cost types are entered as non-taxable. If there are two phases, and the material is taxable on this type of job, the phase overrides are entered with the Taxable checkbox selected. This causes material in these two phases to be taxable, and all other material to be tax exempt.

Related information

- [New/Edit A/P Tax Overrides windows](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/newedit-ap-tax-overrides-windows)
