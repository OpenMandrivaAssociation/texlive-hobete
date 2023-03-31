Name:		texlive-hobete
Version:	27036
Release:	2
Summary:	Unofficial beamer theme for the University of Hohenheim
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/hobete
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hobete.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hobete.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
