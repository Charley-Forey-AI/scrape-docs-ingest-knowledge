---
title: "SM Daily Trip Tickets | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/service-management-reports/service-management-general-reports/sm-daily-trip-tickets"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/service-management-reports/service-management-general-reports/sm-daily-trip-tickets"
---

# SM Daily Trip Tickets

You can use the SM Daily Trip Tickets report to print out
 all trip tickets for a given Technician for a give date range by selecting Service Management > Reports > SM Daily Trip Tickets.
The SM Daily Trip Tickets is designed to print out all trip tickets for a given Technician for a give date range. The ticket is mostly a form meant to be filled out in the field. Contains areas to record Labor, Materials, Equipment, and Miscellaneous details regarding what was done in the field.
Display\Parameter Restrictions:
The top section of the report will show necessary contact and service site address information along with scope and serviceable item information (if provided). Report only sees open trips and work orders. Along with being able to filter the report down to a specific company and technician, the report can also print trip tickets for a given date range supplied in in the Trip Date parameter or all open trips\work orders if the same field is left blank. Date field in upper right of the report will default to the first trip date it finds in the list of trips associated with work order. If no trip is associated with the work order it will default to the current date. If associated trips have information in the detail field the report will show this information instead of the scope information. The report is designed to only show a single scope\trip detail instance. Any additional instances of either can be optionally printed in the same report instance. This can be controlled by the Show Extra Scopes on Continuation Page parameter.
The NTE field in the area above the scope description displays the Not To Exceed value for that scope
If the report finds no open Trips or Scopes for the provided parameters the report will return a blank form.
Data Sources:

- SMWorkOrder

- HQCO

- SMWorkOrderScope

- SMCustomerInfo

- SMServiceSite

- SMTrip

- SMTechnician (SMTechnician_WO)

- SMTechnician (SMTechnician_Trip)

- PREHName (PREHName_WO)

- PREHName (PREHName_Trip)

Sub Reports:

- ScopeInformationSingleScope

- ScopeInformation

- Related Reports:

- SM Trip Ticket

Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Work Order (blank for all)
Click the Field Lookup
 button or press F4 to select the work order or leave blank for
 all.

Technician
Select the Field Lookup button or press F4 to select the technician.

Beginning Trip Date
Enter beginning trip date.

Ending Trip Date
Enter ending trip date.

Show Extra Scopes on Continuation Page
checkbox to show extra scopes on a continuation page.
