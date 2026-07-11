%global tl_name numname
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Convert a number to its English expression
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/numname
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/numname.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/numname.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package can generate cardinal (one, two, ...) and ordinal (first,
second, ...) numbers. The code derives from the memoir class, and is
extracted for the convenience of non-users of that class.

