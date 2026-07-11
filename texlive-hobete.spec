%global tl_name hobete
%global tl_revision 27036

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Unofficial beamer theme for the University of Hohenheim
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/hobete
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hobete.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hobete.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a beamer theme which features the Ci colors of the
University of Hohenheim. Please note that this is not an official Theme,
and that there will be no support for it, from the University.
Furthermore there is NO relationship between the University and this
theme.

