
CVMFS Stratum-1 Replicator
==========================

This is a relatively simple set of systemd units that keep a Stratum-1 up-to-date.

- `cvmfs-snapshot.service`: The top-level service for all snapshotting activity.
- `cvmfs-snapshot@.service`: The template for individual snapshot jobs.
- `cvmfs-snapshot@.timer`: The template for individual snapshot timers.
- `cvmfs-snapshot-generator`: Generates one tempalted snapshot service/timer per installed repo.
- `cvmfs-stratum1-replicator.spec`: RPM spec file.

To use, copy files into a tarball and build/install the RPM.  Then, enable the cvmfs-snapshot service:

```
systemctl enable cvmfs-snapshot
systemctl start cvmfs-snapshot
```

The second line will enable one unit per repo.  To stop snapshots, disable the top-level service:

```
systemctl stop cvmfs-snapshot
```

Overriding Defaults
-------------------

By default, we check for updates every 20s; this is relatively aggressive.  To adjust the defaults,
create a file `/etc/systemd/system/cvmfs-snapshot@.timer.d/10-increase-timer.conf` with the following contents:

```
[Timer]
OnUnitInactiveSec=30s
```

Reload systemd and restart the services:

```
systemctl daemon-reload
systemctl restart cvmfs-snapshot
```

