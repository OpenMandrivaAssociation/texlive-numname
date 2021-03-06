# revision 18130
# category Package
# catalog-ctan /macros/latex/contrib/numname
# catalog-date 2010-05-03 00:02:21 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-numname
Version:	20190228
Release:	1
Summary:	Convert a number to its English expression
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/numname
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numname.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numname.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100503-2
+ Revision: 754449
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100503-1
+ Revision: 719143
- texlive-numname
- texlive-numname
- texlive-numname

