paper_crawler
=============

Supplementary code for the TMLR paper
`Estimating the Adoption of Software Engineering Best Practices in Machine Learning Research
<https://openreview.net/forum?id=13ThuknGwY>`_.

Installation
------------

.. code-block:: bash

   pip install .

Create a ``.env`` file with your OpenReview credentials:

.. code-block:: bash

   PYTHONPATH=.
   OPENREVIEW_USERNAME=YOUR_OPENREVIEW_ACCOUNT_NAME
   OPENREVIEW_PASSWORD=YOUR_PASSWORD

If your account uses multi-factor authentication, run
``python scripts/openreview_token.py`` once in a terminal. It asks for your code and
stores an ``OPENREVIEW_TOKEN`` in ``.env``, which is used instead of the password.
The token expires after one week.

The Selenium crawler requires an installed Chrome browser.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   api
   citation