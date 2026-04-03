---
title: "Timberline Precision Estimating Setup | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/estimating-systems/project-setup-timberline-overview/timberline-precision-estimating-setup"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/estimating-systems/project-setup-timberline-overview/timberline-precision-estimating-setup"
---

# Timberline Precision Estimating Setup

This Project Setup module can be used to link a
 non-Spectrum estimating program to the Spectrum Construction Management software.
Important: Note that one may need access to the Timberline
 Estimating Standards Password to make any of these changes. This password would be
 something set up by the Timberline Estimating database administrator / chief
 estimator.

## To specify the job cost interface type for an existing database

- Launch Sage Timberline Office Estimating Tools.

- Click Setup  >  Change Job Cost
 Information.

- Locate and select the database folder and from it double-click
 the .dat file. The Change
 Job Cost Information screen displays.

- In the Job cost
 interface type drop-down list, select text or Sage Timberline Office:

- The Text option does not give you any descriptions (descriptions
 will be assigned during the Spectrum import using the standard Spectrum phase
 descriptions that are setup in the Project Setup module).

- The Sage
 Timberline Office format does give you the descriptions that are
 setup in the Estimating system and these will then be in the import file. If
 these descriptions are in the import file then they will be used during the
 import.

- In the Job Cost
 Categories section, complete the label entries exactly as shown. The Timberline categories MUST be hard coded to the Timberline
 Labels without regard to how the cost types are defined in Timberline.

The Addons and Deducts may also need to be adjusted in Timberline Estimating. The Standards password is needed to do this.

- Open the Addon/Deduct menu option under Database and select the item that
 needs to be changed.

- Click Job
 Cost and type the Category Description, which is "OTH" in this case.

Related information

- [Export Timberline Estimating File to a Text File](/en/spectrum/spectrum/project-management/project-setup/estimating-systems/project-setup-timberline-overview/export-timberline-estimating-file-to-a-text-file)
