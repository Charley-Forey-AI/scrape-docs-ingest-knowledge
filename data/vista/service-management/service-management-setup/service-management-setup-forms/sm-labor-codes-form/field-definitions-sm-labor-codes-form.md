---
title: "Field Definitions: SM Labor Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-labor-codes-form/field-definitions-sm-labor-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-labor-codes-form/field-definitions-sm-labor-codes-form"
---

# Field Definitions: SM Labor Codes Form

The following is a list of field descriptions for the SM
 Labor Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Labor Code

Enter a labor code, up to 15 characters, to identify a repair or resolution commonly used when performing service work.

## Description

Enter a description of this labor code, up to 60 characters. This description will default as the description for work completed labor lines referencing this labor code.

## Active

Check this box to activate this labor code. Once activated, it will be available for selection when assigning labor codes to work completed labor entries in SM Work Orders (Work Completed tab), and will be included in labor code lookups.
Uncheck this box to deactivate this labor code. Labor code will not be available for selection when assigning call types to work completed labor entries, nor will it be included in labor code lookups.

## JC Cost Type

Enter the JC cost type (from JC Cost Types) to use
 as a default when referencing this SM labor code on work completed labor lines for a job
 work order. The system will use this cost type, in conjunction with the phase specified for
 the work order sequence, to post the costs to Job Cost (via the JC Cost Detail table).
Note: You can assign any valid cost type here; however, when adding work completed labor lines to a job work order, the following applies:

- If the job is locked (i.e. the Phases on this job
 are locked box is checked in JC Jobs), the cost type must be set up
 in JC Job Phases for the phase specified on the work order sequence; otherwise,
 the system displays a warning and will not allow you to save the work completed
 record until you specify a valid job/phase cost type.

-  If the job is not locked, the cost type must be set
 up in JC Job Phases or JC Phases for the phase specified on the work order
 sequence; otherwise, the system displays a warning and will not allow you to save
 the work completed record until you specify a valid phase cost type.

- The cost type specified here overrides the JC cost type defined at the SM Cost Type level, as well as the SM Pay Type level (by earnings code). The system will only default the JC cost type defined at the SM Cost Type or SM Pay Type levels if no labor code is specified for the work completed labor line or if a labor code is specified, but no JC cost type is assigned.
