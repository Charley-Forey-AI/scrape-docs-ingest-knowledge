---
title: "About the PM Revenue Projections Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-revenue-projections-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-revenue-projections-form"
---

# About the PM Revenue Projections Form

 Use this form to review the impact to revenue projections
 within PM Cost Projections.
Projection numbers are “realtime” (meaning that, as you update cost
 projections, those updates flow to revenue), and you can make adjustments and ultimately post the
 revenue projections.
To enable this feature, the Activate revenue projection feature checkbox was added to the PM Company Parameters form's Projections tab. This checkbox allows administrators to enable, or disable, the Revenue Projections button for users to review revenue projections from the PM Cost Projections form.
Revenue Projections should
 be used in the following instances:

- For
 T&M contracts where there is no contract amount, use to calculate the
 contract to be equal to the billed amount, cost plus markup, or projected
 cost plus markup.

- For
 Progress contracts where the unit price is fixed but you are paid on
 units completed, use to calculate the contract units based on the
 projected units established in PM Cost Projections.

- For Progress contracts with unprocessed change orders where costs have
 already been incurred, use to override the contract amount by plugging
 the projected revenue. This will allow reporting cost to revenue on the
 same basis.

For normal Progress
 contracts based on fixed contract units and/or amounts that are typically
 only revised by change orders, this form should not be required and does
 not have to be updated monthly. For those contracts, it should only be
 used as described above to account for change orders in a month prior to
 their final processing. In a subsequent month, when the change orders
 have been processed, the adjustment should be removed to bring the
 projected revenue back to the contract amount.
Many contract reports will
 display the Revenue Projection if not zero, but will otherwise show the
 Current Contract. Therefore, for most contracts, revenue projections are
 not required and will only be used as an override.

Both the
 Current Contract and Projected Contract amounts are displayed above the
 grid.
You can manually enter projections, have the program calculate projections
 for you (via the Calculate Projections option, Options menu), or use a
 combination of both methods. Regardless of which method you use, the
 following applies:

- Contract
 must be valid and specified items must exist on the contract.

- Contract
 must have a status of 'Open' unless you allow posting to hard- and/or
 soft-closed jobs (flags in PM Company Parameters), in which case,
 contracts with a status of 'Soft-Closed' or ‘Hard-Closed’ are also
 eligible.

- Contract
 cannot exist in any other projection batches.

- Batch
 month must be open in subledgers.

Tasks
Plugging Projections

The projections grid shows you the Current Units and Dollars, Future CO's
 Units and Dollars, and Previous Projected Units and Dollars, and provides
 columns for entering adjusted units and/or dollars or projected units
 and/or dollars. Values entered directly in the Projected Units/Projected
 Dollars columns are considered 'plugged' values, regardless of whether
 you are entering projections manually or overriding initialized values.
 On several reports, this value will be used instead of the Current
 Contract.

If you initialized projections, the projected values (adjusted
 units/dollars and projected units/dollars) will be based on the
 projection method used during initialization (i.e., Units from Cost
 Projections, Billed Units and Dollars, Actual Cost Plus Markup Percent,
 or Projected Cost plus Markup). You can 'plug' the projected values for
 any contract item by either manipulating the adjusted units or dollars or
 the projected units or dollars.
If plugging 'adjusted' values, you will typically specify the amount by
 which to increase or decrease the final projected values. For example, if
 your current projected units are 20,000.000 and the final projected units
 will be 25,000.000, you would enter 5,000.000 as the adjusted units.
 However, if there are no projected values (i.e. adjusted and projected
 values are all 0.00), the adjusted values will become the final projected
 values (e.g. if adjusted units are 25,000.000, final projected units will
 be 25,000.00).

If plugging 'projected' values, just enter the final projected amount
 (units or dollars), and the system will automatically calculate the
 adjusted unit and/or dollar values. To 'unplug' a value, set the
 Projected Units/Dollars to zero. This will allow the WIP reports to use
 the Current Estimate.

Resetting Projected Amounts for Contract Items
The Reset Projected Item Amounts option (Options menu) allows you to reset
 projected amounts for items on the contract to their previous projected
 units and/or dollars. For example, you initialize projections for a
 contract and plug the values for several items on the contract. You then
 determine that the plugged values are incorrect for one or more items.
 Using this option, you can reset the projected values for those items to
 their Previous Projected Units and/or Previous Projected Dollars.

Projected values must be reset for each item individually.
 This allows you to correct values for specific items without affecting
 other items on the contract.

Adding Attachments
You can add attachments to any contract item in the grid. Just highlight
 the contract item, select the Attachments icon (or the Scanning icon if
 attaching a scanned image), attach the image, and click OK. Once the
 projection batch is posted, attachments are added.
