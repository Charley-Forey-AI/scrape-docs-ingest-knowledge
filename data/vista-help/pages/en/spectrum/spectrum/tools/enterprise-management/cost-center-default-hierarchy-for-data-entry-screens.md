---
title: "Cost Center Default Hierarchy for Data Entry Screens | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/enterprise-management/cost-center-default-hierarchy-for-data-entry-screens"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/tools/enterprise-management/cost-center-default-hierarchy-for-data-entry-screens"
---

# Cost Center Default Hierarchy for Data Entry Screens

In data entry screens, Spectrum looks to the first cost
 center it finds based on the following hierarchy.

1. Spectrum first looks to the cost center of the assigned element. In this case, the cost center defaults and it cannot be changed.

1. If a cost center was not found for the assigned element, Spectrum looks to the cost centers of the shared element. If the element only has one valid cost center, it will default.

1. If a valid cost center is not found, Spectrum looks to the cost center in the header record.

1. If Spectrum still hasn't found a cost center at this point, it looks to the detail line for the cost center.If none of the above apply, then the last cost center entered by the operator will default.
