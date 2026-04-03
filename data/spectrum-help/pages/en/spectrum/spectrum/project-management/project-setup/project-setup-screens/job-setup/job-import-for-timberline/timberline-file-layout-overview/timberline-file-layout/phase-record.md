---
title: "Phase Record | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/job-import-for-timberline/timberline-file-layout-overview/timberline-file-layout/phase-record"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/job-import-for-timberline/timberline-file-layout-overview/timberline-file-layout/phase-record"
---

# Phase Record

Note regarding Phase Codes:
Phase codes for Equipment, Labor, Materials, Subcontract and Other must be entered as three characters as follows:

## EQU = Equipment

## LAB = Labor

## MAT = Materials

## SUB = Subcontract

## OTH = Other

When imported into Spectrum, these three-digit codes will be converted into single-digit cost types (E, L, M, S, O). Any unrecognized phase codes will automatically be converted to O.
Field Name
Type
Description
Length

RECTYPE
A
P to indicate a phase record type
1

PHASEID
A
Job cost phase code
15

DESCRIPTION
A
Phase description
25

CATEGORY
A
Job cost category
3

TRANDATE
N
Date file generated (mmddyyyy format)
8

QUANTITY
N
Phase quantity of item
8.2

UM
A
Unit of measure
4

NULL
A
Three null fields to match category record
0
