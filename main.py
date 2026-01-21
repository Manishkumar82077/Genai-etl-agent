import pandas as pd
import sqlite3
import json
import sys
import os
from typing import List, Dict, Any

# ==========================================
# 1. THE GENAI AGENT
# ==========================================
def llm_generate_flattening_logic(sample_record: Dict[str, Any]) -> str:
    """Simulates LLM analyzing schema and generating transformation code."""
    print(f"\n[AGENT] 🔍 Inspecting Schema...")
    
    # Simulate reasoning
    if "customer" in sample_record:
        print(f"[AGENT] Detected nested object: 'customer'")
    if "items" in sample_record:
        print(f"[AGENT] Detected list array: 'items'")

    print(f"[AGENT] 💡 Plan: Flatten JSON and rename columns.")

    # Dynamically generated code
    generated_code = """
def flatten_and_transform(json_data):
    # 1. Flatten JSON
    df = pd.json_normalize(json_data)
    
    # 2. Semantic Renaming
    df.columns = df.columns.str.replace('customer.details.', 'cust_', regex=False)
    df.columns = df.columns.str.replace('payment.', 'pay_', regex=False)
    df.columns = df.columns.str.replace('customer.', 'cust_', regex=False)
    
    # 3. Drop complex lists
    if 'items' in df.columns:
        df = df.drop(columns=['items'])
        
    # 4. Handle Missing Values
    if 'discount_code' not in df.columns:
        df['discount_code'] = "NONE"
    df['discount_code'] = df['discount_code'].fillna("NONE")
    
    # 5. Type Casting
    if 'total_amount' in df.columns:
        df['total_amount'] = pd.to_numeric(df['total_amount'], errors='coerce').fillna(0.0)
    
    return df
    """
    return generated_code

# ==========================================
# 2. THE ORCHESTRATOR
# ==========================================
def run_ecommerce_etl():
    print("--- STEP 1: INGESTION ---")
    try:
        if not os.path.exists('data.json'):
            raise FileNotFoundError("'data.json' not found.")
            
        with open('data.json', 'r') as f:
            data_obj = json.load(f)
            
        print(f"✅ Loaded {len(data_obj)} JSON events.")
        
    except Exception as e:
        print(f"❌ Ingestion Error: {e}")
        return

    print("\n--- STEP 2: AGENT PLANNING ---")
    flattening_script = llm_generate_flattening_logic(data_obj[0])
    
    print("\n--- STEP 3: CODE GENERATION ---")
    print(flattening_script)
    
    print("\n--- STEP 4: EXECUTION ---")
    local_scope = {}
    local_scope['pd'] = pd
    
    try:
        exec(flattening_script, globals(), local_scope)
        transform_func = local_scope['flatten_and_transform']
        
        clean_df = transform_func(data_obj)
        print("✅ Transformation Successful.")
        print(f"ℹ️  Rows Processed: {len(clean_df)}")
        
    except Exception as e:
        print(f"❌ Execution Error: {e}")
        return

    print("\n--- STEP 5: LOAD TO SQL ---")
    conn = sqlite3.connect(":memory:") 
    clean_df.to_sql("fact_orders", conn, index=False)
    
    print("🔎 Verifying SQL Data:")
    result = pd.read_sql("""
        SELECT order_id, cust_name, pay_method, discount_code, total_amount 
        FROM fact_orders
    """, conn)
    
    print(result.to_string(index=False))

if __name__ == "__main__":
    run_ecommerce_etl()