---
title: "About the Agreement Status | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-the-agreement-status"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-the-agreement-status"
---

# About the Agreement Status

The status of an agreement can change several times during the agreement's life cycle, and is updated automatically by the system based on agreement activity.
The Current Status field in SM Agreements shows the overall status of the agreement. It does not impact the status of revisions; it only reflects the status of the agreement for the current date based on the status of the revision that covers the current date. If the revision is active, the Current Status will be Active. If there are no revisions that are active for the agreement (that is, all revisions are in a Quote, Terminated, or Expired status), the Current Status will be Inactive.
If you enter and activate a new agreement and the effective date is in the future, the revision status is set to Active; however, the Current Status remain as Inactive until the effective date is reached, at which time it becomes Active.
If you activate a renewal for an agreement that is Active, the Current Status is set to Active, regardless of the Effective Date of the renewal. This is because the current date either falls within the terms of the current Active revision or the renewal revision. The only time this is not true is if there is a lapse between the Expiration Date of the Active revision and the Effective Date of the renewal (for example, the Expiration Date for the current revision is July 31, 2019 and the renewal has an Effective Date of September 1, 2019). In which case, the Current Status changes to Inactive once the current revision expires and then back to Inactive when the renewal Effective Date is reached.
If the renewal is for an agreement that has already expired, the Current Status remains as Inactive until the renewal Effective Date is reached.
You can only generate Amendments for active agreements; therefore, if the Effective Date for an amendment is in the future, the Current Status remains Active until the new Effective Date is reached.
