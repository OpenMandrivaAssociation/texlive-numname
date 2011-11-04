# revision 18130
# category Package
# catalog-ctan /macros/latex/contrib/numname
# catalog-date 2010-05-03 00:02:21 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-numname
Version:	20100503
Release:	1
Summary:	Convert a number to its English expression
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/numname
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numname.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numname.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package can generate cardinal (one, two, ...) and ordinal
(first, second, ...) numbers. The code derives from the memoir
class, and is extracted for the convenience of non-users of
that class.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/numname/numname.sty
%doc %{_texmfdistdir}/doc/latex/numname/README
%doc %{_texmfdistdir}/doc/latex/numname/numname.pdf
%doc %{_texmfdistdir}/doc/latex/numname/numname.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
