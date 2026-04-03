---
title: "In-Depth - Freight Cost Reconciliation | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/freight-cost-reconciliation/in-depth---freight-cost-reconciliation"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/freight-cost-reconciliation/in-depth---freight-cost-reconciliation"
---

# In-Depth - Freight Cost Reconciliation

This screen serves two purposes: reconciling any differences between the calculated freight and the actual freight charged by the vendor, and grouping tickets together to create an A/P invoice. A selection by batch code is available on this screen, which allows you to select tickets that have been reconciled in groups by quantity.
For haulers that charge by the ton, the Freight Hours Reconciliation can be skipped and the reconciliation / posting to A/P can be done in one step.
However, for haulers that charge by the hour, you need some control over
 where the hours adjustment is to be done. Since the hours / amount can be adjusted in the
 Freight Cost Reconciliation screen, the Freight Hours
 Reconciliation screen could be skipped and the reconciliation could be done
 in this screen. To control where hourly ticket adjustments are performed in the software,
 Spectrum offers a flag on the Materials Management Installation > Properties screen. If the Require quantity reconciliation checkbox is selected,
 tickets first have to be adjusted or approved in the Freight Hours
 Reconciliation screen before they can be grouped to pay an invoice in the
 Freight Cost Reconciliation screen. Tickets that have not yet
 been quantity reconciled will not appear in the Freight Cost
 Reconciliation screen. If this checkbox is left clear, all selected
 tickets, regardless of whether they were adjusted/approved in the Freight Hours
 Reconciliation entry screen, are displayed and ready for reconciliation.
Once the tickets have been reconciled and grouped, the Freight Cost Reconciliation Update groups tickets together for reconciliation with the vendor's invoice. Once reconciled, the actual A/P invoice is created. The screen / update allows for both Ton and Hourly freight charges to be reconciled on a ticket-by-ticket basis.
