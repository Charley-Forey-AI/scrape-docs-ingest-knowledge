---
title: "Hard Dollar Overview | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/estimating-systems/hard-dollar-overview"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/estimating-systems/hard-dollar-overview"
---

# Hard Dollar Overview

The Project Setup Hard Dollar method supports file imports
 from the Hard Dollar Estimating Office System (EOS) software.
The Job Import starting screen prompts for labor base, equipment, rental, materials,
 subcontractor, tax, supplies, other, and labor burden cost types. Labor and equipment hours
 are imported to the Job Setup file.
EOS has a cost file that is defined by the Work Breakdown Structure (WBS). This can be independent of the owner's bid item structure. The WBS is defined by an activity code that is broken down to a maximum of five levels of detail. At each level, there is an account number, which can be used to assign the Spectrum phase code. Independently, the estimator can have a pay item revenue file with the revenue information stored. (The pay item is the owner's pay item number). There is a process that allows the estimator to attach the WBS cost levels to pay items which is similar to the way that Spectrum can attach billing items to cost phases in Job Cost.
For backward compatibility, EOS has a feature that allows the estimator to copy the bid (pay) item into the Level-1 activity code of the WBS. This gives the linkage to the cost breakdown that the previous version had (if prior to version 99.04).
EOS has general overhead items that are user-defined. These general overhead items have an account number that can be assigned as the phase; Project Setup does import these items. EOS also has three cost classifications: labor burden, supplies, and other costs. These are brought across in the direct cost file format.
Cost Accounts must be set up in the Hard Dollar cost account library. If a cost account is used that is not maintained in the library, the system displays a message that it is not in the library. (The cost account will remain on the spreadsheet.) However, when the BUDGET.TXT file is created, that cost account will not be included on the export.

Related information

- [Project Setup Installation for Hard Dollar](/en/spectrum/spectrum/project-management/project-setup/estimating-systems/hard-dollar-overview/project-setup-installation-for-hard-dollar)
