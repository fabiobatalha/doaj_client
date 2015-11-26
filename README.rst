doaj_client
-----------

Python Cliente library for DOAJ API

.. image:: https://travis-ci.org/fabiobatalha/doaj_client.svg
    :target: https://travis-ci.org/fabiobatalha/doaj_client
    
HowTo
-----

::
    >>> from doaj.articles import Articles
    >>> articles = Articles()
    >>> article = articles.get('255723f2f2374f1fbb8865eeb044c9d2')
    >>> article.keys()
    [u'admin', u'last_updated', u'id', u'bibjson', u'created_date']
    >>> article['bibjson']['title']
    u'Efeitos do resfriamento e aquecimento articular no desempenho funcional do ombro'
