Name     : jdk-commons-httpclient
Version  : 3.1
Release  : 1
URL      : http://archive.apache.org/dist/httpcomponents/commons-httpclient/source/commons-httpclient-3.1-src.tar.gz
Source0  : http://archive.apache.org/dist/httpcomponents/commons-httpclient/source/commons-httpclient-3.1-src.tar.gz
Source1  : http://repo.maven.apache.org/maven2/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : apache-ant
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-logging
BuildRequires : jdk-junit4
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : lxml
BuildRequires : xmvn
#BuildRequires : 
BuildRequires : apache-maven
BuildRequires : xmvn
BuildRequires : openjdk-dev
BuildRequires : javapackages-tools
BuildRequires : python3
BuildRequires : six
BuildRequires : lxml
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-guice
BuildRequires : jdk-guava
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-wagon
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-sisu
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-slf4j
Patch0   : jakarta-commons-httpclient-disablecryptotests.patch
Patch1   : jakarta-commons-httpclient-addosgimanifest.patch
Patch2   : jakarta-commons-httpclient-encoding.patch
Patch3   : jakarta-commons-httpclient-CVE-2012-5783.patch
Patch4   : jakarta-commons-httpclient-CVE-2014-3577.patch
Patch5   : jakarta-commons-httpclient-CVE-2015-5262.patch

%description
Jakarta HttpClient
===========================
Welcome to the HttpClient component of the Jakarta HttpComponents project.

%prep
%setup -q -n commons-httpclient-3.1
mkdir lib
rm -rf docs/apidocs docs/*.patch docs/*.orig docs/*.rej

%patch0
pushd src/conf
%patch1
popd
%patch2
%patch3 -p2
%patch4 -p1
%patch5 -p1

# Use javax classes, not com.sun ones
# assume no filename contains spaces
pushd src
    for j in $(find . -name "*.java" -exec grep -l 'com\.sun\.net\.ssl' {} \;); do
        sed -e 's|com\.sun\.net\.ssl|javax.net.ssl|' $j > tempf
        cp tempf $j
    done
    rm tempf
popd

python3 /usr/share/java-utils/mvn_alias.py : apache:commons-httpclient
python3 /usr/share/java-utils/mvn_file.py ":{*}" jakarta-@1 "@1" commons-httpclient3

%build
ant \
  -Dbuild.sysclasspath=first \
  -Djavadoc.j2sdk.link=/usr/share/javadoc/java \
  -Djavadoc.logging.link=/usr/share/javadoc/jakarta-commons-logging \
  -Dtest.failonerror=false \
  -Dlib.dir=/usr/share/java \
  -Djavac.encoding=UTF-8 \
  dist test

%install
python3 /usr/share/java-utils/mvn_artifact.py %{SOURCE1} dist/commons-httpclient.jar

xmvn-install  -R .xmvn-reactor -n jakarta-commons-httpclient -d %{buildroot} 

%files
%defattr(-,root,root,-)
/usr/share/java/commons-httpclient.jar
/usr/share/java/commons-httpclient3.jar
/usr/share/java/jakarta-commons-httpclient.jar
/usr/share/maven-metadata/jakarta-commons-httpclient.xml
/usr/share/maven-poms/commons-httpclient.pom
/usr/share/maven-poms/commons-httpclient3.pom
/usr/share/maven-poms/jakarta-commons-httpclient.pom
