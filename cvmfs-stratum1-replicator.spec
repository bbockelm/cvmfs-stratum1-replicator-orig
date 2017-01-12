Name:		cvmfs-stratum1-replicator
Version:	0.1
Release:	1%{?dist}
Summary:	Snapshot services for the CVMFS Stratum-1

Group:		Applications/System
License:	BSD
URL:		https://github.com/bbockelm/cvmfs-stratum1-replicator

# To generate tarball:
# git archive --format=tgz --prefix=%{name}-%{version}/ v%{version} > %{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz

%{?systemd_requires}
BuildRequires: systemd

Requires:	cvmfs-server

%description
A set of systemd-based unit files and generators for synchronizing repositories
on a CVMFS Stratum-1 server.

%prep
%setup -q

%build

%install

install -d $RPM_BUILD_ROOT/%{_unitdir}
install -d $RPM_BUILD_ROOT/usr/lib/systemd/system-generators
install -m 0644 cvmfs-snapshot.service $RPM_BUILD_ROOT%{_unitdir}/cvmfs-snapshot.service
install -m 0644 cvmfs-snapshot@.service $RPM_BUILD_ROOT%{_unitdir}/cvmfs-snapshot@.service
install -m 0644 cvmfs-snapshot@.timer $RPM_BUILD_ROOT%{_unitdir}/cvmfs-snapshot@.timer
install -m 0755 cvmfs-snapshot-generator $RPM_BUILD_ROOT/usr/lib/systemd/system-generators/cvmfs-snapshot-generator

%post
%systemd_post cvmfs-snapshot.service

%preun
%systemd_preun cvmfs-snapshot.service

%postun
%systemd_postun_with_restart cvmfs-snapshot.service


%files

%{_unitdir}/cvmfs-snapshot.service
%{_unitdir}/cvmfs-snapshot@.service
%{_unitdir}/cvmfs-snapshot@.timer
/usr/lib/systemd/system-generators/cvmfs-snapshot-generator

%changelog

