---
title: "About the EM Warranties Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-warranties-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-warranties-form"
---

# About the EM Warranties Form

Use this form to enter and track warranty information about equipment and parts.
Warranties can be on the equipment itself and/or on any part that is attached to the equipment. If you will be moving items from one piece of equipment to another, set up each item as a component for accurate warranty tracking.
Because of the flexibility required for warranty information, many of the fields on this form are optional. In addition, warranties are informational only. However, if one or more warranties exist for a piece of equipment, a notification message will display on any work order referencing the equipment in the [EM Work Order Edit](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form) form.
Once you specify the equipment code and sequence number, enter the information needed for each warranty, as well as any notes that pertain specifically to the warranty or piece of equipment.
Example
Let’s say you purchase a Ford pickup that comes with a ’5-year or 50,000-mile’ warranty. You must first set up the truck in the Equipment Master so that it has an equipment number. Then set up the warranty information for the pickup as follows:
Field
Data

Equipment #
10101 (Ford F150 Pickup)

Sequence #
1

Manufacturer
Ford

Part Code
F150

Serial No
2G1FP357I248330 (VIN #)

Part Description
Ford F-150 Pickup

Warranty Description
5 years or 50,000 miles

AP Company
1

AP Vendor
11000 (Pacific NW Ford)

HQ Material
(leave blank)

AP Invoice #
P-12005

Date Purchased
06/01/11

Status
Active

Installation Information
(leave blank)

Warranty Information: Miles
50,000

Warranty Information: Warranty UM
Years

Warranty Information: Period
5

Warranty Information: Starting Date
06/01/11

Warranty Information: Expiration Date
06/01/16**

** If you enter the Period and
 Start
 Date, the system will automatically calculate the expiration date for
 you. However, you can also enter the Start Date and Expiration
 Date and the system will calculate the Period
 value for you.
You then purchase a new set of tires for the F-250
 pickup. The tires come with a 60,000-mile warranty. At the time of installation, the
 truck odometer reading is 54,000 miles. You would set up the warranty information as
 follows:
Field
Data

Equipment #
10101 (Ford F150 Pickup)

Sequence #
2

Manufacturer
Michelin

Part Code
ZX800

Serial No
(leave blank)

Part Description
Set of 4 Michelin ZX800 Radial

Warranty Description
60,000 miles

AP Company
1

AP Vendor
31500 (Joe's Tire Service)

HQ Material
88000 (tires)

AP Invoice #
J-51200

Date Purchased
01/15/14

Status
Active

Installation Information: Date Installed
01/15/14

Installation Information: Miles at Install
54,000

Installation Information: Installed By
Vendor

Warranty Information: Miles
60,000

Warranty Information: Warranty UM
(leave blank)

Warranty Information: Starting Date
01/15/14

Warranty Information: Expiration Date
(leave blank)

Once you enter the warranty information, the system automatically begins tracking the number of hours, miles, and/or days until the warranty expires and displays this information at the top of the form. Expiration values are calculated as follows:

- Hours: Total Hours (calculated in EM Equipment,
 Meters tab) − Warranty Hours = Warranty expires in N hours

- Miles: Total Miles (calculated in EM Equipment,
 Meters tab) − Warranty Miles = Warranty expires in N miles

- Days: Today's date − Expiration Date = Warranty expires in N days (The warranty Start Date field is required for this calculation.)
