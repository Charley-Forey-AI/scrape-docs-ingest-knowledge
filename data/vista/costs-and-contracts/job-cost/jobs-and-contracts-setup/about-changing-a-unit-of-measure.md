---
title: "About Changing a Unit of Measure | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-changing-a-unit-of-measure"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-changing-a-unit-of-measure"
---

# About Changing a Unit of Measure

You can change the unit of measure for a phase/cost type using the JC Job Phases form.
You can change the unit of measure for a phase/cost type when costs have already been entered, as long as the following criteria is met:

- the UM exists in HQUM (HQ Units of Measure).

- no change order detail exists in JCOD (Change Order Detail) where the source status equals ‘J’ (Job Cost) or ‘I’ (Interfaced).

- no change order detail exists in PMOL (Change Order Lines) where the source status equals ‘J’ (Job Cost) or ‘I’ (Interfaced).

- the TotalCmtdCost and RemainCmtdCost = 0.00 for every month in JCCP (Cost by Period).

If this criteria is not met, an error message is displayed providing a reason why the unit of measure cannot be changed, and the entry is not allowed.
If the criteria is met, the change is allowed and will update JCCD (Cost Detail) as follows:

- If the JCCD UM is not equal to the JCCH UM, sets the estimated units to 0.00.

- Updates projections (PF) records, setting the projected and forecast units to 0.00 where the JCCD UM is not equal to the JCCH UM.

- Updates posted units equal to actual units and the posted UM to the JCCH UM where the posted UM is null and the JCTransType is not ‘PF’ or ‘OE’.

- Updates actual units to 0.00 and the JCCD UM to the JCCH UM for all transactions where the JCCD UM is not equal to the JCCH UM and the JCTransType is not 'PF' or 'OE'.

- Updates the actual units equal to the posted units where the posted UM is equal to the JCCH UM and the JCTransType is not ‘PF’ or ‘OE’.

Note: You should double-check that the bill flag and units-to-date
 are correct after changing the unit of measure for any cost type.
