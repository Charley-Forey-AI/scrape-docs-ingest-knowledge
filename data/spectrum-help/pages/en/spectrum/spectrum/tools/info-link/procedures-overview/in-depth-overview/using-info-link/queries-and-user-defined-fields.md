---
title: "Queries and User-Defined Fields | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/queries-and-user-defined-fields"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/queries-and-user-defined-fields"
---

# Queries and User-Defined Fields

The following tables are used to access employee
 user-defined fields.
If you set up new user-defined fields in Spectrum version 11 or
 later, you will need to use the tables listed here when creating queries.

1. PA.PARAM – This file contains the user-defined field sequence according to the object. Spectrum can handle up to 999,999 user-defined fields per object. In the event that you need to use the user-defined field for a non-specified or non-existent object, simply add the proper ID to this file. The current objects already set up in this file include: APINV, ARINV, CNTR, CUST, EMP, EQUIP, ET, GL, ITEM, JOB, PHASE, PMWO, PO, PPO, SI, SITE, SUB, VENDOR and WO.

1. PA.UDEFH – This is the user-defined field header file.

1. PA.XUDFH – This is the user-defined field header x-ref file.

1. PA.UDEFD – This file is the user-defined field validation codes file.

1. PR.UDEMP – This file is the object-related data file; in this case, this file is populated with the user-defined field assigned to each employee.[Using a User-Defined Field in a Query](/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/queries-and-user-defined-fields/using-a-user-defined-field-in-a-query) to view an example of using a user-defined field in a query.
[Using Two User-Defined Fields in a Query](/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/queries-and-user-defined-fields/using-two-user-defined-fields-in-a-query) to view an example of a query using two user-defined fields.
[Using a User-Defined Field in a Crystal-Link Report](/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/queries-and-user-defined-fields/using-a-user-defined-field-in-a-crystal-link-report) to view an example of a query using Crystal-Link reports.
