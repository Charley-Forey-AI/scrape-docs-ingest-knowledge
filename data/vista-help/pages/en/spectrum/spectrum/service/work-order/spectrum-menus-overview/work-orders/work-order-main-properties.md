---
title: "Work Order Main Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/work-order-main-properties"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/work-order-main-properties"
---

# Work Order Main Properties

Use the Work Order Main Properties
 screen to enter general information about the work order including a work order summary,
 dispatch information, and assigned technicians. In addition, purchase orders for the work
 order can be added at this time for Site work orders.
Note: You can quickly navigate between Work
 Order screens via the Info Bar links, or use the
 hot-key equivalents on the command bar.
Field/ButtonDescription
Work orderEnter a work order number.

- If the work order number does not exist or this
 field is left blank, the New Work Order window will open first.

- If a valid work order number is entered, properties
 information for the work order will display on this screen. If the work
 order is completed or the user does not have security authorization to
 this screen, this screen will be view-only.

Site/JobThe site or job name associated with
 the work order will display in this field.
Service ContractThis field will conditionally display
 'Maintenance' or 'Extra Work' if the contract number is stored in the Work
 Order header.Note: This field will appear in
 the header of all the associated Work Order
 screens.

Site AlertThis field will conditionally display
 if there is an alert in the Site
 Main Properties screen, and the 'Display in Work Order' check
 box is selected.Note: This field will appear
 in the header of all the associated Work Order screens.

Info
Work order typeEnter the work order type: residential,
 commercial, job cost, and so forth. The type code entered here must have been
 previously defined in Work Order
 Type Maintenance. The type code that defaults here is from the
 Sites screen, but
 may be overridden if desired. Entry in this field is required.
If a job with a division is entered in the Job Cost > Jobs screen, the division will default in the
 Type field instead. However, the division must be
 a valid G/L department set up with a direct cost flag, and must exist as a
 work order type.
 If
 the work order type is changed, Spectrum will validate that the cost center
 matches the one in the Work Order Billing Setup page.
 If the cost center does not match, an error message will direct you to
 change the cost center.

NameFor Site work orders, the name of the
 work order displays from the Work Site Address File Maintenance file. For Job
 work orders, the name of the work order displays from the
 Jobs screen. No changes are allowed.
Service contractEnter the service contract #. The
 description will display to the right of this field. When this field is
 entered, the Service Contract alert will appear in the header of this screen
 indicating 'Extra Work'.
This field will be view-only if
 this is a maintenance service contract.
This field
 will be unavailable if the service Contract module is not
 installed.

Customer P.O.Enter the customer's purchase order
 number in this field.
This field will be hidden if a job
 work order is selected.

Customer's jobIf this is a Materials work order and
 you have set up any special pricing for this customer, select the job to assign
 to this work order.
PhoneEnter telephone numbers for the work
 order. Do not enter parenthesis or a hyphen; the software will insert these
 characters. For Job work orders, this phone number is the site phone in the
 Jobs screen.
Contact noteEnter the name of the billing contact.
Customer codeEnter the code of the customer to be
 billed for this work order. The customer will default from the job/site file,
 but it is possible to specify a different customer for billing purposes. A
 search window is available for viewing valid customer codes. Entry in this
 field is required.
 If a new customer will be billed for
 this work order, open the search window then select the Maintenance button to set
 up a new customer without backing out of Work Order. While entering new Work
 Order customers, it is not necessary to back out of the current entry screen
 and enter customer data in the Accounts Receivable module. This
 Customer Maintenance window allows entry of new
 customers in the middle of Work Order Entry. The information entered here
 will be used by the software to create the A/R Customer File; duplicate
 entry will not be necessary.
Note: If
 this selected customer's status is set to 'Not Used' in the Accounts
 Receivable module, entry is not allowed. If the customer's status is set to
 'Inactive' in the Accounts Receivable module, entry is allowed in this
 screen, however the software will warn you of the customer's status.


Credit AlertIf the selected customer is over
 pre-established credit limit, the following message displays below the
 customer's code and name: "Customer over credit limit".
Dispatch
ZoneEnter the zone in which this work is to
 be performed. The zone entered here must have been previously set up in
 Zip Code Zone Maintenance. A search window is
 available for viewing valid zone codes. Note: If the work order was created from a service contract, the dispatch zone
 defaults from the site.

