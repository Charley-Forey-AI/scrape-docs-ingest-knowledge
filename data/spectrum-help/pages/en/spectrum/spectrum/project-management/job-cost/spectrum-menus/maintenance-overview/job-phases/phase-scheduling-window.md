---
title: "Phase Scheduling window | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-phases/phase-scheduling-window"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-phases/phase-scheduling-window"
---

# Phase Scheduling window

The Phase Scheduling window is used to record inter-dependencies among phases. These fields are available to store relationships between project tasks. The window also allows you to record unlimited phase dependencies, as well as lead and lag time.
Field
Description

Predecessor phase
Enter the prerequisite summary phase code, or press F4 or double-click on this field to select from a list of valid phase codes. For example, a predecessor phase may be drywall if the successor phase is painting walls. It is not necessary to list all prerequisite phases for a given phase provided that the prerequisite is implied (for example, you would not need to list "foundation" as a predecessor for painting walls).

Description
The description for the predecessor phase displays. No entry is allowed.

Link type
There are four types of phase dependency that can be used to define the relationship between the Phase code field and the Predecessor phase line transaction. Select the appropriate link type from the drop-down menu options:

- Finish-to-start = A phase starts after its predecessor finishes.

- Start-to-start = A phase starts when its predecessor starts, that is, the phases start at the same time.

- Start-to-finish = A phase finishes after its predecessor starts, that is, the first phase cannot finish until the second phase has started.

- Finish-to-finish = A phase finishes when its predecessor finishes, that is, the second phase cannot finish before the first phase finishes.

Lag/Lead time
Enter the lag or lead time.
Note: Enter lead times as negative numbers and enter
 lag times as positive numbers.

Lag units
Entry in this field is required if a number was entered in the Lag / lead time field. Select the lag units from the drop-down menu options:

- Day

- Elapsed days (including weekends and holidays)

- Hour

- Minute

- Week
