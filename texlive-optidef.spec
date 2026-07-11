%global tl_name optidef
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1
Release:	%{tl_revision}.1
Summary:	Environments for writing optimization problems
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/optidef
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/optidef.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/optidef.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small library provides a standard set of environments for writing
optimization problems. It automatically aligns the problems in three
points with an optional fourth: Beginning of the words "minimize/argmin"
and "subject to" The objective function and the longest left hand side
of the constraints. The $= | > | <$ signs of the constraints.
Optionally, the user can add manually a double align character && to
align some common constraints feature. A clear example could be the
constraints names, e.g. (boundary constraint) alignment with (dynamic
constraint). Furthermore, it provides an easy interface to define
optimization problem for three different reference situations: Where no
equation is referenced/numbered. Where the problem is referenced with a
single number. Where each equation has an individual reference. Finally,
it also allows a definition of any optimization problem without a
limitless number of constraints.

