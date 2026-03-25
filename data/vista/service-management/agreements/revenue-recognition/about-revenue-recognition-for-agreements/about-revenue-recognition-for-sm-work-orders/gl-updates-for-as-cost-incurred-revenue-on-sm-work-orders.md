---
title: "GL Updates for 'As Cost Incurred' Revenue on SM Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-revenue-recognition-for-sm-work-orders/gl-updates-for-as-cost-incurred-revenue-on-sm-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-revenue-recognition-for-sm-work-orders/gl-updates-for-as-cost-incurred-revenue-on-sm-work-orders"
---

# GL Updates for 'As Cost Incurred' Revenue on SM Work Orders

 When recognizing "as cost incurred" revenue for SM work
 orders, the system handles the GL updates a little differently than "as billed"
 revenue.
The system updates the recognized revenue amount for all work
 completed line on an "as cost incurred" work order as follows:

- If the work completed line is posted to a customer work
 order, the system uses the Work Order Deferred Rev account specified for the
 service center department or division (if a division is specified for the
 scope).

- If the work completed line is posted to an agreement work
 order, the system uses the Agreement Deferred Rev account specified for the
 agreement service division or service center department. If no division or
 service center is specified for the agreement service, the system uses the
 department assigned to the agreement type on the agreement.

The system then posts offsetting entries as follows:

- For T&M
 scopes (customer and agreement work orders) - Offsetting entries
 are posted to the Revenue account or Revenue WIP account (if tracking WIP for
 the scope's call type) based on the line's cost type/cost type category and the
 division assigned to the work order scope or the service center department (if
 no division on the scope). If no cost type is specified for the work completed
 line, the system uses the Revenue or Revenue WIP account for the line type
 category.For example, say you enter a work completed
 miscellaneous line with a subcontract cost type/cost type category for a
 scope that is assigned a division and a call type that is tracking WIP. In
 this case, the offsetting entry is posted to the Subcontract Revenue WIP
 account defined for the Division department.
If you
 had not specified a cost type for the work completed line, the system would
 have updated the Other Revenue WIP account, since that is the revenue
 account used for miscellaneous work completed lines that don't reference a
 cost type
Note: For miscellaneous lines coming from Accounts
 Payable that do not have a cost type specified, the system will use the
 material cost type category.

- For Flat Price
 scopes (customer and agreement work orders) - Offsetting entries
 are posted to the Revenue account or Revenue WIP account (if tracking WIP for
 the scope's call type) based on the line's cost type/cost type category and the
 division assigned to the work order scope or the service center department (if
 no division on the scope). If no cost type is specified for the work completed
 line, the system uses the Revenue or Revenue WIP account for the line type
 category.For example, say you enter a work completed
 equipment line with an equipment cost type/cost type category for a flat
 price scope that has no division specified and is assigned a call type that
 is not tracking WIP. In this case, the system posts the offsetting entry to
 the Equipment Revenue account defined for the service center
 department.
If you had not specified a cost type
 for the work completed line, the system would have updated the Equipment
 Revenue account because equipment work completed lines use the equipment
 cost type category.Note: For miscellaneous lines
 coming from Accounts Payable that do not have a cost type specified, the
 system will use the material cost type category

- For
 Non-Billable scopes (agreement work orders only) - Offsetting
 entries are posted to the Revenue Account or Revenue WIP account (if tracking
 WIP for the scope's call type) based on the line's cost type/cost type category
 and the division as follows:

- If a division is specified for the agreement service
 associated with the scope, it will use the department assigned to the
 division

- If there is no division specified for the agreement
 service, then it will use the service center department

- If there is no service center at the agreement
 service, then it will use the department assigned to the agreement
 type For example, say you have an agreement
 service that is assigned at Division. You enter a work completed
 labor line with a labor cost type for a non-billable scope
 associated with that agreement service. The work order scope is
 assigned a call type that is tracking WIP. In this case, when
 recognizing revenue, the system posts the offsetting entry to the
 Labor Revenue WIP account defined for the division's department.

If you had not specified a division on the
 agreement service, the system would then have posted the offsetting
 entry to the revenue WIP account for the service center department.
 If you had not specified a service center at the agreement service,
 it would have then posted it to the revenue WIP account for the
 agreement type department.

Note: For miscellaneous lines coming from Accounts
 Payable that do not have a cost type specified, the system will use the
 material cost type category.

When you bill a work order, the system moves the recognized revenue
 amount from the Agreement Deferred Rev account (agreement work orders) or Work Order
 Deferred account (customer work orders) to the Revenue GL account defined for the
 invoice's receivable type in AR Receivable Types. The amounts in the offset Revenue or
 Revenue WIP accounts are left intact.

Related concepts

- [About Revenue Recognition for SM Work Orders](/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-revenue-recognition-for-sm-work-orders)

- [SM Revenue Recognition Form](/en/vista/vista/service-management/agreements/revenue-recognition/service-management-revenue-recognition-forms/sm-revenue-recognition-form)
