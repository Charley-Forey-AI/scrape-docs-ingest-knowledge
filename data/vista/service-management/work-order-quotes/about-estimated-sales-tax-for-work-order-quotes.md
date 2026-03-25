---
title: "About Estimated Sales Tax for Work Order Quotes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-order-quotes/about-estimated-sales-tax-for-work-order-quotes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-order-quotes/about-estimated-sales-tax-for-work-order-quotes"
---

# About Estimated Sales Tax for Work Order Quotes

When setting up budgets for taxable work order quote scopes, the system calculates the estimated sales tax based on the scope type.
Estimated sales tax for applicable work order scopes displays in the Taxes section below the Budget totals on the scope Info tab. The quote scope's price method (flat price or time and materials) determines how the estimated tax amount is derived:

- Flat Price - The system calculates the tax amount based on the taxable split revenue amounts and the tax rate for the specified tax code. For example, if you have three split revenue sequences for a total of $5,000, but only one sequence for $2,000 is flagged as taxable, tax is only calculated on $2,000. You can enter taxable split revenue amounts in SM Flat Price Revenue. For more information, see [Entering Flat Price Revenue](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-flat-rate-agreement-service/enter-flat-price-revenue).

- Time and Materials - There are two options for determining the quote scope's estimated tax amount:

- To have the tax amount equal the sum of all sales tax amounts for the scope's required and material and miscellaneous lines, select the Derived checkbox in the Budget totals section.

- To have the tax amount equal the sum of all sales tax amounts for the scope's taxable cost estimates, clear the Derived checkbox. You can set cost estimates to be taxed in SM WO Quote Cost Detail. For more information, see [Entering Summarized Cost Estimates for WO Quote Scopes](/en/vista/vista/service-management/work-order-quotes/about-work-order-quote-scope-budgets/enter-summarized-cost-estimates-for-wo-quote-scopes).

Note: For material cost estimates, the system considers the Matl Tax Override option selected for the quote scope. If it is set to No Tax or Use Tax, you cannot select the Default Tax Amount? checkbox, nor will the system calculate a tax amount. However, you can manually enter a tax amount.
