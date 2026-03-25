---
title: "About Technician Availability / Overbooking | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/about-using-the-dispatch-board/about-technician-availability--overbooking"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/about-using-the-dispatch-board/about-technician-availability--overbooking"
---

# About Technician Availability / Overbooking

When you schedule service work, the system determines technician availability to help prevent overbooking.
If you have defined work schedules for technicians (in SM Technicians), the system uses the work schedules to determine technician availability when scheduling technicians for service work in SM Trips or using the SM Dispatch Board. If you assign a technician that is not scheduled to work on the specified day, the system displays a warning; however, you are allowed to save the entry.
If the technician is already scheduled for other trips on the specified day, the system displays a warning and lists all work orders the technician is scheduled for, along with the trip number and estimated duration for each trip. For example:
Warning: Technician is currently scheduled for:
Order: 585 Trip: 1 Estimated Duration: 2.00
Order: 592 Trip: 2 Estimated Duration: 1.00
Order: 663 Trip: 1 Estimated Duration: 5.00
You can make the necessary changes or save the record as is.
Saved trips display on the Trips tab in the SM Work Orders form. If you are using the SM Dispatch Board, saved trips display on the board for the specified date and technician. If you did not specify a date, but assigned a technician, the trip displays in the Unscheduled column for the specified technician. If you assigned a date, but not a technician, it will display in the Unassigned row for the specified date. If you did not assign a date or technician, it displays in the Unassigned/Unscheduled column.
