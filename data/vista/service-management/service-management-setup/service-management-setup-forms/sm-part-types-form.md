---
title: "SM Part Types Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-part-types-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-part-types-form"
---

# SM Part Types Form

Use the SM Part Types form to define the different types of parts associated with site equipment (for example, belts, filters, fuses, etc.).
Part types are primarily used to categorize the parts associated with standard tasks (set up in SM Standard Tasks). Although standard tasks can apply to multiple serviceable items, the parts used may differ based on the make and model of the equipment being serviced. Part types allow you to indicate what parts are required for the standard task without specifying the actual part numbers.
You can also assign part types to serviceable items
 (in SM Serviceable Items, Parts tab) and associate them with HQ materials. This allows
 the system to easily determine the part numbers needed to perform standard tasks on a
 work order referencing the serviceable item.
For example:You set up a part type of
 'Filter' and assign it to a standard task called "Change Air Filter". The standard
 task applies to several serviceable items, so you set up the part type for each
 serviceable item and reference the appropriate HQ material.
Serviceable ItemPart TypeHQ Material
100Filter220000
200Filter330000
300Filter440000

You then create a work order and set up Scope 1 for
 Serviceable Item 100 and Scope 2 for Serviceable Item 200. You assign standard task
 "Change Air Filter" to each scope. The system compares the part types on the
 standard task with those on the serviceable items and finds a match for part type
 'Filter'. For Serviceable Item 100, it defaults material 220000; for Serviceable
 Item 200, it defaults material number 330000
