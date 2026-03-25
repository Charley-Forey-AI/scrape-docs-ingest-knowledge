---
title: "About Buy Out | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/about-buy-out"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/about-buy-out"
---

# About Buy Out

Use the Buy Out checkbox in JC Cost Projections to indicate when the buyout is complete for a phase/cost type; that is, total commitments
 have been made through subcontracts, purchase orders, and/or material orders.
The Buy Out checkbox initially defaults based on the setting for
 each phase/cost type in JC Job Phases, and is only used when the projection method (in
 JC Company Parameters) is set to ‘Actual + Committed’. It may be overridden; however, if
 you change the setting, make sure to recalculate your projections.
When buyout is complete for a phase/cost
 type (including linked cost types), the Final and Forecast amounts will be calculated as
 the actual cost plus total remaining committed cost. Once calculated, buyout amounts are
 not considered “plugged” amounts, and are ignored when projections are recalculated. In
 addition, because buyouts are not considered plugged amounts, the Write Over Plugged
 Values options (in the Projection Initialization window) will not have any effect on
 them.
If the Buy Out box is checked for a
 phase/cost type with a plugged value, and the plugged value does not equal the buyout
 value, the line color changes to light blue.
