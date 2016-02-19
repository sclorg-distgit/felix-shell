%global pkg_name felix-shell
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global project felix
%global bundle org.apache.felix.shell

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.4.3
Release:        5.9%{?dist}
Summary:        Apache Felix Shell Service

License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://archive.apache.org/dist/%{project}/%{bundle}-%{version}-source-release.tar.gz

BuildArch: noarch

BuildRequires: %{?scl_prefix_java_common}javapackages-tools
BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: maven30-felix-osgi-core
BuildRequires: maven30-felix-osgi-compendium
BuildRequires: maven30-maven-clean-plugin
BuildRequires: maven30-maven-plugin-bundle
BuildRequires: maven30-felix-parent


%description
A simple OSGi command shell service.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -n %{bundle}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x

%pom_remove_plugin org.codehaus.mojo:rat-maven-plugin

%mvn_file : %{project}/%{bundle}
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
 
%{?scl:EOF}
%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.4.3-5.9
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.4.3-5.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.4.3-5.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.3-5.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.3-5.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.3-5.4
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.3-5.3
- Remove requires on java

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.3-5.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.3-5.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4.3-5
- Mass rebuild 2013-12-27

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 1.4.3-4
- Migrate away from mvn-rpmbuild (Resolves: #997489)

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.3-3
- Remove workaround for rpm bug #646523

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.3-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 15 2013 Mat Booth <fedora@matbooth.co.uk> - 1.4.3-1
- Update to latest upstream version rhbz #895405.
- Enable tests

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4.2-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 06 2012 Hui Wang <huwang@redhat.com> - 1.4.2-6
- Bug 810214

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 02 2010 Hui Wang <huwang@redhat.com> - 1.4.2-3
- Fix source0
- Remove "rm -rf target/site/api/*"

* Fri Jul 30 2010 Hui Wang <huwang@redhat.com> - 1.4.2-2
- Add LICENSE to javadoc subpackage
- Use upstream source tarball
- Fix directory that owned by other package in files section

* Fri Jun 25 2010 Hui Wang <huwang@redhat.com> - 1.4.2-1
- Initial version of the package
