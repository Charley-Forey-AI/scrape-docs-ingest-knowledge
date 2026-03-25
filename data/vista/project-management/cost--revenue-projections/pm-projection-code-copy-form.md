---
title: "PM Projection Code Copy Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/cost--revenue-projections/pm-projection-code-copy-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/cost--revenue-projections/pm-projection-code-copy-form"
---

# PM Projection Code Copy Form

Use the PM Projection Code Copy form to copy the projection codes from one project to another.
There are several things you should know about copying projection codes:

- The process works best when the phases/cost types are the same on both the source and destination projects.

- All projection codes on the source project are copied to the destination project. If the phases/cost types associated with a projection code do not exist on the destination project, the projection code is still copied to the destination project but the phases/cost types are not copied. This means the Phase/Cost Type tab on the PM Projection Codes form will be empty for that projection code.

- You can run the process more than once on the same two projects, but all of the projection codes on the destination project are overwritten each time you run the process. This means that if you used the copy process and then made some changes to the projection codes in the destination project, those changes will be lost if you run the copy process again.

- You can copy projection codes when creating a new project using the PM Copy Project. If you use the PM Copy Project form to create a new project, you can copy the projection codes already set up on the source project to the destination project using the Projection Codes box (PM Copy Project).

- Projection codes set up on the source project that are associated with inactive phases (those with Active Phase checkbox unselected in JC Job Phases, Info tab) or cost types (those with Active checkbox unselected in JC Job Phases, Cost Types tab) are copied to the destination project.

- Projection codes that are set up on the source project as inactive (those with Active checkbox unselected in PM Projection Codes) will be copied to the destination project.

Related tasks

- [Copy Projection Codes](/en/vista/vista/project-management/cost--revenue-projections/copy-projection-codes)
