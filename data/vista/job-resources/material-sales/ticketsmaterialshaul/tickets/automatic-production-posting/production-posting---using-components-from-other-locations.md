---
title: "Production Posting - Using Components From Other Locations | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/automatic-production-posting/production-posting---using-components-from-other-locations"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/automatic-production-posting/production-posting---using-components-from-other-locations"
---

# Production Posting - Using Components From Other Locations

When posting production, there may be situations where the standard Bill of Materials is not appropriate because one or more of the components will come from a location other than the one at which the finished good is produced.
The Bill of Materials Override program allows you to set up a Bill of Materials that specifies which location each component will be pulled from.
When a component from another location is specified, it must first be sold or transferred from the source location to the production/sales location. How components are handled in this situation is determined by the Usage Option in IN Company Parameters.

## Transfer Usage Option

- IN Detail (INDT) – “Transfer
 from” and “transfer to” transactions are created for each component with a
 source location that does not match the production/sales location.

- IN Materials (INMT) – The “on
 hand” units are updated for the component at the source location, and the
 “on hand” units, average unit cost, and last unit cost are updated for the
 component at the production/sales location. (Note:   The last unit cost
 will only be updated if the sales date is greater than or equal to the “Last
 Cost Update” in IN Location Materials.)

## Sale Usage Option

- IN Detail (INDT) – “Sale” and
 “purchase” transactions are created for each component with a source
 location that does not match the production/sales location.

- IN Materials (INMT) – The “on
 hand” units are updated for the component at the source location, and the
 “on hand” units, average unit cost, and last unit cost are updated for the
 component at the production/sales location. (Note:   The last unit cost
 will only be updated if the sales date is greater than or equal to the “Last
 Cost Update” in IN Location Materials.)