PriorityEnter the priority for this work order.
 Two spaces are available, and either numbers, letters, or a combination of both
 may be used in establishing priorities.
If color-coded
 indicators have been set up in Priority Maintenance
 for the priority number you've entered, a color-coded circle will appear
 indicating the priority level. For example, the red ball can be associated
 with the highest priority

Case typeEnter the case type to apply to the
 work order. Note: If the work order was created from a
 service contract, the case type defaults from the site.

Price methodUse the drop-down menu to select the
 price type.
See the [What is included on Work Order invoices](/en/spectrum/spectrum/service/work-order/in-depth-overview/what-is-included-on-work-order-invoices) document for more information on selecting a
 price type.

QuoteEnter the dollar amount quoted to the
 customer.
HoursEnter the total projected hours for the
 entire Work Order visit.
Est. arrivalEnter the estimated arrival time.
This information displays in the Est Arrival field on the
 Crystal-Link Work Order printout.

Status
Dispatch codeEnter the dispatch status code for this
 work order. The code entered here must have been previously set up in
 Dispatch Status Maintenance.
The code that displays in parenthesis after the dispatch status code is the
 work order's status. This information is also available in Lookup mode on
 the Work Order Entry screen.
If color-coded indicators have been set up in
 Dispatch Status Maintenance for the status number
 you've entered, a color-coded flag will appear indicating the status. For
 example, the yellow square can be assigned to the HOLD status.

Status typeThe status type label assigned to the
 dispatch status code will display in this field. If no dispatch code is
 assigned, this field will say 'Open'.
Work summaryEnter a summary of the work ordered (up
 to 250 characters).
Dates
Ordered dateThe ordered date and time will be set
 to the current work order processing date and time when a new work order is
 added.
The ordered date can be changed in the
 New and Edit windows if the
 operator has the appropriate security level.

Requested date/timeEnter the date and time this work is
 scheduled to begin. These fields are recorded automatically on the
 Dispatch Board and on the Dispatch
 Schedule screens when the work order is scheduled in either of
 the dispatch screens.
This information displays in the
 Est Arrival field on the Crystal-Link Work Order printout.

Scheduled date/timeEnter the date on which the work order
 request was scheduled. In the second field, enter the time at which the request
 was scheduled. Entry in these fields is optional.
Assigned dateEnter the date and time this work order
 was assigned to a technician. These fields are recorded automatically when a
 technician is assigned to this work order.
Arrived date/timeEnter the date on which the
 technician(s) arrived to complete the work. In the second field, enter the time
 at which the technician(s) arrived. These fields are recorded automatically
 when the work order status is changed to Arrived.
Finished date/timeEnter the date on which the technician
 completed the work. In the second field, enter the time at which the work was
 completed. Entry in these fields is optional.
Technicians
Entries in this listbox will appear on the Dispatch Schedule for the selected work order.
E-mailSelect to send an email to
 the selected technician.
New / EditSelect to add a new
 technician, or edit the selected technician. You can add a technician to the
 selected work order multiple times.

- Enter the code for the technician you want to assign
 to the work order. The Technician Name will display to the right of this
 field. If you are editing or viewing a technician, no changes are
 allowed.

- Choose the technician's responsibility from the
 drop-down list. Options include Lead, Second, or blank. The first
 technician assigned to the work order will automatically be assigned the
 Lead responsibility, and any subsequent assignments for this technician
 will also have the same responsibility. The second technician assigned to
 the work order will automatically be assigned the Second responsibility.

- Enter the date and time this work is scheduled to
 begin. These fields are recorded automatically on the Dispatch
 Board and on the Dispatch Schedule
 screens when the work order is scheduled in either of the dispatch
 screens. This information displays in the Est Arrival field on the
 Crystal-Link Work Order printout.

- Enter the total number of hours the technician is
 expected to work on the work order.

DeleteSelect to delete a selected
 technician from the work order.
ViewIf the selected work order is
 view-only, the View button will be the only available
 option.
Requested techThe requested technician specified in
 Site Main Properties screen displays to the right of
 the action buttons.

Related information

- [Reopen Completed Work Order](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-orders/reopen-completed-work-order)

- [Work Order Form](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-orders/work-order-form)
