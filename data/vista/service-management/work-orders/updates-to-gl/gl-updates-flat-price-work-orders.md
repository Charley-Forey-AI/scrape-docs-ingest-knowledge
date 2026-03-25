---
title: "GL Updates: Flat Price Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-flat-price-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-flat-price-work-orders"
---

# GL Updates: Flat Price Work Orders

When you bill a flat price work order scope, the system
updates the General Ledger based on the department and other setup factors.
The system
 determines the GL account to update based on:

- the department assigned to the service
 center or division (if you assigned a division to the work order scope and the
 division is assigned an alternate department);

- the call type assigned to the work order
 scope and;

- the split revenue entries defined for the scope in SM Flat
 Price Revenue.

During the invoicing process, the system generates a GL entry for
 each split revenue entry associated with the work order scope.
Note: Update to GL will only occur if the GL
 Invoice Interface in AR Company Parameters (Invoices tab) is set to Summary
 or Transaction. If set to No Update, no update to GL will occur, nor will any revenue
 entries be added to the Posted Detail tab in SM Work Orders; however, the system will still
 create the batch reports with the same information that would be included if you were
 updating GL.
The following explains how the system determines the GL account
 to update for each split revenue entry.

## Split Revenue with Cost Type Category and Cost Type

1. The system first looks in the Overrides table (in SM Departments) to see if an
 override exists for the cost type category/cost type/call type specified for the
 split revenue entry. If one exists, it will use the override Revenue WIP Account (if
 the call type is tracking WIP) or the Revenue Account (if not tracking WIP).

1. If a match is not found for the cost type category/cost type/call type, it will then
 look for an override matching the cost type category/cost type. If one exists, it
 will use the override Revenue WIP or Revenue account (as indicated above).

1. If a match is not found for the cost type category/cost type, it will then look for
 an override matching the cost type category/call type. If one exists, it will use the
 override Revenue WIP or Revenue account (as indicated above).

1. If a match is not found for the cost type category/call type, it will then use the
 standard Revenue WIP or Revenue account defined for the cost type category in SM
 Departments (Info tab).

## Split Revenue with Cost Type Category, No Cost Type

1. The system first looks in the Overrides table (in SM Departments) to see if an
 override exists for the cost type category and call type specified for the split
 revenue entry. If one exists, it will use the override Revenue WIP Account (if the
 call type is tracking WIP) or the Revenue Account (if not tracking WIP).

1. If a match is not found for the cost type category and call type, it will then use
 the standard Revenue WIP or Revenue account defined for the cost type category in SM
 Departments (Info tab).

If you enter work completed lines for a flat price work order scope, the system will
 update GL using the standard process for work completed lines. For more information, see
 [GL Updates: Work Completed](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed).
