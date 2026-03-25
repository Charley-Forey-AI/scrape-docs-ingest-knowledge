---
title: "IN Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/setup--maintenance/maintenance/in-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/setup--maintenance/maintenance/in-purge-form"
---

# IN Purge Form

Use this form to delete inactive locations and/or materials from the Inventory database tables.
You can also delete locations or materials that have not yet had detail posted to them using the associated setup form (the IN Locations or IN Materials form).
Purge options available:

- Delete Location and all of its Materials

- Delete all Materials, but leave Location on file

- Delete a selected Material from a Location

Regardless of which option you select, the purge process removes all eligible entries (see Purge Criteria below) from the Inventory Detail (INDT), Monthly Activity (INMA), Material UM (INMU), and Materials (INMT) database tables.
If you select the Delete Location and all of its Materials option, the system also purges eligible entries from the Location Company Category (INLC), Location Company Override (INLS), Location Category Override (INLO), and Location Master (INLM) database tables.
Note: The purge process does not update the PM Subcontract Detail form or the item detail in the PM Material Orders form.

## Purge Criteria

In order for a material to be eligible for purging, all these conditions must be met:

- On Hand, On Order, Allocated, and Received Not/Invoiced quantities are 0.00;

- Transactions do not exist for the material in any open month;

- Ins and Outs from closed months balance;

- Sum of units in the IN Inventory Detail table (INDT) equals 0.00;

- Material does not exist as a finished good or component on any Bill of Materials in the Bill of Materials Override table (INBO).

By default, the system applies the purge to all materials unless you select materials individually. The purge process cycles through all materials, skipping those materials that do not meet the criteria, and purging those that do. As the purge process completes, the system provides a summary indicating the number of materials purged and the number of materials that could not be purged.
Once the purge process is complete, a message displays stating that the purge was successful and provides the option to perform another purge.
If errors are encountered during the purge process, a message displays stating why the purge cannot be completed.
