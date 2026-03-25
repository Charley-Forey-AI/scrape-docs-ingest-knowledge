---
title: "Field Definitions: SM Work Scope Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-work-scopes-form/field-definitions-sm-work-scope-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-work-scopes-form/field-definitions-sm-work-scope-form"
---

# Field Definitions: SM Work Scope Form

The following is a list of field descriptions for the SM Work
 Scope form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Work Scope

Enter a name or code to identify this scope of work. Up to 20 characters allowed.

## Description

Enter a brief description of this scope of work. Up to 60 characters allowed.

## Priority

Required.
Enter the priority of this work scope. The priority assigned here will default automatically when this work scope is assigned to a work order scope; however, it may be overridden as necessary.

- High

- Medium

- Low

## Details

Use this field to enter information about the scope of work. This might generally be details about the scope of work, such as materials needed, measurements, special requirements, specific directions, and so forth.
Informational only; not currently used anywhere in SM.

## Default Phase

Enter the phase (from JC Phases) to use as a default
 when adding this work scope to a work order sequence in SM Work Orders. When capturing work
 completed for the work order, the system will use this phase and the cost type specified on
 the work complete line to post the costs to Job Cost (via the JC Cost Detail table).

- You can assign any valid phase to a work scope.
 However, when adding the work scope to a job work order, if the job is locked (i.e.
 the Phases on
 this job are locked box is checked in JC Jobs) and the phase is not
 set up for the job (in JC Job Phases), the system displays a warning and will not
 allow you to save the record until you specify a valid phase. If you want to use the
 default phase, you can press F5 from the work order scope to access JC Job Phases and
 add the phase to the job.

- The phase specified here may be overridden once the work scope is designated for a work order sequence.

## Prevent Scope Auto Close when Billing

The Prevent Scope Auto Close when Billing checkbox on the Info tab of the SM Work Scopes form.

Select this checkbox to prevent the currently selected scope from being closed automatically when billed.
If you reference this scope on a work order (in SM Work Orders, Scope field), when you fully bill the work order scope, the system leaves the work order scope open, even if you selected the Auto Close Work Order on Final Bill checkbox in SM Company Parameters. You will need to manually close the work order scope.
If you leave this checkbox unselected and you selected the Auto Close Work Order on Final Bill checkbox in SM Company Parameters, upon fully billing the work order scope, the system will auto-close the work order scope.
Note: If the Auto Close Work Order on Final Bill checkbox is not selected in SM Company Parameters, you must manually close work order scopes, no matter how you set this checkbox.
