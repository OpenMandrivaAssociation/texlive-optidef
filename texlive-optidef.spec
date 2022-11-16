Name:		texlive-optidef
Version:	50941
Release:	1
Summary:	Environments for writing optimization problems
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/optidef
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/optidef.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/optidef.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small library provides a standard set of environments for
writing optimization problems. It automatically aligns the
problems in three points with an optional fourth: Beginning of
the words "minimize/argmin" and "subject to" The objective
function and the longest left hand side of the constraints. The
$= | > | <$ signs of the constraints. Optionally, the user can
add manually a double align character && to align some common
constraints feature. A clear example could be the constraints
names, e.g. (boundary constraint) alignment with (dynamic
constraint). Furthermore, it provides an easy interface to
define optimization problem for three different reference
situations: Where no equation is referenced/numbered. Where the
problem is referenced with a single number. Where each equation
has an individual reference. Finally, it also allows a
definition of any optimization problem without a limitless
number of constraints.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/optidef
%doc %{_texmfdistdir}/doc/latex/optidef

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
