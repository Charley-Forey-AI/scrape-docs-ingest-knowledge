---
title: "Use Tax Example | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/use-tax-example"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/use-tax-example"
---

# Use Tax Example

In the state of Texas, a contractor needs to pay different tax amounts on different material items within a single job. For example, if a job is a state job and therefore tax exempt, most material purchased for the job is non-taxable. However, some material (for example, material not left in the building, such as concrete forms) is taxable even on a tax-exempt job.
To further complicate matters, in many cases the vendor will not list the correct sales tax amount on the invoice. For example, the vendor may be invoicing several material items for a job. Since the job is tax exempt, the vendor has not charged any sales tax on the invoice. However, some of the line items are taxable. In this case, the correct sales tax needs to be calculated by the user, added to the invoice amount, and posted to accounts payable and paid to the vendor. The vendor needs to be able to see the tax amount paid to advise them how much tax to remit to the state.
For example, the vendor may have invoiced the user for $100.00 of material and no tax. The user calculates the tax amount as $4.00. In this case, the user will pay the vendor $104.00 and needs to indicate to the vendor that $4.00 is the tax.
In many cases, the user is able to code jobs such that the taxable status can be determined by the cost type. For example, material might be taxable but labor might be tax exempt. In these cases, cost type can be used to automatically determine the taxability of each A/P invoice line.
However, in some cases certain material is taxable on a job while other material is tax exempt. For example, on tax exempt jobs for the state, material which is "left in the building" is tax exempt but other material (for example, consumables) in taxable. In looking at the issue, it has been determined that setting up two material cost types in this case would be too cumbersome. Instead, the user may track consumables as a phase within the material cost type. For this reason, the tax table has to allow overrides by phase as well as cost type.
Normally, there will be a relationship between the A/P sales tax setup and the A/R setup. For example, in some states the contractor has the option of paying sales tax at the time of purchase or charging tax at the time of sale. If tax is paid at the time of purchase, then no tax is charged at the time of sale; otherwise, no tax is paid at purchase and it is charged at time of sale. Because of this relationship, it makes sense for A/R and A/P sales tax issues to be handled in one table. This will allow the user setting up the table to establish the correct relationship for the job.
