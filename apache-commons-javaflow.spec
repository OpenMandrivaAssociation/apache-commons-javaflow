%{?_javapackages_macros:%_javapackages_macros}
%global base_name  javaflow
%global short_name commons-%{base_name}
%global namedreltag -SNAPSHOT
%global namedversion %{version}%{?namedreltag}
Name:          apache-commons-javaflow
Version:       1.0
Release:       0.6.20120509SNAPSHOT.0%{?dist}
Summary:       Commons Javaflow
License:       ASL 2.0
Url:           http://commons.apache.org/sandbox/javaflow/
# svn export http://svn.apache.org/repos/asf/commons/sandbox/javaflow/trunk/  commons-javaflow-1.0-SNAPSHOT
# tar czf commons-javaflow-1.0-SNAPSHOT-src-svn.tar.gz commons-javaflow-1.0-SNAPSHOT
Source0:       %{short_name}-%{namedversion}-src-svn.tar.gz

BuildRequires: java-devel

BuildRequires: mvn(asm:asm)
BuildRequires: mvn(asm:asm-analysis)
BuildRequires: mvn(asm:asm-commons)
BuildRequires: mvn(asm:asm-tree)
BuildRequires: mvn(asm:asm-util)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.bcel:bcel)
BuildRequires: mvn(org.apache.commons:commons-jci-core)

# test deps
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(junit-addons:junit-addons)

BuildRequires: maven-local
#BuildRequires: maven-antrun-plugin
#BuildRequires: maven-plugin-bundle
#BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-provider-junit4

BuildArch:     noarch

%description
Sometimes it is useful if we can capture the state of the application,
its stack of function calls, which includes local variables, the global
variables and the program counter, and save them into an object. If
this object would give us the ability to restart the processing from
the point stored in it.
A continuation is exactly the type of object that we need. Think of a
continuation as an object that, for a given point in your program,
contains a snapshot of the stack trace, including all the local
variables, and the program counter. You can not only store these
things in the continuation object, but also restore the execution
of the program from a continuation object. This means that the stack
trace and the program counter of the running program become the ones
stored in a continuation.
Continuations are powerful concepts from the world of functional
languages, like Scheme, but they are becoming popular in other
languages as well.

%package ant
Summary:       Development files for Commons Javaflow
Requires:      ant
Requires:      %{name} = %{version}-%{release}

%description ant
This package enables support for the Commons Javaflow ant tasks.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{namedversion}
find . -name "*.class" -delete
find . -name "*.jar" -delete

%pom_remove_parent
#sed -i "s|commons-sandbox-parent|commons-parent|" pom.xml
%pom_xpath_inject "pom:project" "<groupId>org.apache.commons</groupId>"

%build

%mvn_file :%{short_name} %{name}
%mvn_file :%{short_name} %{short_name}
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant %{short_name}" > %{short_name}
install -p -m 644 %{short_name} %{buildroot}%{_sysconfdir}/ant.d/%{short_name}

%files -f .mfiles
%doc CREDITS.txt LICENSE.txt NOTICE.txt TODO.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%files ant
%config(noreplace) %{_sysconfdir}/ant.d/%{short_name}

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.20120509SNAPSHOT
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 gil cattaneo <puntogil@libero.it> 1.0-0.5.20120509SNAPSHOT
- switch to XMvn
- minor changes to adapt to current guideline

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.20120509SNAPSHOT
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-0.3.20120509SNAPSHOT
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.20120509SNAPSHOT
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 09 2012 gil cattaneo <puntogil@libero.it> 1.0-0.1.20120509SNAPSHOT
- initial rpm