### RPM cms cmssw CMSSW_4_2_10
Requires: cmssw-tool-conf python cms-git-tools

%define runGlimpse      yes
%define useCmsTC        yes
%define saveDeps        yes
%define branch          CMSSW_4_2_X
%define source1         git://github.com/cms-sw/cmssw.git?protocol=https&obj=%{branch}/CMSSW_4_2_8_lowpupatch1&module=%{cvssrc}&export=%{srctree}&output=/src.tar.gz

## IMPORT scram-project-build
