`GoTo School @ Summer 2016 <http://goto.msk.ru/school/>`_ baseline
------------------------------------------------------------------

|goto-ru| |apache-2| |mit|

Using
=====

Preparing environment
#####################

.. code:: sh

        git clone $project
        cd $project

        virtualenv devenv
        source devenv/bin/activate

        make deps

        make download_data extract_data


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

