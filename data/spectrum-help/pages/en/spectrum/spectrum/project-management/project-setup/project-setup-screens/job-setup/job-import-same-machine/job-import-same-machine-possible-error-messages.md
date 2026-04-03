---
title: "Job Import, Same Machine, Possible Error Messages | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/job-import-same-machine/job-import-same-machine-possible-error-messages"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/job-import-same-machine/job-import-same-machine-possible-error-messages"
---

# Job Import, Same Machine, Possible Error Messages

PROIV will run the BIDCONVT program, so any errors from that program are possible here. Subsequently, PROIV uses the DOS "copy" command to copy the converted file into the user's PROIV data directory. A DOS/XENIX/UNIX "copy" error displays if the transfer file does not exist.
If an error should occur, the system attempts to abort the update. However, in some situations PROIV will be unable to detect that there was an error and will proceed with the update (DOS commands in particular do not seem to return error codes to PROIV). This is completely harmless; after the user has corrected the problem the import can be repeated with the same Spectrum job number.
If a "file not found error" occurs:

- Exit PROIV

- Insert the transfer file disk in drive A:.

- For UNIX, at the $ type "dosdir A:" and press RETURN; for DOS, type "dir A:" and press RETURN.

- Verify that the file BIDSUM.XXX (XXX = summary number to be imported) actually exists on the disk. If that file is not on the disk, the conversion program BIDCONVT must be run again before proceeding. If the file is on the disk, then verify that the disk was actually placed in drive A: when the import was attempted.

- Log back into PROIV and repeat the Project Setup import procedures.
