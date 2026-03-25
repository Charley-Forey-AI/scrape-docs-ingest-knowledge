---
title: "About Sub-Sub Phases | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/about-sub-sub-phases"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/about-sub-sub-phases"
---

# About Sub-Sub Phases

During the initial implementation of the Vista, you determined the format of your phase code structure. The most common format of 13 positions (XXXXX–XXX–XXX), with the last three places blank, allows the sub-sub phase to be used for specific tracking situations. The ability to manually assign the sub-sub phase is also dependent upon the Number of Valid Characters in Phase Code option in JC Company Parameters. Following are some options for sub-sub phase use when all sub-sub phases are initially blank.

- Change Orders Using 1 to 199 – Use for approved change order numbers to track detailed costs. For example:

Database Phase Optional Phase
01060-120- 01060-120-  4
Development Fees Development Fees for ACO #4

- Work/Field Orders Using 600 to 799 – Use for work or field orders to track costs that will become approved change orders when completed. For example:

Database Phase Optional Phase
03160-407- 03160-407-612
Expansion Joints Add'l Expansion Joints, FO #112

- Back Charges Using 800 to 999– Use to track costs that will be a back charge to a subcontractor/supplier. For example:

Database Phase Optional Phase
04210-  - 04210-  -811
Brick Masonry Brick Masonary Cleanup, BC #1

Those with Heavy/Highway estimating software, or those using Viewpoint’s Vision Item Bidding software, may choose to add the bid or item number as the sub-sub phase when importing to Project Management. Users that have assigned sub-sub phase numbers during implementation have more limited choices. Incorporating alpha characters into the sub-sub phase will differentiate between database phases and special phases. Following are some options for sub-sub phase use when sub-sub phase database numbers exist:

- Change Orders Using C01 to C99 – Use for approved change order numbers to track detailed costs. For example:

Database Phase w/Item Optional Phase
603-120-112 603-120-CO2
Sewer Pipe Add Sewer Pipe, ACO #2

- Work/Field Orders Using FO1 to F99 – Use for work or field orders to track costs that will become approved change orders when completed. For example:

Database Phase w/Item Optional Phase
513-  -074 513-  -F18
Railings Add Railings, FO #18

- Back Charges Using B01 to B99 – Use to track costs that will be a back charge to a subcontractor/supplier. For example:

Database Phase w/Item Optional Phase
608-200- 18 608-200- B29
Concrete Walks Concrete Walks Cleanup, BC #29

Some users prefer to assign specific phases in the database to track detailed costs for variable situations. The database phases can then be personalized for each situation. For example:
Database Phase Optional Phase Optional Phase
900-  -   992-  - 103 992-  - 104
Change Orders Change Order #1, Item 3 Change Order #1, Item 4

Database Phase Optional Phase
992-  -   992-  - 182
Field Orders Field Order #18, Item 2

These examples illustrate the flexibility of the sub-sub phase. You will have to decide what will meet the needs of your company by examining how you handle these situations now and how you want your costs reported in the future. Allow sufficient room for growth, and most importantly, make sure that sub-sub phase usage is consistent throughout your company.
