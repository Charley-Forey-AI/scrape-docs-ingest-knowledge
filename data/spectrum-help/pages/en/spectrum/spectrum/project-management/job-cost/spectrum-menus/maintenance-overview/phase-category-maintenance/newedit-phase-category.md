---
title: "New/Edit Phase Category | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/phase-category-maintenance/newedit-phase-category"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/phase-category-maintenance/newedit-phase-category"
---

# New/Edit Phase Category

Use this window to build and maintain a file of standard phases, categories, and major and minor groups. Standard phases are a helpful way to maintain consistency across jobs.
Fields/Buttons
Descriptions

Code
Enter a unique code for the phase.

Category name
Enter the description for this standard phase. As phases are later defined for specific jobs, the description entered here will default whenever this phase is added.

Properties

- Phase mask

-  Major group start position

- Major group end position

- Minor group start position

- Minor group end position

- Enter the phase category properties. See [Job Setup](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-setup) for more information.

Grid

Type
The default for this field is set during Job Cost Installation. Please refer to the [Installation Overview](/en/spectrum/spectrum/project-management/job-cost/installation-overview) for more information.
From the Type box, select Phase, Minor group, or Major group (shortcuts: p, g, m).
Three levels of detail can be defined with major and minor groups:

1. Major group: This is the summary view of the project-- the top level of information.

1. Minor group: This is the second tier of detail. Information is summarized to a level below the major group.

1. Phase detail: This level contains detail transactions.
More about major and minor groups:
Major and minor groups are ways to subtotal similar costs together for reporting purposes. They help you manage the job better by rolling costs, estimates, and projections together for the purpose of analysis. While the use of these groups is optional, they provide a key role when analyzing a project.

Code
The number of characters are based on the mask and start/end positions.
Major group character length must be between 1 and Major end. Minor group character length must be between 1 and Major end + Minor end.
Validation occurs if the "end" positions are entered. Phases display with the mask indicated above.
If the type is a phase, enter a unique code for the job phase. You do not need to enter hyphens. Except for the company-wide categories, the code displays with the mask that you specified in the Properties section. The phase field will display based on the category mask.
If the phase characters are a shorter length than the phase code mask length, Spectrum inserts leading or trailing zeros based on the Job Cost Installation setting (this does not apply to company-wide phase categories).
Note: If you change the phase mask in the Properties section, you will have to change the code before exiting the row. Delete the row and re-enter the data.

Description
Enter the category description, which displays on all reports.

Um
Entry in this field is available for standard phases. Enter the unit of measure, or click the arrow to open the search window.

Work comp
Entry in this field is available for standard phases.
Select the worker's compensation code for this phase from the drop-down list box. Entry in this field is optional.
If a Worker's compensation code is specified for this phase, the code entered here must have been previously set up in Worker's Compensation Code Maintenance. This code will then default when adding a new phase to a job for this standard phase code. Entry of a worker's comp code here alone will not affect defaults in Time Card Entry. This field is used for default purposes into valid job phases in Job Phases.
Workers' compensation codes are discussed in the sections on Jobs and Job Phases as well as in the Payroll help file.

Um description
Entry is available for standard phases.

Work comp description
Entry is available for standard phases.
