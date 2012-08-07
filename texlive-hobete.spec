# revision 27036
# category Package
# catalog-ctan /macros/latex/contrib/beamer-contrib/hobete
# catalog-date 2012-06-26 15:55:21 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-hobete
Version:	20120626
Release:	1
Summary:	Unofficial beamer theme for the University of Hohenheim
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/hobete
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hobete.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hobete.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a beamer theme which features the Ci
colors of the University of Hohenheim. Please note that this is
not an official Theme, and that there will be no support for
it, from the University. Furthermore there is NO relationship
between the University and this theme.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hobete/beamercolorthemehohenheim.sty
%{_texmfdistdir}/tex/latex/hobete/beamerouterthemehohenheim.sty
%{_texmfdistdir}/tex/latex/hobete/beamerouterthemehohenheimposter.sty
%{_texmfdistdir}/tex/latex/hobete/beamerthemehohenheim.sty
%{_texmfdistdir}/tex/latex/hobete/hobete.sty
%doc %{_texmfdistdir}/doc/latex/hobete/README
%doc %{_texmfdistdir}/doc/latex/hobete/hobete_doc.pdf
%doc %{_texmfdistdir}/doc/latex/hobete/hobete_doc.tex
%doc %{_texmfdistdir}/doc/latex/hobete/poster-test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
