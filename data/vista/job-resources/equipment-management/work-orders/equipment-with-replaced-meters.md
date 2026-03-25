---
title: "Equipment with Replaced Meters | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/equipment-with-replaced-meters"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/equipment-with-replaced-meters"
---

# Equipment with Replaced Meters

When determining items due for maintenance on equipment with replaced meters in EM Work Order Initialize, the system uses the following process.

1. Adds the Last Done Miles or Hours + Replaced Meter miles or hours + SMG's interval value (i.e. Perform Service Every __ Miles/Kilometres or Hours), then subtracts the SMG variance (Warn when service within __ Miles/Kilometres or Hours") x the Variance in Advance. For ease of explanation, we will call this Value A.

1. Adds the current miles/kilometres or hours and the replaced meter miles/kilometres or hours defined in [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form). We will call this Value B.

1. Compares Value A to Value B. If Value A is greater than Value B, the item is not considered due for maintenance and will not be added to the Items Due grid (in EM Work Order Initialization). If Value A is less than Value B, the item is considered due for maintenance and will be added to the Items Due grid.
 Example:

Equipment 1000
Equipment 2000

EMEM Current Odometer:
8,000
8,000

EMEM Replaced Odometer:
80,000
80,000

SMG "Perform Service Every __ Miles/Kilometers":
3,000
3,000

SMG "Warn when service within ___ Miles/Kilometers":
200
200

SMG Item Last Done Miles:
7,000
2,000

SMG Item's Last Done Replaced Miles:
80,000
80,000

EM Work Order Init "Variances in Advance":
1
1

Equipment 1000:

- Value A: 7,000 + 80,000 + 3,000 - (200 x 1) = 89,800

- Value B: 8,000 + 80,000 = 88,000

In this example, Equipment 1000 is not due for maintenance because Value A (89,800) is greater than Value B (88,000); therefore, the item will be added to the Items Not Due grid.
Equipment 2000:

- Value A: 2,000 + 80,000 + 3,000 - (200 x 1) = 84,800

- Value B: 8,000 + 80,000 = 88,000

- In this example, Equipment 2000 is due for maintenance because Value A (84,800) is less than Value B (88,000); therefore, the item will be added to the Items Due grid.

Related information

- [About the EM Standard Maintenance Groups Form](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-standard-maintenance-groups-form)
