---
title: "Projected Revenue on Unit Price Jobs | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/in-depth-overview/projected-revenue-on-unit-price-jobs"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/in-depth-overview/projected-revenue-on-unit-price-jobs"
---

# Projected Revenue on Unit Price Jobs

Unit Price jobs allow the contractor to bill for the actual quantities installed. Thus the WIP calculations on the Contract Status Report should be a function of projected quantities installed by the end of the project. One thing to note is that these projected quantities may or may not be driven by change orders.
The Projected Revenue feature will allow the contractor to enter the projected quantities for the job one time and have those same quantities be updated into the Contract file for projected contract. The Contract Status Reports can then be run using this projected contract number instead of the revised contract amount.
The projected contract number is the more accurate contract amount that will be billed for the job, using the original contract amount doesn't reflect the true quantities that are being installed in the job and can greatly distort the true profit on the job which can adversely effect the contractor's bonding capacity.

## Calculations

The Projected Contract is defined as the Projected Quantity times the Billing Rate per Unit as defined in Contracts. The Contract Status Report will then use this projected quantity number. Note that the projected contract is not a period sensitive number.

## Setup

This section discusses the additional steps to create a link between Quantity Entry and Projected Quantities. To facilitate setting up the phases, it is recommended that you complete the job's billing items before continuing.

## Creating the Link between Quantity Entry and Projected Quantities

When creating the quantity cost type phases, enter the appropriate billing item and mark the "Update projected contract quantities automatically?" checkbox. This creates the link between the projected quantities entered on the Quantity Entry screen and the projected quantities in Contracts.

-  Navigate to Job Cost  >  Maintenance  >  Job Phases.

- Enter the Job and Phase as appropriate.

- When creating phases with your quantity cost type, enter the Bill Item that you want linked in the phase's Properties window.

- Also select the Update projected contract quantities automatically checkbox.
