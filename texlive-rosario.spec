Name:		texlive-rosario
Version:	51688
Release:	2
Summary:	Using the free Rosario fonts with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rosario
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rosario.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rosario.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rosario.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the files required to use the Rosario
fonts with LaTeX. Rosario is a set of four fonts provided by
Hector Gatti, Adobe Typekit & Omnibus-Type Team under the Open
Font License (OFL), version 1.1. The fonts are copyright (c)
2012-2015, Omnibus-Type.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/rosario
%{_texmfdistdir}/tex/latex/rosario
%{_texmfdistdir}/fonts/vf/public/rosario
%{_texmfdistdir}/fonts/type1/public/rosario
%{_texmfdistdir}/fonts/tfm/public/rosario
%{_texmfdistdir}/fonts/opentype/public/rosario
%{_texmfdistdir}/fonts/map/dvips/rosario
%{_texmfdistdir}/fonts/enc/dvips/rosario
%doc %{_texmfdistdir}/doc/fonts/rosario

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
