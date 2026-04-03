---
title: "Projected Cost Phase Calculations - $/Unit | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-calculations-window/projected-cost-phase-calculations---unit"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-calculations-window/projected-cost-phase-calculations---unit"
---

# Projected Cost Phase Calculations - $/Unit

A reference for how Spectrum calculates projected costs for dollars per unit.

## To complete / At completion:

$/unit to complete entered
The calculations dependent on whether dollars recalculates Hours or $/Hour:
Dollars are always recalculated:
Dollars to complete = quantity to complete * $/unit to complete
Dollars at completion = Dollars to complete + actual Dollars
Dollars % complete = (actual Dollars / Dollars at completion) * 100
$/unit at completion = dollars at completion / quantity at completion
Then Hours are recalculated:
Hours at completion = dollars at completion / $/Hour at completion
Hours to complete = hours at completion – actual hours
Hours % complete = (actual hours / hours at completion) * 100
Unit/Hr at completion = quantity at completion / hours at completion
Unit/Hr to complete = quantity to complete / hours to complete
Or $/Hour are recalculated:
$/Hour at completion = dollars at completion / hours at completion
$/Hour to complete = dollars to complete / hours to complete
$/unit at completion entered
The calculations dependent on whether dollars recalculates Hours or $/Hour:
Dollars are always recalculated:
Dollars at completion = quantity at completion * $/unit at completion
Dollars to complete = Dollars at completion - actual Dollars
Dollars % complete = (actual Dollars / Dollars at completion) * 100
$/unit to complete = dollars to complete / quantity to complete
Set Method to Projected
Then Hours are recalculated:
Hours at completion = dollars at completion / $/Hour at completion
Hours to complete = hours at completion – actual hours
Hours % complete = (actual hours / hours at completion) * 100
Unit/Hr at completion = quantity at completion / hours at completion
Unit/Hr to complete = quantity to complete / hours to complete
Or $/Hour are recalculated:
$/Hour at completion = dollars at completion / hours at completion
$/Hour to complete = dollars to complete / hours to complete
