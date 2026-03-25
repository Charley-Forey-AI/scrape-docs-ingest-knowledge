---
title: "EM Work Order Parts Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/equipment-management-reports/equipment-management-general-reports/em-work-order-parts-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/equipment-management-reports/equipment-management-general-reports/em-work-order-parts-report"
---

# EM Work Order Parts Report

You can use the EM Work Order Parts Report to see parts
 needed for Work Orders for all locations or for one specific location by selecting
 Equipment Management > Reports > EM Work Order Parts Report.
This report is written to show parts needed for Work Orders for all locations or for one specific location. The report sorts by company, material, and then work order. By material it shows which work order items need the material; it includes quantity needed as well as quantity available by location(s). The parts location if entered will only display work order parts setup for this specific location and the availability for this specific location. If the parts location is left blank, all work order parts (even those without an inventory location - miscellaneous materials) will be shown with an availability section showing availability for all inventory locations. Low Stock Parts include any parts where available stock is less than or equal to the location materials low stock input. Short Stock Parts include any part where available stock is less than zero. Parameters include ranges of Parts and Work Orders, an inventory location or all, and a selection of "All Open Work Orders", "Low Stock Parts", or "Short Stock Parts". Tables used are EMWP, EMWH, INMT, INLM, and HQMT.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Beginning Work Order
Enter or select the applicable beginning work order.

Ending Work Order


 Enter or select the applicable ending work order.
Beginning Part (Material)
Click the Field Lookup
 button or press F4 to select beginning material code or leave
 blank to select all.

Ending Part (Material)Click the Field
 Lookup button or press F4 to select
 ending material code or leave blank to select all.
IN Company (Blank for All)Click the Field
 Lookup button or press F4 to select
 inventory company or leave blank to select all.
Parts LocationClick the Field
 Lookup button or press F4 to select
 parts inventory location or leave blank to select all.
Sort by (M)aterial or (L)ocationEnter M or L.
Include (P)urchased, (S)tocked, or (B)othEnter P, S, or B.
Enter the Closed Codes for Parts separated by commas (i.e. 1,2,3)
Enter the parts closed status code separated by commas (i.e. 1, 2, or 3) or leave blank for all.
