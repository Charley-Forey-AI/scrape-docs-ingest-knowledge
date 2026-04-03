---
title: "Projected Cost Phase Calculations - Quantity | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-calculations-window/projected-cost-phase-calculations---quantity"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-calculations-window/projected-cost-phase-calculations---quantity"
---

# Projected Cost Phase Calculations - Quantity

A reference for how Spectrum calculates projected costs for quantity.

## % complete:

Quantity at completion = (actual Quantity * 100) / Quantity % complete
Quantity to complete = Quantity at completion – actual Quantity

## To complete:

Quantity at completion = actual Quantity + Quantity to complete
Quantity % complete = (actual Quantity * 100) / Quantity at completion

## At completion:

Quantity to complete = Quantity at completion – actual Quantity
Quantity % complete = (actual Quantity * 100) / Quantity at completion
The remaining calculations dependent on which fields are recalculated:
Either dollars are recalculated:
Dollars at completion = quantity at completion * $/unit at completion
Dollars to complete = Dollars at completion – actual Dollars
Dollars % complete = (actual Dollars / Dollars at completion) * 100
$/Hour at completion = dollars at completion / hours at completion
$/Hour to complete = dollars to complete / hours to complete
Or $/unit are recalculated:
$/unit at completion = dollars at completion / quantity at completion
$/unit to complete = dollars to complete / quantity to complete
Then Hours are recalculated:
Hours at completion = quantity at completion / Unit/Hr at completion
Hours to complete = hours at completion – actual hours
Hours % complete = (actual hours / hours at completion) * 100
$/Hour at completion = dollars at completion / hours at completion
$/Hour to complete = dollars to complete / hours to complete
Or Unit/Hr are recalculated:
Unit/Hr at completion = quantity at completion / hours at completion
Unit/Hr to complete = quantity to complete / hours to complete
