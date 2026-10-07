paper_crawler
=============

Supplementary code for the position paper
`More Rigorous Software Engineering Would Improve Reproducibility in Machine Learning Research
<https://arxiv.org/abs/2502.00902>`_.

Installation
------------

.. code-block:: bash

   pip install .

Create a ``.env`` file with your OpenReview credentials:

.. code-block:: bash

   PYTHONPATH=.
   OPENREVIEW_USERNAME=YOUR_OPENREVIEW_ACCOUNT_NAME
   OPENREVIEW_PASSWORD=YOUR_PASSWORD

The Selenium crawler requires an installed Chrome browser.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   api
   citation