PKG_NAME := jdk-commons-httpclient
URL := http://archive.apache.org/dist/httpcomponents/commons-httpclient/source/commons-httpclient-3.1-src.tar.gz
ARCHIVES := http://repo.maven.apache.org/maven2/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.pom %{buildroot}

include ../common/Makefile.common
