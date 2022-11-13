Name:		texlive-numname
Version:	18130
Release:	1
Summary:	Convert a number to its English expression
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/numname
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numname.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numname.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package can generate cardinal (one, two, ...) and ordinal
(first, second, ...) numbers. The code derives from the memoir
class, and is extracted for the convenience of non-users of
that class.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/numname/numname.sty
%doc %{_texmfdistdir}/doc/latex/numname/README
%doc %{_texmfdistdir}/doc/latex/numname/numname.pdf
%doc %{_texmfdistdir}/doc/latex/numname/numname.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
