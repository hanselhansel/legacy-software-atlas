"""Lane M (plan 3): app-store ratings and review windows from iTunes.

``itunes`` wraps the two keyless endpoints (lookup + customer-reviews
RSS), ``collect`` turns ``research/apps.csv`` rows into
``data/derived/apps.parquet`` and ``app_reviews`` items, and ``cli``
registers the ``lsa apps`` command.
"""
