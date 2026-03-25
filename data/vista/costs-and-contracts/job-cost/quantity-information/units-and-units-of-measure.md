---
title: "Units and Units of Measure | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/quantity-information/units-and-units-of-measure"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/quantity-information/units-and-units-of-measure"
---

# Units and Units of Measure

In some cases, when you enter actual costs, you also have the opportunity to enter units.
For example, when entering an invoice in Accounts Payable, you might pay for 600 cubic yards of concrete, which have been posted to the material cost type of phase 12000-10. The 600 units would be updated to Job Cost, with a unit of measure of CY and the designated dollar amount. When posting labor costs, JC Progress Entry allows you to update units complete. Since units are tracked separately by cost type, labor progress can be tracked for a single phase, as well as how much material has been used, and so on. Information about units completed is used by Job Billing and by the JC Cost Projections program, as well as for printing job cost reports that show production.
In order to make sure apples and oranges are not mixed together, the system screens for matching units of measure. Each job/phase/cost type combination has an official unit of measure that can be seen in the JC Job Phases program. This is generally set when the estimate is entered, either from Project Management or directly in the JC Job Phases or JC Original Estimates programs. When you enter or interface costs to JC that have units attached, the units accumulators in JCCP (Cost by Period) are updated only if the incoming transaction’s unit of measure matches the official one, or if there is a conversion for the unit of measure set up in HQMT (Materials). JCCD (Cost Detail) and the dollar amounts in JCCP are updated in all cases.

## Example

Suppose the estimate for material on phase 12000-10 is given in cubic yards. If 600 cubic yards of concrete are posted in AP Transaction Entry, the ‘Units’ field in JCCP would be increased by 600. However, if the next line item is for 2,000 pounds of reinforcing steel on the same phase, that item would not affect the units in JCCP. Both items would create JCCD entries, each with its appropriate costs and units; 600 cubic yards on the first and 2000 lbs. on the second.
If a job/phase/cost type is accidentally set up with the wrong unit of measure, you can change it in JC Job Phases, and the program will attempt to correct JCCP by looking at JCCD. However, it is recommended that you pay close attention when setting up units of measure to ensure that they are set up correctly.
