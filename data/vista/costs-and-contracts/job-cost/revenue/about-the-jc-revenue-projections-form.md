---
title: "About the JC Revenue Projections Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form"
---

# About the JC Revenue Projections Form

This form allows you to adjust contract amounts by contract item for reporting purposes by establishing a 'projected' revenue amount.
Although referred to as JC Revenue Projections, its functionality is very different from JC Cost Projections.
Revenue Projections should be used in the following instances:

- For T&M contracts where there is no contract amount, use to calculate
 the contract to be equal to the billed amount, cost plus markup, or projected cost
 plus markup.

- For Progress contracts where the unit price is fixed but you are paid on
 units completed, use to calculate the contract units based on the projected units
 established in JC Cost Projections.

- For Progress contracts with unprocessed change orders where costs have
 already been incurred, use to override the contract amount by plugging the projected
 revenue. This will allow reporting cost to revenue on the same basis.

For normal Progress contracts based on fixed contract units and/or amounts that are typically only revised by change orders, this form should not be required and does not have to be updated monthly. For those contracts, it should only be used as described above to account for change orders in a month prior to their final processing. In a subsequent month, when the change orders have been processed, the adjustment should be removed to bring the projected revenue back to the contract amount.
Many contract reports will display the Revenue Projection if not zero, but will otherwise show the Current Contract. Therefore, for most contracts, revenue projections are not required and will only be used as an override.
Note: Both the Current Contract and Projected Contract amounts are displayed above the grid.
You can manually enter projections, have the program calculate projections for you (via the Calculate Projections option, Options menu), or use a combination of both methods. Regardless of which method you use, the following applies:

- Contract must be valid and specified items must exist on the contract.

- Contract must have a status of 'Open' unless you allow posting to hard-
 and/or soft-closed jobs (flags in JC Company Parameters), in which case, contracts
 with a status of 'Soft-Closed' or ‘Hard-Closed’ are also eligible.

- Contract cannot exist in any other projection batches.

- Batch month must be open in subledgers

- Plugging Projections - The projections grid shows you the Current Units and
 Dollars, Future CO's Units and Dollars, and Previous Projected Units and
 Dollars, and provides columns for entering adjusted units and/or dollars or
 projected units and/or dollars. For details, see [Plugging Projections](/en/vista/vista/costs-and-contracts/job-cost/revenue/plugging-projections#concept-5588--en__concept-5588)

- Refresh Data - Select Options > Refresh Data to refresh the current units and dollars, and future CO units and
 dollars on all items in the grid.

- Resetting Projected Amounts for Contract Items - The Reset
 Projected Item Amounts option (Options menu) allows you to reset projected
 amounts for items on the contract to their previous projected units and/or
 dollars. For example, you initialize projections for a contract and plug the
 values for several items on the contract. You then determine that the plugged
 values are incorrect for one or more items. Using this option, you can reset the
 projected values for those items to their Previous Projected Units and/or
 Previous Projected Dollars. Note: Projected
 values must be reset for each item individually. This allows you to correct
 values for specific items without affecting other items on the
 contract.

- Attachments - You can add attachments to any contract item in the grid. Just
 highlight the contract item, select the Attachments button (or the Scan button
 if attaching a scanned image), attach the image, and click OK. Once the
 projection batch is posted, the attachments are added (by JCCo, Contract, and
 Contract Item) to the JCID (Contract Item Detail) table.

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-calculation-form)Calculate Projections
[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-filter)Item and Bill Type Filter
[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-future-co-form)Future Change Orders
