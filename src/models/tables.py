# src/models/tables.py
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, ForeignKey, Index, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# ───────── BRONZE LAYER (Raw Ingestion Staging) ─────────
class BronzeRawScrape(Base):
    __tablename__ = "bronze_raw_scrape"
    id = Column(Integer, primary_key=True, autoincrement=True)
    source_url = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    raw_payload = Column(Text, nullable=False)  # JSON/String blob
    ingested_at = Column(DateTime, nullable=False)
    status = Column(String, default="pending")  # pending, processed, failed

# ───────── DIMENSION TABLES (Star Schema) ─────────
class DimProduct(Base):
    __tablename__ = "dim_products"
    product_key = Column(Integer, primary_key=True, autoincrement=True)
    product_id_ext = Column(String, unique=True, nullable=False)  # External ID from scraper
    product_name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    brand = Column(String, nullable=True)
    url = Column(String, nullable=False)

class DimCompetitor(Base):
    __tablename__ = "dim_competitors"
    competitor_key = Column(Integer, primary_key=True, autoincrement=True)
    competitor_id_ext = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    profile_url = Column(String, nullable=True)

class DimTime(Base):
    __tablename__ = "dim_time"
    date_key = Column(Integer, primary_key=True)  # Format: YYYYMMDD
    full_date = Column(Date, unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    week = Column(Integer, nullable=False)
    quarter = Column(Integer, nullable=False)
    day_of_week = Column(String, nullable=False)

# ───────── FACT TABLE (Analytical Core) ─────────
class FactMarketTrends(Base):
    __tablename__ = "fact_market_trends"
    trend_id = Column(Integer, primary_key=True, autoincrement=True)
    
    product_key = Column(Integer, ForeignKey("dim_products.product_key"), nullable=False)
    competitor_key = Column(Integer, ForeignKey("dim_competitors.competitor_key"), nullable=False)
    date_key = Column(Integer, ForeignKey("dim_time.date_key"), nullable=False)
    
    price = Column(Float, nullable=False)
    discount_pct = Column(Float, nullable=True)
    sentiment_score = Column(Float, nullable=False)  # -1.0 to 1.0
    review_volume = Column(Integer, default=0)
    
    # Indexes for analytical query performance (SRS NFR-2)
    __table_args__ = (
        Index("idx_fact_date_product", "date_key", "product_key"),
        Index("idx_fact_competitor_price", "competitor_key", "price"),
    )
