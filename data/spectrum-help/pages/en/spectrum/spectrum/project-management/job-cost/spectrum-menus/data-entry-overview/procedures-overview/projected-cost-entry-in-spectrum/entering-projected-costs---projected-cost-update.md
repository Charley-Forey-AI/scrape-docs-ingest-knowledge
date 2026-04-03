---
title: "Entering Projected Costs - Projected Cost Update | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/procedures-overview/projected-cost-entry-in-spectrum/entering-projected-costs---projected-cost-update"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/procedures-overview/projected-cost-entry-in-spectrum/entering-projected-costs---projected-cost-update"
---

# Entering Projected Costs - Projected Cost Update

The Projected Cost History file allows for date-sensitive projected cost reporting (JC.PHIST). Before transactions are updated, the software validates the operator's security authorization; this way only key users can update projected cost. Meanwhile, limited-access users are allowed to view the Projected Cost Edit Listing.
When the Projected Cost Update is performed the amounts update to:

- Phase File – PM.PROJ (cost), PM.HPROJ (hours) and PM.LPROJDT (date) in JC.PHSE

- Billing Balance File – BB.PROJ(1)-(13) and BB.HPROJ(1)-(13) in JC.BBAL

- Projected Cost History File (see attached example of data stored in this file)
 The standard reports generally use the projected cost amounts in the Billing Balance file, and the Projected Cost History file is used to rebuild amount in the Billing Balance file if necessary. If a client wants projected cost amounts to be sensitive by day rather than by period, than the Projected Cost History file can be used.
