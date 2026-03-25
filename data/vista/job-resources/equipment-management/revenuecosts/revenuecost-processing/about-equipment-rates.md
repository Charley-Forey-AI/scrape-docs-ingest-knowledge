---
title: "About Equipment Rates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-equipment-rates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-equipment-rates"
---

# About Equipment Rates

When posting equipment usage, the revenue code you specify
 determines the equipment rate used.
Because you can override the rates defined
 by category at the equipment and/or revenue template level, the system follows a
 specific hierarchy when determining the rate to use:

1. If you are posting usage to a job, the system
 first looks to see if the job is using a revenue template (assigned in EM Job
 Templates) and if so, uses the rate defined at the equipment level (in EM Rev
 Rate by Equip Template). If no rate defined at the equipment level, it then uses
 the rate defined for the equipment’s category (in EM Rev Rate by Catgy
 Template).

1. If a revenue template is not being used (or usage is not being posted to a job),
 the system checks to see if a rate has been defined by equipment (in EM Revenue
 Rates by Equipment) and uses that. If no rate defined at the equipment level, it
 then uses the rate specified for the category (EM Revenue Rates by Category).
