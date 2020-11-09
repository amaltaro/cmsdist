### RPM external py2-zsi 2.0
## INITENV +PATH PYTHONPATH %i/${PYTHON_LIB_SITE_PACKAGES}

#Source: http://switch.dl.sourceforge.net/sourceforge/pywebsvcs/ZSI-%{realversion}.tar.gz
Source: https://sourceforge.net/projects/pywebsvcs/files/ZSI/ZSI-%{realversion}/ZSI-%{realversion}.tar.gz/download
Requires: python py2-pyxml

%prep 
%setup -n ZSI-%{realversion}

%build
python setup.py build

%install
mkdir -p %i/$PYTHON_LIB_SITE_PACKAGES
PYTHONPATH=%i/$PYTHON_LIB_SITE_PACKAGES:$PYTHONPATH \
python setup.py install --prefix=%i
find %i -name '*.egg-info' -exec rm {} \;
for f in %i/bin/wsdl2*; do perl -p -i -e 's{.*}{#!/usr/bin/env python} if $. == 1 && m{#!.*/bin/python}' $f; done
