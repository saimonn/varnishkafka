Name:           varnishkafka
Version:        1.0.11_c2c_r2
Release:        1%{?dist}
Summary:        Varnish log collector with Apache Kafka integration.

Group:          admin
License:        Wikimedia
URL:            https://github.com/camptocamp/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  git
BuildRequires:  varnish-libs-devel, librdkafka-devel, yajl-devel, ghc-zlib-devel


%description
Varnish log collector with Apache Kafka integration.

%prep
%setup -q

%build
make %{?_smp_mflags} VER=%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/*



%changelog
