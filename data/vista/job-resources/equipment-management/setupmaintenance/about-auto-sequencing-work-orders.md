---
title: "About Auto Sequencing Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-auto-sequencing-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-auto-sequencing-work-orders"
---

# About Auto Sequencing Work Orders

Whether you enter or initialize work orders, you can manually assign work order numbers or have the system generate them automatically.
If you always use numeric work order numbers, you
 can select the Auto Sequence Work Order # check
 box in EM Company Parameters (Work Orders tab) to have the system generate work
 order numbers for you. Depending on the Last Work Order option you select, generated
 numbers will be based on the Lastthe last company or shop work order number. If you
 select this method, you
If you use both numeric and alphanumeric work order numbers, then manual entry will probably work best for you.
If you elect to use auto numbering, choose either to use a company-wide numbering scheme or to assign numbers sequentially by shop.

- If numbering by company, the Last
 Company W.O. # field will determine the next sequential work
 order number assigned during work order initialization.

- If numbering by shop, assign a ‘last work order
 number’ to each shop set up in EM Shops. When initializing work orders, the
 system assigns numbers based on the specified shop and the Last WO
 #specified for the shop.

Note: For multiple companies sharing the same shop group:

- When multiple companies share the same shop group and are using the auto-sequence by shop option, the system will search all companies for the highest work order number in existence for the specified shop, then assign the next sequential work order number.

- When companies share the same shop group, but are not using the auto-sequence by shop (i.e. are auto-sequencing by company), the system will exclude those companies when searching for the highest work order number for the shop. Auto-numbering for those companies will be based on the highest work order number for the company. This may result in multiple companies having the same work order numbers.
