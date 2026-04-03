---
title: "Equipment Tracking Installation - Rate Brackets | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-tracking/equipment-tracking-installation/equipment-tracking-installation---rate-brackets"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-tracking/equipment-tracking-installation/equipment-tracking-installation---rate-brackets"
---

# Equipment Tracking Installation - Rate Brackets

Use the Rate brackets section of the Equipment Tracking
 Installation screen to define different 'Rate Brackets' for internal (job) and external (site
 rental) requisitions for hourly, daily, weekly or monthly rates. These settings will be used
 in calculating the recurring billing for equipment.These settings can be changed as needed at
 any time.
Use this section to enter brackets for hourly, daily, weekly or monthly
 rates. This will be used in calculating the recurring billing for equipment. For example,
 the minimum rental period at a given company is one hour. You will enter Use hourly rate if
 over 1 hours up to 24 hours. This enables you to issue equipment, and if it is returned
 within the 24-hour period, no bill will be generated. In the weekly rate, you would then
 put Use weekly rate if over 3 days up to 999 days. This will always use the weekly rates
 for any charge over 3 days. The monthly rate will never be used in their case. The system
 will treat the weekly rates as 7 days if Sat/Sun are both chargeable, 6 days if one is
 chargeable, and 5 days if both days are not chargeable. For monthly rates, this will
 correspond to 28, 24, or 20 days.
Example: A particular company is set up for Saturday billing but not
 Sunday billing. They issue a piece of equipment out on Monday, August 7th. This particular
 equipment is set up for $100 / week for the stand-by rates. The equipment is returned on
 Saturday, August 19th. The billing would be calculated as follows: It was issued for 11
 billable days, the system will use 6 days in a week, so it was out for 11/6 = 1.83 weeks @
 $100 / week would yield a final bill for $183.33.
Fields
Descriptions

Use hourly rate if over
The minimum rental period at a given company is one hour.
 Type the minimum and maximum hours in the first and second fields on this
 line for hourly rates. For example, you might type 0 in the first field,
 followed by 12 in the second field. No bill will be generated for equipment
 that is returned within the hour.

Use daily rate if over
Type the minimum hours in the first field and maximum
 days in the second fields on this line for daily rates. For example, you
 might type 13 in the first field, followed by 3 in the second field.

Use weekly rate if over
Type the minimum and maximum days in the first and second
 fields on this line for weekly rates. For example, you might type 3 in the
 first field, followed by 20 in the second field. For equipment returned
 after 3 days, the weekly rate will be charged.

Use monthly rate if over
Type the minimum and maximum days in the first and second
 fields on this line for monthly rates. For example, you might type 20 in the
 first field, followed by 40 in the second field. For equipment returned
 after 20 days, the monthly rate will be used.
