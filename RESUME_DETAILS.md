# 📄 Executive Resume & Interview Master Guide
## Project: Retail Customer Intelligence & Retention Engine

---

## 1. Ready-to-Paste Resume Bullet Points

### Option A: Standard 4-Bullet Format (Recommended for 1-Page DS / ML / Analytics Resumes)

**Retail Customer Analytics & Retention Engine | End-to-End Machine Learning System**
*Python, Scikit-learn, K-Means, PCA, Streamlit, Pandas, CI/CD, Git, GitHub* | [Live Web App](https://kumarvivek-customer-segmentation-retention.streamlit.app) | [GitHub](https://github.com/kumarvivek321/customer-segmentation-retention)
- **Engineered an end-to-end customer analytics pipeline** processing 541K+ retail transactions across 37 countries, isolating £8.29M net revenue from returns/cancellations and identifying £1.44M (14.8%) in guest-checkout revenue leakage.
- **Implemented a hybrid segmentation framework** combining a 7-tier hierarchical RFM rule engine with Scaled K-Means ($k=4$) and PCA dimensionality reduction; identified top 23% of customers (Champions/Loyalists) generating >68% of net revenue.
- **Developed a 13-month triangular cohort retention matrix** and 30/60/90-day second-purchase velocity models, pinpointing an initial M1 drop to 22% retention and generating an automated 90-day inactivity watchlist to mitigate customer churn.
- **Productionized and deployed an interactive 7-view Streamlit Cloud application** with real-time segment inference, strategic retention playbooks, and continuous deployment (CI/CD) integrated via GitHub.

---

### Option B: Comprehensive 5-Bullet Format (For Senior / Lead / Dedicated ML Engineer Profiles)

**E-Commerce Customer Segmentation & Retention Intelligence Platform**
*Python, Scikit-learn, K-Means, PCA, Seaborn, Streamlit, Automated CI/CD* | [Live App](https://kumarvivek-customer-segmentation-retention.streamlit.app) | [GitHub](https://github.com/kumarvivek321/customer-segmentation-retention)
- **Data Engineering & Audit**: Designed a modular ETL pipeline processing 541,900+ raw transactions across 4,370+ global customers; filtered administrative overhead codes and conducted data-quality audits exposing 135K unauthenticated transactions worth £1.44M.
- **Unsupervised Machine Learning**: Applied log-transformation and feature scaling on Recency, Frequency, and Monetary metrics; evaluated optimal cluster count using Elbow and Silhouette metrics ($k=4$), validated by 2D Principal Component Analysis (PCA).
- **Hierarchical Business Segmentation**: Established a 7-tier RFM behavioral scoring engine (Champions, Loyal, At-Risk, Hibernating, etc.), surfacing a Pareto concentration where 22.8% of the customer base accounts for £5.8M+ in revenue.
- **Cohort Retention & Churn Prevention**: Modeled month-over-month customer lifecycle decay via triangular heatmaps; engineered an automated 90-day inactivity watchlist to trigger targeted re-engagement campaigns before permanent churn.
- **Enterprise Web App & CI/CD**: Built a production 7-view Streamlit dashboard with custom CSS and live segment inference; deployed to Streamlit Cloud with automated Git push-to-deploy CI/CD and sub-3-second load times.

---

### Option C: Compact 2-Bullet Format (For Space-Constrained Resumes)

**Retail Customer Segmentation & Retention Engine** | [Live App](https://kumarvivek-customer-segmentation-retention.streamlit.app) | *Python, Scikit-Learn, Streamlit*
- Built an end-to-end customer intelligence system on 541K+ global transactions, combining 7-tier RFM segmentation, Scaled K-Means ($k=4$), and PCA to uncover customer tiers driving >68% of £8.29M net revenues.
- Modeled 13-month triangular cohort retention matrices and built a 90-day churn risk watchlist inside an interactive 7-page Streamlit application deployed via CI/CD.

---

## 2. Key Metrics & Business Impact (Numbers to Memorize)

| Metric | Exact Value | Business Significance |
| :--- | :--- | :--- |
| **Transaction Volume** | **541,909 records** | Enterprise-scale transaction dataset across 37 international countries |
| **Gross / Net Revenue** | **£8.91M Gross / £8.29M Net** | Cleaned cancellations (prefix 'C') and £614K in refunds/adjustments |
| **Revenue Leakage Audited** | **£1.44M (14.8% of volume)** | 135,080 guest transactions without CustomerID — key business case for account creation incentives |
| **Customer Base** | **4,372 identified accounts** | Analyzed across Recency, Frequency, and Monetary parameters |
| **Pareto Concentration** | **Top 22.8% $\rightarrow$ 68.4% Revenue** | Champions & Loyalists drive majority of store profitability |
| **Retention Decay** | **Month 1 Drop to ~22%** | Demonstrates the critical need for 30-day onboarding campaigns |
| **Inactivity Threshold** | **90-Day Dormancy Rule** | Catches high-value churn risks before customer lifetime loss |

---

## 3. ATS Technical & Business Keywords (To Include in Skills Section)

- **Machine Learning & Stats**: K-Means Clustering, Principal Component Analysis (PCA), Feature Scaling, Log-Transformation, Silhouette Score, Elbow Method, RFM Segmentation, Cohort Analysis, Customer Lifetime Value (CLV).
- **Languages & Frameworks**: Python 3.11+, Pandas, NumPy, Scikit-Learn, Streamlit, Matplotlib, Seaborn, Flask.
- **Software Engineering**: Modular Pipeline Architecture, Object Serialization (`dill`/`joblib`), Custom Logging & Exception Handling, Unit Testing, Setup packaging (`setup.py`).
- **DevOps & Cloud**: Git, GitHub, Streamlit Cloud, Continuous Integration / Continuous Deployment (CI/CD), Data Compression (`gzip`).
- **Domain Competencies**: E-Commerce Analytics, Churn Prevention, Repeat Purchase Velocity, Customer Segmentation, Data Quality Auditing.

---

## 4. The 30-Second Interview Elevator Pitch

> *"In this project, I built an end-to-end Customer Intelligence and Retention Engine analyzing over 540,000 international e-commerce transactions across 37 countries.*
> 
> *The core business problem was two-fold: high revenue leakage from guest checkouts and lack of visibility into customer retention decay. I engineered a modular machine learning pipeline combining a 7-tier hierarchical RFM engine with Scaled K-Means and PCA, proving that the top 23% of customers generate over 68% of the company's net revenue.*
> 
> *I also built a triangular cohort retention matrix and a 90-day inactivity watchlist to trigger re-engagement before churn. Finally, I deployed the complete solution as a production 7-view interactive dashboard on Streamlit Cloud with automated CI/CD."*

---

## 5. STAR Method Interview Deep-Dives

### Q1: "Walk me through how you handled data quality and transaction grain."
- **Situation**: The raw dataset had 541,909 records with mixed transaction types (sales, returns, administrative fees, and guest checkouts).
- **Task**: Standardize the grain into distinct purchase vs. refund views without leaking duplicate revenue or skewing customer profiles.
- **Action**: 
  1. Identified and removed non-product stock codes (`POST`, `D`, `BANK CHARGES`, `CRUK`).
  2. Isolated genuine refunds (Invoice prefix 'C' or negative quantities) from positive sales.
  3. Audited 135K unauthenticated rows missing `CustomerID`, quantifying £1.44M in untracked guest revenue.
  4. Aggregated at customer grain for RFM modeling while preserving line-item grain for basket analytics.
- **Result**: Delivered 100% auditable metrics: £8.91M gross sales, £614K returns, and £8.29M clean net revenue across 4,372 validated customers.

### Q2: "Why did you use both Rule-Based RFM and Unsupervised K-Means?"
- **Answer**: 
  *"Rule-based RFM gives deterministic, actionable business tiers that marketing and CRM teams instantly understand (e.g., Champions, At-Risk, Hibernating). However, rules are heuristic and can create arbitrary boundary cutoffs.*
  *To validate and uncover natural data clusters, I trained an unsupervised K-Means model on log-transformed and standardized Recency, Frequency, and Monetary features, using PCA for 2D variance inspection. The K-Means clusters closely mapped to our RFM tiers, proving our business rules aligned with the underlying statistical distribution of customer behavior."*

### Q3: "How does the Cohort Retention analysis create tangible business value?"
- **Answer**: 
  *"Acquiring a new customer costs 5x to 7x more than retaining an existing one. By building a triangular cohort matrix tracking 13 months, we uncovered that retention drops sharply to ~22% by Month 1, but stabilizes thereafter. Furthermore, 30/60/90-day second-purchase velocity showed that 50%+ of repeat buyers return within 45 days.*
  *This insight transformed marketing strategy: instead of generic discounts, we established a 30-day post-purchase welcome sequence and an automated 90-day inactivity watchlist targeting high-value customers at immediate churn risk."*
