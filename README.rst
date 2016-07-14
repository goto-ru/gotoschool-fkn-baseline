`GoTo School @ Summer 2016 <http://goto.msk.ru/school/>`_ baseline
------------------------------------------------------------------

|goto-ru| |apache-2| |mit|

(`School announcement on habrahabr.ru <https://habrahabr.ru/company/goto/blog/305526/>`_ (in Russian), with additional school description and extended explanation of methods used.)

This repository features two baseline versions (both based on collaborative filtration): a simpler one (``baseline-simple.ipynb``) based on cosine similarity between film audiences and a more complex one (``baseline-intermediate.ipynb``) using TSVD user-item matrix decomposition.
There's also a notebook with simple examples on data manipulation (opening, mostly) with an intuitive name of ``data_manipulation.ipynb``.

The metric used is mAP@10 (NB: be sure to check the notes in the notebooks before comparing scores!).

Using
=====

.. code:: sh

        git clone $project
        cd $project

        virtualenv devenv
        source devenv/bin/activate

        make deps

        make download_data extract_data

        jupyter notebook


Licensed under Apache 2 and MIT.


.. |goto-ru| image:: https://img.shields.io/badge/GoTo-project-4bb89b.svg
        :target: https://github.com/goto-ru/
        :alt: GoTo project
.. |apache-2| image:: https://img.shields.io/badge/license-Apache%202-blue.svg
	:target: https://www.apache.org/licenses/LICENSE-2.0
	:alt: Apache 2 license
.. |mit| image:: https://img.shields.io/badge/license-MIT-blue.svg
	:target: https://opensource.org/licenses/MIT
	:alt: MIT license

