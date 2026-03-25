---
title: "PM Template Phases Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-template-phases-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-template-phases-form"
---

# PM Template Phases Form

Use this form to set up templates that contain phases and cost
 types that are common to the various types of projects performed by your
 company.
 Once you set up a template, you can roll it into a project using PM Copy Template. A ‘roll-in’ uses the template to initially set up projects that require the phases and cost types you specified. Once the project is set up, you can tailor the phases and cost types to the specific needs of the project using PM Project Phases. For more information about template roll-ins, see [PM Copy Template Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-copy-template-form).
When you set up a template, assign a code and a description that easily identifies the type of project with which this template is associated. For example:

- OFFICE = Office building

- HOUSING = Housing development

- STREET = Street work

## Phases/Cost Types

Phases and cost types are set up for a template in the lower section of the form. The Info tab (and/or Grid tab) is used to set up all of the phases that are typical to projects that will use the template, and to link them to contract items and standard item codes (if applicable). When the template is rolled into a project, each phase is assigned to the specified contract item. If the assigned contract item does not exist on the contract, the roll-in will automatically set it up on the contract with the same description as the first phase assigned to it. If no contract item is specified for the phase, but a standard item code is specified, the standard item code will become the contract item, and the standard item code's description will be used as the contract item description. Phases with no contract item or standard item code assigned will automatically be assigned to contract item #1.
The Cost Types tab is used to define the cost types that will be used with
 each phase. When a phase is added, all of the cost types defined for the phase (in
 JC Phases) are automatically added for the phase here. You can then add or delete
 cost types as necessary; however, cost types added for a phase here must also be
 defined for the phase in JC Phases.
Templates can be set up according to specific areas of work. Multiple templates can be rolled into one project to add different areas of work for a specific project. Even though templates may contain the same phase, that phase will appear only once on the project.
