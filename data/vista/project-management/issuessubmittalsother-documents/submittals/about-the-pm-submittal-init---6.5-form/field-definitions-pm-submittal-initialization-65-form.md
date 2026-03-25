---
title: "Field Definitions: PM Submittal Initialization-65 Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-init---6.5-form/field-definitions-pm-submittal-initialization-65-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-init---6.5-form/field-definitions-pm-submittal-initialization-65-form"
---

# Field Definitions: PM Submittal Initialization-65 Form

The following is a list of field descriptions for the PM
 Submittal Initialization-65 form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Specify the project for which to initialize submittals. Must be a valid project set up in PM Projects.

##  Starting Submittal Number

 Specify the number with which to begin numbering submittals.

##  Submittal Type

 Specify the type of submittal to initialize. Must be a document type (defined in PM Document Types) with a document category of ‘Submittal’.

## Initialize Submittals

- Initialize Submittal for Each Unique Phase — Select this option if
 you want to initialize a submittal for each unique phase (within the range of phases
 specified) on the project.

- Initialize Submittal for Each Phase Using Valid Part of Phase Code
 — Select this option if you want to initialize a submittal for each phase (within the
 range of phases specified) based on the Number Of Valid Characters In Phase Code defined
 in JC Company Parameters. In other words, a submittal will be generated for each phase
 code for which the valid part of phase differs. For example, if the valid part of phase
 code is 5:

03110-100-001 > Submittal #1
03110-100-002 Submittal #1
03112-100-001 Submittal #2

## Beginning/Ending Phase

Indicate the phase with which to begin and end the submittal
 initialization.
Note: Only those phases within the specified range of phases that are set up for
 the submittal in PM Phase Submittals and are already set up for the job, will be
 initialized. All others will be skipped.

##  Required Receipt Date

 Specify the date that these submittals are required back from the subcontractor.

##  Required Activity Date

 Specify the date by which all activities indicated on initialized submittals are scheduled to begin.
