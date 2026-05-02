import pytest
from sqlalchemy import inspect
from src.utils.database import engine

def test_star_schema_tables_exist():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    required = ["dim_products", "dim_competitors", "dim_time", "fact_market_trends", "bronze_raw_scrape"]
    for tbl in required:
        assert tbl in tables, f"Missing table: {tbl}"

def test_foreign_keys_integrity():
    inspector = inspect(engine)
    fact_fks = inspector.get_foreign_keys("fact_market_trends")
    fk_targets = {fk["referred_table"] for fk in fact_fks}
    assert {"dim_products", "dim_competitors", "dim_time"}.issubset(fk_targets), "Missing FKs in fact table"

def test_indexes_present():
    inspector = inspect(engine)
    idxs = [i["name"] for i in inspector.get_indexes("fact_market_trends")]
    assert "idx_fact_date_product" in idxs
    assert "idx_fact_competitor_price" in idxs
