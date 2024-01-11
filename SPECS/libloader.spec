Name: libloader
Version: 1.1.3
Release: 32%{?dist}
Summary: Resource Loading Framework
License: LGPLv2
#Original source: http://downloads.sourceforge.net/jfreereport/%%{name}-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: %{name}-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant, java-devel, jpackage-utils
BuildRequires: libbase >= 1.1.3
Requires: java-headless, jpackage-utils, libbase >= 1.1.3
BuildArch: noarch
Patch0: libloader-1.1.2.build.patch
Patch1: libloader-1.1.2.java11.patch
Patch2: libloader-1.1.3-remove-antcontrib-support.patch
Patch3: libloader-1.1.3-remove-commons-logging.patch

%description
LibLoader is a general purpose resource loading framework. It has been
designed to allow to load resources from any physical location and to
allow the processing of that content data in a generic way, totally
transparent to the user of that library.

%package javadoc
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
%patch1 -p1 -b .java11
%patch2 -p1 -b .no_antcontrib
%patch3 -p1 -b .no_commons_logging

find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib libbase
cd lib
ln -s /usr/share/java/ant ant-contrib

%build
ant jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.1.3-32
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Apr 27 2021 Caolán McNamara <caolanm@redhat.com> - 1.1.3-31
- Remove ant-contrib support dropped compile.res_copy target so
  .properties files didn't get included in the jar so libloader
  didn't use its built-in loaders so libreoffice's database
  report generator didn't work

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.1.3-30
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937
- Related: rhbz#1951284 replace apache-commons-logging with java.util.logging

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Nicolas Lécureuil <neoclust@mageia.org> - 1.1.3-28
- Remove ant-contrib support

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Caolán McNamara <caolanm@redhat.com> - 1.1.3-26
- Related: rhbz#1858035 build in side-tag

* Fri Jul 17 2020 Caolán McNamara <caolanm@redhat.com> - 1.1.3-25
- Resolves: rhbz#1858035 disable failing javadoc parts

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.1.3-24
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue May 05 2020 Caolán McNamara <caolanm@redhat.com> - 1.1.3-23
- allow rebuild with java 11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Stephan Bergmann <sbergman@redhat.com> - 1.1.3-20
- Use /usr/share/java instead of _javadir macro for build dependencies

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Caolán McNamara <caolanm@redhat.com> - 1.1.3-11
- Resolves: rhbz#1068358 Switch to java-headless (build)requires

* Wed Oct 23 2013 Caolán McNamara <caolanm@redhat.com> - 1.1.3-10
- Resolves: rhbz#1022134 remove versioned jars

* Tue Aug 06 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.1.3-9
- Fix bogus date in %%changelog
- ant-nodeps is dropped from ant-1.9.0-2 build in rawhide
- Drop buildroot, %%clean, %%defattr and removal of buildroot in %%install

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 03 2012 Caolán McNamara <caolanm@redhat.com> - 1.1.3-6
- repack source to remove bundled multi-license .jars

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Caolán McNamara <caolanm@redhat.com> 1.1.3-3
- Related: rhbz#749103 drop gcj aot

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 02 2009 Caolan McNamara <caolanm@redhat.com> 1.1.3
- latest version

* Tue Nov 17 2009 Caolan McNamara <caolanm@redhat.com> 1.1.2
- latest version

* Fri Jul 24 2009 Caolan McNamara <caolanm@redhat.com> 1.0.0-2.OOo31
- make javadoc no-arch when building as arch-dependant aot

* Mon Mar 16 2009 Caolan McNamara <caolanm@redhat.com> 1.0.0-1.OOo31
- Post release tuned for OpenOffice.org reportbuilder

* Mon Mar 09 2009 Caolan McNamara <caolanm@redhat.com> 0.4.0-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 07 2008 Caolan McNamara <caolanm@redhat.com> 0.3.7-1
- initial fedora import
