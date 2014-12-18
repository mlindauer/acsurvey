# ACSurvey

ACSurvey is small web project to list literature regarding Algorithm Configuration and related topics, such as Hyperparameter Optimization and Global Optimization.
The website is hosted at [aclib.net/acbib/](aclib.net/acbib/)

## Submitting new papers

The website is updated and maintained by the "Research Group on Learning, Optimization, and Automated Algorithm Design" at the University of Freiburg.
However, it is pratically infeasible for us to read all papers and maybe we miss some papers sometimes.
Therefore, everyone is encouraged to submit new entries for our website. 

## Bibtex Guideline

Please follow the following guideline how to format new bibtex entries:

* bibkeys: 
    * [lastname first author]-[conference abbrevation][year][a-d] (e.g.: hutter-aaai14a)
    * proceedings (mainly in procs.bib): [acronym][year] (e.g. aaai09 for "Proceedings of the Conference on Artificial Intelligence (AAAI'09)")
* author/editor names: only first character of the first name and last name (no additional first names) (e.g. "F. Hutter and M. Lindauer")
* use crossrefs for all proceedings 
* add proceedings in proc.bib 
* don't abbreviate journal names (e.g. "ACM Transactions on Computational Logic" is good, but "ACM Trans. Comp. Log." is not)
* use "{}" as field contents delimiter (as used by dblp)
* in paper titles, enclose capital letters (other than first letter) that must not be converted to lowercase by "{" and "}" (e.g. "{SAT}" or "{P}etri Nets")
* use the Strings which are defined in lib.bib
* use "-" rather than "--" for hyphens in pages/volume/number fields and don't terminate field contents by "." (bibliography style and BibTeX will sort it out uniformly)
* never copy-paste the contents of fields from PDF files because parts may disappear (e.g. the combination "fi" is a single letter in PDF and won't show up after LaTeXing)
* the bibtex files are encoded in UTF-8

## Contact

Marius Lindauer (University of Freiburg)
lindauer@cs.uni-freiburg.de
