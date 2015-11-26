doaj_client
-----------

Python Cliente library for DOAJ API

.. image:: https://travis-ci.org/fabiobatalha/doaj_client.svg
    :target: https://travis-ci.org/fabiobatalha/doaj_client
    
HowTo
-----

Retrieving an article::

    >>> from doaj.articles import Articles
    >>> articles = Articles()
    >>> article = articles.get('255723f2f2374f1fbb8865eeb044c9d2')
    >>> article['bibjson']['title']
    u'Efeitos do resfriamento e aquecimento articular no desempenho funcional do ombro'

Retrieving articles from a search::

    >>> from doaj.articles import Articles
    >>> articles = Articles()
    >>> for art in articles.search('issn:1806-9940'):
    ...  print art['bibjson']['title'][0:30]
    ...
    Efeito da oferta dietética de
    Propriedades mecânicas do músc
    Avaliação da reprodutibilidade
    Suplementação de creatina e tr
    Incidência de lesões nos jogad
    Influência da utilização da ór
    ...
    >>>

Retrieving a journal::

    >>> from doaj.journals import Journals
    >>> journals = Journals()
    >>> journal = journals.get('022bf3ad951c4c5fa77a8279a59c437e')
    >>> journal['bibjson']['title']
    u'Revista Brasileira de Medicina do Esporte'

Retrieving journals from a search::

    >>> from doaj.journals import Journals
    >>> journals = Journals()
    >>> for j in journals.search('provider:scielo'):
    ...   print j['bibjson']['title']
    ...
    Revista de Protección Vegetal
    Brazilian Dental Journal
    Revista de Salud Animal
    RAUSP : Revista de Administração da Universidade de São Paulo
    BAR : Brazilian Administration Review
    Yesterday and Today
    ...
    >>>