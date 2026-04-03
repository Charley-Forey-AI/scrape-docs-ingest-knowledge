---
title: "Projected Cost Phase Calculations - Dollars | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-calculations-window/projected-cost-phase-calculations---dollars"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-calculations-window/projected-cost-phase-calculations---dollars"
---

# Projected Cost Phase Calculations - Dollars

A reference for how Spectrum calculates Projected cost.

## % complete:

Dollars at completion = (actual dollars * 100) / dollars % complete
Dollars to complete = dollars at completion – actual dollars

## To complete:

Dollars at completion = actual dollars + dollars to complete
Dollars % complete = (actual dollars * 100) / dollars at completion

## At completion:

dollars to complete = dollars at completion – actual dollars
dollars % complete = (actual dollars * 100) / dollars at completion
The remaining calculations are dependent on either Hours or $/Hour being recalculated:
$/unit are recalculated first:
$/unit at completion = dollars at completion / quantity at completion
$/unit to complete = dollars to complete / quantity to complete
Then either Hours are recalculated:
Hours at completion = dollars at completion / $/Hour at completion
Hours to complete = hours at completion – actual hours
Hours % complete = (actual hours / hours at completion) * 100
Unit/Hr at completion = quantity at completion / hours at completion
Unit/Hr to complete = quantity to complete / hours to complete
Or $/Hour are recalculated:
$/Hour at completion = dollars at completion / hours at completion
$/Hour to complete = dollars to complete / hours to complete
